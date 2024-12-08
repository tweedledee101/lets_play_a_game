import random
import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Fantasma's: Game of Horror")
root.geometry("600x400")  # Set window size

# Global variables
user_name = ""
message_label = None
user_input = None

def clear_screen():
    """Clear everything from the window."""
    for widget in root.winfo_children():
        widget.destroy()

def show_message(message):
    """Display a message in the window."""
    global message_label
    message_label = tk.Label(root, text=message, font=("Helvetica", 14), wraplength=500, justify="center")
    message_label.pack(pady=20)

def get_user_input(prompt, button_text="Submit", next_function=None):
    """Create an input box and button to get input from the user."""
    global user_input
    input_label = tk.Label(root, text=prompt, font=("Helvetica", 12))
    input_label.pack()
    
    user_input = tk.Entry(root, font=("Helvetica", 14))
    user_input.pack(pady=10)
    
    submit_button = tk.Button(root, text=button_text, command=lambda: next_function(user_input.get()))
    submit_button.pack()

def start_game():
    """Initial screen where user enters their name."""
    clear_screen()
    show_message("Welcome to Fantasma's: Game of Horror\n\nWhat's your name, dear friend?")
    get_user_input("Enter your name:", "Continue", on_name_submit)

def on_name_submit(name):
    """After user enters their name, show next screen."""
    global user_name
    user_name = name
    clear_screen()
    show_message(f"Ah yes, {user_name}, I thought I smelled fear.")
    next_button = tk.Button(root, text="Next", command=feelings_menu)
    next_button.pack()

def feelings_menu():
    """Show the feelings menu to the user."""
    clear_screen()
    show_message(f"{user_name}, how do you feel about Fantasma?")
    
    feelings = {
        "1": "Insulted",
        "2": "Scared",
        "3": "Doesn't care"
    }
    
    for key, value in feelings.items():
        button = tk.Button(root, text=f"{key}: {value}", command=lambda choice=key: on_feelings_choice(choice))
        button.pack(pady=5)

def on_feelings_choice(choice):
    """Handle user's feeling choice."""
    clear_screen()
    
    options = {
        "1": "A spirited one, eh, and disrespectful to boot. Maybe we should learn a lesson or two before we continue.",
        "2": "Quit your blubbering, you oafish cow! Get some backbone, we've got work to do.",
        "3": "So, a magical being brings you to a world unknown, and you're not the least bit curious? Alright, we'll see how you do on your own for a bit, hope you don't choke off your own ego!"
    }

    if choice in options:
        show_message(options[choice])
    else:
        show_message("Invalid choice. Please select 1, 2, or 3.")

    play_again_button = tk.Button(root, text="Play Again", command=start_game)
    play_again_button.pack(pady=10)
    
    quit_button = tk.Button(root, text="Quit", command=root.quit)
    quit_button.pack(pady=10)

# Start the game
start_game()

# Start the tkinter event loop
root.mainloop()
