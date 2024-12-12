import customtkinter
from PIL import Image
import music_tag
import io


class ImageAlbume(customtkinter.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.nameSong = None

        self.myImage = customtkinter.CTkLabel(
            self, text="", image=customtkinter.CTkImage(Image.open("assets/album.jpg"), size=(500, 500)))
        self.myImage.pack()

    def getName(self, getName):
        self.nameSong = getName
        # print(self.nameSong, "imageAlbum")
        self.getImageSong()

    def getImageSong(self):
        f = music_tag.load_file(f"playList/{self.nameSong}")
        image = f['artwork'].first.data

        image = Image.open(io.BytesIO(image))
        image.save('img.png')
        self.myImage.configure(image=customtkinter.CTkImage(
            Image.open('img.png'), size=(500, 500)))

        # print(type(image))
