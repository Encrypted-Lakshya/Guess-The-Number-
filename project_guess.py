import random as r
from tkinter import *
from tkinter import messagebox

lives = 5
get = None

def get_random(x, y):
    return r.randrange(x, y)

def start_game():
    global get, lives

    try:
        x = int(sr_entry.get())
        y = int(er_entry.get())

        if x >= y:
            messagebox.showerror("Invalid Range", "Starting range must be less than ending range.")
            return

        get = get_random(x, y)
        lives = 5
        update_lives()
        guess_entry.delete(0, END)
        messagebox.showinfo("Game Started", f"A number has been selected between {x} and {y}. You have {lives} lives.")
        check.config(state=NORMAL)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid integer values for range.")

def game():
    global lives, get
    try:
        guess = int(guess_entry.get())

        if get is None:
            messagebox.showwarning("Game not started", "Please start the game first.")
            return

        if guess == get:
            messagebox.showinfo("🎉 Congratulation", "You guessed the right number 👏🏻")
            check.config(state=DISABLED)

        else:
            lives -= 1
            if lives == 0:
                update_lives()
                messagebox.showinfo("Game Over", f"😕 You Lost. The number was {get}.")
                check.config(state=DISABLED)
            else:
                update_lives()
                messagebox.showinfo("Wrong Guess", f"❌ Wrong! Try again. {lives} lives left.")

        guess_entry.delete(0, END)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

def update_lives():
    heart = "❤️" * lives
    live.config(text=f"Lives Left= {heart}")

root = Tk()
root.title("Guess The Number")
root.geometry("400x450")
root.configure(background="#A7AAE1")

sr = Label(root, text="Enter Starting Range", font=("georgia", 14, "italic"),fg="#FFD0C7", bg="#A7AAE1", pady=10, justify="center")
sr.pack(pady=5)
sr_entry = Entry(root, fg="#FFD0C7", bg="#A7AAE1", border=2, relief="sunken",width=15, font=("times new roman", 12, "bold"), justify="center")
sr_entry.pack()

er = Label(root, text="Enter Ending Range", font=("georgia", 14, "italic"),fg="#FFD0C7", bg="#A7AAE1", pady=10, justify="center")
er.pack(pady=10)
er_entry = Entry(root, fg="#FFD0C7", bg="#A7AAE1", border=2, relief="sunken",width=15, font=("times new roman", 12, "bold"), justify="center")
er_entry.pack()

guess = Label(root, text="Enter Your Guess", font=("georgia", 14, "italic"),fg="#FFD0C7", bg="#A7AAE1", pady=10, justify="center")
guess.pack(pady=10)
guess_entry = Entry(root, fg="#FFD0C7", bg="#A7AAE1", border=2, relief="sunken",width=15, font=("times new roman", 12, "bold"), justify="center")
guess_entry.pack()

start = Button(root, text="START GAME", font=("georgia", 10, "italic", "bold"), relief="raised",padx=20, pady=8, fg="#FFD0C7", bg="#A7AAE1", border=4, borderwidth=2, command=start_game)
start.pack(pady=20)

check = Button(root, text="CHECK", font=("georgia", 10, "italic", "bold"), relief="raised",padx=30, pady=8, fg="#FFD0C7", bg="#A7AAE1", border=4, borderwidth=2, command=game)
check.pack(pady=10)
check.config(state=DISABLED)  

live = Label(root, text="", pady=10, bg="#A7AAE1", fg="#FFD0C7", font=("georgia", 14, ""))
live.pack(pady=10)

update_lives()

mainloop()
