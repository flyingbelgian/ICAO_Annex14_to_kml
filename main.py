import gui
import logging
import readkml


# Clear content of log file
with open('log.txt', 'w') as file:
    file.write("")
# Setup debugging log
logging.basicConfig(filename='log.txt', encoding='utf-8', level=logging.DEBUG)

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
        kml = readkml.ReadKML(airport_kml)
        if kml.validFileName() and kml.validFileContent():
            rwyend_data = kml.getRwyEndData()
            logging.debug(f"Rwy end data: {rwyend_data}")
            valid_input = True

        # TODO - Calculate runway length

        # TODO - Determine runway code

        # TODO - Determine surfaces to be generated based on RWY code and classification

        # TODO - New button to be generated to allow submission of all parameters

        # TODO - Generate parameters for surfaces
