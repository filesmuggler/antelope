import tkinter as tk
import tkinter.ttk as ttk

class Tab_Frame(tk.Frame):
    '''Fields'''
    info_label = ""
    info_image = ""
    path_to_image = ""
    horizontal_sep_1 = ""
    params_label = ""
    params_frame = ""
    horizontal_sep_2 = ""
   
    



    def __init__(self,master=None,mode_frame=None,path_to_image=None):
        tk.Frame.__init__(self,master)
        self.grid()
        self.createWidgets(mode_frame,path_to_image)

    def createWidgets(self,mode_frame=None,path_to_image=None):
        '''
        Creates all the widgets in the window
        '''
        self.info_label = tk.Label(self, text="Info").grid(column=0,row=0)
        self.info_image = tk.PhotoImage(path_to_image)
        self.horizontal_sep_1 = ttk.Separator(self, orient=tk.HORIZONTAL).grid(column=0, row=2, columnspan=2, sticky=tk.W+tk.E)
        self.params_label = tk.Label(self, text="Parameters").grid(column=0,row=3)
        self.params_frame = mode_frame
        self.horizontal_sep_2 = ttk.Separator(self, orient=tk.HORIZONTAL).grid(column=0, row=2, columnspan=2, sticky=tk.W+tk.E)
        

