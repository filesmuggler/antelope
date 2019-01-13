#include "definitions.h"



	/**
	* Checking for flags from incoming transmission
	*
	if(received=='S')
	{
		new_data = TRUE;
		
		mode_data = TRUE;
		freq_data = FALSE;
		duty_cycle_data = FALSE;
		
		message_index++;
		return;
	}
	else if(received == 'D')
	{
		mode_data = FALSE;
		duty_cycle_data = TRUE;
		freq_data = FALSE;		
		
		message_index++;
		return;
	}
	else if(received == 'F')
	{
		mode_data = FALSE;
		duty_cycle_data = FALSE;
		freq_data = TRUE;
		
		message_index++;
		return;
	}
	else if(received == 'E')
	{
		new_data = FALSE;
		
		mode_data = FALSE;
		freq_data = FALSE;
		duty_cycle_data = FALSE;
		two_channel = FALSE;
		
		message_index = 0;
		return;
	}
	
	/**
	* Incoming data analysis
	*
	if(new_data)
	{
		if(mode_data)
		{
			operation_mode = received;
			if(operation_mode!=49){
				two_channel = TRUE;
			}
		}
		
		if(duty_cycle_data)
		{
			if(!two_channel)
			{
				// for single channel
				duty_cycle_1_t[message_index - 3] = received;
			}
			else
			{
				// for double channel
				if(message_index < 5)
				{
					duty_cycle_1_t[message_index - 3] = received;
				}
				else
				{
					duty_cycle_2_t[message_index - 5] = received;
				}
			}
		}
		
		if(freq_data)
		{
			if(!two_channel)
			{
				// for single channel
				frequency_1_t[message_index - 6] = received;
			}
			else
			{
				// for double channel
				if(message_index < 16)
				{
					frequency_1_t[message_index - 8] = received;
				}
				else
				{
					frequency_2_t[message_index - 16] = received;
				}
			}
		}
		message_index++;
	}*/