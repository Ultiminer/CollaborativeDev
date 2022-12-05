import numpy as np
from scipy import interpolate as ip
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
        # 1st detector position
        self.x_d = config['detector_pos']['x']
        self.y_d = config['detector_pos']['y']
        self.z_d = config['detector_pos']['z']
        # detector layer specs
        self.l_w = config['detector_geo']['layer_width']        
        self.l_d = config['detector_geo']['layer_dist']
        self.l_h = config['detector_geo']['layer_height']        
        self._no_det = config['detector_geo']['no_layers']

        self._direction = self._vec_cl.norm_vec(self.random_vector())
        self.resol = config['detector_char']['resolution']
        self.detectedPoints=[]
        self.raysource = (self.x_s, self.y_s, self.z_s)
        self.self.l_w
        

        self.layerpos = (self.x_d, self.y_d, self.z_d)
        self.edgeUL = (self.layerpos[0]-self.l_w/2, self.layerpos[1]-self.l_w/2, 0)  # upper left corner of detector layer in xy-plane, z=0 
        #(the z=0 because the layer z is already in the function) 

    def random_vector(self):
        """
        It makes use of random fun_ to generate a point 
        to omit a ray
        Returns
        -------------------------------
        random vector : tuple
        """
        x_w = self.l_w / 2

        x = uniform(-self.l_w/2, self.l_w/2)
        y = uniform(-self.l_h/2, self.l_h/2)
        z = self.z_d+ self.z_l
        
        norm = x**2 + y**2 + (z)**2
        
        return (x/norm, y/norm, z/norm)
    
    def ray_collision_layer(self, layer_no, r_vec: tuple):
        """
        Takes the random_vector propagates the ray to the detector
        with the geometry to a layer_no defined from 1 to 5 
        parameter
        ----------------------
        parameter
        """
        z_l = (self.z_d + (layer_no - 1) * self.l_d )
        multiplier = z_l / r_vec[2]
        vec_ = (self.raysource[0] + (r_vec[0]*multiplier),
                self.raysource[1] + (r_vec[1]*multiplier),
                z_l)

        return tuple(np.subtract(vec_,self.edgeUL))

    #How the layer would detect a ray assuming square sensors - BOOLEAN DETECTION
    def DetectRaySquareSensor(self, layerPoint):
    
        #We first of all crop the perfectP to the sensor edge it is collding with
        #using the modulo (fmod) function
        sensorEdge = (layerPoint[0]-(layerPoint[0] % self.resol),
                      layerPoint[1]- (layerPoint[1] % self.resol)
                     )

        #And then shift the sensor Edge to the middle point of the sensor
        return (sensorEdge[0] + self.resol/2, sensorEdge[1] + self.resol/2, layerPoint[2])
    


    