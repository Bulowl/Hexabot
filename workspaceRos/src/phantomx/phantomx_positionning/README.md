# phantomx_positioning 

ROS package providing scripts for positioning the robot in the cave. Returns euler angles and position of the robot in the global frame, in topics /vect_orientation and /vect_position.

## src

Contains positioning scripts. 

### speed.py
From the data of the IMU, computes the linear velocity of the robot.

### pos_tf.cpp
From the data from the lidar and the IMU, computes the position and orientation of the robot.