import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def process_robot_yaw(robot_data):
    # Process yaw data to ensure it is continuous
    robot_data[:, -1] = np.where(robot_data[:, -1] < -1.7, robot_data[:, -1] + 2 * np.pi, robot_data[:, -1])
    robot_data[:,  7] = np.where(robot_data[:,  7] < -1.7, robot_data[:,  7] + 2 * np.pi, robot_data[:,  7])
    return robot_data

# Load Trajectory Data
script_dir = os.path.dirname(os.path.abspath(__file__))
root = os.path.join(script_dir, "../..", "SurRoL_dVTrainer/tests/dVTrainer/Data/exp_data_15/no_fault")
original_robot_data = np.loadtxt(os.path.join(root, "freefault1/robot_sim_data_1.csv"), delimiter=",", skiprows=1)
replayed_robot_data = np.loadtxt(os.path.join(root, "freefault2/robot_sim_data_1.csv"), delimiter=",", skiprows=1)

# Processes yaw data for both sets of data
original_robot_data = process_robot_yaw(original_robot_data)
replayed_robot_data = process_robot_yaw(replayed_robot_data)

# Make time axes relative to start
t_orig = original_robot_data[:, 0] - original_robot_data[0, 0]
t_repl = replayed_robot_data[:, 0] - replayed_robot_data[0, 0]
# Using min to find the end of the x-axis
max_time = min(t_orig[-1], t_repl[-1])

arms = [
    {"name": "Left", "xyz_cols": [2, 3, 4], "yaw_col": 7},
    {"name": "Right", "xyz_cols": [8, 9, 10], "yaw_col": 13}
]

for arm in arms:   
    fig, axs = plt.subplots(4, 1, figsize=(10, 10), sharex=True)
    fig.suptitle(f'{arm["name"]} Robotic Arm Trajectory (X, Y, Z, Yaw) vs Time: Original vs Replayed')

    for ax, col, label in zip(axs[:3], arm["xyz_cols"], ['X', 'Y', 'Z']):
        ax.plot(t_orig, original_robot_data[:, col] - original_robot_data[0, col], label='Original PSM')
        ax.plot(t_repl, replayed_robot_data[:, col] - replayed_robot_data[0, col], '--', label='Replayed PSM')
        ax.set_ylabel(f'{label} position')
        ax.legend()

    axs[3].plot(t_orig, original_robot_data[:, arm["yaw_col"]] - original_robot_data[0, arm["yaw_col"]], label='Original Yaw')
    axs[3].plot(t_repl, replayed_robot_data[:, arm["yaw_col"]] - replayed_robot_data[0, arm["yaw_col"]], '--', label='Replayed Yaw')
    axs[3].set_ylabel('Yaw')
    axs[3].set_xlabel('Time (s)')
    axs[3].legend(loc="upper right")

    for ax in axs:
        ax.set_xlim(0, max_time)
    plt.tight_layout()

plt.show()