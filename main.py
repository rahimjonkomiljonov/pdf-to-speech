from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
import gtts
import pdfplumber
import threading
import pygame
import os

# Color scheme
PRIMARY = "#4A90E2"  # Blue for buttons
SECONDARY = "#F7F9FC"  # Light background
ACCENT = "#E8F0FE"  # Entry and frame background
TEXT_COLOR = "#2D3748"  # Dark text for contrast
HOVER = "#357ABD"  # Darker blue for button hover

FONT_NAME = "Helvetica"
FONT_SIZE = 10

audio_file_name = ""
last_output_path = ""  # Track the last saved MP3 file
is_playing = False  # Track playback state

# Initialize pygame mixer
pygame.mixer.init()


def open_file():
    global audio_file_name
    audio_file_name = fd.askopenfilename(
        title='Open a PDF File',
        initialdir='/',
        filetypes=[('PDF files', '*.pdf')])
    if audio_file_name:
        pdf_path_var.set(audio_file_name)
        result_var.set("PDF selected. Ready to convert.")


def extract_text():
    if audio_file_name:
        with pdfplumber.open(audio_file_name) as pdf:
            text = ""
            for page in pdf.pages:
                current_text = page.extract_text() or ""
                tables = page.extract_tables()
                images = page.images
                if tables or images:
                    current_text += "\n[See PDF for tables and figures]\n"
                text += current_text + "\n"
        return text


def text_to_speech(text, output_path, language='en'):
    tts = gtts.gTTS(text, lang=language)
    tts.save(output_path)


def convert_to_mp3():
    global last_output_path
    pdf_path = pdf_path_var.get()
    if not pdf_path:
        result_var.set("Please select a PDF file.")
        return
    output_path = fd.asksaveasfilename(
        defaultextension=".mp3",
        filetypes=[("MP3 files", "*.mp3")],
        title="Save MP3 File")
    if not output_path:
        result_var.set("Conversion cancelled.")
        return
    result_var.set("Converting to MP3...")
    last_output_path = output_path

    def conversion_thread():
        try:
            text = extract_text()
            text_to_speech(text, output_path)
            result_var.set(f"Conversion complete.\nMP3 saved at: {output_path}")
        except Exception as e:
            result_var.set(f"Conversion failed: {str(e)}")

    threading.Thread(target=conversion_thread, daemon=True).start()


def play_audio():
    global is_playing
    if last_output_path and os.path.exists(last_output_path):
        if not is_playing:
            try:
                pygame.mixer.music.load(last_output_path)
                pygame.mixer.music.play()
                is_playing = True
                result_var.set("Playing audio...")
                play_button.grid_remove()
                pause_button.grid(column=2, row=1, padx=10, pady=15)
            except Exception as e:
                result_var.set(f"Playback failed: {str(e)}")
    else:
        result_var.set("No MP3 file available to play.")


def pause_audio():
    global is_playing
    if is_playing:
        try:
            pygame.mixer.music.pause()
            is_playing = False
            result_var.set("Audio paused.")
            pause_button.grid_remove()
            play_button.grid(column=2, row=1, padx=10, pady=15)
        except Exception as e:
            result_var.set(f"Pause failed: {str(e)}")


# Create the root window
root = Tk()
root.title('PDF to Audio Converter')
root.geometry("600x300")
root.config(bg=SECONDARY, padx=20, pady=20)
root.resizable(False, False)

# Variables
pdf_path_var = StringVar()
result_var = StringVar(value="Select a PDF to start.")

# Style configuration
style = ttk.Style()
style.theme_use('clam')
style.configure("TButton",
                font=(FONT_NAME, FONT_SIZE),
                padding=10,
                background=PRIMARY,
                foreground=TEXT_COLOR,
                borderwidth=0)
style.map("TButton",
          background=[('active', HOVER)],
          foreground=[('active', 'white')])
style.configure("TEntry",
                padding=5,
                font=(FONT_NAME, FONT_SIZE))
style.configure("TLabel",
                background=ACCENT,
                foreground=TEXT_COLOR,
                font=(FONT_NAME, FONT_SIZE))

# Main frame
frame = Frame(root, bg=ACCENT, padx=20, pady=20, relief="flat")
frame.pack(fill=BOTH, expand=True)

# PDF selection
pdf_label = ttk.Label(frame, text="Select PDF:")
pdf_label.grid(column=0, row=0, sticky="e", padx=5, pady=5)

pdf_entry = ttk.Entry(frame, textvariable=pdf_path_var, width=50)
pdf_entry.grid(column=1, row=0, columnspan=2, sticky="w", padx=5, pady=5)

open_button = ttk.Button(frame, text="Browse", command=open_file)
open_button.grid(column=3, row=0, padx=10, pady=5)

# Action buttons
convert_button = ttk.Button(frame, text="Convert to MP3", command=convert_to_mp3)
convert_button.grid(column=1, row=1, padx=10, pady=15)

play_button = ttk.Button(frame, text="Play Audio", command=play_audio)
play_button.grid(column=2, row=1, padx=10, pady=15)

pause_button = ttk.Button(frame, text="Pause Audio", command=pause_audio)
# Pause button is initially hidden; shown only when playing

# Status label
result_label = ttk.Label(frame, textvariable=result_var, wraplength=500)
result_label.grid(column=0, row=2, columnspan=4, pady=10)

# Run the application
root.mainloop()