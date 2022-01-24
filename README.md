# ICAO_Annex14_to_kml

This script will generate a KML that includes the basic Annex 14 Obstacle Assessment Surfaces based on user parameters.

TODO:
- User input window:
  - Airport name and/or code
  - File select KML with RWY coordinates (THRxx, CWYxx)
  - RWY classification (non-instrument, non-precision, precision cat I, precision Cat II)
    - impossible to select Cat II for Code 1 or 2 RWY
  - Output file name
  - Window shows
    - calculated runway length
    - runway code
    - surfaces that will be generated
- Generate kml
  - Include calculated surfaces
- Generate parameter file
