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
  # App constants.
  FONT_FAMILY = "Roboto"
  LABEL_FONT_SIZE = 18
  BUTTON_FONT_SIZE = 14
  PAD_X = 14  # X-axis padding.
  PAD_Y = 14   # Y-axis padding.

  def __init__(self):
    super().__init__()  # Inherit from CTk and initialize.

    # Data storage.
    self.selected_entry = None

    # App settings.
    self.title("extfix")      # Set the title of the app.
    self.geometry("600x400")  # Set app size.
    self.resizable(0, 0)      # Make app unresizeable.

    # App creation.
    self.create_directory_section()
    self.create_extensions_section()


  def create_directory_section(self):
    # Directory selector section.
    dir_frame = ctk.CTkFrame(self, fg_color="transparent")
    dir_frame.pack(fill="x")
    # Directory label.
    dir_label = ctk.CTkLabel(dir_frame, text="Target Directory: ",
                            font=(self.FONT_FAMILY, self.LABEL_FONT_SIZE))
    dir_label.pack(padx=(self.PAD_X, self.PAD_X/2), pady=(self.PAD_Y, 0),
                   side="left")
    # Selected entry label.
    self.selected_entry = ctk.CTkEntry(dir_frame, font=(self.FONT_FAMILY,
                                                        self.LABEL_FONT_SIZE),
                                  border_width=0, corner_radius=0,
                                  fg_color=("gray70", "gray30"))
    self.selected_entry.insert(0, "No Directory Selected")
    self.selected_entry.configure(state="readonly")
    self.selected_entry.pack(padx=(0, self.PAD_X), pady=(self.PAD_Y, 0),
                             side="left", fill="x", expand=True)
    # Directory selector button.
    dir_selector_btn = ctk.CTkButton(self, text="Select",
                                     font=(self.FONT_FAMILY,
                                           self.BUTTON_FONT_SIZE))
    dir_selector_btn.pack(padx=self.PAD_X, pady=(self.PAD_Y/2, 0), anchor="w")

  def create_extensions_section(self):
    ext_frame = ctk.CTkFrame(self, fg_color="transparent")
    ext_frame.pack(fill="x")
    # Target extension (extension to be replaced).
    target_ext_label = ctk.CTkLabel(ext_frame, text="Target Extension:",
                                    font=(self.FONT_FAMILY,
                                          self.LABEL_FONT_SIZE))
    target_ext_label.pack(padx=(self.PAD_X, self.PAD_X/2),
                          pady=self.PAD_Y, side="left")
    target_ext_entry = ctk.CTkEntry(ext_frame, corner_radius=0,
                                    placeholder_text="example: .png")
    target_ext_entry.pack(side="left")
    # New extension (extension to replace with).
    new_ext_entry = ctk.CTkEntry(ext_frame, corner_radius=0,
                                 placeholder_text="example: .jpg")
    new_ext_entry.pack(padx=(0, self.PAD_X), side="right")
    new_ext_label = ctk.CTkLabel(ext_frame, text="New Extension:",
                                 font=(self.FONT_FAMILY,
                                       self.LABEL_FONT_SIZE))
    new_ext_label.pack(padx=(0, self.PAD_X/2), side="right")


if __name__ == "__main__":
  app = ExtFixApp()
  app.mainloop()
