/****************************************************************************************
	mach_inject.h $Revision: 1.1.1.1 $
	
	Copyright (c) 2003 Red Shed Software. All rights reserved.
	by Jonathan 'Wolf' Rentzsch (jon * redshed * net)
	
	************************************************************************************/
	
/************************************************************************************//**
	@mainpage	mach_inject
	@author		Jonathan 'Wolf' Rentzsch (jon * redshed * net)
	
	This package, coded in C to the Mach API, allows you to "inject" code into an
	arbitrary process. "Injection" means both 1) copying over the necessary code into the
	target's address space and 2) remotely creating a new thread to execute the code.

	************************************************************************************/

#ifndef		_mach_inject_
#define		_mach_inject_
#ifdef MACOSX

#include <stdio.h>
#include <unistd.h>
#include <assert.h>
#include <stddef.h>
#include <sys/errno.h>
#include <sys/types.h>
#include <mach/error.h>
#include <mach/vm_types.h>
#include <AvailabilityMacros.h>

#define	err_threadEntry_image_not_found			(err_local|1)

#define	INJECT_ENTRY		injectEntry
#define	INJECT_ENTRY_SYMBOL	"injectEntry"

typedef	void	(*mach_inject_entry)( ptrdiff_t codeOffset, void *paramBlock, size_t paramSize );
	
/************************************************************************************//**
	Starts executing threadEntry in a new thread in the process specified by
	targetProcess.
	
	@param	threadEntry		->	Required pointer to injected thread's entry point.
	@param	paramBlock		->	Optional pointer to block of memory to pass to the
								injected thread.
	@param	paramSize		->	Optional size of paramBlock.
	@param	targetProcess	->	Required target process ID.
	@param	stackSize		->	Optional stack size of threadEntry's thread. Set to zero
								for default (currently 8K usable).
	@result					<-	mach_error_t

	************************************************************************************/

	mach_error_t
mach_inject(
		const mach_inject_entry	threadEntry,
		const void				*paramBlock,
		size_t					paramSize,
		pid_t					targetProcess,
		vm_size_t				stackSize ) AVAILABLE_MAC_OS_X_VERSION_10_3_AND_LATER;

/************************************************************************************//**
	Given a pointer, returns its Mach-O image and image size.
	
	@param	pointer	->	Required pointer.
	@param	image	<-	Optional returned pointer to image (really a mach_header).
	@param	size	<-	Optional returned size of the image.
	@result			<-	mach_error_t
	
	************************************************************************************/

	mach_error_t
machImageForPointer(
		const void *pointer,
		const void **image,
		unsigned long *size ) AVAILABLE_MAC_OS_X_VERSION_10_3_AND_LATER;

#endif	//	MACOSX
#endif	//	_mach_inject_
