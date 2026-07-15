# Pitch Analysis

This project was developed for a Digital Signal Processing (DSP) course to analyze speech signals using time-frequency analysis techniques.

## Features

- Load recorded WAV audio files
- Generate and visualize spectrograms
- Compare spectrogram parameters:
  - Window type
  - Window length
  - Overlap
- Generate synthetic signals:
  - Sine wave
  - Square wave
  - Triangle wave
- Compute and visualize FFT
- Estimate and visualize pitch

## Project Structure

```
pitch-analysis/
├── data/
│   ├── recorded/
│   └── synthetic/
├── outputs/
│   ├── fft/
│   ├── pitch/
│   └── spectrograms/
├── src/
│   ├── analysis.py
│   ├── audio.py
│   ├── pitch.py
│   ├── utils.py
│   └── visualization.py
├── main.py
├── requirements.txt
└── README.md
```

## Installation

Create and activate a virtual environment:

```bash
python -m venv .venv

source .venv/bin/activate      # macOS/Linux
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the project:

```bash
python main.py
```

## Results

The generated figures are saved in the `outputs/` directory.

The project includes:

- Spectrogram analysis
- FFT analysis
- Synthetic signal analysis
- Pitch estimation

## Requirements

- Python 3.12+
- NumPy
- SciPy
- Matplotlib
- SoundFile

## License

This project was developed for educational purposes.