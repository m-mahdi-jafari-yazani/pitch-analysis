import soundfile as sf


def load_audio(file_path):
    """
    Load a WAV audio file.

    Parameters
    ----------
    file_path : str
        Path to the audio file.

    Returns
    -------
    signal : numpy.ndarray
        Audio samples.
    sample_rate : int
        Sampling frequency.
    """

    signal, sample_rate = sf.read(file_path)

    if signal.ndim > 1:
        signal = signal[:, 0]

    return signal, sample_rate