"""Projectile motion with quadratic air resistance, solved numerically.

This is the same code that is built up step by step in 01_physics_simulation.ipynb.
It lives here too so the other notebooks can `import` it.
"""
import numpy as np

g = 9.81  # gravitational field strength, m/s^2


def derivatives(state, b):
    """Return ds/dt for the state s = (x, y, vx, vy).

    b = k/m is the drag parameter (units 1/m), where the drag force is -k|v|v.
    """
    x, y, vx, vy = state
    v = np.sqrt(vx**2 + vy**2)
    return np.array([vx, vy, -b * v * vx, -g - b * v * vy])


def euler_step(state, dt, b):
    """One step of Euler's method (first order: error is proportional to dt)."""
    return state + dt * derivatives(state, b)


def rk4_step(state, dt, b):
    """One step of the 4th-order Runge-Kutta method (error is proportional to dt^4)."""
    k1 = derivatives(state, b)
    k2 = derivatives(state + 0.5 * dt * k1, b)
    k3 = derivatives(state + 0.5 * dt * k2, b)
    k4 = derivatives(state + dt * k3, b)
    return state + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)


def simulate(v0, angle_deg, b, dt=0.01, step=rk4_step):
    """Simulate a launch from the origin until the projectile lands (y = 0).

    Returns (times, states), where states has one row (x, y, vx, vy) per time.
    """
    theta = np.radians(angle_deg)
    state = np.array([0.0, 0.0, v0 * np.cos(theta), v0 * np.sin(theta)])
    t = 0.0
    times, states = [t], [state]

    while True:
        new_state = step(state, dt, b)
        if new_state[1] < 0:
            # It went below the ground during this step, so use linear
            # interpolation to find where y = 0 between the two points.
            fraction = state[1] / (state[1] - new_state[1])
            landing = state + fraction * (new_state - state)
            landing[1] = 0.0
            times.append(t + fraction * dt)
            states.append(landing)
            break
        state = new_state
        t += dt
        times.append(t)
        states.append(state)

    return np.array(times), np.array(states)
