import os

import matplotlib.pyplot as plt
import numpy as np


def create_output_directory(path):
    if path:
        os.makedirs(path, exist_ok=True)


def plot_spectrogram(
    frequencies,
    times,
    spectrum,
    title,
    save_path=None,
):
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

    if save_path is not None:
        create_output_directory(os.path.dirname(save_path))
        plt.savefig(save_path, dpi=300, bbox_inches="tight")

    plt.show()
    plt.close()


def plot_fft(
    frequencies,
    magnitude,
    title,
    save_path=None,
):
    plt.figure(figsize=(10, 4))

    plt.plot(frequencies, magnitude)

    plt.title(title)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")

    plt.grid(True)
    plt.tight_layout()

    if save_path is not None:
        create_output_directory(os.path.dirname(save_path))
        plt.savefig(save_path, dpi=300, bbox_inches="tight")

    plt.show()
    plt.close()


def plot_pitch(
    times,
    pitch,
    save_path=None,
):
    plt.figure(figsize=(10, 4))

    plt.plot(times, pitch)

    plt.title("Pitch")
    plt.xlabel("Time (s)")
    plt.ylabel("Frequency (Hz)")

    plt.grid(True)

    plt.tight_layout()

    if save_path is not None:
        create_output_directory(os.path.dirname(save_path))
        plt.savefig(save_path, dpi=300, bbox_inches="tight")

    plt.show()
    plt.close()