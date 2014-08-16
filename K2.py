import numpy as np
from collections import deque
from astropy.io import fits

space_craft_orientation = None #numpy array of (N_int, 3): alpha, beta, gamma
# N_int number of short cadence
# integrations

# each pixel has an index

# focal plane coordinates: x,y
# map directly to RA, DEC

#Dictionary linking unique postage stamp id to (x,y) coordinates which specify the origin of that postage stamp in
# focal plane coordinates.
#postage_stamp_positions = {"postage_stamp_id": np.array(x, y), "postage_stamp_id2": np.array(x, y)}

#function that takes x,y position, space_craft_orientation and delivers RA
#def get_RA_DEC((x,y), space_craft_orientation):
    #WCS magic
    #return RA_DEC
#    return None

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
    Container for the downlinked data.
    '''

    def __init__(self, time, timecorr, id, raw, flux, flux_err, flux_bkg, flux_bkg_err, cosmic_rays, quality,
                 pos_corr1, pos_corr2, postageStamp=None):

        self.time = time #The integration time (start or end or midpoint?)
        self.timecorr = timecorr
        self.id = id #CADENCENO, unique ID for the integration

        #Following are shape (Npix, Npix) images
        self.raw = raw #Raw Counts
        self.flux = flux
        self.flux_err = flux_err
        self.flux_bkg = flux_bkg
        self.flux_bkg_err = flux_bkg_err
        self.cosmic_rays = cosmic_rays

        self.quality = quality #Quality flag. 0 == good.
        self.pos_corr = np.array([pos_corr1, pos_corr2])

        self.postageStamp = postageStamp #A reference to the object to which this belongs

        self.shape = self.flux.shape

    @classmethod
    def from_row(cls, row, postageStamp=None):
        '''
        Load a DataFrame from a FITS record array row.
        '''

        #Unpack the FITS row
        #TIME, TIMECORR, CADENCENO, RAW_CNTS, FLUX, FLUX_ERR, FLUX_BKG, FLUX_BKG_ERR, \
        #COSMIC_RAYS, QUALITY, POS_CORR1, POS_CORR2 = row
        return cls(*row, postageStamp=postageStamp)

    #All of the necessary static properties of the DataFrame (ie, chip positions) can be queried
    # from the PostageStamp parent object.
    @property
    def origin(self):
        if self.PostageStamp is not None:
            return(self.PostageStamp.origin)
        else:
            return (0, 0)

class PostageStamp:
    '''
    A container of DataFrames.

    '''
    def __init__(self, args):

        self.shape = (None, None) #The shape of all the DataFrames inside it
        self.dataFrames = deque()

    @classmethod
    def from_FITS(cls, FITS, frames=None):
        '''
        Load a PostageStamp from a FITS file.

        FITS: string of file.

        TODO: Optionally select loading only a subslice of frames, so you can load say just the first 10 frames.
        '''

        hdulist = fits.open(FITS)

        #Read the important attributes from the header
        #hdulist[0].header
        # KEPLERID=             60021426 / unique Kepler target identifier
        # CHANNEL =                   28 / CCD channel
        # SKYGROUP=                   60 / roll-independent location of channel
        # MODULE  =                    9 / CCD module
        # OUTPUT  =                    4 / CCD output
        # OBSMODE = 'long cadence'       / observing mode
        # RADESYS = 'ICRS    '           / reference frame of celestial coordinates
        # RA_OBJ  =             0.049891 / [deg] right ascension
        # DEC_OBJ =             2.687339 / [deg] declination

        #hdulist[1].header
        #NAXIS2  =                  440 / length of second array dimension, ie, how many integrations
        #TUNIT1  = 'BJD - 2454833'      / column units: barycenter corrected JD
        # WCSN4P  = 'PHYSICAL'           / table column WCS name
        # WCAX4P  =                    2 / table column physical WCS dimensions
        # 1CTY4P  = 'RAWX    '           / table column physical WCS axis 1 type, CCD col
        # 2CTY4P  = 'RAWY    '           / table column physical WCS axis 2 type, CCD row
        # 1CUN4P  = 'PIXEL   '           / table column physical WCS axis 1 unit
        # 2CUN4P  = 'PIXEL   '           / table column physical WCS axis 2 unit
        # 1CRV4P  =                   43 / table column physical WCS ax 1 ref value
        # 2CRV4P  =                  876 / table column physical WCS ax 2 ref value
        # 1CDL4P  =                  1.0 / table column physical WCS a1 step
        # 2CDL4P  =                  1.0 / table column physical WCS a2 step
        # 1CRP4P  =                    1 / table column physical WCS a1 reference
        # 2CRP4P  =                    1 / table column physical WCS a2 reference
        # WCAX4   =                    2 / number of WCS axes
        # 1CTYP4  = 'RA---TAN'           / right ascension coordinate type
        # 2CTYP4  = 'DEC--TAN'           / declination coordinate type
        # 1CRPX4  =                      / [pixel] reference pixel along image axis 1
        # 2CRPX4  =                      / [pixel] reference pixel along image axis 2
        # 1CRVL4  =     0.04989100000005 / [deg] right ascension at reference pixel
        # 2CRVL4  =             2.687339 / [deg] declination at reference pixel
        # 1CUNI4  = 'deg     '           / physical unit in column dimension
        # 2CUNI4  = 'deg     '           / physical unit in row dimension
        # 1CDLT4  =                      / [deg] pixel scale in RA dimension
        # 2CDLT4  =                      / [deg] pixel scale in DEC dimension
        # 11PC4   =                      / linear transformation matrix element cos(th)
        # 12PC4   =                      / linear transformation matrix element -sin(th)
        # 21PC4   =                      / linear transformation matrix element sin(th)
        # 22PC4   =                      / linear transformation matrix element cos(th)

        # BJDREFI =              2454833 / integer part of BJD reference date
        # BJDREFF =           0.00000000 / fraction of the day in BJD reference date
        # TIMEUNIT= 'd       '           / time unit for TIME, TSTART and TSTOP
        # TELAPSE =           8.99078616 / [d] TSTOP - TSTART
        # LIVETIME=           8.27723170 / [d] TELAPSE multiplied by DEADC
        # TSTART  =        1860.04011824 / observation start time in BJD-BJDREF
        # TSTOP   =        1869.03090440 / observation stop time in BJD-BJDREF
        # LC_START=       56692.55033502 / mid point of first cadence in MJD
        # LC_END  =       56701.52068762 / mid point of last cadence in MJD
        # DEADC   =           0.92063492 / deadtime correction
        # TIMEPIXR=                  0.5 / bin time beginning=0 middle=0.5 end=1
        # TIERRELA=             5.78E-07 / [d] relative time error
        # TIERABSO=                      / [d] absolute time error
        # INT_TIME=       6.019802903270 / [s] photon accumulation time per frame
        # READTIME=       0.518948526144 / [s] readout time per frame
        # FRAMETIM=       6.538751429414 / [s] frame time (INT_TIME + READTIME)
        # NUM_FRM =                  270 / number of frames per time stamp
        # TIMEDEL =     0.02043359821692 / [d] time resolution of data
        # DATE-OBS= '2014-02-04T12:57:46.215Z' / TSTART as UTC calendar date
        # DATE-END= '2014-02-13T12:44:30.140Z' / TSTOP as UTC calendar date


        PS = cls(None)

        #We'll have to figure out which args are needed. We could potentially store all of these as a dictionary, and
        #as functionality is added, we can then do a lookup. Otherwise, follow a model after DataFrame
        #PS = cls(args)

        table = hdulist[1].data

        #Loop through all the rows and add_frames
        for row in table:
            PS.add_frame(DataFrame.from_row(row, postageStamp=PS))

        hdulist.close()

        return PS

    def add_frame(self, dataFrame):
        self.dataFrames.append(dataFrame)


#Could add an Aperture class, but it sounds like we won't be using this part of the data product.

def likelihood_function(ModelFrame, DataFrame):
    return None