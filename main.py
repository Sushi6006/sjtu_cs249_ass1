from tkinter import *
from algo import *

#TODO: build heap by file??

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
        self.menu_page = ActionPage(self.root, self)

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
        self.title = Label(self.main_frame, text="THE HEAP SORT W/ GUI", font=GUI.FONT)
        self.start_button = Button(self.main_frame, text=" Start ", command=self.start)
        self.title.pack(pady=15)
        self.start_button.pack(pady=15)

    def start(self):
        self.gui_object.switch_page(self.gui_object.menu_page)


class ActionPage:
    def __init__(self, window, gui_object):
        # load info from parents
        self.root = window
        self.gui_object = gui_object

        # create elements for the menu
        self.main_frame = Frame(self.root)
        self.menu_title = Label(self.main_frame, text="")

        # insert
        self.insert_frame = Frame(self.main_frame)
        self.insert_label = Label(self.insert_frame, text="Number to Insert:")
        self.insert_entry = Entry(self.insert_frame)
        self.insert_button = Button(self.insert_frame, text=" Insert ", command=self.insert_node)
        self.insert_label.grid(row=0, column=0)
        self.insert_entry.grid(row=0, column=1)
        self.insert_button.grid(row=0, column=2)

        # get size
        self.size_frame = Frame(self.main_frame)
        self.size_button = Button(self.size_frame, text=" Get Size ", command=self.get_size)
        self.size_button.pack()

        # remove max
        self.remove_max_frame = Frame(self.main_frame)
        self.remove_max_button = Button(self.remove_max_frame, text=" Remove Max ", command=self.remove_max)
        self.remove_max_button.pack()

        # get Max
        self.get_max_frame = Frame(self.main_frame)
        self.get_max_button = Button(self.get_max_frame, text=" Get Max ", command=self.get_max)
        self.get_max_button.pack()

        # sort
        self.sort_frame = Frame(self.main_frame)
        self.sort_button = Button(self.sort_frame, text=" Heap Sort ", command=self.sort)
        self.sort_button.pack()

        # build by file
        self.build_frame = Frame(self.main_frame)
        self.build_button = Button(self.build_frame, text=" Build Heap by File ", command=self.build_heap)
        self.build_button.pack()

        # back
        self.back_button = Button(self.main_frame, text=" Restart ", command=self.restart)

        # pack all the frames
        self.insert_frame.pack(pady=10)
        self.size_frame.pack(pady=10)
        self.remove_max_frame.pack(pady=10)
        self.get_max_frame.pack(pady=10)
        self.sort_frame.pack(pady=10)
        self.build_frame.pack(pady=10)
        self.back_button.pack(pady=30)

        # i did not want to mix gui with the algorithms
        # but
        # i cant be fucked
        self.num_list = []


    def get_size(self):
        title = "Size of Heap"
        msg = "The size of the heap is " + str(len(self.num_list))
        self.pop_message(title, msg)

    def insert_node(self):

        # algorithmatically insert the number
        number_to_insert = int(self.insert_entry.get())
        self.num_list.append(number_to_insert)
        self.num_list = heapify(self.num_list, 0, len(self.num_list))

        # gui
        self.insert_entry.delete(0, END)  # empty the entry
        title = "Insert Successful"
        msg = f'The number {number_to_insert} has been inserted.\nThe new heap is {str(self.num_list)}'
        self.pop_message(title, msg)

    def remove_max(self):
        self.num_list = heapify(self.num_list, 0, len(self.num_list))
        removed_num = self.num_list.pop(0)
        title = "Max Removed"
        msg = f'The number {removed_num} has been removed\nThe new heap is {str(self.num_list)}'
        self.pop_message(title, msg)

    def get_max(self):  # which does not sort nor heapify the list
        title = "Max Found"
        max_num = heapify(self.num_list, 0, len(self.num_list))[0]
        msg = f'The max number in the heap is {max_num}'
        self.pop_message(title, msg)

    def sort(self):
        self.num_list = heap_sort(self.num_list)
        title = "List Sorted"
        msg = f'The list has been sorted using leap\nThe new list is {self.num_list}'
        self.pop_message(title, msg)

    def build_heap(self):
        pass

    def pop_message(self, title, msg):
        popup = Tk()
        popup.title(title)
        label = Label(popup, text=msg)
        back_button = Button(popup, text=" Okay ", command=popup.destroy)
        label.pack()
        back_button.pack()
        popup.mainloop()

    def restart(self):
        self.num_list = []
        self.gui_object.switch_page(self.gui_object.main_page)


#TODO: status_page? make all above in a notification window?

GUI()
