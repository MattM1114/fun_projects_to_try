# 1st we import all the important libraries 
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pygame
import os 
from tkinter import messagebox

class music_player:
    
    def __init__(self,root):
        self.root = root
        
        #this is the title of the music player 
        self.root.title("Matt's music player")
        
        #setting the root window geometry
        self.root.geometry("750x400")
        self.root.resizable(False,False)
        
        #setting the background image 
        self.bg_image = tk.PhotoImage(file = os.path.join(os.getcwd(), "MusicPlayer/images", "bg_con.png"))
        self.bg_label = ttk.Label(self.root, image=self.bg_image)
        self.bg_label.place(relx=0, rely=-0, relwidth=1,relheight=1)
        
        #setting style for the root window 
        s = ttk.Style()
        s.theme_use('clam')
        s.configure('.', background='black', foreground='black')
        s.configure('TFrame', background='white', foreground='white')
        s.configure('TButton', font=('Arial',12), background='black', foreground='white',
                                            activebackground='brown', actieforegronud='white')
        s.configure('TLabel', font=('Arial',12),background='black', foreground='white')
        s.configure('TScale', background='white')
        
        #Initializing Pygame
        pygame.init()
        
        #Initializing Pygame Mixer
        pygame.mixer.init()
        
    # playlist Frame
        self.playlist_frame = tk.Frame(self.root)