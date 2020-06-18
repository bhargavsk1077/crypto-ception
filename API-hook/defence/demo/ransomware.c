#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define BUFLEN 65536
void destroy(char *buffer, int len)
{
	// This could have been an encryption function
	memset(buffer, 'F', len);
	buffer[len] = '\n';
}

int main()
{
	char *files[] = {"1.dat", "2.dat", "3.dat", "4.dat", "5.dat", "6.dat", "7.dat", "8.dat", "9.dat", "10.dat", "11.dat", "12.dat", "13.dat", "14.dat", "15.dat", "16.dat", "17.dat", "18.dat", "19.dat", "20.dat", "21.dat", "22.dat", "23.dat", "24.dat", "25.dat", "26.dat", "27.dat", "28.dat", "29.dat", "30.dat", "31.dat", "32.dat", "33.dat", "34.dat", "35.dat", "36.dat", "37.dat", "38.dat", "39.dat", "40.dat", "41.dat", "42.dat", "43.dat", "44.dat", "45.dat", "46.dat", "47.dat", "48.dat", "49.dat", "50.dat"};
	int n = 50;
	char *buffer = calloc(BUFLEN, sizeof *buffer);
	int readlen;
	for(int i=0; i<n; i++)
	{
		FILE *fptr = fopen(files[i], "r");
		readlen = fread(buffer, sizeof *buffer, BUFLEN, fptr);
		fclose(fptr);
		fptr = fopen(files[i], "w");
		destroy(buffer, readlen);
		fwrite(buffer, sizeof *buffer, readlen+1, fptr);
		fclose(fptr);
	}
	free(buffer);
	return 0;
}
