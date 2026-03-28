"""Mass rename file extensions in a specified folder to a different extension.

  This program iterates through a specified directory and
  replaces all occurrences of the target extension with a
  new specified extension.

  Example (.png to .jpg):
    file1.png -> file1.jpg
    file2.png -> file2.jpg
  
  Attributes:
    DIRECTORY_NAME (str): The directory path with all the files to be fixed.
    TARGET_EXT (str): The extension you want to be replaced.
    NEW_EXT (str): The new extension to replace with.
"""

import sys
from pathlib import Path


DIRECTORY_NAME = "Test"   # The directory path with all the files to be fixed.
TARGET_EXT = ".jpg"       # The extension you want to be replaced.
NEW_EXT = ".png"          # The new extension to replace with.


def main():
  # Clean the extensions incase of user-error.
  target_ext = TARGET_EXT.lower().strip()
  new_ext = NEW_EXT.lower().strip()
  # If user forgets the ".", add it for them.
  if target_ext and not target_ext.startswith("."):
    target_ext = "." + target_ext
  if new_ext and not new_ext.startswith("."):
    new_ext = "." + new_ext

  # Counters
  success_count = 0
  warning_count = 0
  error_count = 0

  # Grab every file in the directory into the list.
  directory = Path(DIRECTORY_NAME)
  if not directory.exists():
    print(f"[Error] {directory}: is not a valid directory.")
    sys.exit(1)

  # For every file in the subdirectory.
  for file in directory.iterdir():
    # If it is not a file, skip it.
    if not file.is_file():
      warning_count += 1
      print(f"[WARNING] {file.name}: skipped, not a valid file.")
      continue

    # File does not have the right extension to convert.
    if not file.name.endswith(target_ext):
      warning_count += 1
      print(f"[WARNING] {file.name}: skipped, not the "
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
      print(f"[ERROR] {file.name}: cannot be converted, "
            f"{new_file.name} already exists!")
      error_count += 1
      continue

    # File can be renamed.
    file.rename(new_file)
    success_count += 1

  print(f"Finished converting {success_count} files with "
        f"{warning_count} skipped and {error_count} errors.")


if __name__ == "__main__":
  main()
  input("Press enter to close...")
