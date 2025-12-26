import os
from pathlib import Path

FOLDER_NAME = "Test"  # The directory path with all the files to be fixed.
TARGET_EXT = ".png"   # The extension you want to be replaced.
NEW_EXT = ".jpg"      # The new extension to replace with.

if __name__ == "__main__":
  # Lowercase the extensions incase of user-error.
  TARGET_EXT = TARGET_EXT.lower()
  NEW_EXT = NEW_EXT.lower()

  # Counters
  successCount = 0
  skipCount = 0
  errorCount = 0

  files = [
    os.path.join(FOLDER_NAME, file)                     # (3) Save file path from subdirectory.
    for file in os.listdir(FOLDER_NAME)                 # (1) For every file in subdirectory.
    if os.path.isfile(os.path.join(FOLDER_NAME, file))  # (2) If it is a valid file.
  ]
  
  # For every file in the subdirectory.
  for file in files:
    # Obtain path.
    filePath = Path(file)

    # File does not have the right extension to convert.
    if filePath.suffix.lower() != TARGET_EXT:
      skipCount += 1
      print(f"[WARNING] {filePath} has been skipped since it is not the target extension ({TARGET_EXT}).")
      continue

    # Create new file with the extension.
    if TARGET_EXT == "":
      # No extension for the file, just concat the extension.
      newFile = file + NEW_EXT
    else:
      newFile = str(filePath.with_suffix(NEW_EXT))

    # Already a file with the same name using that extension!
    if os.path.exists(newFile):
      print(f"[ERROR] {filePath} cannot be converted, {newFile} already exists!")
      errorCount += 1
      continue

    # File can be renamed.
    if (filePath.suffix.lower() == TARGET_EXT):
      os.rename(file, newFile)
      successCount += 1
  
  print(f"Finished converting {successCount} files with {skipCount} skipped and {errorCount} errors.")
