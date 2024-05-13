# Three-Body Problem

The three-body problem is a classic problem in celestial mechanics that studies the motion of three massive bodies under mutual gravitational influence. Although a general analytical solution to the problem does not exist, it is possible to study its orbits and behavior using numerical methods.

## Method Used

To solve the three-body problem in this project, I employed the numerical method of ordinary differential equation (ODE) integration. Specifically, I used the DOP853 solver, for its high accuracy and computational efficiency, making it suitable for complex problems like the three-body problem.

## Code Structure

The code consists of a Python script that defines the differential equations of the three-body system and utilizes the DOP853 solver to integrate them over time. The code then generates animations of the particles' movements over time.

## Usage Instructions

To use the code, follow these steps:

1. Clone the repository to your local environment.
2. Make sure you have Python installed on your system.
3. Install the necessary dependencies, such as NumPy, Matplotlib, and SciPy, using your preferred package manager (e.g., pip).
4. Run the provided Python script.
5. Animated GIFs of the particles' movements will be generated in the project directory.

## Results

Here are the animated GIFs demonstrating the particles' movements over time:

### Two-Body Motion

![GIF1](2bodies.gif)

### Three-Body Motion 

![GIF2](3bodies.gif)

