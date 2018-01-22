# Import libraries
import pyart
import os

# Find directory for NEXRAD files

radar = pyart.io.read_nexrad_archive("G:\RadarData\KRLX20160811_001004_V06")


print(radar.latitude["data"], ",", radar.longitude["data"])
# Import NEXRAD files using PyArt.io.read to return radar object

# Begin Radar cleaning

# Find gating objects (things that block radar signatures like trees or mountains) using
# pyart.correct.find_objects

# pyart.retreive.kdp_maesaka to get differential phase.  Noisy differential phase is a sign of
# biological activity


# compute noise
