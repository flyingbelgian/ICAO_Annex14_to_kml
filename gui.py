import tkinter
import tkinter.filedialog
import tkinter.messagebox
from windows import set_dpi_awareness

set_dpi_awareness()

color_bg_dark = "#adadad"
color_bg_light = "#cccccc"


class Window(tkinter.Tk):
    def __init__(self,
                 airport_name,
                 airport_classification,
                 airport_kml,
                 *args, **kwargs):
        super().__init__()
        self.title("Annex 14 to KML")
        self.resizable(False, False)
        self.config(padx=20, pady=20, bg=color_bg_dark)
        self.airport_name = airport_name
        self.airport_classification = airport_classification
        self.airport_kml = airport_kml

        # Frames for various sections of the window
        frame_airport = tkinter.Frame(self, bg=color_bg_dark)
        frame_airport.grid(column=0, row=0, pady=(0, 10), sticky='ew')
        frame_classifications = tkinter.Frame(self, bg=color_bg_light)
        frame_classifications.grid(column=0, row=1, sticky='ew')
        frame_kml = tkinter.Frame(self, bg=color_bg_dark)
        frame_kml.grid(column=0, row=2, pady=(10, 0), sticky='ew')
        frame_buttons = tkinter.Frame(self, bg=color_bg_dark)
        frame_buttons.grid(column=1, row=0, rowspan=3, padx=(20, 0), sticky='ns')
        frame_buttons.rowconfigure(0, weight=1)

        def selectKML():
            '''Opens file selection dialog for selecting KML'''
            '''and saves it to airport_kml variable'''
            self.airport_kml = tkinter.filedialog.askopenfilename()
        button_kml = tkinter.Button(frame_kml, text="Select KML File", command=selectKML)
        button_kml.grid(column=0, row=0, sticky='ew')

        def airport_update(*args):
            '''Update the airport_name variable with user input'''
            self.airport_name = input_airport.get()
        input_airport = tkinter.StringVar(self, value=self.airport_name)
        aerodrome = tkinter.Entry(frame_airport, textvariable=input_airport,
                                  width=20, justify='left')
        aerodrome.grid(column=0, row=0, columnspan=2, sticky='w')
        input_airport.trace('w', airport_update)

        def classification_update():
            '''Update the airport_classification variable with user input'''
            self.airport_classification = input_classification.get()
        input_classification = tkinter.StringVar(self, value=self.airport_classification)
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
                bg=color_bg_light,
                text=description,
                value=description,
                var=input_classification,
                command=classification_update)
            b.grid(column=0, row=i, sticky='w')

        button_quit = tkinter.Button(frame_buttons, text="Quit", bg=color_bg_dark, command=quit)
        button_quit.grid(column=0, row=0, sticky='es')
        button_submit = tkinter.Button(frame_buttons, text="Submit", command=self.destroy)
        button_submit.grid(column=0, row=1, sticky='es', pady=(10, 0))

    def promptInvalidInput(self):
        tkinter.messagebox.showinfo(
            "Invalid Input",
            "Annex 14 to KML error:\n\n" +
            "One of the input paramaters is incorrect, please check and re-submit."
        )


class ParameterDisplay(tkinter.Tk):
    def __init__(self, parameters, *args, **kwards):
        super().__init__()
        self.title("Annex 14 to KML: Parameters")
        self.resizable(False, False)
        self.config(padx=20, pady=20, bg=color_bg_dark)
        label_airport_name = tkinter.Label(self, text=parameters['airport'])
        label_airport_name.pack()
        label_rwy_code = tkinter.Label(self, text=parameters['code'])
        label_rwy_code.pack()
        label_rwy_length = tkinter.Label(self, text=parameters['length'])
        label_rwy_length.pack()
        label_rwy_classification = tkinter.Label(self, text=parameters['class'])
        label_rwy_classification.pack()
        label_rwy_bearing_to = tkinter.Label(self, text=parameters['bearing_to'])
        label_rwy_bearing_to.pack()
        label_rwy_bearing_from = tkinter.Label(self, text=parameters['bearing_from'])
        label_rwy_bearing_from.pack()
