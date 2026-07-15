import numpy as np

from src.audio import load_audio
from src.analysis import (
    compute_spectrogram,
    compute_fft,
    generate_sine_wave,
    generate_square_wave,
    generate_triangle_wave,
)
from src.pitch import estimate_pitch
from src.visualization import (
    plot_spectrogram,
    plot_fft,
    plot_pitch,
)

AUDIO_FILE = "data/recorded/statement.wav"


def main():
    signal, sample_rate = load_audio(AUDIO_FILE)

    # --------------------------------------------------
    # Default spectrogram
    # --------------------------------------------------

    frequencies, times, spectrum = compute_spectrogram(
        signal,
        sample_rate,
    )

    plot_spectrogram(
        frequencies,
        times,
        spectrum,
        "Default Spectrogram",
        "outputs/spectrograms/default.png",
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
            f"outputs/spectrograms/window_length_{nperseg}.png",
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
            f"outputs/spectrograms/overlap_{overlap}.png",
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
            f"outputs/spectrograms/{window}.png",
        )

    # --------------------------------------------------
    # Stage 2.2.1
    # --------------------------------------------------

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
        "outputs/fft/synthetic_fft.png",
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
        "outputs/spectrograms/synthetic.png",
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
        "outputs/fft/square_fft.png",
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
        "outputs/spectrograms/square.png",
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
        "outputs/fft/triangle_fft.png",
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
        "outputs/spectrograms/triangle.png",
    )

    # --------------------------------------------------
    # Stage 2.3
    # Pitch estimation
    # --------------------------------------------------

    audio_files = [
        "statement.wav",
        "question.wav",
        "sustained_ah.wav",
        "sustained_ee.wav",
        "sustained_oo.wav",
    ]

    for audio_file in audio_files:
        audio_path = f"data/recorded/{audio_file}"

        signal, sample_rate = load_audio(audio_path)

        frequencies, times, spectrum = compute_spectrogram(
            signal,
            sample_rate,
        )

        pitch = estimate_pitch(
            frequencies,
            spectrum,
        )

        output_name = audio_file.replace(".wav", "_pitch.png")

        plot_pitch(
            times,
            pitch,
            f"outputs/pitch/{output_name}",
        )


if __name__ == "__main__":
    main()