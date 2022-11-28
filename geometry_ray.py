import numpy as np
import scipy as sc
from config import config

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
        self.x = config['source']['x']
        self.y = config['source']['x']
        self.z = config['source']['x']
        self._vec_cl = vector()#
        self._direction = self._vec_cl.norm_vec(self.random_vector())


    def random_vector(self):
        """
        It makes use of random fun_ to generate a point 
        and apply vector_class_fun to omit a ray
        and normalize it with norm_vec ---> normalized ray
        """
        
        return 0
    
    def propagate_fun(self):
        """
        Takes the random_vector propagates the ray to the detector
        with the geometry 
        """
        return 0
    
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


    