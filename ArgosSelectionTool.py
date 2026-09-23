#-------------------------------------------------------------
# ArgosSelectionTool.py
#
# Description: Reads in an Argos tracking data file and allows
#   the user to identify the tracked sitings found within a 
#   specified bounding box.
#
# Author: Tallulah Bowden (tsb66@duke.edu)
# Date:   September 22, 2026
#--------------------------------------------------------------

# Create the geographic selection box
the_box = {
    "x_min" : 34.00,
    "y_min" : -76.00,
    "x_max" : 34.50,
    "y_max" : -75.00
}

# Copy and paste a line of data as the lineString variable value
lineString = '10154641239,true,2019-05-14 16:05:36.000,-75.52452,34.68404,,0.0,-121.0,4.0167962144E8,3481.0,217,"46",34.68404,34.68404,"0",-75.52452,-75.52452,10,0,3,51.0,602.0,3818.0,3173.0,4,4,0,1,"1",,,"argos-doppler-shift","Pterodroma hasitata","174441","HA09","Satellite tracking of black-capped petrels, 2019"'

# Use the split command to parse the items in lineString into a list object
line_data = lineString.split(",")

# Assign variables to specific items in the list
event_id = line_data[0] # Argos tracking event ID ("event-id")
timestamp = line_data[2] # Observation date ("timestamp")
lat = float(line_data[4]) # Observation latitude ("location-lat")
lon = float(line_data[3]) # Observation longitude ("location-lon")
lc = line_data[14] # Observation location class ("argos:lc")
tag_id = line_data[33] # Tag identified ("tag-local-identifier")

# Evaluate latitude and longitude conditions
lat_condition = the_box["y_min"] < lat < the_box["y_max"]
lon_condition = the_box["x_min"] < lon < the_box["x_max"]

# Report the status of the points
if lat_condition & lon_condition:
    print(f"Record {event_id}: {tag_id} was IN the box at {timestamp}")
else:
    print(f"Record {event_id}: {tag_id} was NOT IN the box at {timestamp}")