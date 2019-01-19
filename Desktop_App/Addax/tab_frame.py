import tkinter as tk
import tkinter.ttk as ttk

class Tab_Frame(tk.Frame):
    '''Fields'''
    info_label = ""
    info_image = ""
    horizontal_sep_1 = ""
    params_label = ""
    params_frame = ""
    horizontal_sep_2 = ""
    set_button = ""
    



    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        '''
        Creates all the widgets in the window
        '''
        self.info_label = tk.Label(self, text="Info").grid(column=0,row=0)
        self.params_label = tk.Label(self, text="Parameters").grid(column=0,row=3)


