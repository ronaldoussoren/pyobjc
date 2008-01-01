#include "../config.h"

const char* GetPlatformExtensionsString()
{
	const char *extensions = NULL;
#ifdef WGL_PLATFORM
	typedef const char* (*T_wglGetExtensionsStringEXT)();
	T_wglGetExtensionsStringEXT wglGetExtensionsStringEXT = (T_wglGetExtensionsStringEXT)wglGetProcAddress("wglGetExtensionsStringEXT");
	SetLastError(0);
	if (wglGetExtensionsStringEXT)
	{
		extensions = (char*)wglGetExtensionsStringEXT();
	}
	else
	{
		typedef const char* (*T_wglGetExtensionsStringARB)(HDC dc);
		T_wglGetExtensionsStringARB wglGetExtensionsStringARB = (T_wglGetExtensionsStringARB)wglGetProcAddress("wglGetExtensionsStringARB");
		SetLastError(0);
		if (wglGetExtensionsStringARB)
		{
			extensions = (char*)wglGetExtensionsStringARB(wglGetCurrentDC());
		}
	}
#endif
	return extensions;
}


void* GetExtProc(const char* name)
{
	void *proc = NULL;
#ifdef CGL_PLATFORM
	NSSymbol symbol;
	char *symbolName;
	
	/* This comes from Apple Technical Q&A QA1188
	 Prepend a '_' for the Unix C symbol mangling convention */
	symbolName = malloc (strlen (name) + 2);
	strcpy(symbolName + 1, name);
	symbolName[0] = '_';
	symbol = NULL;
	if (NSIsSymbolNameDefined (symbolName))
	  symbol = NSLookupAndBindSymbol (symbolName);
	free (symbolName);
	proc = symbol ? NSAddressOfSymbol (symbol) : NULL;
#elif defined(WGL_PLATFORM)
	proc = wglGetProcAddress(name);
	SetLastError(0);
#elif defined(GLX_PLATFORM) && defined(GLX_ARB_get_proc_address)
	proc = glXGetProcAddressARB(name);
#endif
	return proc;
}
