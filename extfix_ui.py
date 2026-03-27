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
  SECTION_FONT = (FONT_FAMILY, 20, "bold")
  LABEL_FONT = (FONT_FAMILY, 18)
  BUTTON_FONT = (FONT_FAMILY, 14, "bold")
  PAD_X = 14  # X-axis padding.
  PAD_Y = 14   # Y-axis padding.

  def __init__(self):
    super().__init__()  # Inherit from CTk and initialize.

    # Data storage.
    self.selected_entry = None
    self.progress_bar = None
    self.extfix_output = None

    # App settings.
    self.title("extfix")      # Set the title of the app.
    self.geometry("500x500")  # Set app size.
    self.resizable(0, 0)      # Make app unresizeable.

    # App creation.
    self.create_directory_section()
    self.create_extensions_section()
    self.create_confirm_section()


  def create_directory_section(self):
    # Directory section.
    dir_label = ctk.CTkLabel(self, text="Directory",
                             font=self.SECTION_FONT,
                             fg_color=("gray70", "gray30"))
    dir_label.pack(fill="x")
    # Directory frame.
    dir_frame = ctk.CTkFrame(self, fg_color="transparent")
    dir_frame.pack(fill="x")
    # Selected entry label.
    self.selected_entry = ctk.CTkEntry(dir_frame, font=self.LABEL_FONT,
                                       border_width=0, corner_radius=0,
                                       fg_color=("gray80", "gray20"))
    self.selected_entry.insert(0, "No Directory Selected")
    self.selected_entry.configure(state="readonly")
    self.selected_entry.pack(padx=self.PAD_X, pady=(self.PAD_Y/2, 0),
                             fill="x", expand=True)
    # Directory selector button.
    dir_selector_btn = ctk.CTkButton(self, text="Select", font=self.BUTTON_FONT)
    dir_selector_btn.pack(padx=self.PAD_X, pady=(self.PAD_Y/2, 0))

  def create_extensions_section(self):
    # Extensions section.
    ext_label = ctk.CTkLabel(self, text="Extension Settings",
                             font=self.SECTION_FONT,
                             fg_color=("gray70", "gray30"))
    ext_label.pack(fill="x", pady=(self.PAD_Y, 0))
    # Extensions frame.
    ext_frame = ctk.CTkFrame(self, fg_color="transparent")
    ext_frame.pack(fill="x")
    # Target extension (extension to be replaced).
    target_ext_label = ctk.CTkLabel(ext_frame, text="Target:",
                                    font=self.LABEL_FONT)
    target_ext_label.pack(padx=(self.PAD_X, self.PAD_X/2),
                          pady=(self.PAD_Y/2, 0), side="left")
    target_ext_entry = ctk.CTkEntry(ext_frame, corner_radius=0,
                                    placeholder_text="example: .png")
    target_ext_entry.pack(pady=(self.PAD_Y/2, 0), side="left")
    # New extension (extension to replace with).
    new_ext_entry = ctk.CTkEntry(ext_frame, corner_radius=0,
                                 placeholder_text="example: .jpg")
    new_ext_entry.pack(padx=(0, self.PAD_X),
                       pady=(self.PAD_Y/2, 0), side="right")
    new_ext_label = ctk.CTkLabel(ext_frame, text="New:",
                                 font=self.LABEL_FONT)
    new_ext_label.pack(padx=(0, self.PAD_X/2), pady=(self.PAD_Y/2, 0),
                       side="right")

  def create_confirm_section(self):
    # Confirm section.
    confirm_label = ctk.CTkLabel(self, text="ExtFix", font=self.SECTION_FONT,
                                 fg_color=("gray70", "gray30"))
    confirm_label.pack(fill="x", pady=(self.PAD_Y, 0))
    # Confirm frame.
    confirm_frame = ctk.CTkFrame(self, fg_color="transparent")
    confirm_frame.pack(fill="both", expand=True)
    # Confirm button.
    confirm_btn = ctk.CTkButton(confirm_frame, text="Fix",
                                font=self.BUTTON_FONT)
    confirm_btn.pack(pady=(self.PAD_Y/2, 0))
    # Progress bar.
    self.progress_bar = ctk.CTkProgressBar(confirm_frame,
                                           orientation="horizontal",
                                           height=self.PAD_Y, corner_radius=0)
    self.progress_bar.set(0)
    self.progress_bar.pack(pady=(self.PAD_Y/2, 0), fill="x")
    # ExtFix output.
    self.extfix_output = ctk.CTkTextbox(confirm_frame, state="disabled")
    self.extfix_output.pack(fill="both", expand=True)


if __name__ == "__main__":
  app = ExtFixApp()
  app.mainloop()
