import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import os

class Tab_Frame(tk.Frame):
    '''Fields'''
    info_label = ""
    info_image_image = ""
    info_image_label = ""
    path_to_image = ""
    horizontal_sep_1 = ""
    params_label = ""
    params_frame = ""
    horizontal_sep_2 = ""

    def __init__(self,master=None,path_to_image=""):
        tk.Frame.__init__(self,master)
        self.grid()
        self.createWidgets(path_to_image)

    def createWidgets(self,path_to_image=""):
        '''
        Creates all the widgets in the window
        '''
        self.info_label = tk.Label(self, text="Info").grid(column=0,row=0, sticky=tk.W)

        self.dir = os.path.dirname(__file__)
        
        self.filename = os.path.join(self.dir,path_to_image)
        try:
            self.info_image_image = ImageTk.PhotoImage(Image.open(self.filename))
        except FileNotFoundError:
            path_to_image = "default.jpg"
            self.filename = os.path.join(self.dir,path_to_image)
            self.info_image_image = ImageTk.PhotoImage(Image.open(self.filename))

        
        self.info_image_label = tk.Label(self,image = self.info_image_image).grid(column=0,row=1,columnspan=2)
        self.horizontal_sep_1 = ttk.Separator(self, orient=tk.HORIZONTAL).grid(column=0, row=2, columnspan=2, sticky=tk.W+tk.E)
        self.params_label = tk.Label(self, text="Parameters").grid(column=0,row=3, sticky=tk.W)
        
        self.horizontal_sep_2 = ttk.Separator(self, orient=tk.HORIZONTAL).grid(column=0, row=2, columnspan=2, sticky=tk.W+tk.E)
        

