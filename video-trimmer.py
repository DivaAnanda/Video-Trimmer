import tkinter as tk
from tkinter import filedialog
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os

def select_input_file():
    file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.avi *.mkv")])
    input_entry.delete(0, tk.END)
    input_entry.insert(0, file_path)
    if file_path:
        output_file = os.path.splitext(file_path)[0] + "_cut.mp4"
        output_entry.delete(0, tk.END)
        output_entry.insert(0, output_file)

def trim_video():
    input_file = input_entry.get()
    output_file = output_entry.get()

    start_hour = int(start_hour_entry.get())
    start_minute = int(start_minute_entry.get())
    start_second = int(start_second_entry.get())
    end_hour = int(end_hour_entry.get())
    end_minute = int(end_minute_entry.get())
    end_second = int(end_second_entry.get())

    start_time = start_hour * 3600 + start_minute * 60 + start_second
    end_time = end_hour * 3600 + end_minute * 60 + end_second

    ffmpeg_extract_subclip(input_file, start_time, end_time, targetname=output_file)
    status_label.config(text="Video has been trimmed and saved successfully.")

# Create the main window
root = tk.Tk()
root.title("Video Trimmer")

# Input file selection
tk.Label(root, text="Input Video File:").grid(row=0, column=0, padx=10, pady=5)
input_entry = tk.Entry(root, width=100)
input_entry.grid(row=0, column=1, padx=10, pady=5)
tk.Button(root, text="Browse", command=select_input_file).grid(row=0, column=2, padx=10, pady=5)

# Output file display (automatically filled)
tk.Label(root, text="Output Video File:").grid(row=1, column=0, padx=10, pady=5)
output_entry = tk.Entry(root, width=100)
output_entry.grid(row=1, column=1, padx=10, pady=5)

# Start time input
tk.Label(root, text="Start Time:").grid(row=2, column=0, padx=10, pady=5)
start_hour_entry = tk.Entry(root, width=5)
start_hour_entry.grid(row=2, column=1, sticky="w", padx=10, pady=5)
tk.Label(root, text="Hours").grid(row=2, column=1, padx=45, pady=5, sticky="w")
start_minute_entry = tk.Entry(root, width=5)
start_minute_entry.grid(row=2, column=1, padx=100, pady=5, sticky="w")
tk.Label(root, text="Minutes").grid(row=2, column=1, padx=135, pady=5, sticky="w")
start_second_entry = tk.Entry(root, width=5)
start_second_entry.grid(row=2, column=1, padx=200, pady=5, sticky="w")
tk.Label(root, text="Seconds").grid(row=2, column=1, padx=235, pady=5, sticky="w")

# End time input
tk.Label(root, text="End Time:").grid(row=3, column=0, padx=10, pady=5)
end_hour_entry = tk.Entry(root, width=5)
end_hour_entry.grid(row=3, column=1, sticky="w", padx=10, pady=5)
tk.Label(root, text="Hours").grid(row=3, column=1, padx=45, pady=5, sticky="w")
end_minute_entry = tk.Entry(root, width=5)
end_minute_entry.grid(row=3, column=1, padx=100, pady=5, sticky="w")
tk.Label(root, text="Minutes").grid(row=3, column=1, padx=135, pady=5, sticky="w")
end_second_entry = tk.Entry(root, width=5)
end_second_entry.grid(row=3, column=1, padx=200, pady=5, sticky="w")
tk.Label(root, text="Seconds").grid(row=3, column=1, padx=235, pady=5, sticky="w")

# Trim button
tk.Button(root, text="Trim Video", command=trim_video).grid(row=4, column=1, padx=10, pady=10)

# Status label
status_label = tk.Label(root, text="")
status_label.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

# Run the GUI event loop
root.mainloop()