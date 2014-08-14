import numpy as np

space_craft_orientation = None #numpy array of (N_int, 3): alpha, beta, gamma. N_int number of short cadence
# integrations

postage_stamp_positions = {"postage_stamp_id": np.array(x, y), "postage_stamp_id2": np.array(x, y)}

#function that takes x,y position, space_craft_orientation and delivers RA
def get_RA_DEC((x,y), space_craft_orientation):
    #WCS magic
    return RA_DEC

class Star:
    def __init__(self):
        RA
        DEC
        Luminosity

    get_luminosity()
    set_luminosity()

def PSF(Star, subpixel_positions):
    '''
    Spread out the PSF over the subpixel_positions
    '''
    #Creates numpy array that uses stellar parameters to return an array

    #Some PSF function implemented here
    return illumination

class PRF:
    '''
    Pixel response function for each Frame. Each pixel response function is assumed to be Gaussian
    '''
    def __init__(self):
    #efficiency
    #sigma x
    #sigma y
        pass

    def observe(self, illumination):
        '''
        Illumination is an oversampled array that is huge
        '''

        pass
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