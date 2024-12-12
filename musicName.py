import customtkinter


class MusicName(customtkinter.CTkFrame):
    def __init__(self, myfont, master=None):
        super().__init__(master)
        self.myFont = myfont
        self.master = master

        self._fg_color = "transparent"

        self.label = customtkinter. CTkLabel(
            self, text=" ", font=self.myFont)

        self.label.pack()

    def change(self, nameMusic):
        self.label.configure(text=nameMusic)
