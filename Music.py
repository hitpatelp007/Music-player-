import pygame
from tkinter import *
import tkinter.filedialog as tk

class Music(Frame):
    def __init__(self,master):
        super(Application, self).__init__(master)
        self.playlistbox = Listbox(self, width = 50, height = 12, selectmode = SINGLE)

        self.grid(rowspan=5, columnspan=4)
        self.playlistbox.grid(row = 1)
        
        #Buttons 
        self.playButton = Button(self, text = 'play', command = self.play)
        self.loopButton = Button(self, text = 'loop', command = self.loop)
        self.stopButton = Button(self, text ='stop', command=self.stop)
        self.closeButton = Button(self, text ='close', command=self.close)        
        self.playButton.grid(row=4, column = 0)
        self.loopButton.grid(row=4, column = 1)
        self.stopButton.grid(row=4, column = 2)
        self.closeButton.grid(row=4, column = 3)
        self.pack()
        pygame.init()

    def play(self):
            pygame.mixer.music.load("KilDil.mp3")
            pygame.mixer.music.play(0,0.0)

    def close(self):
            pygame.mixer.quit()

    def stop(self):
            pygame.mixer.music.stop()
            
    def loop(self):
            pygame.mixer.music.stop()
            pygame.mixer.music.play(-1,0.0)

root = Tk()
root.title('Music player')
root.geometry('500x200')
app = Music(root)
app.mainloop()

 
