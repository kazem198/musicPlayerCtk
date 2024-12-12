import customtkinter
from PIL import Image
import pygame


class SliderVloum(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.volum = customtkinter.DoubleVar(self, .3)
        # print(self.volum.get())

        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        self.upVloum = customtkinter.CTkLabel(self,
                                              image=customtkinter.CTkImage(light_image=Image.open("./assets/volumeUp.jpg"),
                                                                           dark_image=Image.open(
                                                  "./assets/volumeDarkup.jpg"), size=(20, 20)

                                              ), text="")
        self.downVloum = customtkinter.CTkLabel(self,
                                                image=customtkinter.CTkImage(light_image=Image.open("./assets/volumedown.jpg"),
                                                                             dark_image=Image.open(
                                                    "./assets/volumeDarkdown.jpg"), size=(20, 20)
                                                ), text="")

        self.progrss = customtkinter.CTkSlider(
            self, orientation="vertical", command=self.handelVolum, from_=0, to=1, variable=self.volum)

        self.upVloum.grid(column=0, row=0, sticky="nswe", )
        self.progrss.grid(column=0, row=1, sticky="nswe", )
        self.downVloum.grid(column=0, row=2, sticky="nswe", )

    def handelVolum(self, value):
        pygame.mixer.music.set_volume(value)

    def handelMouseVolum(self, value):
        volum = self.volum.get()

        if value == -120:

            self.volum.set(volum - .05)
        elif value == 120:
            self.volum.set(volum + .05)

        pygame.mixer.music.set_volume(self.volum.get())
