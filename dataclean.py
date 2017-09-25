# Script to clean up PM's speeches and prep for RNN
# Nomblr, September 2017

import os
import re

# Load and clean all txt files
for filename in os.listdir("./data"):
    if filename.endswith(".txt"):
        file = open("./data/"+filename,"r")
        filetxt_raw = file.read()
        file.close()
        filetxt_cl1 = re.sub('[\-]+', " ", filetxt_raw) # replace hyphens with spaces
        filetxt_cl2 = re.sub('[^A-Za-z0-9\.\,\'" "]+', "", filetxt_cl1) # remove non alphanumeric characters
        filetxt_cl3 = re.sub(r'\.([a-zA-Z])', r'. \1', filetxt_cl2) # insert spaces after full stops where absent
        savename = filename[0:-4]+"_CLEAN.txt" # save as a CSV
        file = open("./data/"+savename,"w") # create a new file to write the clean data to
        file.write(filetxt_cl3)

