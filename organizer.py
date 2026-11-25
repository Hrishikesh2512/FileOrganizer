
import os
import shutil
import re

# RuleBook
IMAGES = ["jpg", "jpeg", "png", "gif", "webp", "svg", "tiff", "bmp"]
VIDEOS = ["mp4", "mkv", "avi", "mov", "wmv", "flv", "webm", "m4v"]
AUDIO = ["mp3", "wav", "aac", "flac", "ogg", "wma", "m4a", "opus"]
DOCUMENTS = ["pdf", "doc", "docx", "odt", "rtf", "txt", "md", "xls", "xlsx", "csv", "ppt", "pptx"]
ARCHIVES = ["zip", "rar", "7z", "tar", "gz", "bz2", "xz", "iso"]
CODE = ["py", "c", "cpp", "h", "java", "js", "ts", "html", "css", "php", "sql", "sh"]
EXECUTABLES = ["exe", "msi", "deb", "rpm", "apk", "jar", "bin", "appimage"]


HIDDEN_EXTENSIONS = [
    "json", "yaml", "yml", "toml", "xml",
    "ini", "conf", "cfg", "config",
    "txt", "log", "bak", "old", "tmp",
    "sh", "py", "js", "lua",
    "db", "sqlite", "sqlite3",
    "pem", "key", "crt", "pub",
    "local", "env", "example",
    "gitignore", "gitconfig", "gitattributes"
]

src_folder_path = "/home/tushar/Projects/HandCoded/FileOrganizer/test_download"
organized_folder = "/home/tushar/Projects/HandCoded/FileOrganizer/organized_folder"


# Functions
def handle_duplicate(file, target):
    if not os.path.exists(target):
        return 0
    for filename in os.listdir(target):
        if filename == file:
            return -1
    return 0


def handle_collision(file, target):
    parts = re.split(r"([._])", file)
    existing = set(os.listdir(target)) if os.path.isdir(target) else set()

    # Hidden files
    if parts[0] == "":

        # Numeric suffix at the end: .bashrc_1 -> .bashrc_2
        if parts[-2] == "_" and parts[-1].isdigit():
            parts[-1] = str(int(parts[-1]) + 1)
            new_filename = "".join(parts)

        # Hidden files with recognized extensions
        elif (
            len(parts) > 3
            and parts[-1].lower() in HIDDEN_EXTENSIONS
            and parts[-1].lower() not in ["local", "env", "example",
                                          "gitignore", "gitconfig",
                                          "gitattributes"]
        ):
            hidden_extension = parts[-1]

            # Numeric suffix before extension:
            # .config_1.json -> .config_2.json
            if parts[-3].isdigit() and parts[-4] == "_":
                parts[-3] = str(int(parts[-3]) + 1)
            else:
                # .config.json -> .config_1.json
                parts[-2:-2] = ["_", "1"]

            new_filename = "".join(parts)

        else:
            # .bashrc -> .bashrc_1
            new_filename = file + "_1"

        if new_filename in existing:
            return handle_collision(new_filename, target)

        return new_filename

    # Normal files
    name, extension = os.path.splitext(file)

    # Find existing numeric suffix
    match = re.search(r"_(\d+)$", name)

    if match:
        base_name = name[:match.start()]
        number = int(match.group(1)) + 1
    else:
        base_name = name
        number = 1

    new_filename = base_name + "_" + str(number) + extension

    if new_filename in existing:
        return handle_collision(new_filename, target)

    return new_filename



def hidden_file(file):
    if file.startswith("."):
        return 1
    else:
        return 0


for filename in os.listdir(src_folder_path):
    if os.path.isdir(os.path.join(src_folder_path, filename)):
        continue

    extension = filename.split(".")[-1]

    if hidden_file(filename)==1:
        os.makedirs(os.path.join(organized_folder,"Linux"),exist_ok=True)
        if handle_duplicate(filename, os.path.join(organized_folder,"Linux"))==0:
            shutil.move(os.path.join(src_folder_path,filename),os.path.join(organized_folder,"Linux"))
        else:
            new_filename=handle_collision(filename,os.path.join(organized_folder,"Linux"))
            shutil.move(os.path.join(src_folder_path,filename),os.path.join(organized_folder,"Linux",new_filename))

    elif extension.lower() in CODE or extension.lower() in EXECUTABLES:
        os.makedirs(os.path.join(organized_folder, "Exe"), exist_ok=True)

        if handle_duplicate(filename, os.path.join(organized_folder, "Exe")) == 0:
            shutil.move(os.path.join(src_folder_path, filename), os.path.join(organized_folder, "Exe"))
        else:
            new_filename = handle_collision(filename, os.path.join(organized_folder, "Exe"))
            shutil.move(os.path.join(src_folder_path, filename), os.path.join(organized_folder, "Exe", new_filename))

    elif extension.lower() in VIDEOS:
        os.makedirs(os.path.join(organized_folder, "Videos"), exist_ok=True)

        if handle_duplicate(filename, os.path.join(organized_folder, "Videos")) == 0:
            shutil.move(os.path.join(src_folder_path, filename), os.path.join(organized_folder, "Videos"))
        else:
            new_filename = handle_collision(filename, os.path.join(organized_folder, "Videos"))
            shutil.move(os.path.join(src_folder_path, filename), os.path.join(organized_folder, "Videos", new_filename))

    elif extension.lower() in IMAGES:
        os.makedirs(os.path.join(organized_folder, "Images"), exist_ok=True)

        if handle_duplicate(filename, os.path.join(organized_folder, "Images")) == 0:
            shutil.move(os.path.join(src_folder_path, filename), os.path.join(organized_folder, "Images"))
        else:
            new_filename = handle_collision(filename, os.path.join(organized_folder, "Images"))
            shutil.move(os.path.join(src_folder_path, filename), os.path.join(organized_folder, "Images", new_filename))

    elif extension.lower() in AUDIO:
        os.makedirs(os.path.join(organized_folder, "Audios"), exist_ok=True)

        if handle_duplicate(filename, os.path.join(organized_folder, "Audios")) == 0:
            shutil.move(os.path.join(src_folder_path, filename), os.path.join(organized_folder, "Audios"))
        else:
            new_filename = handle_collision(filename, os.path.join(organized_folder, "Audios"))
            shutil.move(os.path.join(src_folder_path, filename), os.path.join(organized_folder, "Audios", new_filename))

    elif extension.lower() in DOCUMENTS:
        os.makedirs(os.path.join(organized_folder, "Docs"), exist_ok=True)

        if handle_duplicate(filename, os.path.join(organized_folder, "Docs")) == 0:
            shutil.move(os.path.join(src_folder_path, filename), os.path.join(organized_folder, "Docs"))
        else:
            new_filename = handle_collision(filename, os.path.join(organized_folder, "Docs"))
            shutil.move(os.path.join(src_folder_path, filename), os.path.join(organized_folder, "Docs", new_filename))

    elif extension.lower() in ARCHIVES:
        os.makedirs(os.path.join(organized_folder, "Archives"), exist_ok=True)

        if handle_duplicate(filename, os.path.join(organized_folder, "Archives")) == 0:
            shutil.move(os.path.join(src_folder_path, filename), os.path.join(organized_folder, "Archives"))
        else:
            new_filename = handle_collision(filename, os.path.join(organized_folder, "Archives"))
            shutil.move(os.path.join(src_folder_path, filename), os.path.join(organized_folder, "Archives", new_filename))

    else:
        os.makedirs(os.path.join(organized_folder, "Others"), exist_ok=True)

        if handle_duplicate(filename, os.path.join(organized_folder, "Others")) == 0:
            shutil.move(os.path.join(src_folder_path, filename), os.path.join(organized_folder, "Others"))
        else:
            new_filename = handle_collision(filename, os.path.join(organized_folder, "Others"))
            shutil.move(os.path.join(src_folder_path, filename), os.path.join(organized_folder, "Others", new_filename))
