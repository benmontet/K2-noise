import numpy as np
from collections import deque

space_craft_orientation = None #numpy array of (N_int, 3): alpha, beta, gamma
# N_int number of short cadence
# integrations

# each pixel has an index

# focal plane coordinates: x,y
# map directly to RA, DEC

#Dictionary linking unique postage stamp id to (x,y) coordinates which specify the origin of that postage stamp in
# focal plane coordinates.
postage_stamp_positions = {"postage_stamp_id": np.array(x, y), "postage_stamp_id2": np.array(x, y)}

#function that takes x,y position, space_craft_orientation and delivers RA
def get_RA_DEC((x,y), space_craft_orientation):
    #WCS magic
    return RA_DEC

class Star:
    def __init__(self, RA, DEC, luminosity):
        self.RA = RA
        self.DEC = DEC
        self.luminosity = luminosity

    @property
    def luminosity(self):
        return self.luminosity

    @luminosity.setter
    def luminosity(self, luminosity):
        '''
        Update new luminosity with timestep
        '''
        self.luminosity = luminosity
        pass

def PSF(Star, subpixel_positions):
    '''
    Spread out the PSF over the subpixel_positions
    '''
    #Creates numpy array that uses stellar parameters to return an array

    #Some PSF function implemented here
    illumination = None
    return illumination

class PRF:
    '''
    Pixel response function for each Frame. Each pixel response function is assumed to be Gaussian
    '''
    def __init__(self, efficiency, sigmax, sigmay):
        #All of these are 2D arrays of size (50, 50)
        self.efficiency = efficiency
        self.sigmax = sigmax
        self.sigmay = sigmay

    def observe(self, illumination):
        '''
        illumination is an oversampled array that is huge, greater than (50,50).
        The illumination is integrated over the PRF to give a ModelFrame
        '''
        ModelFrame = None
        return ModelFrame


class ModelFrame:
    '''
    Downsampled representation of a single Frame, produced by the model.
    '''
    def __init__(self):
        pass

class DataFrame:
    '''
    Container for the downlinked data

    PostageStamp: Which container is this inside?
    '''
    def __init__(self, time, quality, raw, flux, flux_err, flux_bkg_err, cosmic_rays, PostageStamp=None):
        self.time = time #The integration time (start or end or midpoint?)
        self.quality = quality #Quality flag

        #Following are (N,N) images
        self.raw = raw #Raw Counts
        self.flux = flux
        self.flux_err = flux_err
        self.flux_bkg_err = flux_bkg_err
        self.cosmic_rays = cosmic_rays

        self.PostageStamp = PostageStamp

        self.shape = self.flux.shape

    @classmethod
    def from_row(cls, row, PostageStamp):
        '''
        Load a DataFrame from a FITS record array row.
        '''

        #Unpack the FITS row
        time, quality, raw, flux, flux_err, flux_bkg_err, cosmic_rays = row

        return cls(time, quality, raw, flux, flux_err, flux_bkg_err, cosmic_rays, PostageStamp)

    @property
    def origin(self):
        if self.PostageStamp is not None:
            return(self.PostageStamp.origin)
        else:
            return (0, 0)

class PostageStamp:
    '''
    A container of DataFrames.

    Origin: specifies the origin of the 50x50 chip in focal plane coordinates
    '''
    def __init__(self, origin=None):
        self.origin = (None, None)
        self.shape = (None, None) #The shape of all the DataFrames inside it
        self.DataFrames = deque()

    def add_frame(self, dataFrame):
        self.DataFrames.append(dataFrame)

def likelihood_function(ModelFrame, DataFrame):
    return None