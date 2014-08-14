import numpy as np

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
    '''
    def __init__(self):
        pass

def likelihood_function(ModelFrame, DataFrame):
    return chisq