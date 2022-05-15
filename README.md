# AUTO4508 Project - GROUP 3
## Basics:
### KEY INFORMATION:
+ Code currently located on pioneer3 in: `/home/netipc/AUTO4508_Group3/AUTO4508_Project`
+ sudo pswd: `netipc`
+ To use another robot, simply clone this repo (and make sure it is all up to date), you can use these references to help:
	+ https://cli.github.com/manual/
	+ https://education.github.com/git-cheat-sheet-education.pdf
	+ If you don't know what git is, shoot Lucie a message
+ We are writing this in as much Python as possible
+ First read Pierre-Louis' ppt which can be found in the announcements on LMS
+ These links may help understanding ROS:
	+ http://wiki.ros.org/rospy_tutorials
	+ http://wiki.ros.org/ROS/Tutorials#Core_ROS_Tutorials
	+ http://wiki.ros.org/ROS/Technical%20Overview

### Basic Steps To Run
> NOTE: all code blocks are to be run in the terminal
 1. Run ROS Noetic
`roscore`
 2. In another terminal start RosAria
`rosrun rosaria RosAria _port:=/dev/ttyS1`
	+ To manually drive robot with teleop
	`rosrun rosaria_client interface`
	+ To see nodes:
	`rosnode list`
	+ To see topics:
	`rostopic list`
	+ To output of topic:
	`rostopic echo /the_topic_wanted`
3. In another terminal start GPS node
`rosrun nmea_navsat_driver nmea_serial_driver _port:=/dev/ttyACM0 _baud=9600`




## Current Progress
+ Wrote `waypoints.py` to be a node that publishes information about waypoints. Currently we do not know how these waypoints will be formatted so the code is a little empty
+ Wrote `drive.py` to be the main node that controls the robot. It will need to subscribe to many RosAria topics to be investigated.


## To Do
+ Find and process messages from RosAria including:
	+ Instantaneous velocity (/RosAria/cmd_vel is the topic)
	+ Instantaneous position OR some sort of distance measure from start
	+ Any sensor that can see barriers
	+ etc.
+ This will probably help: http://wiki.ros.org/tf
+ Actually do things in the callback functions in `drive.py`
+ All other things listed here: http://old.roblab.org/courses/mobrob/project/general/Project-Info.pdf

