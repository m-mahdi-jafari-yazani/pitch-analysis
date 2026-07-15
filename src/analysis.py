from scipy.signal import spectrogram


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