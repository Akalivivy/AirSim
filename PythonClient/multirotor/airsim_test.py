
import setup_path
import airsim

# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()

# get control
client.enableApiControl(True)

# unlock
client.armDisarm(True)

# Async methods return Future. Call join() to wait for the task to complete.
client.takeoffAsync().join()
ret=client.simCustomInfo("aaa")
print(ret)
# camera_pose = airsim.Pose(airsim.Vector3r(0, 0, 0), airsim.to_quaternion(0, 0, 0))  #PRY in radians
# client.simSetCameraPose(0, camera_pose)

# camera_pose = airsim.Pose(airsim.Vector3r(0, 0, 0), airsim.to_quaternion(45, 45, 0))  #PRY in radians
# client.simSetCameraPose(0, camera_pose)
# # # Set camera pose (position and orientation)
# # client.simSetCameraPose("0", airsim.Pose(airsim.Vector3r(0, 0, 0), airsim.to_quaternion(0, 0, 0)))  # Reset camera pose

# # # Rotate camera horizontally by 45 degrees
# # client.simSetCameraPose("0", airsim.Pose(airsim.Vector3r(0, 0, 0), airsim.to_quaternion(0, -45, 0)), vehicle_name="Drone1")

# # # Rotate camera vertically by 45 degrees
# # client.simSetCameraPose("0", airsim.Pose(airsim.Vector3r(0, 0, 0), airsim.to_quaternion(45, 0, 0)), vehicle_name="Drone1")

# # Capture depth image
# responses = client.simGetImages([
#     airsim.ImageRequest('front_center', airsim.ImageType.DepthPlanar, False, False)])
# img_1d = np.frombuffer(responses[0].image_data_uint8, dtype=np.uint8)
# img_depthvis_bgr = img_1d.reshape(responses[0].height, responses[0].width, 3)


# # # Save depth image to local file
# # # airsim.write_file(os.path.normpath('depth_image.png'), img_rgb)
# cv2.imwrite('depth_image.png', img_depthvis_bgr)






# Land
client.landAsync().join()

# lock
client.armDisarm(False)

# release control
client.enableApiControl(False)
