# Import libraries
import pyart
import matplotlib.pyplot as plt

# Find directory for NEXRAD files

radar = pyart.io.read_nexrad_archive("G:\RadarData\KFFC20160811_150625_V06")


print("Lat/Long"
      "n", radar.latitude["data"], ",", radar.longitude["data"])
print("Sweep Mode\n", radar.sweep_mode)
print("Sweep Number\n", radar.sweep_number)
print("Fixed Angle\n", radar.fixed_angle)
print("NSweeps\n", radar.nsweeps)
print("Elevation \n", radar.get_elevation(1))
print("Radar Fields \n",radar.fields)
print("VCP Pattern \n", radar.metadata["vcp_pattern"])
vcppatt = radar.metadata["vcp_pattern"]
if vcppatt == 32 or vcppatt == 31:
      print("Select radar, it's good for finding birds.")
radarplot = pyart.graph.RadarDisplay(radar)
print("Radar Plot\n", radarplot.loc)
print("\n\n\n\n")
display = pyart.graph.RadarDisplay(radar)
fig = plt.figure(figsize=(6,5))

ax = fig.add_subplot(111)
display.plot('velocity', 0, title = 'NEXRAD Velocity',
             vmin=-1, vmax=1, colorbar_label='', ax=ax)
display.plot_range_ring(radar.range['data'][-1]/ 1200., ax=ax)
display.set_limits(xlim=(-400,400), ylim=(-400, 400), ax=ax)
plt.show()
#drawradar = pyart.core.antenna_to_cartesian(radar.range, radar.get_azimuth(1), radar.get_elevation)
#print(drawradar)
# Import NEXRAD files using PyArt.io.read to return radar object

# Begin Radar cleaning

# Find gating objects (things that block radar signatures like trees or mountains) using
# pyart.correct.find_objects

# pyart.retreive.kdp_maesaka to get differential phase.  Noisy differential phase is a sign of
# biological activity


# compute noise
