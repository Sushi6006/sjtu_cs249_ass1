from tkinter import *


def get_size():
    pass

def insert():
    pass

def remove_max():
    pass

def get_max():
    pass

def heap_sort():
    pass

def build_heap_by_file():
    pass


class GUI:
    WIDTH = 600
    HEIGHT = 400
    TITLE = "THE FULL MARK HEAP SORT"
    FONT = ("Courier", 40)

    def __init__(self):

        # init window
        self.root = Tk()
        self.root.title(self.TITLE)
        self.root.geometry("{}x{}".format(self.WIDTH, self.HEIGHT))
        self.root.resizable(False, False)
        self.current_frame = None

        # create windows
        self.main_page = MainPage(self.root, self)
        self.menu_page = MenuPage(self.root, self)

        # start
        self.switch_page(self.main_page)

        # mainloop
        self.root.mainloop()

    #TODO: make original page optional?
    #TODO: a way to unpack whatever is packed?
    def switch_page(self, new_page):
        if self.current_frame:
            self.current_frame.place_forget()
        new_page.main_frame.place(relx=.5, rely=.5, anchor="c")
        self.current_frame = new_page.main_frame


class MainPage:
    def __init__(self, window, gui_object):
        # load info from parents
        self.root = window
        self.gui_object = gui_object

        # create elements on the main page aka welcome page
        self.main_frame = Frame(self.root)
        self.title = Label(self.main_frame, text="THE FULL MARK HEAP SORT", font=GUI.FONT)
        self.start_button = Button(self.main_frame, text="Mark: 120%...? (Start)", command=self.start)
        self.title.pack(pady=15)
        self.start_button.pack(pady=15)

    def start(self):
        self.gui_object.switch_page(self.gui_object.menu_page)


class MenuPage:
    def __init__(self, window, gui_object):
        # load info from parents
        self.root = window
        self.gui_object = gui_object

        # create elements for the menu
        self.main_frame = Frame(self.root)
        self.menu_title = Label(self.main_frame, text="")

        # get size
        self.size_frame = Frame(self.main_frame)
        self.size_button = Button(self.size_frame, text="Get Size", command=self.get_size)

        # insert
        self.insert_frame = Frame(self.main_frame)
        self.insert_label = Label(self.insert_frame, text="Number to Insert:")
        self.insert_entry = Entry(self.insert_frame)
        self.insert_button = Button(self.insert_frame, text="Insert", command=self.insert_node)

        # remove max
        self.remove_max_frame = Frame(self.main_frame)
        self.remove_max_button = Button(self.remove_max_frame, text="Remove Max", command=self.remove_max)

        # get Max
        self.get_max_frame = Frame(self.main_frame)
        self.get_max_button = Button(self.get_max_frame, text="Get Max", command=self.get_max)

        # sort
        self.sort_frame = Frame(self.main_frame)
        self.sort_button = Button(self.sort_frame, text="Heap Sort", command=self.sort)

        # build by file
        self.build_frame = Frame(self.main_frame)
        self.build_button = Button(self.build_frame, text="Build Heap by File", command=self.build_heap)

        # pack all the frames
        self.size_frame.pack()
        self.insert_frame.pack()
        self.remove_max_frame.pack()
        self.get_max_frame.pack()
        self.sort_frame.pack()
        self.build_frame.pack()

    def get_size(self):
        pass

    def insert_node(self):
        pass

    def remove_max(self):
        pass

    def get_max(self):
        pass

    def sort(self):
        pass

    def build_heap(self):
        pass


#TODO: status_page? make all above in a notification window?


GUI()
