# Pitch Analysis

A Digital Signal Processing (DSP) project for analyzing recorded speech and synthetic signals using Fourier Transform, Spectrogram, and Pitch Estimation.

---

## Project Overview

This project implements the main concepts of speech signal analysis required in the course assignment. It analyzes recorded audio files and generated synthetic signals using frequency-domain and time-frequency analysis techniques.

The implementation includes:

- Spectrogram computation
- Effect of spectrogram parameters
- Fourier Transform (FFT)
- Synthetic signal generation
- Pitch estimation

---

## Project Structure

```text
pitch-analysis/
├── data/
│   └── recorded/
│       ├── question.wav
│       ├── statement.wav
│       ├── sustained_ah.wav
│       ├── sustained_ee.wav
│       └── sustained_oo.wav
│
├── outputs/
│   ├── fft/
│   ├── pitch/
│   └── spectrograms/
│
├── src/
│   ├── analysis.py
│   ├── audio.py
│   ├── pitch.py
│   └── visualization.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Requirements

- Python 3.12+
- NumPy
- SciPy
- Matplotlib
- Librosa
- SoundFile

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Project

Execute:

```bash
python main.py
```

The program automatically performs all required analyses and saves the generated figures inside the `outputs` directory.

---

## Implemented Tasks

### 1. Spectrogram Analysis

The project computes spectrograms for a recorded speech signal.

The influence of the following parameters is investigated:

- Window length
- Window overlap
- Window type

Supported window functions:

- Boxcar
- Hann
- Hamming

---

### 2. Frequency Analysis

The project generates synthetic signals and analyzes them using the Fast Fourier Transform (FFT).

Generated signals include:

- Sinusoidal signal
- Square wave
- Triangle wave

For each signal, both the FFT and spectrogram are computed.

---

### 3. Pitch Estimation

Pitch is estimated for all recorded speech samples:

- statement.wav
- question.wav
- sustained_ah.wav
- sustained_ee.wav
- sustained_oo.wav

The estimated pitch contour is plotted and saved automatically.

---

## Output Files

All generated figures are stored automatically.

```text
outputs/
├── fft/
│   ├── synthetic_fft.png
│   ├── square_fft.png
│   └── triangle_fft.png
│
├── pitch/
│   ├── question_pitch.png
│   ├── statement_pitch.png
│   ├── sustained_ah_pitch.png
│   ├── sustained_ee_pitch.png
│   └── sustained_oo_pitch.png
│
└── spectrograms/
    ├── default.png
    ├── boxcar.png
    ├── hann.png
    ├── hamming.png
    ├── synthetic.png
    ├── square.png
    ├── triangle.png
    ├── overlap_256.png
    ├── overlap_512.png
    ├── overlap_768.png
    ├── window_length_512.png
    ├── window_length_1024.png
    └── window_length_2048.png
```

---

## Recorded Dataset

The recorded dataset consists of five speech recordings:

| File | Description |
|------|-------------|
| statement.wav | Declarative sentence |
| question.wav | Interrogative sentence |
| sustained_ah.wav | Sustained vowel /a/ |
| sustained_ee.wav | Sustained vowel /i/ |
| sustained_oo.wav | Sustained vowel /u/ |

---

## Technologies

- Python
- NumPy
- SciPy
- Matplotlib
- Librosa

---

## Summary

This project demonstrates the fundamental techniques used in speech signal processing, including spectrogram analysis, frequency analysis using FFT, synthetic signal generation, and pitch estimation. All generated results are automatically saved for further inspection.