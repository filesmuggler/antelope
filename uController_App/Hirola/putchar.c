#include <reg51.h>

char putchar (char c)
{
	SBUF=c;
	while(!TI);
	TI=0;
	return c;
}