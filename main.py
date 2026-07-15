from src.audio import load_audio
from src.analysis import compute_spectrogram
from src.visualization import (
    plot_spectrogram,
    plot_fft,
)
import numpy as np
from src.analysis import (
    compute_fft,
    generate_sine_wave,
    generate_square_wave,
    generate_triangle_wave,
)


AUDIO_FILE = "data/recorded/statement.wav"


def main():
    signal, sample_rate = load_audio(AUDIO_FILE)

    # Default spectrogram
    frequencies, times, spectrum = compute_spectrogram(
        signal,
        sample_rate,
    )

    plot_spectrogram(
        frequencies,
        times,
        spectrum,
        "Default Spectrogram",
    )

    # --------------------------------------------------
    # Experiment 1: Window length
    # --------------------------------------------------

    window_lengths = [512, 1024, 2048]

    for nperseg in window_lengths:
        frequencies, times, spectrum = compute_spectrogram(
            signal,
            sample_rate,
            nperseg=nperseg,
            noverlap=nperseg // 2,
        )

        plot_spectrogram(
            frequencies,
            times,
            spectrum,
            f"Window Length = {nperseg}",
        )

    # --------------------------------------------------
    # Experiment 2: Overlap
    # --------------------------------------------------

    overlaps = [256, 512, 768]

    for overlap in overlaps:
        frequencies, times, spectrum = compute_spectrogram(
            signal,
            sample_rate,
            nperseg=1024,
            noverlap=overlap,
        )

        plot_spectrogram(
            frequencies,
            times,
            spectrum,
            f"Overlap = {overlap}",
        )

    # --------------------------------------------------
    # Experiment 3: Window type
    # --------------------------------------------------

    windows = [
        "boxcar",
        "hann",
        "hamming",
    ]

    for window in windows:
        frequencies, times, spectrum = compute_spectrogram(
            signal,
            sample_rate,
            window=window,
            nperseg=1024,
            noverlap=512,
        )

        plot_spectrogram(
            frequencies,
            times,
            spectrum,
            f"Window = {window}",
        )

    # ----------------------------------------
    # Stage 2.2.1
    # ----------------------------------------

    sample_rate = 48000
    duration = 1.0

    signal_100 = generate_sine_wave(
        100,
        duration,
        sample_rate,
    )

    signal_150 = generate_sine_wave(
        150,
        duration,
        sample_rate,
    )

    signal_180 = generate_sine_wave(
        180,
        duration,
        sample_rate,
    )

    synthetic_signal = np.concatenate(
        [
            signal_100,
            signal_150,
            signal_180,
        ]
    )

    frequencies, magnitude = compute_fft(
        synthetic_signal,
        sample_rate,
    )

    plot_fft(
        frequencies,
        magnitude,
        "FFT of Synthetic Signal",
    )

    frequencies, times, spectrum = compute_spectrogram(
        synthetic_signal,
        sample_rate,
    )

    plot_spectrogram(
        frequencies,
        times,
        spectrum,
        "Spectrogram of Synthetic Signal",
    )
        # --------------------------------------------------
    # Stage 2.2.2
    # Square wave
    # --------------------------------------------------

    square_signal = generate_square_wave(
        frequency=100,
        duration=3,
        sample_rate=sample_rate,
    )

    frequencies, magnitude = compute_fft(
        square_signal,
        sample_rate,
    )

    plot_fft(
        frequencies,
        magnitude,
        "FFT of Square Wave",
    )

    frequencies, times, spectrum = compute_spectrogram(
        square_signal,
        sample_rate,
    )

    plot_spectrogram(
        frequencies,
        times,
        spectrum,
        "Spectrogram of Square Wave",
    )

    # --------------------------------------------------
    # Triangle wave
    # --------------------------------------------------

    triangle_signal = generate_triangle_wave(
        frequency=100,
        duration=3,
        sample_rate=sample_rate,
    )

    frequencies, magnitude = compute_fft(
        triangle_signal,
        sample_rate,
    )

    plot_fft(
        frequencies,
        magnitude,
        "FFT of Triangle Wave",
    )

    frequencies, times, spectrum = compute_spectrogram(
        triangle_signal,
        sample_rate,
    )

    plot_spectrogram(
        frequencies,
        times,
        spectrum,
        "Spectrogram of Triangle Wave",
    )


if __name__ == "__main__":
    main()