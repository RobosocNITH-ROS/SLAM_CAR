# 🧽 SLAMurai — SLAM Project using ROS 2

This repository contains a complete SLAM pipeline for a differential drive robot (or similar) using **ROS 2**, simulated in **Gazebo** or deployed on **hardware**. It uses **SLAM Toolbox**, **Nav2 stack**, and custom control nodes.

---

## 🗂️ Workspace Structure

```bash
slamurai_ws/
├── src/
│   ├── slamurai_description
│   ├── slamurai_controller
│   ├── slamurai_mapping
│   ├── slamurai_firmware
│   ├── slamurai_localization
│   └── ... (other packages)
```

---

## 🚀 Setup Instructions

### 1️⃣ Clone the Repo

```bash
cd ~/slamurai_ws/src
git clone <your-repository-url>
```

---

### 2️⃣ Install Dependencies

```bash
cd ~/slamurai_ws
rosdep install --from-paths src --ignore-src -r -y
```

Make sure you have required system packages too:

```bash
sudo apt update
sudo apt install python3-colcon-common-extensions ros-humble-navigation2 ros-humble-slam-toolbox
```

> Replace `humble` with your ROS 2 distro if different.

---

### 3️⃣ Build the Workspace

```bash
cd ~/slamurai_ws
colcon build --symlink-install
source install/setup.bash
```

---

### 4️⃣ Launch Simulation or Hardware

* **For Gazebo Simulation**:

```bash
ros2 launch slamurai_description gazebo.launch.py
```

* **For Hardware Interface**:

```bash
ros2 launch slamurai_firmware hardware_interface.launch.py
```

* **For LIDAR Hardware Only**:

```bash
ros2 launch slamurai_localization lidar.launch.py
```

---

### 5️⃣ Launch Controller

```bash
ros2 launch slamurai_controller controller.launch.py
```

---

### 6️⃣ Launch SLAM Toolbox

```bash
ros2 launch slamurai_mapping slam.launch.py
```

---

### 7️⃣ Start Teleoperation

```bash
ros2 run slamurai_controller teleop_custom.py
```

---

### 8️⃣ Launch RViz for Visualization

```bash
rviz2
```

* Add the following plugins manually:

  * RobotModel
  * TF
  * LaserScan (select `/scan` topic)
  * Map
  * Pose
  * Odometry
  * Global/Local Costmaps (if using Nav2 later)
  * SLAM Toolbox GUI (optional)

---

## 📦 Notes

* Ensure all sensors (e.g., LIDAR, IMU) are publishing to correct topics.
* Check TF tree using `ros2 run tf2_tools view_frames` if transforms are missing.
* Use `ros2 topic echo <topic_name>` for debugging topic data.

---

## 🤖 Future Extensions

* Add Nav2 Navigation stack for autonomous navigation.
* Integrate camera and ArUco marker detection.
* Use MoveIt for robotic arm control (if available).
