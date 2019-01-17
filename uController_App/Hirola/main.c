/**
 * @author Krzysztof Stezala
 * @date 2019-01-12
 * @version 1.0
 * @brief UART communication with third-party app
 */
 
 
 
#include "aduc831.h"
#include "timers.h"
#include "definitions.h"
#include "putchar.h"

char buffer[25];																									// general buffer for data
char uart_buffer[25];
int local_index;

char message_index;

int frequency_1;																									// ch#1 freq value
char frequency_1_t[8];																						// char array to analyze
int duty_cycle_1;																									// after processing
char duty_cycle_1_t[2];																						// before processing

int frequency_2;																									// ch#2 freq value
char frequency_2_t[8];																						// char array to convert
int duty_cycle_2;																									// ch#2 duty cycle value
char duty_cycle_2_t[2];																						//
	
char operation_mode;

char ascii_offset;
int conversion_scaler;
int i;
int j;

bool new_data = FALSE;
bool mode_data = FALSE;
bool duty_cycle_data = FALSE;
bool freq_data = FALSE;
bool two_channel = FALSE;
bool is_read = TRUE;

bool do_it_once = TRUE;


void sendMessage()
{
	j = 0;
	for(j = 0;j<25;j++){
		if(j==1)
		{
			putchar(operation_mode);
		}
		else{
			putchar(buffer[j]);
		}
	}	
	putchar('\n');
}

void receiveMessage() interrupt 4
{
	/**
	* Receiving transmission
	*/
	char received = 0;
	if(RI==1){
		received = (char)SBUF;
		RI = 0;

		if((message_index == 1) && (received == 'G'))
		{
			sendMessage();
			message_index = 0;
			return;
		}
		else
		{
			buffer[message_index] = received;
		}
		message_index = message_index + 1;
		
	}
	if(TI==1){
		TI = 0;
	}
	
	if(received == 'E')
	{
		is_read = FALSE;
		message_index = 0;
		return;
	}
	else
	{
		is_read = TRUE;
	}
	
	return;
}



void analyzeData()
{
	if(buffer[local_index]=='S')
			{
				new_data = TRUE;
		
				mode_data = TRUE;
				freq_data = FALSE;
				duty_cycle_data = FALSE;
		
				local_index = local_index + 1;
				return;
			}
			else if(buffer[local_index] == 'D')
			{
				mode_data = FALSE;
				duty_cycle_data = TRUE;
				freq_data = FALSE;		
		
				local_index = local_index + 1;
				return;
			}
			else if(buffer[local_index] == 'F')
			{
				mode_data = FALSE;
				duty_cycle_data = FALSE;
				freq_data = TRUE;
				
				local_index = local_index + 1;
				return;
			}
	
			/**
			* Incoming data analysis
			*/
			if(new_data)
			{
				if(mode_data)
				{
					operation_mode = buffer[local_index];
					if(operation_mode == 49)
					{
						two_channel = FALSE;
					}
					else
					{
						two_channel = TRUE;
					}
				}
			}
		
			if(duty_cycle_data)
			{
				if(!two_channel)
				{
					// for single channel
					duty_cycle_1_t[local_index - 3] = buffer[local_index];
				}	
				else
				{
					// for double channel
					if(local_index < 5)
					{
						duty_cycle_1_t[local_index - 3] = buffer[local_index];
					}
					else
					{
						duty_cycle_2_t[local_index - 5] = buffer[local_index];
					}
				}
			}
		
			if(freq_data)
			{	
				if(!two_channel)																						// for single channel
				{
					frequency_1_t[local_index - 6] = buffer[local_index];
				}
				else																												// for two channels
				{
					if(local_index < 16)
					{
						frequency_1_t[local_index - 8] = buffer[local_index];
					}
					else
					{
						frequency_2_t[local_index - 16] = buffer[local_index];
					}
				}
			}
			//SBUF = buffer[local_index];
			local_index = local_index + 1;
			return;
}


void getValues()																										// convert duty cycles and freqs to ints
{	
	if(!two_channel)
	{
		conversion_scaler = 1;																					// scaler for retrieving values
		
		frequency_1 = 0;																								// resetting frequency 1
				
		for(i=7;i>=0;i--)																								// calculating frequency 1
		{			
			frequency_1 = (frequency_1_t[i] - ascii_offset) * conversion_scaler + frequency_1;			
			conversion_scaler = conversion_scaler * 10;                   // incrementing order of magnitude
		}
		
		conversion_scaler = 1;																					// scaler for retrieving values
		
		duty_cycle_1 = 0;																								// resetting duty cycle 1
		
		for(i=1;i>=0;i--)																								// calculating duty cycle 1
		{
			duty_cycle_1 = (duty_cycle_1_t[i] - ascii_offset) * conversion_scaler + duty_cycle_1;
			conversion_scaler = conversion_scaler * 10;                   // incrementing order of magnitude
		}
	}
	else
	{
		conversion_scaler = 1;																					// scaler for retrieving values		
		
		frequency_1 = 0;																								// resetting frequency 1
		
		for(i=7;i>=0;i--)																								// calculating frequency 1
		{
			frequency_1 = (frequency_1_t[i] - ascii_offset) * conversion_scaler + frequency_1;	
			conversion_scaler = conversion_scaler * 10;                   // incrementing order of magnitude
		}
		
		conversion_scaler = 1;																					// scaler for retrieving values		
		
		duty_cycle_1 = 0;																								// resetting duty cycle 1
				
		for(i=1;i>=0;i--)																								// calculating duty cycle 1
		{
			duty_cycle_1 = (duty_cycle_1_t[i] - ascii_offset) * conversion_scaler + duty_cycle_1;
			conversion_scaler = conversion_scaler * 10;                   // incrementing order of magnitude
		}
		
		conversion_scaler = 1;																					// scaler for retrieving values		
		
		frequency_2 = 0;																								// resetting frequency 2
		
		for(i=7;i>=0;i--)																								// calculating frequency 2
		{
			frequency_2 = (frequency_2_t[i] - ascii_offset) * conversion_scaler + frequency_2;	
			conversion_scaler = conversion_scaler * 10;                   // incrementing order of magnitude
		}
		
		conversion_scaler = 1;																					// scaler for retrieving values
		
		duty_cycle_2 = 0;																								// resetting duty cycle 2
		
		for(i=1;i>=0;i--)																								// calculating duty cycle 2
		{
			duty_cycle_2 = (duty_cycle_2_t[i] - ascii_offset) * conversion_scaler + duty_cycle_2;
			conversion_scaler = conversion_scaler * 10;                   // incrementing order of magnitude
		}
	}
}



/**
 * main function
 */
void main()
{
	/**
  * Enable the interrupts - general and UART
	*/
	ES = 1;
	EA = 1;
	
	/**
  * UART set into Mode 1 (8-bit, Variable Baud Rate)
	*/
	SM0 = 0;
	SM1 = 1;
	SM2 = 0;
	REN = 1;
	
	/**
  * Timer 1 set into 8-bit, autoreload mode, 9600bps at 11,0952 MHz
	*/
	TMOD = T1_MODE_8B_AUTORELOAD;
	TH1 = T1_9600_11;	
	TR1 = 1;
	
	/**
  * Initial set up
	*/
	message_index = 0;
	local_index = 0;
	ascii_offset = 48;	
	
	while(1)
	{
		while(buffer[local_index]!='E' && !is_read)
		{
			analyzeData();
		}
		if(buffer[local_index]=='E')
		{
			is_read = TRUE;
			getValues();
			local_index = 0;
		}		
	}
}