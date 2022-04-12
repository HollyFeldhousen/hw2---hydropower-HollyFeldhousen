#######################################################################
# Program Filename: HW2
# Author: Holly Feldhousen
# Date: 04/25/22
# Description: Calculating total power consumption given a set of data
# Input: Starting year, ending year
# Output: Total world power consumption in those years
#######################################################################
import pandas as pd   # importing fun amazing programs
import numpy as np
#
#  importing data !!
file_path = 'C:/Users/holly/Downloads/energy_use_terrawatthours.csv'
energyuse = pd.read_csv(file_path)
#
year = energyuse.loc[:, 'year']  # setting arrays? I think
type = energyuse.loc[:, 'variable']
power = np.array(energyuse.loc[:, 'generation_twh'])
#
cntr1 = 0
cntr2 = 0
cntr3 = 0
cntr4 = 0
cleanpower1 = np.empty(1)  # These have to be set to 1 because I got errors otherwise :0
fossilpower1 = np.empty(1)
cleanpower2 = np.empty(1)
fossilpower2 = np.empty(1)
year_store = np.empty(1)
#
# Getting Inputs from user
#
lower_year = int(input("Type your starting year between 2000-2021: "))
higher_year = int(input("Type your end year between 2000-2021: "))
power_types = ["blah blah blah"]  # add later!!!!
#
# Getting energy in start year
#
for x in range(len(year)):
    if type[x] == 'Clean' and year[x] == int(lower_year):
       cleanpower1[cntr1] = power[x]
    if type[x] == 'Fossil' and year[x] == int(lower_year):
        fossilpower1[cntr2] = power[x]
poweryear1 = float(cleanpower1) + float(fossilpower1)
#
# Getting energy in end year
#
for x in range(len(year)):
    if type[x] == 'Clean' and year[x] == int(higher_year):
        cleanpower2[cntr3] = power[x]
    if type[x] == 'Fossil' and year[x] == int(higher_year):
        fossilpower2[cntr4] = power[x]
poweryear2 = float(cleanpower2) + float(fossilpower2)
#
# Printing outputs
#
percentchange = np.floor(100*((poweryear2 - poweryear1)/poweryear2))
yearschange = (higher_year - lower_year) + 1

print("The total world power consumption in year", lower_year, "was", poweryear1, "twh and in", higher_year, "total \
world power consumption was", poweryear2, "twh.")
print(" ")

# I don't know how to do this :)
# userinput = ("Pick a type of power: (Bioenergy, Clean, Coal, Fossil, Gas, Hydro, Nuclear, Other Fossil, Other \
    # Renewables, Solar, Wind)")
#
# for x in range(len(year)):
    # if userinput == energyuse.loc[:, "variable"]:
        # print("The total energy used in the year ", lower_year, " is ", "")
