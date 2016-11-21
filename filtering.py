#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 15:33:47 2016

@author: danielvillarreal
"""

import numpy as np
import pylab as pl
import sklearn as sk
import scipy as sp
from scipy import signal as signal
import glob
import cPickle as pickle



def lowpassFilter(dataset):

    #Lowpass filter coeffs to limit frequency to fpass=48Hz,fstop=60Hz
    lowpass = np.array([
      0.0003194879408334,   0.0014884935669, 0.002756297394609, 0.002527987761899,
  5.362695365564e-05, -0.00243770798774, -0.00170860212805, 0.001892311230087,
   0.003520459948692,-4.511889945953e-05,-0.004654721809233,-0.003123293581869,
   0.003955620050576, 0.006712327972941,  -0.0006428799523,-0.009063869803266,
  -0.005120029444439, 0.008255315539391,  0.01188710132296,-0.002861932087191,
   -0.01701929928469,-0.007269030381619,  0.01719508771868,  0.02043974870977,
  -0.009261476787136, -0.03300042305167,-0.009096370513322,  0.03946519748719,
    0.03958028959013, -0.03176612092443,   -0.087247487232, -0.01015124471945,
     0.1976409649711,   0.3823069979099,   0.3823069979099,   0.1976409649711,
   -0.01015124471945,   -0.087247487232, -0.03176612092443,  0.03958028959013,
    0.03946519748719,-0.009096370513322, -0.03300042305167,-0.009261476787136,
    0.02043974870977,  0.01719508771868,-0.007269030381619, -0.01701929928469,
  -0.002861932087191,  0.01188710132296, 0.008255315539391,-0.005120029444439,
  -0.009063869803266,  -0.0006428799523, 0.006712327972941, 0.003955620050576,
  -0.003123293581869,-0.004654721809233,-4.511889945953e-05, 0.003520459948692,
   0.001892311230087, -0.00170860212805, -0.00243770798774,5.362695365564e-05,
   0.002527987761899, 0.002756297394609,   0.0014884935669,0.0003194879408334],dtype='float64')
    
    result = np.zeros(dataset.shape)
    rows,chans = dataset.shape
    for c in range(0,chans):
        result[:,c] = signal.convolve(dataset[:,c],lowpass,mode='same')
    return result

#eeg['data'][:,0] = signal.convolve(eeg['data'][:,0],lowpass,mode='same')
#eeg['data'][:,1] = signal.convolve(eeg['data'][:,1],lowpass,mode='same')
#eeg['data'][:,2] = signal.convolve(eeg['data'][:,2],lowpass,mode='same')