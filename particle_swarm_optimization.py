import numpy as np
import matplotlib.pyplot as plt

# Define the function to be minimized
def f(x):
    return 10*np.sin((0.3*x)*np.sin(1.3*(x**2)+0.00001*(x**4)+0.2*x+80))

# Define the particle swarm optimization algorithm
def particle_swarm_optimization(func, x0, bounds, num_particles=10, maxiter=100, w=0.5, c1=1, c2=2):
    # Initialize the particles' positions and velocities
    particles_pos = np.random.uniform(bounds[0], bounds[1], size=(num_particles, len(x0)))
    particles_vel = np.zeros_like(particles_pos)

    # Initialize the best known position and fitness for each particle
    particles_best_pos = particles_pos.copy()
    particles_best_fitness = np.array([func(pos) for pos in particles_pos])

    # Initialize the global best known position and fitness
    global_best_pos = particles_best_pos[np.argmin(particles_best_fitness)]
    global_best_fitness = np.min(particles_best_fitness)

    # Perform the particle swarm optimization algorithm for the specified number of iterations
    for i in range(maxiter):
        # Update the particles' velocities and positions
        r1 = np.random.uniform(size=(num_particles, len(x0)))
        r2 = np.random.uniform(size=(num_particles, len(x0)))
        particles_vel = w*particles_vel + c1*r1*(particles_best_pos - particles_pos) + c2*r2*(global_best_pos - particles_pos)
        particles_pos = particles_pos + particles_vel

        # Apply the bounds to the particles' positions
        particles_pos = np.clip(particles_pos, bounds[0], bounds[1])

        # Update the best known position and fitness for each particle
        particles_fitness = np.array([func(pos) for pos in particles_pos])
        particles_best_mask = particles_fitness < particles_best_fitness
        particles_best_pos[particles_best_mask] = particles_pos[particles_best_mask]
        particles_best_fitness[particles_best_mask] = particles_fitness[particles_best_mask]

        # Update the global best known position and fitness
        if np.min(particles_best_fitness) < global_best_fitness:
            global_best_pos = particles_best_pos[np.argmin(particles_best_fitness)]
            global_best_fitness = np.min(particles_best_fitness)

    return global_best_pos, global_best_fitness

# Define the initial position and bounds for each dimension
x0 = [0]
bounds = [-10, 10]

# Run the particle swarm optimization algorithm with 50 particles for 500 iterations
best_position, best_fitness = particle_swarm_optimization(f, x0, bounds, num_particles=50, maxiter=500)

# Display the results
print("Best position:", best_position)
print("Best fitness:", best_fitness)

# Generate data for the function
x = np.linspace(-10, 10, 1000)
y = f(x)

# Plot the function and the particle swarm optimization solution
fig = plt.figure(figsize=(10, 5))
plt.plot(x, y)
plt.scatter(best_position, best_fitness, color='red', s=100)
plt.xlim(-10, 10)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
