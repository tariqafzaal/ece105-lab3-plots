"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""

import numpy as np
import matplotlib.pyplot as plt

# Create a function generate_data(seed) that returns sensor_a, sensor_b,
# and timestamps arrays with the same parameters as in the notebook.
# Use NumPy-style docstring with Parameters and Returns sections.

def generate_data(seed):
    """Generate synthetic temperature sensor readings.

    Parameters
    ----------
    seed : int
        Random number generator seed for reproducibility.

    Returns
    -------
    sensor_a : numpy.ndarray
        Temperature readings from sensor A in Celsius, shape (200,).
    sensor_b : numpy.ndarray
        Temperature readings from sensor B in Celsius, shape (200,).
    timestamps : numpy.ndarray
        Measurement timestamps in seconds, shape (200,).
    """
    rng = np.random.default_rng(seed=seed)
    sensor_a = rng.normal(loc=25.0, scale=3.0, size=200)
    sensor_b = rng.normal(loc=27.0, scale=4.5, size=200)
    timestamps = rng.uniform(low=0.0, high=10.0, size=200)
    return sensor_a, sensor_b, timestamps

# Create plot_scatter(sensor_a, sensor_b, timestamps, ax) that draws
# the scatter plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.

def plot_scatter(sensor_a, sensor_b, timestamps, ax):
    """Draw a scatter plot of sensor readings vs timestamps.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Temperature readings from sensor A in Celsius, shape (200,).
    sensor_b : numpy.ndarray
        Temperature readings from sensor B in Celsius, shape (200,).
    timestamps : numpy.ndarray
        Measurement timestamps in seconds, shape (200,).
    ax : matplotlib.axes.Axes
        Axes object to draw the plot on.

    Returns
    -------
    None
    """
    ax.scatter(timestamps, sensor_a, color='blue', label='Sensor A', alpha=0.6, s=30)
    ax.scatter(timestamps, sensor_b, color='orange', label='Sensor B', alpha=0.6, s=30)
    ax.set_xlabel('Time (seconds)')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Temperature Sensors Over Time')
    ax.legend()
    ax.grid(True, alpha=0.3)

# Overlaid histogram of Sensor A and Sensor B temperature distributions.
# NumPy-style docstring. Modifies ax in place, returns None.

def plot_histogram(sensor_a, sensor_b, ax):
    """Draw an overlaid histogram of sensor temperature distributions.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Temperature readings from sensor A in Celsius, shape (200,).
    sensor_b : numpy.ndarray
        Temperature readings from sensor B in Celsius, shape (200,).
    ax : matplotlib.axes.Axes
        Axes object to draw the plot on.

    Returns
    -------
    None
    """
    ax.hist(sensor_a, bins=30, alpha=0.5, color='blue', label='Sensor A')
    ax.hist(sensor_b, bins=30, alpha=0.5, color='orange', label='Sensor B')
    ax.axvline(sensor_a.mean(), color='blue', linestyle='dashed', linewidth=2, label=f'Sensor A Mean: {sensor_a.mean():.1f}°C')
    ax.axvline(sensor_b.mean(), color='orange', linestyle='dashed', linewidth=2, label=f'Sensor B Mean: {sensor_b.mean():.1f}°C')
    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('Count')
    ax.set_title('Temperature Distribution by Sensor')
    ax.legend()

# Side-by-side box plot comparing Sensor A and Sensor B distributions.
# NumPy-style docstring. Modifies ax in place, returns None.

def plot_boxplot(sensor_a, sensor_b, ax):
    """Draw a side-by-side box plot of sensor temperature distributions.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Temperature readings from sensor A in Celsius, shape (200,).
    sensor_b : numpy.ndarray
        Temperature readings from sensor B in Celsius, shape (200,).
    ax : matplotlib.axes.Axes
        Axes object to draw the plot on.

    Returns
    -------
    None
    """
    ax.boxplot([sensor_a, sensor_b], tick_labels=['Sensor A', 'Sensor B'])
    ax.axhline(np.concatenate([sensor_a, sensor_b]).mean(),
               color='red', linestyle='dashed', linewidth=2, label='Overall Mean')
    ax.set_xlabel('Sensor')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Sensor Temperature Distribution Comparison')
    ax.legend()

# Create main() that generates data, creates a 2x2 subplot figure,
# calls each plot function, adjusts layout, and saves as sensor_analysis.png
# at 150 DPI with tight bounding box.

def main():
    """Generate sensor data and save all three plots as a PNG file.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    sensor_a, sensor_b, timestamps = generate_data(seed=8986)
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    plot_scatter(sensor_a, sensor_b, timestamps, axes[0, 0])
    plot_histogram(sensor_a, sensor_b, axes[0, 1])
    plot_boxplot(sensor_a, sensor_b, axes[1, 0])
    axes[1, 1].axis('off')
    plt.tight_layout()
    plt.savefig('sensor_analysis.png', dpi=150, bbox_inches='tight')
    print("Saved sensor_analysis.png")

if __name__ == '__main__':
    main()