# Autonomous Quadruped Inspection Robot for Industrial Defect Detection and Monitoring Using ROS 2

This project focuses on the development of an autonomous quadruped inspection robot capable of navigating industrial environments and performing automated visual inspection tasks. The robot utilizes ROS 2, SLAM, Nav2, computer vision, and simulation technologies to inspect automotive manufacturing facilities for defects in car body panels.

The project leverages an existing ROS 2 compatible quadruped robot model and extends its capabilities through autonomous navigation, mapping, inspection planning, defect detection, and real-time monitoring systems.

The system is designed to autonomously map unknown environments, navigate between inspection checkpoints, capture images of manufactured components, detect defects such as dents, scratches, cracks, and paint imperfections, and generate inspection reports. A real-time dashboard provides visualization of robot status, mission progress, inspection results, and collected data.

## Project Breakdown

| Phase | Description | Target Date |
|--------|------------|------------|
| Phase 1 | Selecting and setting up an existing ROS 2 compatible quadruped robot model | 16-06-2026 |
| Phase 2 | Understanding and customizing the robot's URDF/Xacro structure | 16-06-2026 |
| Phase 3 | Integrating Camera, LiDAR, and IMU sensors and visualizing the robot in RViz | 17-06-2026 |
| Phase 4 | Setting up Gazebo simulation environment and spawning the robot | 18-06-2026 |
| Phase 5 | Implementing robot control and basic quadruped locomotion | 19-06-2026 |
| Phase 6 | SLAM-based mapping of the environment | 20-06-2026 |
| Phase 7 | Autonomous navigation using Nav2 | 21-06-2026 and 22-06-2026 |
| Phase 8 | Inspection mission planning and checkpoint management | 23-06-2026 and 24-06-2026 |
| Phase 9 | Computer vision-based car body panel defect detection | 25-06-2026 |
| Phase 10 | Dashboard development, reporting, and monitoring system | 26-06-2026 |

## Target Defects

- Dent Detection
- Scratch Detection
- Crack Detection
- Paint Defect Detection

## Technology Stack

- ROS 2 Jazzy
- Existing ROS 2 Compatible Quadruped Robot Model (SpotMicroAI)
- URDF / Xacro
- Gazebo Harmonic
- RViz 2
- SLAM Toolbox
- Nav2
- OpenCV
- YOLO
- PyTorch
- Python
- FastAPI
- React
- PostgreSQL
- Git
- GitHub
