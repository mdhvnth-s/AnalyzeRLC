import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
def analyze_rlc():
    print("----RLC Circuit Analyzer----")
    try:
        R=float(input("Enter Resistance (Ohms):"))
        L=float(input("Enter Inductance (Henries):"))
        C=float(input("Enter Capacitance (Farads):"))
    except ValueError:
        print("Please enter valid numbers.")
        return
    num = [1 / (L * C)]
    den = [1, R / L, 1 / (L * C)]
    system = signal.TransferFunction(num, den)
    t, y = signal.step(system)
    w, mag, phase = signal.bode(system)
    plt.figure(figsize=(12, 8))
    plt.subplot(2, 1, 1)
    plt.plot(t, y, 'b', linewidth=2)
    plt.title(f'Transient Response (Step Input)\nR={R}Ω, L={L}H, C={C}F')
    plt.xlabel('Time (s)')
    plt.ylabel('Output Voltage (V)')
    plt.grid(True)
    plt.subplot(2, 1, 2)
    plt.semilogx(w, mag, 'r', linewidth=2)
    plt.title('Frequency Response (Bode Plot)')
    plt.xlabel('Frequency (rad/s)')
    plt.ylabel('Magnitude (dB)')
    plt.grid(True, which="both", ls="-")
    plt.tight_layout()
    print("\nDisplaying plots...")
    plt.show()