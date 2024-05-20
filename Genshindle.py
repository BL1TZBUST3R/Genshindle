import tkinter as tk
from tkinter import messagebox
import random
from tabulate import tabulate

characters = [
    {"name": "Venti", "element": "Anemo", "weapon": "Bow", "region": "Mondstadt"},
    {"name": "Amber", "element": "Pyro", "weapon": "Bow", "region": "Mondstadt"},
    {"name": "Barbara", "element": "Hydro", "weapon": "Catalyst", "region": "Mondstadt"},
    {"name": "Diluc", "element": "Pyro", "weapon": "Claymore", "region": "Mondstadt"},
    {"name": "Fischl", "element": "Electro", "weapon": "Bow", "region": "Mondstadt"},
    {"name": "Kaeya", "element": "Cryo", "weapon": "Sword", "region": "Mondstadt"},
    {"name": "Lisa", "element": "Electro", "weapon": "Catalyst", "region": "Mondstadt"},
    {"name": "Mona", "element": "Hydro", "weapon": "Catalyst", "region": "Mondstadt"},
    {"name": "Ningguang", "element": "Geo", "weapon": "Catalyst", "region": "Liyue"},
    {"name": "Qiqi", "element": "Cryo", "weapon": "Sword", "region": "Liyue"},
    {"name": "Tartaglia", "element": "Hydro", "weapon": "Bow", "region": "Snezhnaya"},
    {"name": "Xiangling", "element": "Pyro", "weapon": "Polearm", "region": "Liyue"},
    {"name": "Xiao", "element": "Anemo", "weapon": "Polearm", "region": "Liyue"},
    {"name": "Xingqiu", "element": "Hydro", "weapon": "Sword", "region": "Liyue"},
    {"name": "Xinyan", "element": "Pyro", "weapon": "Claymore", "region": "Liyue"},
    {"name": "Zhongli", "element": "Geo", "weapon": "Polearm", "region": "Liyue"},
    {"name": "Ayaka", "element": "Cryo", "weapon": "Sword", "region": "Inazuma"},
    {"name": "Yoimiya", "element": "Pyro", "weapon": "Bow", "region": "Inazuma"},
    {"name": "Sayu", "element": "Anemo", "weapon": "Claymore", "region": "Inazuma"},
    {"name": "Kujou Sara", "element": "Electro", "weapon": "Bow", "region": "Inazuma"},
    {"name": "Raiden Shogun", "element": "Electro", "weapon": "Polearm", "region": "Inazuma"},
    {"name": "Kamisato Ayato", "element": "Hydro", "weapon": "Sword", "region": "Inazuma"},
    {"name": "Tighnari", "element": "Dendro", "weapon": "Bow", "region": "Sumeru"},
    {"name": "Collei", "element": "Dendro", "weapon": "Bow", "region": "Sumeru"},
    {"name": "Dori", "element": "Electro", "weapon": "Claymore", "region": "Sumeru"},
    {"name": "Lyney", "element": "Pyro", "weapon": "Bow", "region": "Fontaine"},
    {"name": "Lynette", "element": "Anemo", "weapon": "Sword", "region": "Fontaine"},
    {"name": "Albedo", "element": "Geo", "weapon": "Sword", "region": "Mondstadt"},
    {"name": "Ganyu", "element": "Cryo", "weapon": "Bow", "region": "Liyue"},
    {"name": "Hu Tao", "element": "Pyro", "weapon": "Polearm", "region": "Liyue"},
    {"name": "Kazuha", "element": "Anemo", "weapon": "Sword", "region": "Inazuma"},
    {"name": "Klee", "element": "Pyro", "weapon": "Catalyst", "region": "Mondstadt"},
    {"name": "Sucrose", "element": "Anemo", "weapon": "Catalyst", "region": "Mondstadt"},
    {"name": "Thoma", "element": "Pyro", "weapon": "Polearm", "region": "Inazuma"},
    {"name": "Yanfei", "element": "Pyro", "weapon": "Catalyst", "region": "Liyue"},
    {"name": "Yelan", "element": "Hydro", "weapon": "Bow", "region": "Liyue"},
    {"name": "Shenhe", "element": "Cryo", "weapon": "Polearm", "region": "Liyue"},
    {"name": "Arataki Itto", "element": "Geo", "weapon": "Claymore", "region": "Inazuma"},
    {"name": "Gorou", "element": "Geo", "weapon": "Bow", "region": "Inazuma"},
    {"name": "Sangonomiya Kokomi", "element": "Hydro", "weapon": "Catalyst", "region": "Inazuma"},
    {"name": "Yae Miko", "element": "Electro", "weapon": "Catalyst", "region": "Inazuma"},
    {"name": "Dehya", "element": "Pyro", "weapon": "Claymore", "region": "Sumeru"},
    {"name": "Mika", "element": "Cryo", "weapon": "Polearm", "region": "Sumeru"},
    {"name": "Nilou", "element": "Hydro", "weapon": "Sword", "region": "Sumeru"},
    {"name": "Cyno", "element": "Electro", "weapon": "Polearm", "region": "Sumeru"},
    {"name": "Candace", "element": "Hydro", "weapon": "Polearm", "region": "Sumeru"},
    {"name": "Diona", "element": "Cryo", "weapon": "Bow", "region": "Mondstadt"},
    {"name": "Beidou", "element": "Electro", "weapon": "Claymore", "region": "Liyue"},
    {"name": "Razor", "element": "Electro", "weapon": "Claymore", "region": "Mondstadt"},
    {"name": "Chongyun", "element": "Cryo", "weapon": "Claymore", "region": "Liyue"},
    {"name": "Noelle", "element": "Geo", "weapon": "Claymore", "region": "Mondstadt"},
    {"name": "Bennett", "element": "Pyro", "weapon": "Sword", "region": "Mondstadt"},
    {"name": "Arlecchino", "element": "Pyro", "weapon": "Polearm", "region": "Fontaine"},
    {"name": "Furina", "element": "Hydro", "weapon": "Sword", "region": "Fontaine"},
    {"name": "Baizhu", "element": "Dendro", "weapon": "Catalyst", "region": "Liyue"},
    {"name": "Alhaitham", "element": "Dendro", "weapon": "Sword", "region": "Sumeru"},
    {"name": "Nahida", "element": "Dendro", "weapon": "Catalyst", "region": "Sumeru"},
    {"name": "Chiori","element": "Geo","weapon": "Sword","region": "Fontaine"},
]

class Menu:
    def __init__(self, master):
        self.master = master
        self.master.title("Genshin Impact Character Guesser")
        self.master.geometry("600x200")  # Widen the window

        self.title_label = tk.Label(self.master, text="Genshin Impact Character Guesser", font=("Arial", 24))
        self.title_label.pack(pady=20)

        self.normal_mode_button = tk.Button(self.master, text="Normal Mode", command=self.start_normal_mode, font=("Arial", 18))
        self.normal_mode_button.pack(pady=20)

        self.abyss_mode_button = tk.Button(self.master, text="Abyss Mode", command=self.start_abyss_mode, font=("Arial", 18))
        self.abyss_mode_button.pack(pady=20)

        self.exit_button = tk.Button(self.master, text="Exit", command=self.master.destroy, font=("Arial", 18))
        self.exit_button.pack(pady=20)

    def start_normal_mode(self):
        self.master.destroy()
        root = tk.Tk()
        my_gui = GenshinDel(root)
        root.mainloop()

    def start_abyss_mode(self):
        self.master.destroy()
        root = tk.Tk()
        my_gui = GenshinDel(root, mode="abyss")  # Pass the mode as an argument
        root.mainloop()


class GenshinDel:
    def __init__(self, master):
        self.next_round_button = None
        self.master = master
        self.target_character = random.choice(characters)
        self.guesses = []
        self.max_guesses = 5
        self.clue_table = [["Guess", "Element", "Weapon", "Region", "Correct Clues"]]
        self.streak = 0
        self.high_score = 0
        self.try_count = 0

        self.master.geometry("1200x600")  # Set the window size
        self.master.title("Genshin Impact Character Guesser")

        self.top_frame = tk.Frame(self.master)
        self.top_frame.pack(fill="x")

        self.streak_label = tk.Label(self.top_frame, text="Streak: 0", font=("Arial", 18), bg="#f0f0f0")
        self.streak_label.pack(side="left", padx=10)

        self.high_score_label = tk.Label(self.top_frame, text="High Score: 0", font=("Arial", 18), bg="#f0f0f0")
        self.high_score_label.pack(side="left", padx=10)

        self.try_count_label = tk.Label(self.top_frame, text="Try Count: 0", font=("Arial", 18), bg="#f0f0f0")
        self.try_count_label.pack(side="right", padx=10)

        self.guess_label = tk.Label(self.master, text="Enter a character's name:", font=("Arial", 18), bg="#f0f0f0")
        self.guess_label.pack(pady=20)

        self.guess_entry = tk.Entry(self.master, font=("Arial", 18))
        self.guess_entry.pack()

        self.guess_button = tk.Button(self.master, text="Guess", command=self.check_guess, font=("Arial", 18))
        self.guess_button.pack(pady=10)

        self.clue_text = tk.Text(self.master, height=10, width=80, font=("Arial", 14))
        self.clue_text.pack(pady=20)
        self.clue_text.insert(tk.END, tabulate(self.clue_table, headers="firstrow", tablefmt="orgtbl") + "\n")
        self.clue_text.config(state="disabled")

        self.new_round_button = tk.Button(self.master, text="New Round", command=self.next_round, font=("Arial", 18))
        self.new_round_button.pack(pady=10)

    def check_guess(self):
        user_guess = self.guess_entry.get()
        self.guess_entry.delete(0, tk.END)

        if user_guess.lower() == self.target_character["name"].lower():
            self.clue_text.config(state="normal")
            self.clue_text.delete(1.0, tk.END)
            self.clue_text.insert(tk.END, "Correct! " + self.target_character["name"] + " (" + self.target_character["element"] + ") with a " + self.target_character["weapon"] + " from " + self.target_character["region"] + "\n")
            self.clue_text.config(state="disabled")
            self.streak += 1
            if self.streak > self.high_score:
                self.high_score = self.streak
            self.streak_label.config(text=f"Streak: {self.streak}")
            self.high_score_label.config(text=f"High Score: {self.high_score}")
        else:
            self.guesses.append(user_guess)
            self.try_count += 1
            self.try_count_label.config(text=f"Try Count: {self.try_count}")

            guess_character = next((char for char in characters if char["name"].lower() == user_guess.lower()), None)
            if guess_character:
                correct_clues = []
                if guess_character["element"] == self.target_character["element"]:
                    correct_clues.append("Element")
                if guess_character["weapon"] == self.target_character["weapon"]:
                    correct_clues.append("Weapon")
                if guess_character["region"] == self.target_character["region"]:
                    correct_clues.append("Region")
                self.clue_table.append([guess_character["name"], guess_character["element"], guess_character["weapon"], guess_character["region"], ", ".join(correct_clues)])
            else:
                self.clue_table.append([user_guess, "Unknown", "Unknown", "Unknown", "Unknown"])

            self.clue_text.config(state="normal")
            self.clue_text.delete(1.0, tk.END)
            self.clue_text.insert(tk.END, tabulate(self.clue_table, headers="firstrow", tablefmt="orgtbl") + "\n")
            self.clue_text.config(state="disabled")

            if len(self.guesses) == self.max_guesses:
                self.clue_text.config(state="normal")
                self.clue_text.insert(tk.END, "Game Over! The character was " + self.target_character["name"] + " (" + self.target_character["element"] + ") with a " + self.target_character["weapon"] + " from " + self.target_character["region"] + "\n")
                self.clue_text.config(state="disabled")
                messagebox.showinfo("Game Over", "The character was " + self.target_character["name"] + " (" + self.target_character["element"] + ") with a " + self.target_character["weapon"] + " from " + self.target_character["region"])

    def next_round(self):
        self.target_character = random.choice(characters)
        self.guesses = []
        self.clue_table = [["Guess", "Element", "Weapon", "Region", "Correct Clues"]]
        self.clue_text.config(state="normal")
        self.clue_text.delete(1.0, tk.END)
        self.clue_text.insert(tk.END, tabulate(self.clue_table, headers="firstrow", tablefmt="orgtbl") + "\n")
        self.clue_text.config(state="disabled")
        self.try_count = 0
        self.try_count_label.config(text=f"Try Count: {self.try_count}")

root = tk.Tk()
my_menu = Menu(root)
root.mainloop()
