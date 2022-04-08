#
# Code Created by : "Lankash
#
# Function Name: Sensor_map
# Description: Function for Sensor Readings Mapping
# Inputs:  value-->> the value to be mapped on new range
#          inMin-->> the mim value in the old range
#          inMax-->> the max value in the old range
#          outMin-->> the mim value in the new range
#          outMin-->> the max value in the new range
# Output:  the mapped value within the new range
#
def MAP(value, inMin, inMax, outMin, outMax):
    return outMin + (((value - inMin) / (inMax - inMin)) * (outMax - outMin))
