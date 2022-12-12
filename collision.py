from geometry_ray import ray
from Direction_fitting import fitting
from config import config
import numpy as np

class simulation(object):
    def __init__(self) :
        self.x_s = 0
        self.ray = ray()
        self.fitting = fitting()
        self.r_vec = self.ray.random_vector
        self.coll_layer = self.ray.ray_collision_layer
        self.dete_ray_square = self.ray.DetectRaySquareSensor
        self.layer_no = config['detector_geo']['no_layers']
        self.sim_no = config['simulation parameter']['no sim']


    def calculate_rays(self):
        rays=[]
        for i in range(0, self.sim_no):
            rvec = self.r_vec()
            rays.append(rvec)
        return rays

    def caclulate_collisions(self, rays):
        """
        
        """
        dete_data = []
        for ray in rays:
            tmp_dete_data = []
            for i in range(self.layer_no):
                layerpoint = self.coll_layer(i, ray)
                #stores the collison data
                tmp_dete_data.append(self.dete_ray_square(layerpoint))
            dete_data.append(tmp_dete_data)
        return dete_data

    def sim_coll_(self):
        """
        runs the simulation for no of simulations for all the detector layer

        returns
        -----------------

        """
        rays_list = self.calculate_rays()

        cal_coll = self.caclulate_collisions(rays_list)
            
        return rays_list, cal_coll

    def tracks(self, rays_list, dete_data):
        """
        takes the rays_list, detection data and
        omits the rays_list and track_direction_data for each ray
        the track_direction_data is calculated using the direction fitting 
        """
        track_data = []
        for i, ray in enumerate(rays_list):
            id_nan = np.argwhere(np.isnan(dete_data[i]))
            dete_data[i]=dete_data[i][:id_nan[0][0]]
            if len(dete_data[i])<2:
                track_data.append(np.nan)
                print('%f ray no. does not hit two detectors' % (i))
                continue
            dir = self.fitting.direction_fitting(dete_data[i])
            track_data.append(dir)

        return  rays_list, track_data

