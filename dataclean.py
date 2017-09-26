# Script to clean up PM's speeches and prep for RNN
# Nomblr, September 2017

import os
import re

catfile = ""

# Load and clean all txt files
for filename in os.listdir("./data/Final Mix"):
    if filename.endswith(".txt"):
        file = open("./data/Final Mix/"+filename,"r")
        catfile = catfile+ file.read()
        file.close()
file = open("FinalMix.txt","w") # create a new file to write the clean data to
file.write(catfile)
