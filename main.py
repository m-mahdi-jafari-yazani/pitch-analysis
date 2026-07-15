from src.audio import load_audio
from src.analysis import compute_spectrogram
from src.visualization import plot_spectrogram


AUDIO_FILE = "data/recorded/statement.wav"


signal, sample_rate = load_audio(AUDIO_FILE)


frequencies, times, spectrum = compute_spectrogram(
    signal,
    sample_rate,
)

plot_spectrogram(
    frequencies,
    times,
    spectrum,
    "Spectrogram",
)