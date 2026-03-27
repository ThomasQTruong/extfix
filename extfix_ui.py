"""Mass renames file extensions in a specified directory.

  This program iterates through a specified directory and
  replaces all occurrences of the target extension with a
  new specified extension.

  Example (.png to .jpg):
    file1.png -> file1.jpg
    file2.png -> file2.jpg
"""

import customtkinter as ctk


ctk.set_appearance_mode("dark")  # Set to dark mode.


class ExtFixApp(ctk.CTk):
  def __init__(self):
    super().__init__()  # Inherit from CTk and initialize.

    self.title("extfix")      # Set the title of the app.
    self.geometry("600x400")  # Set app size.
    self.resizable(0, 0)      # Make app unresizeable.

    self.create_directory_section()


  def create_directory_section(self):
    # Directory selector section.
    dir_frame = ctk.CTkFrame(self, fg_color="transparent")
    dir_frame.pack(fill="x")
    # Directory label.
    dir_label = ctk.CTkLabel(dir_frame, text="Target Directory: ",
                            font=("Roboto", 18))
    dir_label.pack(padx=(10, 7), pady=7, side="left")
    # Selected entry label.
    selected_entry = ctk.CTkEntry(dir_frame, font=("Roboto", 18),
                                  border_width=0, corner_radius=0,
                                  fg_color=("gray70", "gray30"))
    selected_entry.insert(0, "No Directory Selected")
    selected_entry.configure(state="readonly")
    selected_entry.pack(padx=(0, 10), ipadx=10, side="left", fill="x",
                        expand=True)
    # Directory selector button.
    dir_selector_btn = ctk.CTkButton(self, text="Select", font=("Roboto", 14))
    dir_selector_btn.pack(padx=10, anchor="w")


if __name__ == "__main__":
  app = ExtFixApp()
  app.mainloop()
