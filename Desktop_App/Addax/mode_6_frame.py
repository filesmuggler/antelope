
import tkinter as tk
import tkinter.ttk as ttk

class Mode_6_Frame(tk.Frame):
    '''Fields'''
    user_period_label = ""
    user_duty_label = ""


    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        '''
        Creates all the widgets in the window
        '''
        #self.user_period_label = tk.Label(self, text="Not found").grid(column=0,row=0)
        #self.user_duty_label = tk.Label(self, text="yet").grid(column=1,row=0)
        print("")
