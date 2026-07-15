import numpy as np


def estimate_pitch(frequencies, spectrum):
    """
    Estimate pitch from a spectrogram by selecting
    the frequency with the maximum energy in each frame.
    """

    pitch = []

    for column in spectrum.T:
        index = np.argmax(column)
        pitch.append(frequencies[index])

    return np.array(pitch)