#!/usr/bin/python3

import tkinter as tk
from tkinter import messagebox
import os
import random
import csv

# Predefined lists of words for generating code names
adjectives = ["Silent", "Crimson", "Shadow", "Swift", "Mighty", "Stealthy", "Lone", "Iron",
              "Agile", "Bold", "Bright", "Brilliant", "Calm", "Clever", "Cold","Courageous", "Daring",
              "Dazzling", "Deep", "Diligent", "Divine", "Dynamic", "Elegant", "Fierce", "Fiery",
              "Gentle", "Glorious", "Golden", "Graceful", "Grand", "Hardy", "Heavenly", "Heroic",
              "Keen", "Luminous", "Majestic", "Noble", "Peaceful", "Powerful", "Pristine", "Radiant",
              "Regal", "Resilient", "Robust", "Sacred", "Serene", "Sharp", "Shining", "Silent", "Stalwart",
              "Strong", "Tenacious", "Tranquil", "True", "Unyielding", "Vibrant", "Vivid", "Wise"]

nouns = ["Falcon", "Wolf", "Tiger", "Phantom", "Eagle", "Raven", "Panther", "Sword",
         "Archer", "Arrow","Bear", "Blaze", "Blossom", "Boulder", "Breeze", "Bull",
         "Canyon","Champion", "Comet", "Crest", "Crown", "Dagger", "Dragon", "Ember",
         "Fang", "Flame", "Glacier", "Griffin", "Guardian", "Hawk", "Horizon",
         "Hunter", "Kraken", "Lantern", "Lion", "Lynx", "Mammoth", "Meteor",
         "Moon", "Mountain", "Ocean", "Oracle", "Phoenix", "Pillar", "River",
         "Saber", "Sentinel", "Shield", "Sky", "Spear", "Spirit", "Stag",
         "Star", "Storm", "Tempest", "Thunder", "Trail", "Warden" ]

# Function to generate a random codename
def generate_codename():
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    return f"{adjective} {noun}"

# Function to save the codename and additional details into a .csv file
def save_to_csv(codename, details):
    filename = "codenames.csv"

    # Check if the file exists
    file_exists = os.path.exists(filename)

    # Open the file in append mode
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Write headers if the file is new
        if not file_exists:
            writer.writerow(["Codename", "Details"])
        
        # Write the new codename and details
        writer.writerow([codename, details])

# Function to handle the button click event
def on_generate_and_save():
    codename = generate_codename()
    details = details_entry.get()

    if details.strip() == "":
        messagebox.showerror("Error", "Details cannot be empty.")
        return

    save_to_csv(codename, details)
    messagebox.showinfo("Success", f"Codename '{codename}' saved successfully!")
    codename_label.config(text=f"Generated Codename: {codename}")
    details_entry.delete(0, tk.END)

# Create the main tkinter window
root = tk.Tk()
root.title("Codename Generator")
root.geometry("400x300")

# Add a label for instructions
instruction_label = tk.Label(root, text="Enter details for the case, person, or investigation:")
instruction_label.pack(pady=10)

# Add an entry field for case details
details_entry = tk.Entry(root, width=50)
details_entry.pack(pady=5)

# Add a button to generate and save the codename
generate_button = tk.Button(root, text="Generate and Save Codename", command=on_generate_and_save)
generate_button.pack(pady=10)

# Add a label to display the generated codename
codename_label = tk.Label(root, text="")
codename_label.pack(pady=20)

# Run the tkinter event loop
root.mainloop()
