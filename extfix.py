"""Mass rename file extensions in a specified folder to a different extension.

  This program iterates through a specified directory and
  replaces all occurrences of the target extension with a
  new specified extension.

  Example (.png to .jpg):
    file1.png -> file1.jpg
    file2.png -> file2.jpg
"""

import os
import sys
import customtkinter as ctk
from tkinter import filedialog
from pathlib import Path
from PIL import Image, ImageTk

ctk.set_appearance_mode("dark")  # Set to dark mode.

def get_resource_path(rel_path):
  """Get absolute path to resource for dev and PyInstaller."""
  try:
    base_path = sys._MEIPASS  # pylint: disable=protected-access
  except AttributeError:
    base_path = os.path.abspath(".")
  return os.path.join(base_path, rel_path)


class ExtFixApp(ctk.CTk):
  """
  A CustomTkinter-based GUI application for mass-renaming file extensions.

  This class inherits from the CustomTkinter class, creates the UI layout,
  and handles the file renaming logic with a visual progress bar.

  Attributes:
    selected_entry (ctk.CTkEntry): Display, shows the current target directory.
    target_ext_entry (ctk.CTkEntry): Input field, the extension to be replaced.
    new_ext_entry (ctk.CTkEntry): Input field, the extension to replace with.
    start_btn (ctk.CTkButton): Control, triggers the renaming task.
    progress_bar (ctk.CTkProgressBar): Display, shows the progress of the task.
    extfix_output (ctk.CTkTextbox): Display, shows the task log warnings,
        errors, and completion messages.
  """

  # App constants.
  FONT_FAMILY = "Roboto"
  SECTION_FONT = (FONT_FAMILY, 20, "bold")
  LABEL_FONT = (FONT_FAMILY, 18)
  BUTTON_FONT = (FONT_FAMILY, 14, "bold")
  PAD_X = 14  # X-axis padding.
  PAD_Y = 14   # Y-axis padding.

  def __init__(self):
    """Initialize the application window and build the UI layout."""
    super().__init__()  # Inherit from CTk and initialize.

    # Data storage.
    self.selected_entry = None
    self.target_ext_entry = None
    self.new_ext_entry = None
    self.start_btn = None
    self.progress_bar = None
    self.extfix_output = None
    self.icon = None

    # App settings.
    self.title("extfix")                  # Set the title of the app.
    self.geometry("500x400")              # Set app size.
    self.resizable(0, 0)                  # Make app unresizeable.
    self.after(200, self.set_app_icon)  # Set the app icon.

    # App creation.
    self.create_directory_section()
    self.create_extensions_section()
    self.create_extfix_section()


  def set_app_icon(self):
    try:
      # Obtain path to icon and set it.
      icon_path = get_resource_path("icon.png")
      if not os.path.exists(icon_path):
        icon_path = get_resource_path(os.path.join(".assets", "app",
                                                   "icon.png"))
      # User is on Windows OS.
      if sys.platform.startswith("win"):
        ico_path = icon_path.replace(".png", ".ico")
        self.iconbitmap(ico_path)
      else:
        # Not Windows OS, use a different method.
        raw_img = Image.open(icon_path)
        self.icon = ImageTk.PhotoImage(raw_img)
        self.wm_iconphoto(False, self.icon)
    except (FileNotFoundError, AttributeError):
      # App icon cant be found, ignore and leave default icon.
      pass

  def create_directory_section(self):
    """Create the Directory section of the UI."""
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
    dir_selector_btn = ctk.CTkButton(self, text="Select", font=self.BUTTON_FONT,
                                     command=self.browse_directory)
    dir_selector_btn.pack(padx=self.PAD_X, pady=(self.PAD_Y/2, 0))

  def create_extensions_section(self):
    """Create the Extensions section of the UI."""
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
    self.target_ext_entry = ctk.CTkEntry(ext_frame, corner_radius=0,
                                         placeholder_text="example: .png")
    self.target_ext_entry.pack(pady=(self.PAD_Y/2, 0), side="left")
    # New extension (extension to replace with).
    self.new_ext_entry = ctk.CTkEntry(ext_frame, corner_radius=0,
                                      placeholder_text="example: .jpg")
    self.new_ext_entry.pack(padx=(0, self.PAD_X),
                            pady=(self.PAD_Y/2, 0), side="right")
    new_ext_label = ctk.CTkLabel(ext_frame, text="New:",
                                 font=self.LABEL_FONT)
    new_ext_label.pack(padx=(0, self.PAD_X/2), pady=(self.PAD_Y/2, 0),
                       side="right")

  def create_extfix_section(self):
    """Create the ExtFix section of the UI."""
    # ExtFix section.
    extfix_label = ctk.CTkLabel(self, text="ExtFix", font=self.SECTION_FONT,
                                 fg_color=("gray70", "gray30"))
    extfix_label.pack(fill="x", pady=(self.PAD_Y, 0))
    # ExtFix frame.
    extfix_frame = ctk.CTkFrame(self, fg_color="transparent")
    extfix_frame.pack(fill="both", expand=True)
    # Start button.
    self.start_btn = ctk.CTkButton(extfix_frame, text="Start",
                                     font=self.BUTTON_FONT,
                                     command=self.start_extfix)
    self.start_btn.pack(pady=(self.PAD_Y/2, 0))
    # Progress bar.
    self.progress_bar = ctk.CTkProgressBar(extfix_frame,
                                           orientation="horizontal",
                                           height=self.PAD_Y, corner_radius=0)
    self.progress_bar.set(0)
    self.progress_bar.pack(pady=(self.PAD_Y/2, 0), fill="x")
    # ExtFix output.
    self.extfix_output = ctk.CTkTextbox(extfix_frame, state="disabled")
    self.extfix_output.pack(fill="both", expand=True)

  def browse_directory(self):
    """Open a system folder picker and update the selected_entry field."""
    directory_path = filedialog.askdirectory()
    if directory_path:
      # Unlock the entry.
      self.selected_entry.configure(state="normal")
      # Clear the entry.
      self.selected_entry.delete(0, "end")
      # Insert selected path.
      self.selected_entry.insert(0, directory_path)
      # Lock the entry.
      self.selected_entry.configure(state="readonly")

  def start_extfix(self):
    """
    Initialize the batch renaming process.

    Validate and clean user input, iterate through the directory using pathlib,
    and rename files matching the target extension to the new extension.
    Updates the progress bar in real time.
    """
    self.clear_output()

    # Grab values from entries.
    directory_path = self.selected_entry.get()
    target_ext = self.target_ext_entry.get().lower().strip()
    new_ext = self.new_ext_entry.get().lower().strip()
    # If user forgets the ".", add it for them.
    if target_ext and not target_ext.startswith("."):
      target_ext = "." + target_ext
    if new_ext and not new_ext.startswith("."):
      new_ext = "." + new_ext

    # One or more of the entries were not filled!
    if directory_path == "No Directory Selected":
      self.send_output("[Error] Please select the directory.")
      return

    # Grab the directory and check if it exts.
    directory = Path(directory_path)
    if not directory.exists():
      self.send_output(f"[Error] {directory}: is not a valid directory.")
      return

    # Lock the button so the user can't press until the process is done.
    self.start_btn.configure(state="disabled")

    # Counters
    success_count = 0
    skip_count = 0
    error_count = 0

    # Amount of items in the directory (for progress bar).
    item_total = sum(1 for _ in os.scandir(directory_path))

    # For every file in the subdirectory.
    index = 0
    for file in directory.iterdir():
      # Draw the progress bar (rate limited)!
      index += 1
      if index % 100 == 0 or index == item_total:
        self.progress_bar.set(index/item_total)
        self.update()

      # If it is not a file, skip it.
      if not file.is_file():
        continue

      # File does not have the right extension to convert.
      if not file.name.endswith(target_ext):
        skip_count += 1
        self.send_output(f"[WARNING] {file.name}: skipped, not the "
                         f"target extension ({target_ext}).")
        continue

      # Edge case: target_ext == "" is true for everything.
      if target_ext == "" and file.suffix != "":
        # Skip file if file already has a suffix.
        continue

      # Create new file with the extension.
      clean_name = file.name.removesuffix(target_ext)
      new_file = file.with_name(f"{clean_name}{new_ext}")

      # Already a file with the same name using that extension!
      if new_file.exists():
        self.send_output(f"[ERROR] {file.name}: cannot be converted, "
                         f"{new_file.name} already exists!")
        error_count += 1
        continue

      # File can be renamed.
      file.rename(new_file)
      success_count += 1

    self.send_output(f"Finished converting {success_count} files with "
                     f"{skip_count} skipped and {error_count} errors.")
    self.extfix_output.see("end")

    # Unlock button; process is finished.
    self.update()  # Flush the event queue.
    self.start_btn.configure(state="normal")

  def clear_output(self):
    """Clear the extfix_output log."""
    # Unlock the output.
    self.extfix_output.configure(state="normal")

    # Delete all the output from line 1, character 0 to the end.
    self.extfix_output.delete("1.0", "end")

    # Lock the output.
    self.extfix_output.configure(state="disabled")

  def send_output(self, output_message):
    """
    Send a message to the extfix_output log.
    
    Args:
      output_message (str): The message to send.
    """
    # Unlock the output.
    self.extfix_output.configure(state="normal")

    # Send the output.
    self.extfix_output.insert("end", output_message + "\n")

    # Lock the output.
    self.extfix_output.configure(state="disabled")


if __name__ == "__main__":
  app = ExtFixApp()
  app.mainloop()
