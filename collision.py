from geometry_ray import ray
from Direction_fitting import fitting
from config import config

class simulation(obejct):
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
        for i in self.sim_no:
         rvec=self.r_vec()
         rays.append(rvec)
        return rays
    
    def caclulate_collisions(self, rays):
        """
        
        """
        dete_data = []
        for ray in rays:
            tmp_dete_data = []
            for i in self.layer_no:
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
        track_data = []
        for i, ray in enumerate(rays_list):
            track_data.append(dete_data[i])

        return  rays_list, track_data

