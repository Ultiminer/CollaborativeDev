from geometry_ray import ray
from Direction_fitting import fitting
from config import config
import numpy as np
import pickle

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
        for i in (range(1,self.layer_no)):
            tmp_dete_data = []
            for ray in rays:
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
        pickle.dump(rays_list, open("tmp_files/rays.pkl","wb"))
        pickle.dump(cal_coll, open("tmp_files/collision_points.pkl","wb"))
        return rays_list, cal_coll

    def tracks(self, rays_list, dete_data):
        """
        takes the rays_list, detection data and
        omits the rays_list and track_direction_data for each ray
        the track_direction_data is calculated using the direction fitting 
        """
        track_data = []
        for l_i,l in enumerate(self.layer_no):
            dete_data[l_i][dete_data[l_i][:,0].sort()]
            
        for i, ray in enumerate(rays_list):
            id_nan = np.argwhere(np.isnan(dete_data[i]))
            if id_nan is None:
                for j,_ in enumerate(range(1, self.layer_no)):
                    dete_data[i][j] = dete_data[i][j][:id_nan[0][0]]
                    if len(dete_data[i])<2:
                        track_data.append(np.nan)
                        print('%f ray no. does not hit two detectors' % (i))
                        continue
            dir = self.fitting.direction_fitting(dete_data[i])
            track_data.append(dir)
        pickle.dump(track_data, open("tmp_files/track_dir.pkl", "wb"))
        return  rays_list, track_data

