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

app = ctk.CTk()          # Create app.
app.title("extfix")      # Set the title of the app.
app.geometry("600x400")  # Set app size.
app.resizable(0, 0)      # Make app unresizeable.

# Directory selector section.
directory_selector_frame = ctk.CTkFrame(app, fg_color="transparent", height=50)
directory_selector_frame.pack(fill="x")
# Directory label.
directory_label = ctk.CTkLabel(directory_selector_frame,
                               text="Target Directory: ", font=("Roboto", 18))
directory_label.pack(padx=(14, 7), pady=7, side="left")
# Selected label.
selected_label = ctk.CTkLabel(directory_selector_frame,
                              text="No Directory Selected", font=("Roboto", 18),
                              fg_color=("gray70", "gray30"))
selected_label.pack(ipadx=10, side="left")
# Directory selector button.
btn_directory_selector = ctk.CTkButton(app, text="Select", font=("Roboto", 14))
btn_directory_selector.pack(padx=14, anchor="w")

app.mainloop()
