import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess
from tkinter import messagebox
import registration_form
import login

def open_admin_py():
    try:
        # Ensure that you use the correct path to the Python interpreter and script if necessary
        subprocess.Popen(["python", "admin.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while opening admin.py: {str(e)}")

class LandingPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rent-A-Car Management System")
        self.geometry("800x600")
        self.configure(bg="#F5DEB3")

        # Main container setup
        main_container = ttk.Frame(self, style="MainContainer.TFrame")
        main_container.pack(pady=20, padx=20, fill="both", expand=True)

        # Landing Page Content
        landing_page_frame = ttk.Frame(main_container, style="LandingPage.TFrame")
        landing_page_frame.pack(pady=20)

        logo_image = Image.open("Main_pic.jpeg")
        logo_image = logo_image.resize((200, 200))
        self.logo_photo = ImageTk.PhotoImage(logo_image)
        logo_label = ttk.Label(landing_page_frame, image=self.logo_photo)
        logo_label.pack(pady=10)

        # Button setup
        button_frame = ttk.Frame(main_container, style="ButtonFrame.TFrame")
        button_frame.pack(pady=20)

        self.configure_style()  # Configure styles before creating buttons

        login_button = ttk.Button(button_frame, text="Login", command=self.open_Login_form, style="Custom.TButton")
        login_button.pack(side="left", padx=10)

        register_button = ttk.Button(button_frame, text="Register", command=self.open_registration_form, style="Custom.TButton")
        register_button.pack(side="left", padx=10)

        open_admin_button = ttk.Button(button_frame, text="Open Admin", command=open_admin_py, style="Custom.TButton")
        open_admin_button.pack(side="left", padx=10)

    def open_registration_form(self):
        registration_window = registration_form.RegistrationForm(self)
        registration_window.grab_set()

    def open_Login_form(self):
        login_window = login.LoginForm(self)
        login_window.grab_set()

    def configure_style(self):
        style = ttk.Style()
        style.theme_use("default")

        # Main container and frames style
        style.configure("MainContainer.TFrame", background="#F5DEB3")
        style.configure("LandingPage.TFrame", background="#F5DEB3")
        style.configure("ButtonFrame.TFrame", background="#F5DEB3")

        # Custom button style
        style.configure("Custom.TButton", background="#8B4513", foreground="#FFFFFF", font=("Arial", 14, "bold"), padding=10, relief="raised")
        style.map("Custom.TButton",
                  background=[('active', '#B4690E'), ('pressed', '#A2560D')],
                  foreground=[('pressed', '#FFFFFF'), ('active', '#FFFFFF')])

if __name__ == "__main__":
    app = LandingPage()
    app.mainloop()
