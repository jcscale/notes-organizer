import customtkinter as ctk

class NewWindow(ctk.CTkToplevel):
    def __init__(self, master, title):
        super().__init__(master)
        self.title(title)
        self.geometry("500x500")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # self.lift()
        # self.focus_force()
        # self.grab_set()
        
        # Initial lift and focus
        # self.lift_and_focus()

    def lift_and_focus(self):
        """Lift and focus the window."""
        self.lift()
        self.focus()

    def reset_lift_and_focus(self):
        """Reset the window's stacking order and focus, then lift and focus again."""
        # Withdraw and deiconify to reset stacking order
        self.withdraw()
        self.deiconify()
        # Use after to delay the lift and focus
        self.after(100, self.lift_and_focus)