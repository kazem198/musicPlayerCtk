import customtkinter


class PlayListLabel(customtkinter.CTkFrame):
    def __init__(self, myFont, master=None):
        super().__init__(master)
        self._fg_color = "transparent"
        self.myFont = myFont

        self.label = customtkinter. CTkLabel(
            self, text="play List", font=self.myFont)

        # self.label.grid(column=0, row=0)
        self.label.pack()
