# FileOrganizer

A Python-based file organizer that automatically sorts files into categorized folders.

## Features

- Organizes images, videos, audio, documents, archives, code and executables.
- Moves hidden files into a separate `Linux` folder.
- Handles filename collisions by adding numeric suffixes.
- Skips directories.
- Supports custom source and destination paths.

## Project Structure

```text
FileOrganizer/
├── organizer.py
├── tests/
│   └── test_organizer.py
├── .gitignore
└── README.md
```

## Requirements

- Python 3
- Standard Python libraries

## Usage

Update the source and destination paths in `organizer.py`, then run:

```bash
python organizer.py
```

## Run Tests

```bash
python -m unittest discover -s tests -v
```

## License

MIT License