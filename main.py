import logging
import tkinter
import tkinter.filedialog

#Setup debugging log
logging.basicConfig(filename='log.txt', encoding='utf-8', level=logging.DEBUG)

#########################################################
# Interface Setup

# Main/root window setup
logging.info("Create main window")
window = tkinter.Tk()
color_bg = "#adadad"
font_main = ('Courier', 12, 'bold')
window.title("Annex 14 to KML")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20, bg=color_bg)

# Frames for various sections of the window
logging.info("Create frames")
frame_airport = tkinter.Frame(window, bg=color_bg)
frame_airport.grid(column=0, row=0)
frame_classifications = tkinter.Frame(window, bg=color_bg)
frame_classifications.grid(column=0, row=1)
frame_kml = tkinter.Frame(window, bg=color_bg)
frame_kml.grid(column=0, row=2)
frame_summary = tkinter.Frame(window, bg=color_bg)
frame_summary.grid(column=0, row=3)

# Track input variables for interactive UI
logging.info("Create tracked input variables")
input_classification = tkinter.StringVar(window, value="RWY Classification Selected")
input_kml = tkinter.StringVar(window, value="KML File Name & Path")
input_airport = tkinter.StringVar(window, value="Airport Name or Code")

# Labels for displaying selected variables 
logging.info("Create label for kml filename")
label_kml = tkinter.Label(frame_summary, text=input_kml.get(), width=30, justify='right', anchor='e')
label_kml.grid(column=0, row=0)
logging.info("Create label for runway classification")
label_classification = tkinter.Label(frame_summary, text=input_classification.get(), width=30, justify='right', anchor='e')
label_classification.grid(column=0, row=1)
logging.info("Create label for airport name/code")
label_airport = tkinter.Label(frame_summary, text=input_airport.get(), width=30, justify='right', anchor='e')
label_airport.grid(column=0, row=2)

# Button prompts selection of KML file with runway coordinates
def selectKML():
    '''Opens file selection dialog for selecting KML and updates value in summary frame's KML label'''
    logging.info("Start KML selection dialog and update")
    filename = tkinter.filedialog.askopenfilename()
    input_kml.set(filename)
    label_kml['text']=filename
button_kml = tkinter.Button(frame_kml, text="Select KML File", command=selectKML)
button_kml.grid(column=0,row=0)

# Input field for airport name / code
def airport_update(*args):
    '''Update the label to represent currently entered airport name/code'''
    logging.info("Update airport name/code")
    label_airport.config(text='')
    label_airport.config(text=input_airport.get())
aerodrome = tkinter.Entry(frame_airport, textvariable=input_airport, width=30, justify='right')
aerodrome.grid(column=0,row=0,columnspan=2, sticky="E", padx=(30,0))
input_airport.trace('w', airport_update)

#Populate window with radio buttons for user to select RWY classification
def classification_update():
    '''Update the label to represent currently selected classification'''
    label_classification['text'] = input_classification.get()
rwy_classifications = (
    "Non-Instrument",
    "Non-Precision",
    "Precision Cat I",
    "Precision Cat II"
)
for i in range(len(rwy_classifications)):
    description = rwy_classifications[i]
    b = tkinter.Radiobutton(
        frame_classifications,
        bg=color_bg,
        text=description,
        value=description,
        var=input_classification,
        command=classification_update)
    b.grid(column=0,row=i,sticky="W")

#TODO - Read KML file


#TODO - Identify RWY ends

#TODO - Calculate runway length

#TODO - Determine runway code

#TODO - Determine surfaces to be generated based on RWY code and classification

#TODO - New button to be generated to allow submission of all parameters

# def summarise():
#         label.config(text=(classification.get() + " " + source_kml))

# button = tkinter.Button(window, text="Confirm", command=summarise)
# button.grid(column=1,row=3)

## window can close when all settings are set and input received
window.mainloop()

#TODO - Generate parameters for surfaces