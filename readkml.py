import fastkml.kml

with open ("YSBK.kml", 'rt', encoding="utf-8") as file:
    doc = file.read() 
object_kml = fastkml.kml.KML()
object_kml.from_string(doc)
# features = list(object_kml.features())
# print(len(features))