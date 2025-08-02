import os
import shutil
import ctypes

# Ask user for permission


def ask_user():
    return ctypes.windll.user32.MessageBoxW(
        0,
        "Do you want to clean temporary files?",
        "TempFileCleaner",
        1  # 1 = OK/Cancel
    ) == 1

# Show completion popup


def show_done():
    ctypes.windll.user32.MessageBoxW(
        0,
        "Cleaning done successfully!",
        "TempFileCleaner",
        0  # 0 = OK only
    )

# Delete all files in a given folder


def delete_files_in(folder):
    try:
        for file in os.listdir(folder):
            path = os.path.join(folder, file)
            try:
                if os.path.isfile(path) or os.path.islink(path):
                    os.unlink(path)
                elif os.path.isdir(path):
                    shutil.rmtree(path)
            except:
                pass  # Ignore permission errors
    except:
        pass


# Main execution
if ask_user():
    folders = [
        os.environ.get('TEMP'),
        r"C:\Windows\Temp",
        r"C:\Windows\Prefetch"
    ]
    for folder in folders:
        delete_files_in(folder)
    show_done()
