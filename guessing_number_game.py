import random
import tkinter as tk
from tkinter import messagebox
number = random.randint(1, 100)
attempts = 0
max_attempts = 7
def check_guess():
    global attempts
    try:
        guess = int(entry.get())
        attempts += 1

        if attempts > max_attempts:
            messagebox.showinfo("Game Over", f"You ran out of attempts! Number was {number}")
            root.quit()

        if guess < number:
            result_label.config(text="Too low! Try again.")
        elif guess > number:
            result_label.config(text="Too high! Try again.")
        else:
            messagebox.showinfo("Congratulations", f"You guessed the number in {attempts} attempts!")
            root.quit()

    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid number")

root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("300x200")

title = tk.Label(root, text="Guess the Number (1-100)", font=("Arial", 14))
title.pack(pady=10)

entry = tk.Entry(root)
entry.pack()

guess_button = tk.Button(root, text="Check Guess", command=check_guess)
guess_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
