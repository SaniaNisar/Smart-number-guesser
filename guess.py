import tkinter as tk
import random

class NumberGuesserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guesser - Computer Guesses Your Number")
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        self.initialize_ui()
        self.reset_game()

    def initialize_ui(self):
        tk.Label(self.root, text="Computer Number Guesser", font=("Helvetica", 16, "bold")).pack(pady=10)
        tk.Label(self.root, text="Think of a number, and let the computer guess!", font=("Helvetica", 10)).pack()

        self.range_frame = tk.Frame(self.root)
        self.range_frame.pack(pady=10)
        tk.Label(self.range_frame, text="Min: ").grid(row=0, column=0)
        self.min_entry = tk.Entry(self.range_frame, width=5)
        self.min_entry.grid(row=0, column=1, padx=5)

        tk.Label(self.range_frame, text="Max: ").grid(row=0, column=2)
        self.max_entry = tk.Entry(self.range_frame, width=5)
        self.max_entry.grid(row=0, column=3, padx=5)

        tk.Button(self.root, text="Start", command=self.start_game, width=15, bg="green", fg="white").pack(pady=5)
        self.guess_label = tk.Label(self.root, text="", font=("Helvetica", 14), pady=10)
        self.guess_label.pack()

        self.response_frame = tk.Frame(self.root)
        self.response_frame.pack(pady=10)
        tk.Button(self.response_frame, text="Higher", command=lambda: self.process_response("higher"), width=10).grid(row=0, column=0, padx=5)
        tk.Button(self.response_frame, text="Lower", command=lambda: self.process_response("lower"), width=10).grid(row=0, column=1, padx=5)
        tk.Button(self.response_frame, text="Correct", command=self.correct_guess, width=10, bg="blue", fg="white").grid(row=0, column=2, padx=5)
        
        self.message_label = tk.Label(self.root, text="", font=("Helvetica", 10, "italic"), fg="red")
        self.message_label.pack(pady=5)
        
        tk.Button(self.root, text="Reset Game", command=self.reset_game, width=15, bg="red", fg="white").pack(pady=10)

    def start_game(self):
        try:
            self.min_value = int(self.min_entry.get())
            self.max_value = int(self.max_entry.get())

            if self.min_value >= self.max_value:
                raise ValueError("Min should be less than Max")
            
            self.low = self.min_value
            self.high = self.max_value
            self.message_label.config(text="")
            self.make_guess()
        except ValueError as e:
            self.message_label.config(text=f"Error: {e}")

    def make_guess(self):
        if self.low > self.high:
            self.message_label.config(text="You tricked me! That's impossible.")
            self.guess_label.config(text="🤔")
            return
        
        self.current_guess = random.randint(self.low, self.high)
        self.guess_label.config(text=f"Is it {self.current_guess}?")
        self.message_label.config(text="")

    def process_response(self, response):
        if self.low > self.high:
            self.message_label.config(text="Error: Invalid range! Reset the game.")
            return

        if response == "higher":
            self.low = self.current_guess + 1
        elif response == "lower":
            self.high = self.current_guess - 1

        self.make_guess()

    def correct_guess(self):
        self.guess_label.config(text=f"I guessed it! It's {self.current_guess} 🎉")
        self.message_label.config(text="Click Reset Game to play again.")

    def reset_game(self):
        self.low = 0
        self.high = 0
        self.current_guess = None
        self.min_entry.delete(0, tk.END)
        self.max_entry.delete(0, tk.END)
        self.guess_label.config(text="")
        self.message_label.config(text="Enter the range and click Start.")

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuesserApp(root)
    root.mainloop()
