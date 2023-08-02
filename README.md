# Particle Swarm Optimization (PSO)

![Python](https://img.shields.io/badge/python-3.x-blue.svg)

## Description

This repository contains an implementation of the Particle Swarm Optimization (PSO) algorithm in Python. PSO is an efficient optimization technique inspired by collective behavior in nature, which aims to find the global minimum in complex functions.

The PSO algorithm simulates the behavior of a swarm of particles searching for the optimal solution in a multidimensional space. It iteratively updates the positions of the particles to converge towards the global minimum of a given objective function.

## Features

- Efficient Particle Swarm Optimization algorithm
- Scalable and customizable for different optimization problems
- Finds the global minimum of complex objective functions
- Easily adaptable to various application domains

## Requirements

- Python 3.x
- NumPy
- Matplotlib (for visualization, optional)

## Getting Started

1. Clone the repository:
`git clone https://github.com/yourusername/particle_swarm_optimization.git`
`cd particle_swarm_optimization`

2. Install the required dependencies:
`pip install numpy matplotlib`

3. Customize the objective function in `f(x)` to fit your specific optimization problem.

4. Set the initial position (`x0`) and bounds (`bounds`) for each dimension of the search space.

5. Run the PSO algorithm by executing the script:

6. The script will find the global minimum of the objective function and display the results.

## Parameters

- `func`: The objective function to be minimized.
- `x0`: The initial position in the search space.
- `bounds`: The lower and upper bounds for each dimension of the search space.
- `num_particles`: Number of particles in the swarm (default: 10).
- `maxiter`: Maximum number of iterations for the algorithm (default: 100).
- `w`: Inertia weight (default: 0.5).
- `c1`: Cognitive parameter (default: 1).
- `c2`: Social parameter (default: 2).

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The PSO algorithm implementation is based on the work of [Kennedy, J., & Eberhart, R. (1995)](https://ieeexplore.ieee.org/document/488968).

Feel free to contribute, report issues, or provide suggestions for improvement!

## Author
**Bouchana Hicham**




