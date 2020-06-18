#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>
#include<dlfcn.h>

size_t fwrite(const void *ptr, size_t size, size_t nmemb, FILE *stream)
{
	size_t (*new_fread)(const void *, size_t, size_t, FILE *);
	new_fread = dlsym(RTLD_NEXT, "fwrite");

	char *recorder = "/home/apollo_nox/crypto-ception/API-hook/defence/recorder";
	FILE *fptr = fopen(recorder, "r");
	int counter;
	fscanf(fptr, "%d", &counter);
	fclose(fptr);
	char chk;
	if(counter >= 10)
	{
		printf("We have noticed suspicious activity, allow?(y/n): ");
		scanf("%1s", &chk);
		if(chk != 'y')
			exit(1);
		counter = 0;
	}
	fptr = fopen(recorder, "w");
	fprintf(fptr, "%d", ++counter);
	fclose(fptr);
	return new_fread(ptr, size, nmemb, stream);
}
