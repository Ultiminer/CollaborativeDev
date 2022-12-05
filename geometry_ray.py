import numpy as np
import scipy as sc
from config import config
from random import *

class vector(object):
    def __init__(self, x ,y, z):
        self.x = x
        self.y = y
        self.z = z

    def dot_product(v_1, v_2):
        return v_1*v_2
    
    def cross_product(v_1, v_2):
        return v_1*v_2

    def square_dist(v_1, v_2):
            return v_1*v_2

    def norm_vec(v_1):
        return v_1/(v_1)

    def projection(v_1, v_2):
        return 0
    
    def arg():
        """
        Takes : the width and height 
        returns : angle 
        """
        return 0
    
class ray(object):
    def __init__(self):
        # source position
        self.x_s = config['source']['x']
        self.y_s = config['source']['y']
        self.z_s = config['source']['z']
        # detector position
        self.x_d = config['detector_pos']['x']
        self.y_d = config['detector_pos']['y']
        self.z_d = config['detector_pos']['z']
        # detector layer specs
        self.l_w = config['detector_geo']['layer_width']        
        self.l_d = config['detector_geo']['layer_dist']
        self.l_h = config['detector_geo']['layer_height']        
        self._no_det = config['detector_geo']['no_layers']
        self._vec_cl = vector()  # dont know yet what to do with this
        self._direction = self._vec_cl.norm_vec(self.random_vector())


    def random_vector(self):
        """
        It makes use of random fun_ to generate a point 
        to omit a ray
        Returns:
        theta, phi
        """
        x_w = self.l_w / 2

        s_d = self.z_d + ((self._no_det - 1) * self.l_d)
        theta_max = np.arctan(x_w / s_d)

        theta = uniform(-theta_max, theta_max)
        phi = uniform(-theta_max, theta_max)

        return theta, phi
    
    def ray_collision_layer(self, layer_no, theta, phi):
        """
        Takes the random_vector propagates the ray to the detector
        with the geometry to a layer_no defined from 1 to 5 
        """
        r = (self.z_d + (layer_no - 1) * self.l_d ) / np.cos(phi)

        x = r * np.cos(theta) * np.sin(phi)
        y = r * np.sin(theta) * np.sin(phi)

        return x, y



    