
import tkinter as tk
import random
import time
import csv
import os

colors = ["red", "blue", "green", "yellow"]
words = colors[:]                
num_trials = 20                # 20 trials per experiment
save_dir = "results"                 
save_csv_path = os.path.join(save_dir, "stroop_results.csv")

# make sure that the results folder exists 
os.makedirs(save_dir, exist_ok=True)

#store trial data
trial_data = []           

def log_trial(trial_num, word, ink, response, correct, rt_ms):
    #append trial data t
    trial_data.append(
        {"trial_number": trial_num,
         "word": word,
         "ink_color": ink,
         "response": response,
         "correct": int(correct),
         "rt_ms": rt_ms}
    )

def save_csv():
    #weite trial_data to save_csv
    if not trial_data:
        return
    fieldnames = ["trial_number", "word", "ink_color", "response", "correct", "rt_ms"]
    with open(save_csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(trial_data)
    print(f" Data written to {save_csv_path}")

    #AI attribution: Used ChatGPT
    #Prompt: Why am I getting typeError and data isn't being saved after trial
    #Suggested I change save_csv to save_csv_path because I accidently named a variable the same as the save_csv function.


class StroopGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Stroop Test")

        self.canvas = tk.Canvas(self.root, width=400, height=200, bg="white")
        self.canvas.pack(expand=True)

        
        self.trial_num    = 0
        self.current_word = None
        self.current_ink  = None
        self.start_time   = None   

        # instruction screen
        self.canvas.create_text(
            200, 80,
            text=("Type the INK COLOR for each word.\n"
                  "Keys: r = red, g = green, b = blue, y = yellow\n"
                  "Press space to start."),
            justify="center", font=("Helvetica", 14))
        #bind spacebar = start
        self.root.bind("<space>", self.show_next_trial)
        #any key pressed = user response
        self.root.bind("<Key>",   self.key_handler)

    def show_next_trial(self, event=None):
        if self.trial_num >= num_trials:
            self.end_experiment()
            return

        self.trial_num += 1
        self.current_word = random.choice(words)
        self.current_ink  = random.choice(colors)

        # draw word
        self.canvas.delete("all")
        self.canvas.create_text(
            200, 100,
            text=self.current_word,
            fill=self.current_ink,
            font=("Helvetica", 48, "bold"))

        # start RT timer
        self.start_time = time.perf_counter()

    # key presses for responses 
    def key_handler(self, event):
        if self.start_time is None:   # to ignore key presses before first word shown
            return

        key_map = {"r": "red", "g": "green", "b": "blue", "y": "yellow"}
        response = key_map.get(event.char.lower(), "")
        if response == "":                   # ignore other keys
            return

        rt_ms   = (time.perf_counter() - self.start_time) * 1000
        #rt in milliseconds
        correct = (response == self.current_ink)

        log_trial(self.trial_num, self.current_word, self.current_ink, response, correct, rt_ms)

        self.start_time = None               
        self.show_next_trial()              

    def end_experiment(self):
        self.canvas.delete("all")
        self.canvas.create_text(200, 100, text="Test Completed!\nThanks.", font=("Helvetica", 24))
        
        save_csv() 


        self.root.after(2000, self.root.destroy)   #close application after 2000 milliseconds = 2 seconds

    def run(self):
        self.root.mainloop()

def run_stroop_test():
    StroopGUI().run()

if __name__ == "__main__":
    run_stroop_test()
