# sjtu_cs249_ass1

Assignment 1 - Heap Sort

Group No.04: Yiwen Zhang 张易文, Kaixi Liu 刘铠溪, Haocheng Zhao 赵浩丞, Jiayi Li 李佳忆, Leyan Lin 林乐研

#### How to Run
- Make sure Python 3.x is properly installed with Tcl/Tk
- Unzip the file (since you're already reading this, you've probably done that already)
- Open Terminal/Command Line
- Switch to the working directory of this readme file
- Run `main.py` using Python 3.x
- If an error message appears saying "tkinter package not found", open up the Python file ('`main.py`') and change the first line from `from tkinter import *` to `from Tkinter import *`

#### Assumptions & Justifications:
- Integers are used when inserting to heap and building heap with files
- While insert numbers to the heap, multiple numbers can be inserted to the list/heap at once
- When the heap is built by file, we read every numbers in the file and ignoring all other characters. Then, all the numbers read will be **added** to the list (instead of replacing the original list)
- "Remove Max" removes the maximum number *completely and permanently* from the list/heap
- "Restart" clears all the data and return to main page (welcome page)
