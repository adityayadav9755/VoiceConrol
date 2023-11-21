import speech_recognition as sr
import os
import subprocess

recog = sr.Recognizer()
a = ""
b = []
cmd2 = ""
name = ""
keywords = ["from", "preinstalled", "installed", "pre", "install", ]
ext = {"text": [".txt"],
    "word": [".doc", ".docx"],
    "pdf": [".pdf"],
    "image": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "audio": [".mp3", ".wav", ".flac", ".aac"],
    "video": [".mp4", ".avi", ".mkv", ".mov"],
    "spreadsheet": [".xls", ".xlsx", ".csv"],
    "presentation": [".ppt", ".pptx"],
    "code": [".py", ".java", ".cpp", ".html", ".css"],
    "archive": [".zip", ".tar", ".rar"],
    "executable": [".exe", ".app"],
    "database": [".db", ".sqlite", ".dbf"]}


class Function():
    def recognize(self):
        with sr.Microphone() as source:
            print("Say Command!")
            audio = recog.listen(source, timeout=3, phrase_time_limit=10)
        try:
            a = recog.recognize_google(audio)
            print("You said:", a)

            for x in range(a.count(" ")):
                b.append(a[0:a.index(" ")])
                a = a[a.index(" ") + 1:len(a)]
            b.append(a)

        except sr.UnknownValueError:
            print("Couldn't hear that!")

        return b


    def start(self, appname, apptype):
        if apptype == "preinstalled" or apptype == "pre" or apptype == "preinstall":
            subprocess.run(["start", f"ms-{appname}:"], shell=True)
            print("Starting application...")
        elif apptype == "installed" or apptype == "install":
            os.system(f"start {appname}")
            print("Starting application...")
        else:
            print("Please specify app type as 'preinstalled' or 'installed' as 2nd argument.")

    def open(self, fname, ftype):
        for x in range(len(ext[ftype])):
            try:
                os.startfile(fname + ext[ftype][x])
            except FileNotFoundError:
                continue
            except ValueError:
                print("Please specify file type as 2nd argument.")
            else:
                print("Opening file...")
                break
            print("Mentioned file doesn't exist.")


    def name(self, cmnd):
        for x in cmnd:
            if x in keywords:
                continue
            else:
                name = name + " " + x
        return name
