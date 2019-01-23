#ifndef _definitions_h_
#define _definitions_h_
#include "timers.h"

//variables
typedef enum {TRUE = 1, FALSE = 0} bool;

//Bit operations
#define setBit(bajt, nOfBit) bajt|=(0x01<<nOfBit);
#define clrBit(bajt, nOfBit) bajt&=~(0x01<<nOfBit);

//PWM
#define PWM_PWM0_OFF (0x0001<<7)
#define PWM_PWM0_ON 0x0000
#define PWM_MD2_SET (0x0001<<6)
#define PWM_MD2_CLEAR 0x0000
#define PWM_MD1_SET (0x0001<<5)
#define PWM_MD1_CLEAR 0x0000
#define PWM_MD0_SET (0x0001<<4)
#define PWM_MD0_CLEAR 0x0000
#define PWM_CDIV1_SET (0x0001<<3)
#define PWM_CDIV1_CLEAR 0x0000
#define PWM_CDIV0_SET (0x0001<<2)
#define PWM_CDIV0_CLEAR 0x0000
#define PWM_CSEL1_SET (0x0001<<1)
#define PWM_CSEL1_CLEAR 0x0000
#define PWM_CSEL0_SET (0x0001<<0)
#define PWM_CSEL0_CLEAR 0x0000
#define PWM_2_ON 0x0000
#define PWM_3_ON (0x0001<<6)
#define PWM_MODE0 0x0000
#define PWM_MODE1 (PWM_MD2_CLEAR|PWM_MD1_CLEAR|PWM_MD0_SET|PWM_CDIV1_CLEAR|PWM_CDIV0_CLEAR)
#define PWM_MODE2 (PWM_MD2_CLEAR|PWM_MD1_SET|PWM_MD0_CLEAR)
#define PWM_MODE3 (PWM_MD2_CLEAR|PWM_MD1_SET|PWM_MD0_SET)
#define PWM_MODE4 ((PWM_MD2_SET|PWM_MD1_CLEAR|PWM_MD0_CLEAR)
#define PWM_MODE5 (PWM_MD2_SET|PWM_MD1_CLEAR|PWM_MD0_SET)
#define PWM_MODE6 ((PWM_MD2_SET|PWM_MD1_SET|PWM_MD0_CLEAR)
#define PWM_NODIV_FOSC (PWM_PWM0_ON|PWM_CDIV1_CLEAR|PWM_CDIV0_CLEAR|PWM_CSEL1_SET|PWM_CSEL0_SET)
#define PWM_CFG2 clrBit(CFG831,6)
#define PWM_DIVIDER 1
#define Tx_tau_PWM (float)((float)PWM_DIVIDER/F_OSC)
#define PWM_INITIAL_VALUE(time_pwm_ms) (unsigned int)((float)time_pwm_ms/Tx_tau_PWM/1000.0)
	
//Mode1
#define PWM_M1_PERIOD(time_pwm_ms) PWM1L=PWM_INITIAL_VALUE(time_pwm_ms); PWM1H=PWM_INITIAL_VALUE(time_pwm_ms)>>8
#define PWM_M1_DUTY(time_pwm_ms) PWM0L=PWM_INITIAL_VALUE(time_pwm_ms); PWM0H=PWM_INITIAL_VALUE(time_pwm_ms)>>8

//Mode2
#define PWM_M2_PERIOD(time_pwm_ms) PWM1L=PWM_INITIAL_VALUE(time_pwm_ms);
#define PWM_M2_DUTY1(time_pwm_ms) PWM0L=PWM_INITIAL_VALUE(time_pwm_ms);
#define PWM_M2_DELAY2(time_pwm_ms) PWM1H=PWM_INITIAL_VALUE(time_pwm_ms);
#define PWM_M2_DUTY2(time_pwm_ms) PWM0H=PWM_INITIAL_VALUE(time_pwm_ms);

//Mode3
#define PWM_M3_DUTY1(time_pwm_ms) PWM0L=PWM_INITIAL_VALUE(time_pwm_ms); PWM0H=PWM_INITIAL_VALUE(time_pwm_ms)>>8
#define PWM_M3_DUTY2(time_pwm_ms) PWM1L=PWM_INITIAL_VALUE(time_pwm_ms); PWM1H=PWM_INITIAL_VALUE(time_pwm_ms)>>8

//Mode5
#define PWM_M5_PERIOD1(time_pwm_ms) PWM1L=PWM_INITIAL_VALUE(time_pwm_ms);
#define PWM_M5_PERIOD2(time_pwm_ms) PWM1H=PWM_INITIAL_VALUE(time_pwm_ms);
#define PWM_M5_DUTY1(time_pwm_ms) PWM0L=PWM_INITIAL_VALUE(time_pwm_ms);
#define PWM_M5_DUTY2(time_pwm_ms) PWM0H=PWM_INITIAL_VALUE(time_pwm_ms);


#endif