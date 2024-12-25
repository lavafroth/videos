# Visualizing a 2D convolution

## Getting Started

- Install manim
- Run  
```sh
manim -pql 00.py
```

You may change `ql` to `qh` for changing the quality to high instead of low.
Note that higher quality implies longer render times.

## Parameters

### On-screen objects

The following parameters can be tweaked in the source code to render
a different variant of this animation.

- `input_size` controls the size of the input tensor
- `padding` pads each side of the input tensor with the respective number of zero cells
- `kernel_size` controls the kernel that performs the convolution
- `stride` is how many steps the kernel takes after each dot product

### Faking 3D

Although this animation *appears* 3D, it is not. Manim cannot transform
objects in a 3D scene to fixed 2D objects. In fact, I performed two matrix
transformations on the entire scene to make it look 3D. The following parameters
control how we fake 3D. All angles are in radians.

- `theta` the angle of the camera on the XY plane with respect to the X axis
- `gamma` the azimuthal angle between the Z axis and the XY plane

### Run time

Here are the variables to control how long the animations last.

- `run_time` is the default run time for animation during the first dot product, it decreases
exponentially per dot product. (Default: 1 second)
- `last_run_time` is how long each animation lasts for the final dot product. (Default: 0.1 seconds)
