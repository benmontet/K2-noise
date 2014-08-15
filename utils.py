#Utilities to help process the raw K2 data product
#For now, we are forced to work with the Engineering test data located here: ftp://archive.stsci.edu/pub/k2/tpf_eng/

import numpy as np
from astropy.io import ascii, fits
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

#The catalog of long cadence and short cadence targets are in the two files:

filesc = "data/K2_E2_targets_sc.csv"
filelc = "data/K2_E2_targets_lc.csv"

#These are .csv files with the following fields
#EPIC,    ra,        dec,      Kp,   list
#the sc file also has a "comment" field which is the name of the target

#This is useful for looking up targets within a certain RA/DEC range.
#Thus, given the EPIC number, we can download the target file holds the frames.


base_url = "ftp://archive.stsci.edu/pub/k2/tpf_eng/"

class MASTError(Exception):
    '''
    Raised when something goes wrong getting data from the MAST
    '''
    def __init__(self, msg):
        self.msg = msg

def download_target(EPIC, cadence="l", location=""):
    '''
    Given the EPIC number (as an integer), download the ~25Mb file to location. Cadence can be "l" or "s" to specify
    long or short cadence.
    '''
    assert type(EPIC) == int, "Must supply EPIC as an int"

    file_format = "kplr{:0>9d}-2014044044430_{}-targ.fits"

    #Assemble URL of file on MAST
    if cadence == "l":
        file = file_format.format(EPIC, "lpd")
        url = base_url + "long_cadence/" + file
    elif cadence == "s":
        file = file_format.format(EPIC, "spd")
        url = base_url + "short_cadence/" + file
    else:
        raise MASTError("Must choose long ('l') or short ('s') cadence")

    try:
        response = urlopen(url)
        out_file = open(location + file, "wb")
        out_file.write(response.read())
        out_file.close()
    except (HTTPError, URLError) as e:
        raise MASTError(e)


def main():

    download_target(60017806, cadence="s")

    #Print basic information
    # hdulist.info()
    #
    # print(header)
    #
    # #All available fields in the dataset
    # print(cols)

if __name__=="__main__":
    main()

