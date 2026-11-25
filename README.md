# File Organizer

A Python-based file organizer that automatically sorts files into categorized folders based on their extensions. It also detects hidden files and handles duplicate filenames by generating unique names.

## Features

- **Automatic Categorization:** Sorts files into folders based on their file extensions.
- **Hidden File Detection:** Identifies Linux hidden files and moves them into a separate folder.
- **Duplicate Handling:** Detects existing filenames in the destination.
- **Collision Resolution:** Generates unique filenames using incremental numbering (`file_1.txt`, `file_2.txt`, etc.).
- **Multiple Extension Support:** Handles filenames with multiple dots, such as `archive.tar.gz`.
- **Recursive Collision Handling:** Checks whether generated filenames already exist and increments them when necessary.
- **No External Dependencies:** Built using Python's standard library.

## Folder Structure

After organizing, the destination directory looks like this:

```text
organized_folder/
├── Images/
├── Videos/
├── Audios/
├── Docs/
├── Archives/
├── Exe/
├── Linux/
└── Others/
```

| Folder | File types |
|---|---|
| Images | JPG, PNG, GIF, SVG, WEBP |
| Videos | MP4, MKV, AVI, MOV, WEBM |
| Audios | MP3, WAV, AAC, FLAC, OGG |
| Docs | PDF, DOCX, TXT, XLSX, PPTX |
| Archives | ZIP, RAR, 7Z, TAR, GZ |
| Exe | Python, C, C++, Java, JavaScript, executables |
| Linux | Hidden files |
| Others | Unrecognized file types |

## Requirements

- Python 3.x
- No third-party packages required.

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/FileOrganizer.git
```

Navigate into the project directory:

```bash
cd FileOrganizer
```

## Configuration

Open `organizer.py` and configure the source and destination paths:

```python
src_folder_path = "/path/to/source"
organized_folder = "/path/to/destination"
```

## Usage

Run the script:

```bash
python organizer.py
```

The script scans the source directory, creates category folders in the destination directory, and moves files into their respective categories.

## Duplicate Filename Handling

If a file with the same name already exists in the destination, the organizer generates a new filename instead of overwriting it.

Example:

```text
report.pdf
report_1.pdf
report_2.pdf
report_3.pdf
```

Hidden files and files with multiple extensions are also handled by the collision-resolution logic.

## Project Structure

```text
FileOrganizer/
│
├── organizer.py
└── README.md
```

## Technologies Used

- Python
- os
- shutil
- re

## Future Improvements

- Command-line arguments for source and destination paths.
- Dry-run mode to preview file movements.
- Recursive directory scanning.
- Improved hidden-file detection.
- Logging and detailed error handling.
- Automated test coverage.

## License

This project is licensed under the MIT License.

---

**Built as a hands-on Python project to explore filesystem operations, file handling, regular expressions, recursion, and automation.**