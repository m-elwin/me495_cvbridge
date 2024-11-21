# me495_cvbridge

A quick demonstration on the use of opencv_bridge in python for ROS 2

`ros2 run me495_cvbridge bridger --ros-args -r image:=/source_image_topic` to subscribe to
a raw image published on `/source_image_topic` and publish the transformed image to `image_new`
