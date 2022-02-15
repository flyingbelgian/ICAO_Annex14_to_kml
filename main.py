import gui
import logging
import rwy_assess
import kml_read


# Clear content of log file
with open('log.txt', 'w') as file:
    file.write("")
# Setup debugging log
logging.basicConfig(filename='log.txt', encoding='utf-8', level=logging.DEBUG)

first_run = True
valid_input = False
airport_name = "Airport Code/Name"
airport_name_valid = False
airport_class = "Airport Classification"
airport_class_valid = False
airport_kml = "Airport KML File"
rwyend_data = []

while not valid_input:
    # Main/root window setup
    logging.info("Create main window")
    root = gui.Window(airport_name, airport_class, airport_kml)
    if first_run:
        pass
    else:
        root.promptInvalidInput()

    # window can close when all settings are set and input received
    root.mainloop()

    airport_name = root.airport_name
    if airport_name != "Airport Code/Name":
        logging.debug("Airport Code/Name is valid")
        airport_name_valid = True

    airport_class = root.airport_classification
    if airport_class != "Airport Classification":
        logging.debug("Airport Classification is valid")
        airport_class_valid = True

    if airport_name_valid and airport_class_valid:
        airport_kml = root.airport_kml
        kml = kml_read.ReadKML(airport_kml)
        if kml.validFileName() and kml.validFileContent():
            rwyend_data = kml.getRwyEndData()
            logging.debug(f"Rwy end data: {rwyend_data}")
            rwy_data_raw = rwy_assess.DistSet(rwyend_data)
            rwy_data = {
                'airport': airport_name,
                'class': airport_class,
                'code': rwy_data_raw.code,
                'length': rwy_data_raw.dist,
                'bearing_to': rwy_data_raw.bear_to,
                'bearing_from': rwy_data_raw.bear_from,
            }
            prompt = gui.ParameterDisplay(rwy_data)
            prompt.mainloop()
            valid_input = True

    first_run = False

    # TODO - Calculate runway length

    # TODO - Determine runway code

    # TODO - Determine surfaces to be generated based on RWY code and classification

    # TODO - New button to be generated to allow submission of all parameters

    # TODO - Generate parameters for surfaces
