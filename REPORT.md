# Undergraduate Research Trial Task Submission
## 1. Summary
## 2. Environment and Setup
Currently running the simulator on Ubuntu 20.04 LTS with an Nvidia GPU and AMD CPU. 

## 3. Part 1: Simulator Setup
Initially had issues with X11 BadMatch errors while using a virtual machine or WSL so I eventually switched to booting to Linux. After installing Nvidia drivers (Proprietary nvidia-driver-570) the BadMatch errors were fixed. 

Recording of the simulation can be found at `figures/Report/simulation_recording.mkv` or through the following Google Drive Link: https://drive.google.com/file/d/15rIyGNkr8Ep3xQ90JTgvfhBz3wiwH6VA/view?usp=sharing

Although the simulation had consistent movements, I had varying results everytime the replay ran.
## 4. Part 2: Data Visualization and Trajectory Comparison

I have attached below the inital visualization of the original PSM kinematics of both the left arm and right arm
| Left Arm | Right Arm |
| :---: | :---: |
| ![Left Arm Graph](./figures/Report/left_robotic_arm_1.png)  | ![Right Arm Graph](./figures/Report/right_robotic_arm_1.png)

I then replayed the simulation and plotted the PSM kinematics again which can be seen below

| Left Arm | Right Arm |
| :---: | :---: |
| ![Left Arm Graph](./figures/Report/left_robotic_arm_2.png)  | ![Right Arm Graph](./figures/Report/right_robotic_arm_2.png)

Although they look similar, we can see the difference in time in the kinematics. In addition to that, there is a fairly significant shift between the Robot and the console output.

To better see the difference between the original run and the replayed trajectories, I created another script found in `analysis/network/plot_original_and_replay.py' to plot both the original and replayed trajectories and report error values between the two graphs

| Left Arm | Right Arm |
| :---: | :---: |
| ![Left Arm Graph](./figures/Report/left_arm_original_vs_replayed.png)  | ![Right Arm Graph](./figures/Report/right_arm_original_vs_replayed.png)

### Left Arm Error Values
| Left X| Left Y | Left Z | Left Yaw |
| :---: | :---: | :---: | ---: |
| MAE: 0.004079  | MAE: 0.001655 | MAE: 0.003598 | MAE: 0.044164 |
| Max Error: 0.044101 | Max Error: 0.024820 | Max Error: 0.038269 | Max Error: 0.329238 |

### Right Arm Error Values
| Right X| Right Y | Right Z | Right Yaw |
| :--- | :---: | :---: | ---: |
| MAE: 0.015812  | MAE: 0.002710 | MAE: 0.005327 | MAE: 0.061396 |
| Max Error: 0.072686 | Max Error: 0.024145 | Max Error: 0.044219 | Max Error: 0.831262 |

## 5. Part 3: Simulation Development
## 6. Code Changes
## 7. Usage Instructions
## 8. Results
## 9. Performance Profiling
## 10. Tests
## 11. Limitations and Future Improvements
## 12. GenAI Use Disclosure