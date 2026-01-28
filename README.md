# AnalyzeRLC - RLC Circuit Analyzer

A Python-based simulation tool to analyze the behavior of Series RLC circuits. 

## Features
- Calculates **Step Response** (Transient analysis).
- Generates **Bode Plots** (Frequency response).
- User-defined parameters for Resistance, Inductance, and Capacitance.

## How it Works
The script uses `SciPy` to define the circuit's transfer function based on the differential equation:
$$L\frac{d^2q}{dt^2} + R\frac{dq}{dt} + \frac{1}{C}q = V(t)$$

## Requirements
- Python 3.x
- NumPy
- Matplotlib
- SciPy