# Real-time Cantonese ↔ Mandarin Translator

This repository contains a simple Python script `realtime_translator.py` that listens from the microphone,
translates between Cantonese (廣東話) and Mandarin (普通話), and plays back the translation.

## Requirements

- Python 3.8+
- `speech_recognition`
- `googletrans` (free Google Translate API)
- `gTTS`
- `playsound`

Install dependencies:

```bash
pip install speechrecognition googletrans==4.0.0-rc1 gTTS playsound
```

> Note: `googletrans` uses an unofficial API and may occasionally fail. Consider
> using an official translation API (e.g., Azure Cognitive Services) for
> production use.

## Usage

```bash
python realtime_translator.py --direction cantonese_to_mandarin
```

Options for `--direction`:

- `cantonese_to_mandarin` (default)
- `mandarin_to_cantonese`

Press `Ctrl+C` to exit the loop.

## Architecture Notes

This script demonstrates a local, real-time translator. For enterprise
integration, pair it with Azure or other official services, store
output on SharePoint, and integrate with Power BI or Power Automate as needed.
