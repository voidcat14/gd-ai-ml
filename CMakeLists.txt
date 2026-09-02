cmake_minimum_required(VERSION 3.10)
project(GD_AI)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find X11
find_package(X11 REQUIRED)

# Include X11 directories
include_directories(${X11_INCLUDE_DIR})

# Define the executable
add_executable(gd_ai main.cpp)

# Link the required libraries (X11 and XTest/Xtst)
target_link_libraries(gd_ai ${X11_LIBRARIES} Xtst)
