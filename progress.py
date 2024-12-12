import customtkinter
import music_tag
import time


class Progress(customtkinter.CTkFrame):
    def __init__(self, myFont, controller=None,  master=None):
        super().__init__(master)

        self.master = master
        self.myFontSmall = myFont
        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.controller = controller
        self.length = 0

        self.lblStart = customtkinter.CTkLabel(
            self, text="00:00", font=self.myFontSmall)

        self.lblStart.grid(column=0, row=0)

        self.progrss = customtkinter.CTkSlider(self, height=20, fg_color=(
            "#80ff00", "#483D8B"), progress_color=("#1E90FF", "#B0E0E6"), from_=0, to=100,
            command=self.handelSlider)

        self.progrss.grid(column=1, row=0, sticky="we",)

        self.lblend = customtkinter.CTkLabel(
            self, text="00:00", font=self.myFontSmall)
        self.lblend.grid(column=2, row=0)

        self.progrss.set(0)

    def getName(self, getName):
        self.nameSong = getName
        # print(self.nameSong, "progress")
        self.getImageSong()
        self.progrss.set(0)

    def getImageSong(self):
        f = music_tag.load_file(f"playList/{self.nameSong}")
        self.length = f['#length']

        self.progrss.configure(to=int(self.length))

        totalstring = time.strftime("%M:%S", time.gmtime(int(self.length)))
        self.lblend.configure(text=totalstring)

    def moveProgress(self, value):

        self.progrss.set(value)
        totalstring = time.strftime("%M:%S", time.gmtime(value))
        self.lblStart.configure(text=totalstring)
        if (int(self.length) == value):
            self.controller.handelEndSong()

    def handelSlider(self, val):
        self.progrss.set(val)
        self.controller.handelSliderControlldr(val)
