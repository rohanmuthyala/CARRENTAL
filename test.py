import tkinter as tk
from tkinter import ttk
import subprocess
from tkinter import messagebox
from PIL import Image, ImageTk

# Assume the modules registration_form and login are properly imported if they are needed elsewhere
import registration_form
import login

def open_admin_py():
    try:
        # Correct path to the Python interpreter and script might be needed
        subprocess.Popen(["python", "admin.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)
        print("Admin panel launched!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while opening admin.py: {str(e)}")
        
class LandingPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rent-A-Car Management System")
        self.geometry("800x600")
        self.configure(bg="#F5DEB3")

        main_container = ttk.Frame(self, style="MainContainer.TFrame")
        main_container.pack(pady=20, padx=20, fill="both", expand=True)

        landing_page_frame = ttk.Frame(main_container, style="LandingPage.TFrame")
        landing_page_frame.pack(pady=20)

        logo_image = Image.open("Main_pic.jpeg")
        logo_image = logo_image.resize((200, 200))
        self.logo_photo = ImageTk.PhotoImage(logo_image)
        logo_label = ttk.Label(landing_page_frame, image=self.logo_photo)
        logo_label.pack(pady=10)

        heading_label = ttk.Label(landing_page_frame, text="Welcome to Rent-A-Car", font=("Arial", 24, "bold"), style="Heading.TLabel")
        heading_label.pack(pady=10)

        description_label = ttk.Label(landing_page_frame, text="Discover the joy of hassle-free travel with our premium car rental service. Experience the freedom of the road and create unforgettable memories.", wraplength=500, font=("Arial", 14), style="Description.TLabel")
        description_label.pack(pady=10)

        button_frame = ttk.Frame(main_container, style="ButtonFrame.TFrame")
        button_frame.pack(pady=20)

        login_button = ttk.Button(button_frame, text="Login", command=self.open_Login_form, style="Button.TButton")
        login_button.pack(side="left", padx=10)

        register_button = ttk.Button(button_frame, text="Register", command=self.open_registration_form, style="Button.TButton")
        register_button.pack(side="left", padx=10)

        open_admin_button = tk.Button(button_frame, text="Open Admin", command=open_admin_py)
        open_admin_button.pack(side="left", padx=10)

        self.configure_style()

    def open_registration_form(self):
        registration_window = registration_form.RegistrationForm(self)
        registration_window.grab_set()

    def open_Login_form(self):
        login_window = login.LoginForm(self)
        login_window.grab_set()

    def configure_style(self):
        style = ttk.Style()
        style.theme_use("default")
        style.configure("MainContainer.TFrame", background="#F5DEB3")
        style.configure("LandingPage.TFrame", background="#F5DEB3")
        style.configure("Heading.TLabel", background="#F5DEB3", foreground="#8B4513", font=("Arial", 24, "bold"))
        style.configure("Description.TLabel", background="#F5DEB3", foreground="#4F4F4F", font=("Arial", 14))
        style.configure("ButtonFrame.TFrame", background="#F5DEB3")
        style.configure("Button.TButton", background="#8B4513", foreground="#FFFFFF", font=("Arial", 14, "bold"), padding=10, relief="raised")

if __name__ == "__main__":
    app = LandingPage()
   
