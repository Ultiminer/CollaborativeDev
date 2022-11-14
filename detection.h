#ifndef DETECTION_H_
#define DETECTION_H_
//Getting lists
#include <vector>
//Getting basic mathematics
#include <gcem.hpp>


//Assume that 1=1 cm

//Defining global constants
constexpr const float GLOBAL_LAYER_LENGTH{100};
constexpr const float GLOBAL_LAYER_SENSOR_DISTANCE{25e-4};//We have a power of -4 since we are using cm as the unit of choice 



//Point structure
struct Point2D{
    float x;
    float y;
};
struct Point3D{
    float x;
    float y;
    float z;
};

//operations between points - here treated again as vectors
constexpr Point2D operator+(const Point2D& a, const Point2D& b)
{
    return {a.x+b.x,a.y+b.y};
}
constexpr Point3D operator+(const Point3D& a, const Point3D& b)
{
    return {a.x+b.x,a.y+b.y,a.z+b.z};
}
constexpr Point2D operator-(const Point2D& a, const Point2D& b)
{
    return {a.x-b.x,a.y-b.y};
}
constexpr Point3D operator-(const Point3D& a, const Point3D& b)
{
    return {a.x-b.x,a.y-b.y,a.z-b.z};
}
constexpr bool operator==(const Point2D& a, const Point2D& b)
{
    return (a.x==b.x&&a.y==b.y);
}
constexpr bool operator==(const Point3D& a, const Point3D& b)
{
    return (a.x==b.x&&a.y==b.y&&a.z==b.z);
}

//Error condition: point couldnt be detected! REQUIRES A NANPOINT 
constexpr const Point2D NANPOINT2D{69420.f,69420.f};
constexpr const Point3D NANPOINT3D{69420.f,69420.f,69420.f};

//interpret a 3DPoint as a 3DRay
typedef Point3D Ray3D;

//dotproduct of points aka. vectors
constexpr float dotprod(const Point2D& a, const Point2D& b)
{
    return a.x*b.x+a.y*b.y;
}
constexpr float dotprod(const Point3D& a, const Point3D& b)
{
    return a.x*b.x+a.y*b.y+a.z*b.z;
}

//squaredist of points aka. vectors
constexpr float squaredist(const Point2D& a, const Point2D& b)
{
    const Point2D d= b-a;
    return dotprod(d,d);
}
constexpr float squaredist(const Point3D& a, const Point3D& b)
{
    const Point3D d= b-a;
    return dotprod(d,d);
}
//square of a float 
constexpr float square(const float x)
{
    return x*x;
}

//Layer structure
class Layer
{
    private:
    //the middle point of our layer
    const Point3D layerPos;
    //The source of all rays
    const Point3D raySource;
    //the length - width AND height - of aour layer
    const float length;
    //the diameter of a singular sensor
    const float sensorDist;
    //The upper left edge of the detection layer
    const Point2D edgeUL;
    //the distnce of the layer middle point to the source
    const float distToSource;

    //List of detected Points
    //it is assumed that their coordinates are already in terms of the layer 
    std::vector<Point2D> detectedPoints;
    public:

    //Initialize all the variables with the ray source and the distance from the layer to the source
    Layer(const Point3D& source, const float distance )
    :layerPos{raySource.x+distToSource,raySource.y,raySource.z},raySource(source),length(GLOBAL_LAYER_LENGTH)
    ,sensorDist(GLOBAL_LAYER_SENSOR_DISTANCE),edgeUL{layerPos.z-length/2,layerPos.y-length/2}
    ,distToSource(distance)
    {}
    
    /*projects the ray onto the layer and transforms the coordinates
    so that the upper left edge is considered to be (0,0)
    */
   private:
    constexpr Point2D RayOnLayer(const Ray3D& ray)
    {
        /*since the ray is assumed to be a normal vector we can just calculate the amount 
        it needs to be multiplied with 
        */
       const float multiplier{distToSource/ray.x};

       //We then multiply the z,y coordinates accordingly and view the point as 2D on the (z,y)- Plane
       const Point2D onLayer={raySource.z+ray.z*multiplier,raySource.y+ray.y*multiplier};
       
       /*And finally subtract the upper left edge of the layer from the point 
       so that we can view the point in terms of the upper left edge as the origin
       */
       return onLayer-edgeUL;
    }

    //How the layer would detect a ray assuming square sensors - BOOLEAN DETECTION
    constexpr Point2D DetectRaySquareSensor(const Ray3D& ray)
    {
        const Point2D perfectP{RayOnLayer(ray)};
        /*We first of all crop the perfectP to the sensor edge it is collding with
        using the modulo (fmod) function*/
        const Point2D sensorEdge{perfectP.x-gcem::fmod(perfectP.x,sensorDist),perfectP.y-gcem::fmod(perfectP.y,sensorDist)};

        //And then shift the sensor Edge to the middle point of the sensor
        return {sensorEdge.x+sensorDist/2, sensorEdge.y+sensorDist/2};
    }

    //How the layer would detect a ray assuming circular sensors - BOOLEAN DETECTION
    constexpr Point2D DetectRayCircleSensor(const Ray3D& ray)
    {
        //We first of all calculate the middle point of the sensor
        const Point2D middleSensor{DetectRaySquareSensor(ray)};

        //And also fetch the perfectP again
        const Point2D perfectP{RayOnLayer(ray)};

        /*We now compare the distance of the ray to the sensor to check if it should be detected
        in case of no detection we return the NANPOINT*/
        return (squaredist(middleSensor,perfectP)>square(sensorDist/2))? NANPOINT2D : middleSensor;
    }
    public:
    //Caching in a list of rays assumign square sensors
    void CacheRaySquareSensors(const std::vector<Ray3D>& Rays)
    {
        for(auto ray: Rays)
            detectedPoints.push_back(DetectRaySquareSensor(ray));
    }

    //Caching in a list of rays assumign circular sensors
    void CacheRayCircularSensors(const std::vector<Ray3D>& Rays)
    {
        for(auto ray: Rays)
        {
            const Point2D toCache{DetectRayCircleSensor(ray)};
            if(!(toCache==NANPOINT2D))detectedPoints.push_back(toCache);
        }
    }
};





#endif