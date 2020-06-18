#include<stdio.h>
#include<unistd.h>
#include<dlfcn.h>

int puts(const char * arg)
{
	int (*new_puts)(const char *);
	new_puts = dlsym(RTLD_NEXT, "puts");
	new_puts("The ship has been hijacked! Get off!");
	return new_puts(arg);
}
