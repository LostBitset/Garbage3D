# Project Plan

## Project Description

The project will be a 3D adventure game that takes place on a faraway desolate planet where you try to explore as much of the world as possible, while avoiding avalanches and asteroid strikes. 

## Structual Plan

The `Scene` class stored as `app.scene` handles events, draws extra stuff in `redrawAll`, and returns a list of geometry to render. Geometry that has been defined as `Geom` objects can be assigned lighting algorithms by passing it into `@diffuseShadingAlgorithm` functions, which return a new `Geom` object. Functions decorated with `@renderer` turn `Geom` objects into `(renderer, geometry)` tuples. A function that takes `app` and returns `(renderer, geometry)` pairs is known as a geomsrc.

A `Viewport` actually renders the `Scene`, and it contains lights, a camera, and a geomsrc. This is called in `redrawAll`.

The `Scene` classes that are being used can be found in `scenes.py`, helper functions they use are `scene_components.py`, and geometries used are in `scene_geometry.py`. This pattern is mirrored for `generation.py`, which handles world generation. 


## Algorithmic Plan

The perspective camera model is used, and coordinates are converted into homogenous form, passed into a matrix, and then converted back into 2D coordinates. Screen-space coordinates are found at the last minute, when the flat shading function is called. 

All triangles are drawn in order, sorted by the distance between the camera and their centroids (aka the Painter's algorithm). The image plane is calculated in terms of a point and a normal vector, and only triangles with vertices on the front side of the image plane are rendered. 

For lighting, lights are stored as a property of `Viewport` objects, and passed into the appropriate lighting function by the flat shading function. The Lambertian reflectance model is used.

Most of the complexity of this project can be found in the 3D renderer.

## Version Control Plan

Everything is stored on GitHub, and this codebase can be found [here](https://github.com/HktOverload/Garbage3D).

