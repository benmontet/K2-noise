#Utilities to help process the raw K2 data product
import numpy as np
from astropy.io import fits

#Eventual hope is a class or something but for now just some example scripts to show how to get what you want

filename = "data/kplr060021426-2014044044430_lpd-targ.fits"
hdulist = fits.open(filename)

BINTABLE = hdulist[1] #the FITS hdu that contains the information we care about
APERTURE = hdulist[2] #we'll ignore this, but nice to know it's there

header = BINTABLE.header

data = BINTABLE.data
cols = data.columns

#1-D arrays the length of number of integrations
TIME = data["TIME"]
#Flags that describe spacecraft motion
QUALITY = data["QUALITY"]

#Images we might care about. They are a numpy array with
#shape (nintegrations, N, N) arrays, where N = 50 is the number of pixels in the postage stamp in one direction.
RAW = data["RAW_CNTS"]
FLUX = data["FLUX"]
FLUX_ERR = data["FLUX_ERR"]
FLUX_BKG = data["FLUX_BKG"]
FLUX_BKG_ERR = data["FLUX_BKG_ERR"]
CR = data["COSMIC_RAYS"]

def main():
    #Print basic information
    hdulist.info()

    print(header)

    #All available fields in the dataset
    print(cols)

if __name__=="__main__":
    main()

