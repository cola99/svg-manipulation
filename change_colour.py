# Library
import sys
from tkinter import * 
from tkinter import filedialog 
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfilename 
 

Tk().withdraw() # Stop default Tk window from showing up.
filename = askopenfilename() # Dialog box and return the path to the selected file.
print(filename)


# Function to replace the colour.
def Replace_Colour():

    result = askcolor(title = "Color palette")
    print(result[1]) # [0] = RGB, [1] = HEX

    doc = open(filename, "rt") # Read input file.

    data = doc.read() # Read file contents to string.

    # Circle strings
    data = data.replace('style="fill:#000000;', 'style="fill:{};'.format(result[1])) #replace all occurrences of the required string
    data = data.replace('style="fill:#000000" /></g></g></g>', 'style="fill:{}" /></g></g></g>'.format(result[1])) #replace all occurrences of the required string

    # Camera strings
    # data = data.replace('style="fill:#000000" d="m 178.937,109.509', 'style="fill:{}"'.format(result[1]))
    # data = data.replace('style="fill:#000000" /></g></g><gid="g15"><g', 'style="fill:{}" /></g></g><gid="g15"><g'.format(result[1]))

    doc.close()

    doc = open("result.svg", "wt") # Open the input file in write mode.

    doc.write(data) # Overrite the input file with the resulting data.
    doc.close()

    sys.exit()


# Tk window details.     
root = Tk()
Button(root, text='Choose Color',command=Replace_Colour).pack(pady=20)
topLabl = Label(root,text="Your file will be saved as: 'result.svg' ")
topLabl.pack()
root.title('Color Changer.')
root.geometry("300x100")
root.resizable(False, False)
mainloop()