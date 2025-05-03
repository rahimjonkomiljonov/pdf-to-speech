# pdf-to-speech

## An app to convert pdf files into speech

This is the **PDF to Audio Converter**, a Python app that turns your PDF files into MP3 audio files! Imagine transforming your study notes or textbooks into an audiobook you can listen to anywhere. It features a sleek blue interface, allows you to play or pause the audio, and adds notes for tables or images in your PDFs.

### Features
- **Select PDFs**: Pick any PDF file with a file explorer.
- **Convert to MP3**: Transform text into speech using Google Text-to-Speech.
- **Play & Pause**: Listen and pause like a music player.
- **Smart Handling**: Notes tables or images with "[See PDF for tables and figures]."
- **Modern Design**: Blue-themed interface with clear updates.
- **Background Work**: Converts without freezing the app.

### Requirements
You’ll need Python and some libraries:
- Python 3.6+
- Libraries: `tkinter`, `pdfplumber`, `gtts`, `pygame`

### Installation
Get it running with these steps:

1. **Install Python**: Download from [python.org](https://www.python.org/downloads/) and add to PATH.
2. **Install Libraries**: Run in terminal:

   pip install pdfplumber   pip install gtts   pip install pygame
3. **Get Code**: Save `main.py` to a folder.

### How to Use
Launch it like a game!

1. **Run App**: In terminal, go to the folder and type:

   python main.py
2. **Pick PDF**: Click “Browse” to select a PDF.
3. **Convert**: Click “Convert to MP3” and save the file.
4. **Play Audio**: Click “Play Audio” to listen, “Pause” to stop.
5. **Check Status**: See messages at the bottom.

### Example
Got `history_notes.pdf`? Select it, convert to `history_audio.mp3`, and play it!

### Notes
- **Tables & Images**: Adds notes for non-text content.
- **Errors**: Shows messages if something fails.
- **Language**: English by default (tweakable in code).

### Troubleshooting
- **Freezes?**: Check for large PDFs.
- **No Sound?**: Ensure speakers work and MP3 exists.
- **Library Issues?**: Reinstall with `pip`.

### Customize
- **Add Volume**: Include a slider.
- **Languages**: Change `language` in code.
- **Progress**: Add a progress bar.

### Credits
Made with Python and passion! Uses `tkinter`, `pdfplumber`, `gtts`, `pygame`.

