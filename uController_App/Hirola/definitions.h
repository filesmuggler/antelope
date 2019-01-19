#ifndef _definitions_h_
#define _definitions_h_

typedef enum {TRUE = 1, FALSE = 0} bool;

#define setBit(bajt, nOfBit) bajt|=(0x01<<nOfBit);
#define clrBit(bajt, nOfBit) bajt&=~(0x01<<nOfBit);



#endif