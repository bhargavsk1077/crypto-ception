#include<stdio.h>
#include<unistd.h>
#include<dlfcn.h>
#include<openssl/ssl.h>

int SSL_write(SSL *context, const void *buffer, int bytes)
{
	int (*new_ssl_write)(SSL *, const void *, int);
	new_ssl_write = dlsym(RTLD_NEXT, "SSL_write");
	FILE *logger = fopen("sslwatch.log", "a+");
	fprintf(logger, "Process:%d Data:%s\n", getpid(), (char *)buffer);
	fclose(logger);
	return new_ssl_write(context, buffer, bytes);
}
