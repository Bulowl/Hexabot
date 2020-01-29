# PhantomX Control 

ROS package providing a controller for the Phantom X hexapod robot.

Three different controllers are provided:

- wall_follower.py: simple wall following controller, based on regions to estimate the best output command
- cave_explorer.py: improved wall following to stay in the middle of a corridor
- bang_controller.py: simple bang-bang controllerto avoid walls

These have been tested in simulation and need some work to be used on the real robot, do not use as-is.

## Usage

With Gazebo running, you can run a launch the script with:

    rosrun phantomx_control bang_controller.py

## License

This software is provided by Génération Robots http://www.generationrobots.com and HumaRobotics http://www.humarobotics.com under the Simplified BSD license
