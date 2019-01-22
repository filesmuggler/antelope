import tkinter as tk
import tkinter.ttk as ttk

class Mode_3_Frame(tk.Frame):
    '''Fields'''
    user_freq_label = ""
    user_duty_label_1 = ""
    user_duty_label_2 = ""

    user_freq_scaler = ""
    user_duty_scaler_1 = ""
    user_duty_scaler_2 = ""
   


    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        '''
        Creates all the widgets in the window
        '''
        
        self.user_duty_label_1 = tk.Label(self, text="Duty Cycle 1 (A)").grid(column=0,row=2, sticky=tk.W)
        self.user_duty_scaler_1 = tk.Scale(self, from_=0, to=100, tickinterval = 10, length= 300,orient=tk.HORIZONTAL)
        self.user_duty_scaler_1.grid(column=0, row=3, columnspan=2, padx=5, pady=5)

        self.user_duty_label_2 = tk.Label(self, text="Duty Cycle 2 (B)").grid(column=0,row=4, sticky=tk.W)
        self.user_duty_scaler_2 = tk.Scale(self, from_=0, to=100, tickinterval = 10, length= 300,orient=tk.HORIZONTAL)
        self.user_duty_scaler_2.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
