# - HOW TO USE -
################
# 1. You must manually edit the strings below
# to suit your needs. 

# 2. The .SVG file must have #000000 values
# as the default when submitting.


# General --
import shutil
import sys
import glob
import os.path
# Tkinter --
from tkinter import * 
from tkinter import filedialog 
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askopenfilenames


# Target Directory.
list_of_files = glob.glob('target/*.svg')


# Look for all '.svg' files in '/target/'.
for file_name in list_of_files:
    print("File Loaded : ", file_name)

# Make copies of original files submitted.
for f in list_of_files:
    shutil.copy(f, 'originals')
    print("File Backed-up : ", f)



# Functions --
# Transform the objects to desired colors.
def Transform_Color():

    # Hidden Tkinter Window.
    hidden_window = Tk().withdraw()
    filename = askopenfilenames()
    filename = str(filename)
    result = askcolor(title = filename)

    for file_name in list_of_files:

        # Read input file.
        doc = open(file_name, "rt")
        data = doc.read()

        # Circle strings
        data = data.replace('style="fill:#000000;', 'style="fill:{};'.format(result[1]))
        data = data.replace('style="fill:#000000"', 'style="fill:{}"'.format(result[1]))
        
        # Square strings
        data = data.replace('style="fill:#000000"', 'style="fill:{}"'.format(result[1]))
        data = data.replace('fill:#000000;', 'fill:{};'.format(result[1]))
        
        # Write Changes.
        doc = open(file_name, "wt")

        # Overrite the input file with the resulting data.
        doc.write(data)
        doc.close()


# Apply Square on objects.
def Transform_to_Square():

    # Hidden Tkinter Window.
    hidden_window = Tk().withdraw()
    filename = askopenfilenames()
    filename = str(filename)

    for file_name in list_of_files:

        # Read input file.
        doc = open(file_name, "rt")
        data = doc.read()

        # Square Coordinates
        data = data.replace('d="m 150.485,0.001 c 49.5244,-0.30805092 97.99005,26.13918 124.885,67.66 29.14949,43.41669 32.66869,102.35469 9.029,148.98 -22.3226,45.72399 -69.26524,78.27982 -120.017,82.677 C 116.79963,304.27157 67.626954,284.53159 36.597,248.141 4.2284143,211.43134 -7.8772602,158.34647 5.079,111.186 18.20087,60.591626 59.782145,18.758853 110.292,5.321 c 13.07378,-3.5887368 26.6371,-5.36778112 40.193,-5.32 z m -0.919,16 C 104.07954,15.682674 59.676029,40.73106 36.035,79.522 10.237529,120.258 9.3382219,175.08668 33.754,216.66 c 22.507056,39.83833 66.53845,66.428 112.351,67.284 44.86675,1.74378 89.5149,-21.18229 114.552,-58.394 27.38615,-39.18451 30.93913,-93.31402 9.052,-135.793 C 249.0838,48.105271 205.50868,18.954337 159.041,16.3 c -3.15359,-0.209033 -6.31449,-0.309606 -9.475,-0.299 z"', 'd="m 269.925,0.001 c 16.09972,-0.31510169 30.49384,14.17259 30.075,30.27 -0.1061,80.84884 0.21081,161.71193 -0.156,242.552 C 298.61375,288.46369 283.6522,301.15677 268.03194,300 187.74879,299.89388 107.45138,300.21085 27.177,299.844 11.536306,298.61375 -1.1567723,283.6522 0,268.03194 0.10612413,187.74879 -0.21084904,107.45138 0.156,27.177 1.3862455,11.536306 16.347799,-1.1567723 31.968056,0 111.28704,6.6687171e-4 190.60602,-0.00133361 269.925,0.001 Z M 30.296,16 C 21.973925,15.732721 14.968163,23.80142 16,31.993056 16.103721,111.93578 15.794138,191.89863 16.152,271.829 17.110107,279.66576 25.171747,285.14519 32.841585,284 112.50147,283.89626 192.18147,284.20589 271.829,283.848 279.6657,282.88989 285.14515,274.82817 284,267.15842 283.89626,187.49853 284.20589,107.81853 283.848,28.171 282.89006,20.334162 274.82812,14.854983 267.15842,16 188.20428,16 109.25014,16 30.296,16 Z"')

        # Write Changes.
        doc = open(file_name, "wt")

        # Overrite the input file with the resulting data.
        doc.write(data)
        doc.close()


# Apply Circle on objects.
def Transform_to_Circle():

    # Hidden Tkinter Window.
    hidden_window = Tk().withdraw()
    filename = askopenfilenames()
    filename = str(filename)

    for file_name in list_of_files:

        # Read input file.
        doc = open(file_name, "rt")
        data = doc.read()

        # Circle Coordinates
        data = data.replace('d="m 269.925,0.001 c 16.09972,-0.31510169 30.49384,14.17259 30.075,30.27 -0.1061,80.84884 0.21081,161.71193 -0.156,242.552 C 298.61375,288.46369 283.6522,301.15677 268.03194,300 187.74879,299.89388 107.45138,300.21085 27.177,299.844 11.536306,298.61375 -1.1567723,283.6522 0,268.03194 0.10612413,187.74879 -0.21084904,107.45138 0.156,27.177 1.3862455,11.536306 16.347799,-1.1567723 31.968056,0 111.28704,6.6687171e-4 190.60602,-0.00133361 269.925,0.001 Z M 30.296,16 C 21.973925,15.732721 14.968163,23.80142 16,31.993056 16.103721,111.93578 15.794138,191.89863 16.152,271.829 17.110107,279.66576 25.171747,285.14519 32.841585,284 112.50147,283.89626 192.18147,284.20589 271.829,283.848 279.6657,282.88989 285.14515,274.82817 284,267.15842 283.89626,187.49853 284.20589,107.81853 283.848,28.171 282.89006,20.334162 274.82812,14.854983 267.15842,16 188.20428,16 109.25014,16 30.296,16 Z"', 'd="m 150.485,0.001 c 49.5244,-0.30805092 97.99005,26.13918 124.885,67.66 29.14949,43.41669 32.66869,102.35469 9.029,148.98 -22.3226,45.72399 -69.26524,78.27982 -120.017,82.677 C 116.79963,304.27157 67.626954,284.53159 36.597,248.141 4.2284143,211.43134 -7.8772602,158.34647 5.079,111.186 18.20087,60.591626 59.782145,18.758853 110.292,5.321 c 13.07378,-3.5887368 26.6371,-5.36778112 40.193,-5.32 z m -0.919,16 C 104.07954,15.682674 59.676029,40.73106 36.035,79.522 10.237529,120.258 9.3382219,175.08668 33.754,216.66 c 22.507056,39.83833 66.53845,66.428 112.351,67.284 44.86675,1.74378 89.5149,-21.18229 114.552,-58.394 27.38615,-39.18451 30.93913,-93.31402 9.052,-135.793 C 249.0838,48.105271 205.50868,18.954337 159.041,16.3 c -3.15359,-0.209033 -6.31449,-0.309606 -9.475,-0.299 z"')

        # Write Changes.
        doc = open(file_name, "wt")

        # Overrite the input file with the resulting data.
        doc.write(data)
        doc.close()


# Removes the current decoration.
def Remove_Decoration():

    # Hidden Tkinter Window.
    hidden_window = Tk().withdraw()
    filename = askopenfilenames()
    filename = str(filename)

    for file_name in list_of_files:

        # Read input file.
        doc = open(file_name, "rt")
        data = doc.read()

        # Decoration Coordinates
        data = data.replace('d="m 269.925,0.001 c 16.09972,-0.31510169 30.49384,14.17259 30.075,30.27 -0.1061,80.84884 0.21081,161.71193 -0.156,242.552 C 298.61375,288.46369 283.6522,301.15677 268.03194,300 187.74879,299.89388 107.45138,300.21085 27.177,299.844 11.536306,298.61375 -1.1567723,283.6522 0,268.03194 0.10612413,187.74879 -0.21084904,107.45138 0.156,27.177 1.3862455,11.536306 16.347799,-1.1567723 31.968056,0 111.28704,6.6687171e-4 190.60602,-0.00133361 269.925,0.001 Z M 30.296,16 C 21.973925,15.732721 14.968163,23.80142 16,31.993056 16.103721,111.93578 15.794138,191.89863 16.152,271.829 17.110107,279.66576 25.171747,285.14519 32.841585,284 112.50147,283.89626 192.18147,284.20589 271.829,283.848 279.6657,282.88989 285.14515,274.82817 284,267.15842 283.89626,187.49853 284.20589,107.81853 283.848,28.171 282.89006,20.334162 274.82812,14.854983 267.15842,16 188.20428,16 109.25014,16 30.296,16 Z"', '')
        data = data.replace('d="m 150.485,0.001 c 49.5244,-0.30805092 97.99005,26.13918 124.885,67.66 29.14949,43.41669 32.66869,102.35469 9.029,148.98 -22.3226,45.72399 -69.26524,78.27982 -120.017,82.677 C 116.79963,304.27157 67.626954,284.53159 36.597,248.141 4.2284143,211.43134 -7.8772602,158.34647 5.079,111.186 18.20087,60.591626 59.782145,18.758853 110.292,5.321 c 13.07378,-3.5887368 26.6371,-5.36778112 40.193,-5.32 z m -0.919,16 C 104.07954,15.682674 59.676029,40.73106 36.035,79.522 10.237529,120.258 9.3382219,175.08668 33.754,216.66 c 22.507056,39.83833 66.53845,66.428 112.351,67.284 44.86675,1.74378 89.5149,-21.18229 114.552,-58.394 27.38615,-39.18451 30.93913,-93.31402 9.052,-135.793 C 249.0838,48.105271 205.50868,18.954337 159.041,16.3 c -3.15359,-0.209033 -6.31449,-0.309606 -9.475,-0.299 z"', '')        

        # Write Changes.
        doc = open(file_name, "wt")

        # Overrite the input file with the resulting data.
        doc.write(data)
        doc.close()


# Main Tk Window.
root = Tk()
# Title
root.title('TJCS SVG Editor')

# Logo
img=PhotoImage(file='logo.png')
Label(root,image=img).pack(fill='x', padx='10', pady='10')

# Buttons
Button(root, text='Change > Color', command=Transform_Color, height='2', width='15').pack(side='left', padx='10', pady='10')
Button(root, text='Change > Circle', command=Transform_to_Circle, height='2', width='15').pack(side='left', padx='10', pady='10')
Button(root, text='Change > Square', command=Transform_to_Square, height='2', width='15').pack(side='left', padx='10', pady='10')
Button(root, text='Remove > Decoration', command=Remove_Decoration, height='2', width='20').pack(side='left', padx='10', pady='10')

mainloop()