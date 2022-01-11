import tkinter as tk
import time
import threading


class TypeSpeedGUI:

    def __init__(self):
        self.running = None
        self.root = tk.Tk()
        self.root.title("Speed Typing Application")
        self.root.geometry("1000x600")

        self.frame = tk.Frame(self.root)

        self.sample_label = tk.Label(self.frame, text="In 1996, a tropical cyclone named Olivia hit off the coast of Barrow Island, Australia with such \na force that it broke an incredible record. According to The Weather Channel, Olivia's eyewall \nproduced five extreme three-second wind gusts, the peak of which was a 253 mph gust, which blew \npast the previous wind record of 231 mph set in Mount Washington, New Hampshire back in 1934.", font=("Courier New", 14))
        self.sample_label.grid(row=0, column=0, columnspan=2, padx=5, pady=10)

        self.input_entry = tk.Entry(self.frame, width=40, font=("Courier New", 24))
        self.input_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=10)
        self.input_entry.bind("<KeyRelease>", self.start)

        self.speed_label = tk.Label(self.frame, text="Speed: \n 0.00 WPS \n0.00 WPM", font=("Courier New", 14))
        self.speed_label.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

        self.reset_button = tk.Button(self.frame, text="Reset", font=("Courier New", 14), command=self.reset)
        self.reset_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

        self.frame.pack(expand=True)

        self.counter = 0
        self.started = False

        self.root.mainloop()

    def start(self, event):
        if not self.running:
            if not event.keycode in [16, 17, 18]:
                self.running = True
                t = threading.Thread(target=self.time_thread)
                t.start()
        if not self.sample_label.cget('text').startswith(self.input_entry.get()):
            self.input_entry.config(fg="red")
        else:
            self.input_entry.config(fg="black")
        if self.input_entry.get() == self.sample_label.cget('text'):
            self.running = False
            self.input_entry.config(fg="green")

    def time_thread(self):
        while self.running:
            time.sleep(0.01)
            self.counter += 0.01
            wps = len(self.input_entry.get().split(" ")) / self.counter
            wpm = wps * 60
            self.speed_label.config(text=f"Speed: \n{wps:.2f} WPS\n{wpm:.2f} WPM")

    def reset(self):
        self.running = False
        self.counter = 0
        self.speed_label.config(text="Speed: \n 0.00 WPS \n0.00 WPM")
        self.sample_label.config(text="In 1996, a tropical cyclone named Olivia hit off the coast of Barrow Island, Australia with such \na force that it broke an incredible record. According to The Weather Channel, Olivia's eyewall \nproduced five extreme three-second wind gusts, the peak of which was a 253 mph gust, which blew \npast the previous wind record of 231 mph set in Mount Washington, New Hampshire back in 1934.")
        self.input_entry.delete(0, tk.END)
