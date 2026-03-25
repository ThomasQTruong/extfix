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

DIRECTORY_NAME = "Test"  # The directory path with all the files to be fixed.
TARGET_EXT = ".png"      # The extension you want to be replaced.
NEW_EXT = ".jpg"         # The new extension to replace with.

if __name__ == "__main__":
  # Lowercase the extensions incase of user-error.
  TARGET_EXT = TARGET_EXT.lower()
  NEW_EXT = NEW_EXT.lower()

  # Counters
  success_count = 0
  skip_count = 0
  error_count = 0

  # Grab every file in the directory into the list.
  directory = Path(DIRECTORY_NAME)
  files = [file for file in directory.iterdir() if file.is_file()]

  # For every file in the subdirectory.
  for file in files:
    # File does not have the right extension to convert.
    if file.suffix.lower() != TARGET_EXT:
      skip_count += 1
      print(f"[WARNING] {file.name} has been skipped since it is not the "
            f"target extension ({TARGET_EXT}).")
      continue

    # Create new file with the extension.
    new_file = file.with_suffix(NEW_EXT)

    # Already a file with the same name using that extension!
    if new_file.exists():
      print(f"[ERROR] {file.name} cannot be converted, "
            f"{new_file.name} already exists!")
      error_count += 1
      continue

    # File can be renamed.
    file.rename(new_file)
    success_count += 1

  print(f"Finished converting {success_count} files with "
        f"{skip_count} skipped and {error_count} errors.")
