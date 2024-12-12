import tkinter.filedialog
import customtkinter
from PIL import Image
from CTkListbox import *
import os
# from tkinter.dialog import Dialog
# import tkinter
import shutil
from tkinter import messagebox


class PlayList(customtkinter.CTkFrame):
    def __init__(self, musicNameClass,  imageClass, progress,  master=None):
        super().__init__(master)
        self.musicNameClass = musicNameClass
        self.nameSong = ""
        self.indexSong = -1
        self.imagClass = imageClass
        self.progress = progress

        self.master = master
        self.rowconfigure(tuple((i for i in range(4))), weight=1)
        self.columnconfigure(0, weight=1)

        self.listbox = CTkListbox(
            master=self, command=self.clickListBox)

        self.listbox.grid(column=0, row=0, rowspan=4,
                          sticky="nswe", columnspan=2)

        imageAdd = customtkinter.CTkImage(light_image=Image.open(
            "./assets/add_light.png"), dark_image=Image.open("./assets/add_dark.png"), size=(30, 30))

        imageRemove = customtkinter.CTkImage(light_image=Image.open(
            "./assets/remove_light.png"), dark_image=Image.open("./assets/remove_dark.png"), size=(30, 30))

        self.btnAdd = customtkinter.CTkButton(
            self, image=imageAdd, text="", fg_color="transparent", command=self.openDialog)
        self.btnRemove = customtkinter.CTkButton(
            self, image=imageRemove, text="", fg_color="transparent", command=self.deleteItem)

        self.btnAdd.grid(column=0, row=4)
        self.btnRemove.grid(column=1, row=4)

        self.playList()

    def playList(self):
        self.listbox.delete("0", "end")
        listPaly = os.listdir("./playList")

        for title in listPaly:

            self.listbox.insert("END", title)
        # print(title[i])

    def openDialog(self):
        try:
            dir = tkinter.filedialog.askopenfilename(
                title="choice music", filetypes=[("mp3 files", ".mp3")])
            # print(dir)
            shutil.copy(dir, "playList")

            self.playList()
            # self.listbox.configure()
        except:

            messagebox.Message(
                self, message="choise one file to add", title="not file").show()

    def deleteItem(self):
        index = self.listbox.curselection()
        name = self.listbox.get(index)

        if index is not None:
            self.listbox.delete(index)

            if os.path.exists(f'./playList/{name}'):
                os.remove(f'./playList/{name}')

    def clickListBox(self, selected_option):
        index = self.listbox.curselection()
        self.nameSong = selected_option
        self.indexSong = index
        # print(self.nameSong, "kazem nameffdf song")
        self.musicNameClass.change(selected_option)
        # self.controllerClass.getName(selected_option, index)
        self.imagClass.getName(selected_option)
        self.progress.getName(selected_option)

    def getName(self):

        return (self.nameSong, self.indexSong)

    def activeListbox(self, index):
        try:
            self.listbox.activate(index)
        except IndexError:
            self.listbox.activate(0)

    def deActiveListbox(self):

        # self.listbox.activate(index)

        self.listbox.deactivate(self.indexSong)

        self.nameSong = ""
        self.indexSong = -1
