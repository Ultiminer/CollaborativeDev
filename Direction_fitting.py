import numpy as np
from config import config

class fitting(object):
    def __init__(self):
        self.layer_no = config['detector_geo']['no_layers']
        self.sim_no = config['simulation parameter']['no sim']


    def convert3dtopolar(self, vector_3d):
        """
        TODO: convert the unitary 3d vector to polar coordinates
        Let's set the e_z = 1
        """
        vec = vector_3d / vector_3d[2]
        r = np.sqrt(vec[0]**2 + vec[1]**2)
        theta = np.arcsin(vec[1] / r)# theta is the angle 
        #between x aixs and our polar vector
        vec_polar = [r,theta,1]
        return vec_polar

    def direction_fitting(self, data_array):
        """
        TODO: return the unitary vector of data array
        The element of the array is 3D coordinates [x,y,z]
        The shape of the array is (,3)
        the data array is the collision data points on detector layers
        need to apply the convert3dtopolar function 
        """
        
        x = data_array[:,0]
        y = data_array[:,1]
        z = data_array[:,2]
        model = np.polyfit(z, x, 1)
        e_x = model[0]
        model = np.polyfit(z, y, 1)
        e_y = model[0]
        vector_3d = [e_x,e_y,1]
        vector_3d/np.linalg.norm(vector_3d)
        #c_3d_polar = self.convert3dtopolar(vector_3d)
        return vector_3d


