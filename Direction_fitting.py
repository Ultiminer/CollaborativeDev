import numpy as np

def direction_fitting(data_array):
    # TODO: return the unitary vector of data array
    # The element of the array is 3D coordinates [x,y,z]
    # The shape of the array is (,3)
    x = data_array[:,0]
    y = data_array[:,1]
    z = data_array[:,2]
    model = np.polyfit(x, y, 1)
    e_y = model[0]
    model = np.polyfit(x, z, 1)
    e_z = model[0]
    vector_3d = [1,e_y,e_z]
    return vector_3d/np.linalg.norm(vector_3d)

def convert3dtopolar(vector_3d):
    # TODO: convert the unitary 3d vector to polar coordinates
    # Let's set the e_z = 1
    vec = vector_3d / vector_3d[2]
    r = np.sqrt(vec[0]**2 + vec[1]**2)
    theta = np.arcsin(vec[1] / r)# theta is the angle 
    #between x aixs and our polar vector
    vec_polar = [r,theta,1]
    return vec_polar




data = np.array([[1,1, 2],[2,2,4],[3,3,6],[4,4,8],[5,5,10]])
data = data.reshape(5,3)
dir = direction_fitting(data)
print(dir)
print(convert3dtopolar(dir))