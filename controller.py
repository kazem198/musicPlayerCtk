import customtkinter
from PIL import Image
import pygame


class Controller(customtkinter.CTkFrame):
    def __init__(self, playListClass, titleSong, imageAlbum, progress, master=None):
        super().__init__(master)
        self.nameSong = None
        self.indexSong = -1
        self.isPause = False
        self.playListClass = playListClass
        self.titleSong = titleSong
        self.imageAlbum = imageAlbum
        self.progress = progress
        self.id = -1
        self.pos = 0
        self.tiemMusic = 0

        self.rowconfigure(0, weight=1)
        self.columnconfigure((0, 1, 2, 3,), weight=1)

        self.btnPrevious = customtkinter.CTkButton(self, text="", image=customtkinter.CTkImage(
            Image.open("./assets/pause_light.png"), Image.open("./assets/previous_dark.png"), size=(75, 75)), fg_color="transparent",
            hover="", command=self.preHandel)

        self.btnPause = customtkinter.CTkButton(self, text="", image=customtkinter.CTkImage(
            Image.open("./assets/pause_light.png"), Image.open("./assets/pause_dark.png"), size=(75, 75)), fg_color="transparent",
            hover="", command=self.pauseHandel)

        self.btnPlay = customtkinter.CTkButton(self, text="", image=customtkinter.CTkImage(
            Image.open("./assets/play_light.png"), Image.open("./assets/play_dark.png"), size=(75, 75)), fg_color="transparent",
            hover="", command=self.play)

        self.btnStop = customtkinter.CTkButton(self, text="", image=customtkinter.CTkImage(
            Image.open("./assets/stop_light.png"), Image.open("./assets/stop_dark.png"), size=(75, 75)), fg_color="transparent",
            hover="", command=self.stopHandel)

        self.btnNext = customtkinter.CTkButton(self, text="", image=customtkinter.CTkImage(
            Image.open("./assets/next_light.png"), Image.open("./assets/next_dark.png"), size=(75, 75)), fg_color="transparent",
            hover="", command=self.nextHandel)

        self.btnPrevious.grid(column=0, row=0)
        self.btnPause.grid(column=1, row=0)
        self.btnPlay.grid(column=2, row=0)

        self.btnStop.grid(column=3, row=0)
        self.btnNext.grid(column=4, row=0)

    def play(self):
        self.pos = 0
        if self.isPause == True:
            pygame.mixer.music.unpause()
        else:

            self.nameSong, self.indexSong = self.playListClass.getName()

            pygame.mixer.init()

            pygame.mixer.music.load(f"playList/{self.nameSong}")

            pygame.mixer.music.play(loops=0)
            self.moveProgress()

    def moveProgress(self):

        self.tiemMusic = int(self.pos + pygame.mixer.music.get_pos()/1000)

        self.progress.moveProgress(self.tiemMusic)

        self.id = customtkinter.CTk.after(self, 1000, self.moveProgress)

    def pauseHandel(self):

        if self.isPause == False:
            pygame.mixer.music.pause()
            self.isPause = True
        else:

            pygame.mixer.music.unpause()
            self.isPause = False

    def nextHandel(self):
        self.playListClass.activeListbox(self.indexSong+1)
        self.play()
        self.pos = 0

    def preHandel(self):
        self.playListClass.activeListbox(self.indexSong-1)
        self.play()
        self.pos = 0

    def stopHandel(self):

        self.playListClass.deActiveListbox()
        self.imageAlbum.myImage.configure(image=customtkinter.CTkImage(
            Image.open("assets/album.jpg"), size=(500, 500)))

        self.titleSong.label.configure(text="")

        pygame.mixer.music.stop()
        self.pos = 0

    def handelSliderControlldr(self, pos):

        self.pos = int(pos)
        pygame.mixer.music.set_pos(int(pos))

    def handelEndSong(self):
        self.nextHandel()
