from tkinter import *
import threading
import pyscreenrec

root = Tk()
root.geometry("400x600")
root.title("Screen Recorder")
root.config(bg="#fff")
root.resizable(False, False)

rec = pyscreenrec.ScreenRecorder()
is_recording = False  # Track recording state

def start_recording():
    global is_recording
    file = Filename.get().strip()
    if not file or file == "File Name":
        status_label.config(text="⚠️ Enter a valid filename!", fg="red")
        return
    try:
        # Start recording in a new thread to avoid GUI freeze
        threading.Thread(target=lambda: rec.start_recording(file + ".mp4", 5)).start()
        is_recording = True
        status_label.config(text="🔴 Recording started", fg="green")
    except Exception as e:
        status_label.config(text=f"❌ Error: {e}", fg="red")

def pause_recording():
    try:
        rec.pause_recording()
        status_label.config(text="⏸️ Recording paused", fg="orange")
    except Exception as e:
        status_label.config(text=f"❌ Error: {e}", fg="red")

def resume_recording():
    try:
        rec.resume_recording()
        status_label.config(text="▶️ Recording resumed", fg="green")
    except Exception as e:
        status_label.config(text=f"❌ Error: {e}", fg="red")

def stop_recording():
    global is_recording
    if is_recording:
        try:
            rec.stop_recording()
            is_recording = False
            status_label.config(text="✅ Recording stopped", fg="blue")
        except Exception as e:
            status_label.config(text=f"❌ Error: {e}", fg="red")
    else:
        status_label.config(text="⚠️ Not recording!", fg="red")


# Load icons
try:
    root.iconphoto(False, PhotoImage(file="icon.png"))
    image1 = PhotoImage(file="yelllow.png")
    Label(root, image=image1, bg="#fff").place(x=-2, y=35)
    image2 = PhotoImage(file="blue.png")
    Label(root, image=image2, bg="#fff").place(x=223, y=200)
    image3 = PhotoImage(file="recording.png")
    Label(root, image=image3, bd=0).pack(pady=30)
    image4 = PhotoImage(file="pause.png")
    image5 = PhotoImage(file="resume.png")
    image6 = PhotoImage(file="stop.png")
except:
    # Optional fallback if images not found
    print("Some images not found. Using defaults.")

# Heading
Label(root, text="Screen Recorder", bg="#fff", font="arial 15 bold").pack(pady=20)

# Entry
Filename = StringVar()
entry = Entry(root, textvariable=Filename, width=18, font="arial 15")
entry.place(x=100, y=350)
Filename.set("File Name")

# Buttons
Button(root, text="Start", font="arial 22", bd=0, command=start_recording).place(x=140, y=250)

Button(root, image=image4 if 'image4' in globals() else None, text="Pause", bd=0, bg="#fff", command=pause_recording).place(x=50, y=450)
Button(root, image=image5 if 'image5' in globals() else None, text="Resume", bd=0, bg="#fff", command=resume_recording).place(x=150, y=450)
Button(root, image=image6 if 'image6' in globals() else None, text="Stop", bd=0, bg="#fff", command=stop_recording).place(x=250, y=450)

# Status Label
status_label = Label(root, text="", bg="#fff", font="arial 12")
status_label.pack(pady=10)

root.mainloop()
