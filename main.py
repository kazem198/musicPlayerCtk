import customtkinter
from imageAlbume import ImageAlbume
from musicName import MusicName
from controller import Controller
from progress import Progress
from playListLabel import PlayListLabel
from playList import PlayList
from sliderVloum import SliderVloum


class Screen(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.myFont = customtkinter.CTkFont("MV Boli", size=30)
        self.myFontSmall = customtkinter.CTkFont("MV Boli", size=15)

        # self.parent = Parent()

        self.geometry("1000x750")
        # column
        self.columnconfigure((0, 2, 3), weight=0)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(4, weight=1)

        # print(self.indexMusic, "main")
        # row
        # self.rowconfigure((0, 2, 3), weight=0)

        # MusicName

        self.MusicName = MusicName(self.myFont, master=self)
        self.MusicName.grid(column=1, row=0, pady=20, )

        # image album
        self.imageAlbum = ImageAlbume(master=self)
        self.imageAlbum.grid(column=1, row=1)

        # vloum
        self.vloum = SliderVloum(self, )
        self.vloum.grid(column=2, row=1, sticky="nswe")

        # progress
        self.progress = Progress(
            master=self, myFont=self.myFontSmall)
        self.progress.grid(row=3, columnspan=4,
                           sticky="nswe", pady=(0, 15), padx=10)

        # playList
        self.playListLabel = PlayListLabel(master=self, myFont=self.myFont)
        self.playListLabel.grid(column=4, row=0,
                                pady=(0, 10), padx=15)

        self.playList = PlayList(
            master=self, musicNameClass=self.MusicName, imageClass=self.imageAlbum, progress=self.progress)
        self.playList.grid(column=4, row=1, rowspan=3,
                           sticky="nswe", pady=(0, 10), padx=15)
        # controller
        self.controller = Controller(
            playListClass=self.playList, titleSong=self.MusicName, imageAlbum=self.imageAlbum, progress=self.progress, master=self)
        self.controller.grid(row=2, columnspan=4,
                             sticky="nswe", pady=10, padx=10)

        self.progress.controller = self.controller

        self.bind("<MouseWheel>", self.handelVolum)

    def handelVolum(self, value):
        self.vloum.handelMouseVolum(value.delta)


if __name__ == "__main__":
    screen = Screen()
    screen.mainloop()
