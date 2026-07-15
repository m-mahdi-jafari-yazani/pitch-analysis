from scipy.signal import spectrogram
import numpy as np
from scipy.signal import square, sawtooth


def compute_spectrogram(
    signal,
    sample_rate,
    window="hann",
    nperseg=1024,
    noverlap=512,
):
    """
    Compute STFT spectrogram.
    """

    frequencies, times, spectrum = spectrogram(
        signal,
        fs=sample_rate,
        window=window,
        nperseg=nperseg,
        noverlap=noverlap,
    )

    return frequencies, times, spectrum


def generate_sine_wave(frequency, duration, sample_rate):
    t = np.linspace(
        0,
        duration,
        int(sample_rate * duration),
        endpoint=False,
    )

    return np.sin(2 * np.pi * frequency * t)


def compute_fft(signal, sample_rate):
    spectrum = np.fft.rfft(signal)
    frequencies = np.fft.rfftfreq(
        len(signal),
        d=1 / sample_rate,
    )

    magnitude = np.abs(spectrum)

    return frequencies, magnitude



def generate_square_wave(frequency, duration, sample_rate):
    t = np.linspace(
        0,
        duration,
        int(sample_rate * duration),
        endpoint=False,
    )

    return square(2 * np.pi * frequency * t)


def generate_triangle_wave(frequency, duration, sample_rate):
    t = np.linspace(
        0,
        duration,
        int(sample_rate * duration),
        endpoint=False,
    )

    return sawtooth(
        2 * np.pi * frequency * t,
        width=0.5,
    )