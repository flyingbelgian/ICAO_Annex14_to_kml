import logging


# Define tags used in kml and how many of those are expected in a kml with
# exactly 2 points defined, to avoid trying to parse an incompatible file
# TODO: allow for KML to have multiple runways
name_start = "<name>"  # start tag
name_end = "</name>"  # end tag
valid_name_count_nominal = 4  # how many of these tags are expected in file
coord_start = "<coordinates>"  # start tag
coord_end = "</coordinates>"  # end tag
valid_coord_count_nominal = 2  # how many of these tags are expected in file


class ReadKML:

    def __init__(self, file):
        self.file = file

    def validFileName(self):
        '''Check that the filename has the .kml suffix'''
        if self.file[-4:] == ".kml":
            logging.debug("Filename has .kml suffix")
            return True
        else:
            return False

    def validFileContent(self):
        '''Check that KML file contains exactly 2 points and can be parsed'''
        with open(self.file, 'rt', encoding="utf-8") as file:
            self.file_content = file.read()

        # Add 1 to valid counts to account for trailing bit when splitting string
        valid_name_count = valid_name_count_nominal + 1
        valid_coord_count = valid_coord_count_nominal + 1
        # Count actual occurances of the tag in the file
        name_count = len(self.file_content.split(name_start))
        coord_count = len(self.file_content.split(coord_start))

        if name_count == valid_name_count or coord_count == valid_coord_count:
            logging.debug("File content is valid")
            return True
        else:
            return False

# TODO: ability to read data for multiple runways
    def getRwyEndData(self):
        '''Generate library with point names and coordinates if valid file'''
        rwyend_data = []
        for i in range(2):
            data_entry = {}
            name_raw = self.file_content.split(name_start)[i + 3]
            data_entry["name"] = name_raw.split(name_end)[0]
            coord_raw = self.file_content.split(coord_start)[i + 1]
            coord_list = coord_raw.split(coord_end)[0]
            coords = coord_list.split(",")
            data_entry["lat"] = float(coords[1])
            data_entry["lon"] = float(coords[0])
            rwyend_data.append(data_entry)
        return rwyend_data
