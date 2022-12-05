# CollaborativeDev
>## Description
>A simple project which has to emulate a layer of sensors detecting a particle ray and calculate the direction based on collision data
>
>## Requirements
>* We have a source of charged particles and want to measure the direction of each particle
>* We have a detector 1m away from the source, consisting 5 planar sensors with a distance of 10cm and a surface area of 1x1m 
>* The sensor has a resolution of 25 * 10^-6 m
>## Sensors
>There are indeed different ways of implementing how exactly a sensor of some detector layer should behave. One of such reasons is for example the multihood of 
>interpretations for the word "RESOLUTION" in the context of plasma physics. The main approach in this simulation will be the square geometry. This is due to the various optimizations such a geometry allows.
