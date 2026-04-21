# ECE 105 Lab 3 — Sensor Data Visualizations

A Python script and Jupyter notebook that generate synthetic temperature sensor data and produce publication-quality visualizations.

## Installation

1. Activate the ece105 conda environment:
   conda activate ece105

2. Install dependencies:
   conda install numpy matplotlib -y

## Usage

Run the script:
   python generate_plots.py

This saves sensor_analysis.png in the current directory.

## Output

The script produces three plots:
- Scatter plot: Temperature readings from both sensors over time
- Histogram: Overlaid distributions with mean lines for each sensor
- Box plot: Side-by-side comparison with overall mean line

## AI Tools Used and Disclosure

I used GitHub Copilot CLI and Copilot Chat to assist with generating code for this lab. I wrote intent comments before each prompt to guide the AI, reviewed all generated code before using it, and made sure I understood every line.