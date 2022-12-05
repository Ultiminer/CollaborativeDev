import numpy as np
import scipy as sc
from config import config    

class detector(object):
    def __init__(self):
        self._no_lay = config['detector_geo']['no_layer']
        self._width = config['detector_geo']['layer_width']
        self._height = config['detector_geo']['layer_height']
        self._pos_x = config['detector_pos']['x']
        self._pos_y = config['detector_pos']['y']
        self._pos_z = config['detector_pos']['z']
        self._dete_dist = config['detector_geo']['layer_dist']
    




    
    def clamp():
        """
        simulation to more realistic scenario
        takes : error defined
        returns : a more realistic detection point
        """
        return 0

    def project_to_layer():
        return 0
