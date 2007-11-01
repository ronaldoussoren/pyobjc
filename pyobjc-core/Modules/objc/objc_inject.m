#if defined(__i386__) || defined(__ppc__)
#include "objc_inject.h"
#if defined(MAC_OS_X_VERSION_10_3)
#if MAC_OS_X_VERSION_MAX_ALLOWED >= MAC_OS_X_VERSION_10_3
#include "mach_inject.h"
#include <string.h>
#include <libc.h>
#include <errno.h>
#include <mach/mach.h>
#include <mach/mach_error.h>
#include <mach/machine/vm_param.h>
#include <unistd.h>
#include <pthread.h>
#include <mach-o/loader.h>
#include <mach-o/dyld.h>
#include <crt_externs.h>
#include <Carbon/Carbon.h>

#define PYJECT_LINKOPTIONS (NSLINKMODULE_OPTION_BINDNOW | \
	NSLINKMODULE_OPTION_RETURN_ON_ERROR | \
	NSLINKMODULE_OPTION_PRIVATE)

#if defined(__ppc__) || defined(__ppc64__)
#define TRAP() __asm__ ("trap")
#elif defined(__i386__) || defined(__x86_64__)
#define TRAP() __asm__ __volatile__ ("int3")
#endif

typedef struct {
	task_port_t target_task;
	struct mach_header *mh;
	pointer_t data;
	unsigned int data_count;
	unsigned long mh_address;
	unsigned long func_lookup_ptr;
} target_mach_header;

static void *INJECT_pthread_entry(void *p);
static void INJECT_test_func(void);
static pascal void INJECT_EventLoopTimerEntry(EventLoopTimerRef inTimer, void *p);

#define DEFWRAP(func) __typeof__(&func) func
typedef struct {
    /* internal */
    DEFWRAP(INJECT_pthread_entry);
    DEFWRAP(INJECT_test_func);
    DEFWRAP(INJECT_EventLoopTimerEntry);
	/* dyld bootstrap */
	DEFWRAP(_dyld_func_lookup);
    DEFWRAP(_dyld_image_count);
    DEFWRAP(_dyld_get_image_vmaddr_slide);
    DEFWRAP(_dyld_get_image_header);
    DEFWRAP(_dyld_get_image_name);
	/* dyld funcs */
	DEFWRAP(NSAddImage);
	DEFWRAP(NSLookupSymbolInImage);
	DEFWRAP(NSAddressOfSymbol);
	/* libSystem */
	DEFWRAP(NSCreateObjectFileImageFromFile);
	DEFWRAP(NSLinkModule);
	DEFWRAP(NSLinkEditError);
	DEFWRAP(printf);
	DEFWRAP(snprintf);
	DEFWRAP(pthread_attr_init);
	DEFWRAP(pthread_attr_getschedpolicy);
	DEFWRAP(pthread_attr_setdetachstate);
	DEFWRAP(pthread_attr_setinheritsched);
	DEFWRAP(sched_get_priority_max);
	DEFWRAP(pthread_attr_setschedparam);
	DEFWRAP(pthread_create);
	DEFWRAP(pthread_attr_destroy);
	DEFWRAP(thread_suspend);
	DEFWRAP(mach_thread_self);
	/* Carbon */
	DEFWRAP(NewEventLoopTimerUPP);
	DEFWRAP(GetMainEventLoop);
	DEFWRAP(InstallEventLoopTimer);
} func_wrappers;
#undef DEFWRAP

typedef struct {
	unsigned long funcLookupPtr;
	func_wrappers f;
	int useMainThread;
	unsigned int bundlePathOffset;
	unsigned int systemPathOffset;
	unsigned int carbonPathOffset;
	char stringTable[1];
} objc_inject_param;


/* functions */
static void INJECT_ENTRY(ptrdiff_t codeOffset, objc_inject_param *param, size_t paramSize, char *dummy_pthread_struct);
static target_mach_header *get_target_mach_header(target_mach_header *th);
static target_mach_header *calculate_header(target_mach_header *th);
static kern_return_t dispose_target_mach_header(target_mach_header *th);


static target_mach_header *
get_target_mach_header(target_mach_header *th) {
	kern_return_t k;
	struct mach_header *mh;
	vm_address_t address;
	vm_size_t size;
	vm_region_basic_info_data_t info;
	mach_msg_type_number_t infoCnt;
	mach_port_t objectName;
	pointer_t data;
	unsigned int data_count;
	unsigned long mh_address;

	/*
	 * Look through the target task's regions looking for the region that
	 * has the MH_EXECUTE.  Should be the first guess of 0x1000, cross
	 * your fingers!
	 */

	mh = NULL;
	mh_address = 0;
	address = VM_MIN_ADDRESS;
	do {
		infoCnt = VM_REGION_BASIC_INFO_COUNT;
		// fprintf(stderr, "region for %p\n", (void*)address);
		k = vm_region(th->target_task, &address, &size, VM_REGION_BASIC_INFO,
			(vm_region_info_t)&info, &infoCnt, &objectName);
		if (k == KERN_SUCCESS) {
#if 0
			int changedPermission = 0;
			fprintf(stderr, "  size 0x%d\n", size);
			if (!(info.protection & VM_PROT_READ)) {
				fprintf(stderr, "protection was = %d (max = %d) for %p +0x%X\n", info.protection, info.max_protection, (void*)address, size);
				k = vm_protect(th->target_task, address, size, false, (info.protection | VM_PROT_READ));
				if (k == KERN_SUCCESS) {
					changedPermission = 1;
				} else {
					fprintf(stderr, "couldn't change protection\n");
					address += size;
					continue;
				}
			}
#endif
			k = vm_read(th->target_task, address, size, &data, &data_count);
#if 0
			if (changedPermission) {	
				(void)vm_protect(th->target_task, address, size, false, info.protection);
			}
#endif
			if (k == KERN_SUCCESS) {
				if (data_count > sizeof(struct mach_header)) {
					mh = (struct mach_header *)data;
					mh_address = address;
					/*
					 * If the magic number is right and the size of this
					 * region is big enough to cover the mach header and
					 * load commands assume it is correct.
					 */
					if (
						mh->magic != MH_MAGIC ||
						mh->filetype != MH_EXECUTE ||
						data_count < sizeof(struct mach_header)
					) {
						mh = NULL;
					}
				}
				if (mh != NULL) {
					break;
				} else {
					k = vm_deallocate(mach_task_self(), data, data_count);
					if (k != KERN_SUCCESS) {
						//fprintf(stderr, "couldn't vm_deallocate\n");
						return NULL;
					}
				}
			}
			else if (k != KERN_PROTECTION_FAILURE) {
				//fprintf(stderr, "k != KERN_PROTECTION_FAILURE (%d)\n", k);
				return NULL;
			}
			address += size;
		}
	} while (k != KERN_NO_SPACE && mh == NULL);

	if (mh == NULL) {
		//fprintf(stderr, "mh == NULL\n");
		return NULL;
	}

	th->mh = mh;
	th->data = data;
	th->data_count = data_count;
	th->mh_address = mh_address;
	return th;

}


static target_mach_header *
calculate_header(target_mach_header *th) {
	struct segment_command *sg;
	unsigned long i;
	/* func_lookup_ptr */
	int looking_for = 1;
	if (th == NULL) {
		return NULL;
	}
	sg = (struct segment_command *)((char *)th->mh + sizeof(struct mach_header));
	for (i = 0; i < th->mh->ncmds; i++) {
		if (sg->cmd == LC_SEGMENT) {
			struct section *s = ((struct section *)
				((char *)sg + sizeof(struct segment_command)));
			unsigned long j;
			for (j = 0; j < sg->nsects; j++) {
				if (strncmp(s->segname, "__DATA", sizeof(s->segname)) == 0 &&
					strncmp(s->sectname, "__dyld", sizeof(s->sectname)) == 0) {
					th->func_lookup_ptr = s->addr + sizeof(unsigned long);
					looking_for--;
					break;
				}
				s++;
			}
			if (looking_for == 0) {
				break;
			}
		}
		sg = (struct segment_command *)((char *)sg + sg->cmdsize);
	}
	if (looking_for) {
		return NULL;
	}
	return th;
}


static kern_return_t
dispose_target_mach_header(target_mach_header *th) {
	kern_return_t k;
	k = vm_deallocate(mach_task_self(), th->data, th->data_count);
	return k;
}


/* Runs from injectee */
static void
INJECT_test_func(void) {
}

static void
INJECT_ENTRY(ptrdiff_t codeOffset, objc_inject_param *param, size_t paramSize __attribute__((__unused__)), char *dummy_pthread_struct __attribute__((__unused__))) {
#if defined (__i386__)
	// On intel, per-pthread data is a zone of data that must be allocated.
	// if not, all function trying to access per-pthread data (all mig functions for instance)
	// will crash. 
	extern void __pthread_set_self(char*);
	__pthread_set_self(dummy_pthread_struct);
#endif
	func_wrappers *f = &param->f;
#define CODE_SHIFT(func) f->func = (void *)(((char *)f->func) + codeOffset)
	CODE_SHIFT(INJECT_pthread_entry);
	CODE_SHIFT(INJECT_test_func);
	CODE_SHIFT(INJECT_EventLoopTimerEntry);
#undef CODE_SHIFT
	f->INJECT_test_func();
	f->_dyld_func_lookup = *((__typeof__(&f->_dyld_func_lookup))param->funcLookupPtr);
	/* dyld */
#define DYLD_WRAP(func) f->_dyld_func_lookup("_"#func, (void **)&f->func)
    DYLD_WRAP(_dyld_image_count);
    DYLD_WRAP(_dyld_get_image_vmaddr_slide);
    DYLD_WRAP(_dyld_get_image_header);
    DYLD_WRAP(_dyld_get_image_name);
#undef DYLD_WRAP
#define DYLD_WRAP(func) f->_dyld_func_lookup("__dyld_"#func, (void **)&f->func)
	DYLD_WRAP(NSAddImage);
	DYLD_WRAP(NSLookupSymbolInImage);
	DYLD_WRAP(NSAddressOfSymbol);
#undef DYLD_WRAP

    // my kingdom for strcmp
    uint32_t img_index;
    uint32_t img_count = f->_dyld_image_count();
    for (img_index = 0; img_index < img_count; img_index++) {
        char *a = (char *)&param->stringTable[param->systemPathOffset];
        char *b = (char *)f->_dyld_get_image_name(img_index);
        while (*a != '\0' && *b != '\0' && *a == *b) {
            a++;
            b++;
        }
        if (*a == '\0' && *b == '\0') {
            break;
        }
    }
    if (img_index == img_count) {
        // libSystem not found!
        TRAP();
    }
    intptr_t slide = f->_dyld_get_image_vmaddr_slide(img_index);


#define IMAGE_WRAP(func) f->func = (void *)(((char *)f->func) + slide)
	/* libSystem */
	IMAGE_WRAP(NSCreateObjectFileImageFromFile);
	IMAGE_WRAP(NSLinkModule);
	IMAGE_WRAP(NSLinkEditError);
    IMAGE_WRAP(printf);
    IMAGE_WRAP(snprintf);
	IMAGE_WRAP(pthread_attr_init);
	IMAGE_WRAP(pthread_attr_getschedpolicy);
	IMAGE_WRAP(pthread_attr_setdetachstate);
	IMAGE_WRAP(pthread_attr_setinheritsched);
	IMAGE_WRAP(sched_get_priority_max);
	IMAGE_WRAP(pthread_attr_setschedparam);
	IMAGE_WRAP(pthread_create);
	IMAGE_WRAP(pthread_attr_destroy);
	IMAGE_WRAP(thread_suspend);
	IMAGE_WRAP(mach_thread_self);
#undef IMAGE_WRAP

	pthread_attr_t attr;
	f->pthread_attr_init(&attr);
	
	int policy;
	f->pthread_attr_getschedpolicy( &attr, &policy );
	f->pthread_attr_setdetachstate( &attr, PTHREAD_CREATE_DETACHED );
	f->pthread_attr_setinheritsched( &attr, PTHREAD_EXPLICIT_SCHED );
			
	struct sched_param sched;
	sched.sched_priority = f->sched_get_priority_max( policy );
	f->pthread_attr_setschedparam( &attr, &sched );
			
		
	pthread_t thread; 
	pthread_create( &thread,
					&attr,
                    f->INJECT_pthread_entry,
					(void*) param );
	f->pthread_attr_destroy(&attr);
			
	f->thread_suspend(f->mach_thread_self());
}   


/* Runs from injectee */
static void *
INJECT_pthread_entry(void *p) {
    objc_inject_param *param = (objc_inject_param *)p;
	func_wrappers *f = &param->f;
	EventLoopTimerProcPtr proc = (EventLoopTimerProcPtr)f->INJECT_EventLoopTimerEntry;

	//f->printf("in pthread\n");
	//f->printf("proc: %p\n", proc);
					
	if (param->useMainThread) {
		const struct mach_header *mh = f->NSAddImage((const char *)&param->stringTable[param->carbonPathOffset], NSADDIMAGE_OPTION_WITH_SEARCHING);
		//f->printf("carbon:  %p\n", mh);
#define IMAGE_WRAP(func) f->func = f->NSAddressOfSymbol(f->NSLookupSymbolInImage(mh, "_" # func, NSLOOKUPSYMBOLINIMAGE_OPTION_BIND))
		IMAGE_WRAP(NewEventLoopTimerUPP);
		IMAGE_WRAP(GetMainEventLoop);
		IMAGE_WRAP(InstallEventLoopTimer);
#undef IMAGE_WRAP
#undef NewEventLoopTimerUPP
		EventLoopTimerUPP upp = f->NewEventLoopTimerUPP(proc);
		f->InstallEventLoopTimer(f->GetMainEventLoop(), 0, 0, upp, (void*)param, NULL);
	} else {
		proc(NULL, (void *)param);
	}

	return NULL;
}


/* Runs from injectee */
static pascal void
INJECT_EventLoopTimerEntry(EventLoopTimerRef inTimer __attribute__((__unused__)), void *p) {
    objc_inject_param *param = (objc_inject_param *)p;
	func_wrappers *f = &param->f;
	char *pathname = &param->stringTable[param->bundlePathOffset];
	NSObjectFileImageReturnCode rc;
	NSObjectFileImage image;
	NSModule newModule;
	const char *errString;
	char errBuf[512];

	//f->printf("in main thread!\n");
	//f->printf("loading %s\n", pathname);
	rc = f->NSCreateObjectFileImageFromFile(pathname, &image);
	//f->printf("rc = %d\n", rc);
	switch(rc) {
		default:
		case NSObjectFileImageFailure:
		case NSObjectFileImageFormat:
			/* for these a message is printed on stderr by dyld */
			errString = "Can't create object file image";
		break;
		case NSObjectFileImageSuccess:
			errString = NULL;
			break;
		case NSObjectFileImageInappropriateFile:
			errString = "Inappropriate file type for dynamic loading";
			break;
		case NSObjectFileImageArch:
			errString = "Wrong CPU type in object file";
			break;
		case NSObjectFileImageAccess:
			errString = "Can't read object file (no access)";
			break;
	}
	if (errString == NULL) {
		//f->printf("linking...\n");
		newModule = f->NSLinkModule(image, pathname, PYJECT_LINKOPTIONS);
		//f->printf("linked %p\n", newModule);
		if (newModule == NULL) {
			int errNo;
			const char *fileName, *moreErrorStr;
			NSLinkEditErrors c;
			f->NSLinkEditError( &c, &errNo, &fileName, &moreErrorStr );
			f->snprintf(errBuf, sizeof(errBuf), "Failure linking new module: %s: %s", fileName, moreErrorStr);
			errString = errBuf;
		}
	}
	if (errString) {
		f->printf("%s\n", errString);
	}
}


/* "public" API */
int
objc_inject(pid_t pid, int use_main_thread, char *bundlePath, char *systemPath, char *carbonPath) {
	target_mach_header th;
    intptr_t slide;
    uint32_t img_index;
    uint32_t img_count;
    const struct mach_header *mh;
	objc_inject_param *param;
	mach_error_t err;
	unsigned int bundle_offset = 0;
	unsigned int system_offset = strlen(bundlePath) + 1;
	unsigned int carbon_offset = system_offset + strlen(systemPath) + 1;
	unsigned int strtable_size = carbon_offset + strlen(carbonPath) + 1;
	unsigned int size = sizeof(objc_inject_param) + strtable_size;
	err = task_for_pid(mach_task_self(), pid, &th.target_task);
	if (err) {
		//fprintf(stderr, "couldn't get task for pid\n");
		return -1;
	}
	if (!get_target_mach_header(&th)) {
		//fprintf(stderr, "blew up trying to get at mach_header\n");
		return -1;
	}
	if (!calculate_header(&th)) {
		//fprintf(stderr, "couldn't calculate target mach_header\n");
		return -1;
	}
	param = malloc(size);
	if (param == NULL) {
		return -1;
	}
	param->funcLookupPtr = th.func_lookup_ptr;
	param->useMainThread = use_main_thread;
	param->bundlePathOffset = bundle_offset;
	param->systemPathOffset = system_offset;
	param->carbonPathOffset = carbon_offset;
	strcpy(&param->stringTable[bundle_offset], bundlePath);
	strcpy(&param->stringTable[system_offset], systemPath);
	strcpy(&param->stringTable[carbon_offset], carbonPath);
	dispose_target_mach_header(&th);

	mh = NSAddImage((const char *)&param->stringTable[param->systemPathOffset], NSADDIMAGE_OPTION_RETURN_ONLY_IF_LOADED);
    img_count = _dyld_image_count();
    for (img_index = 0; img_index < img_count; img_index++) {
        if (_dyld_get_image_header(img_index) == mh) {
            break;
        }
    }
    if (img_index == img_count) {
        free(param);
        //fprintf(stderr, "couldn't find libSystem's index\n");
        return -1;
    }
    slide = _dyld_get_image_vmaddr_slide(img_index);
#define IMAGE_WRAP(func) param->f.func = (__typeof__(&func))(((char *)&func) - slide)
	IMAGE_WRAP(NSCreateObjectFileImageFromFile);
	IMAGE_WRAP(NSLinkModule);
	IMAGE_WRAP(NSLinkEditError);
    IMAGE_WRAP(printf);
    IMAGE_WRAP(snprintf);
	IMAGE_WRAP(pthread_attr_init);
	IMAGE_WRAP(pthread_attr_getschedpolicy);
	IMAGE_WRAP(pthread_attr_setdetachstate);
	IMAGE_WRAP(pthread_attr_setinheritsched);
	IMAGE_WRAP(sched_get_priority_max);
	IMAGE_WRAP(pthread_attr_setschedparam);
	IMAGE_WRAP(pthread_create);
	IMAGE_WRAP(pthread_attr_destroy);
	IMAGE_WRAP(thread_suspend);
	IMAGE_WRAP(mach_thread_self);

    slide = 0;
    IMAGE_WRAP(INJECT_pthread_entry);
    IMAGE_WRAP(INJECT_test_func);
    IMAGE_WRAP(INJECT_EventLoopTimerEntry);
#undef IMAGE_WRAP
	err = mach_inject((mach_inject_entry)INJECT_ENTRY, param, size, pid, 0);
	free(param);
	if (err) {
		//fprintf(stderr, "couldn't inject\n");
		return -1;
	}
	return 0;
}

#endif /* MAC_OS_X_VERSION_MAX_ALLOWED >= MAC_OS_X_VERSION_10_3 */
#endif /* MAC_OS_X_VERSION_10_3 */
#endif
