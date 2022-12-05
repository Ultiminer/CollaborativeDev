import numpy as np

#Assume that 1=1 cm

#Defining global constants
GLOBAL_LAYER_LENGTH=100
GLOBAL_LAYER_SENSOR_DISTANCE=25e-4
source=0
distance=0
#We have a power of -4 since we are using cm as the unit of choice 






class Layer:
 
    
    def __init__(self):
     self.detectedPoints=[]
     self.raySource=source
     self.length=GLOBAL_LAYER_LENGTH
     self.distToSource=distance
     self.sensorDist=GLOBAL_LAYER_SENSOR_DISTANCE
     self.layerPos=vector(raySource.x+distToSource,raySource.y,raySource.z)
     self.edgeUL=vector(layerPos.z-length/2,layerPos.y-length/2)
    
    
   
    def RayOnLayer(ray):
    
       
       multiplier=distToSource/ray.x

       onLayer=vector(raySource.z+ray.z*multiplier,raySource.y+ray.y*multiplier);
       
       return onLayer-edgeUL;
    

    #How the layer would detect a ray assuming square sensors - BOOLEAN DETECTION
    def DetectRaySquareSensor(ray):
    
        perfectP =RayOnLayer(ray)
        #We first of all crop the perfectP to the sensor edge it is collding with
        #using the modulo (fmod) function
        sensorEdge=vector(perfectP.x-fmod(perfectP.x,sensorDist),perfectP.y-fmod(perfectP.y,sensorDist))

        #And then shift the sensor Edge to the middle point of the sensor
        return vector(sensorEdge.x+sensorDist/2, sensorEdge.y+sensorDist/2)
    

    
    
    def CacheRaySquareSensors(Rays)
    
        for ray in Rays:
            detectedPoints.insert(DetectRaySquareSensor(ray))
    


