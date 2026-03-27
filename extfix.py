"""Mass renames file extensions in a specified directory.

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

from pathlib import Path

import sys


DIRECTORY_NAME = "Test"   # The directory path with all the files to be fixed.
TARGET_EXT = ".jpg"       # The extension you want to be replaced.
NEW_EXT = ".png"          # The new extension to replace with.


if __name__ == "__main__":
  # Clean the extensions incase of user-error.
  TARGET_EXT = TARGET_EXT.lower().strip()
  NEW_EXT = NEW_EXT.lower().strip()
  # If user forgets the ".", add it for them.
  if TARGET_EXT and not TARGET_EXT.startswith("."):
    TARGET_EXT = "." + TARGET_EXT
  if NEW_EXT and not NEW_EXT.startswith("."):
    NEW_EXT = "." + NEW_EXT

  # Counters
  success_count = 0
  skip_count = 0
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
      continue

    # File does not have the right extension to convert.
    if not file.name.endswith(TARGET_EXT):
      skip_count += 1
      print(f"[WARNING] {file.name}: skipped, not the "
            f"target extension ({TARGET_EXT}).")
      continue

    # Edge case: TARGET_EXT == "" is true for everything.
    if TARGET_EXT == "" and file.suffix != "":
      # Skip file if file already has a suffix.
      continue

    # Create new file with the extension.
    clean_name = file.name.removesuffix(TARGET_EXT)
    new_file = file.with_name(f"{clean_name}{NEW_EXT}")

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
        f"{skip_count} skipped and {error_count} errors.")
