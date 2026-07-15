import matplotlib.pyplot as plt
import numpy as np


def plot_spectrogram(frequencies, times, spectrum, title):
    plt.figure(figsize=(10, 4))

    plt.pcolormesh(
        times,
        frequencies,
        10 * np.log10(spectrum + 1e-12),
        shading="gouraud",
    )

    plt.xlabel("Time (s)")
    plt.ylabel("Frequency (Hz)")
    plt.title(title)

    plt.colorbar(label="Power (dB)")

    plt.tight_layout()
    plt.show()


def plot_fft(frequencies, magnitude, title):
    plt.figure(figsize=(10, 4))

    plt.plot(frequencies, magnitude)

    plt.title(title)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")

    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_pitch(times, pitch):
    plt.figure(figsize=(10, 4))

    plt.plot(times, pitch)

    plt.title("Pitch")
    plt.xlabel("Time (s)")
    plt.ylabel("Frequency (Hz)")

    plt.grid(True)

    plt.tight_layout()
    plt.show()