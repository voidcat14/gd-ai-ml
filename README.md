# Geometry Dash AI (ML)

A professional, cross-platform AI for playing Geometry Dash in real-time using Machine Learning.

## Features
- **Real-Time Play**: Low-latency input and vision loop.
- **Machine Learning**: Uses a Q-Learning agent to learn jump timings based on obstacle distance.
- **Autonomous Calibration**: Automatically detects player and background colors.
- **Visual Overlay**: Draws a "Hacker Vision" debug feed on top of the game (PlayerX, SpikeX, Distance).
- **Cross-Platform**: Supports Windows, macOS, and Linux (X11/Wayland) via a Platform Abstraction Layer.
- **Cheat-Free**: Uses screen-based data extraction rather than memory hacking.

## Tech Stack
- **Language**: C++ 17
- **Build System**: CMake
- **Libraries**: OpenCV, X11/Xtst (Linux), Win32 (Windows), Quartz (macOS).

## How to Run
1. Install dependencies (OpenCV, GLFW).
2. Create a build directory: `mkdir build && cd build`
3. Generate: `cmake ..`
4. Compile: `make`
5. Run: `./gd_ai`
