
import os

def find_libiconv_dll():
    # Common directories where libiconv.dll may be located
    common_directories = [
        os.path.join(os.getcwd(), 'libiconv.dll'),  # Current working directory
        os.path.join(os.getcwd(), 'libiconv', 'libiconv.dll'),  # Subdirectory libiconv
        os.path.join(os.getcwd(), 'DLLs', 'libiconv.dll'),  # Subdirectory DLLs
        '/usr/lib/libiconv.dll',  # Linux system library directory
        '/usr/local/lib/libiconv.dll',  # Linux local library directory
        'C:\\MinGW\\bin\\libiconv.dll',  # Example MinGW installation directory
        'C:\\msys64\\usr\\bin\\libiconv.dll',  # Example MSYS2 installation directory
    ]

    # Check each directory for the existence of libiconv.dll
    for directory in common_directories:
        if os.path.exists(directory):
            return directory

    return None  # libiconv.dll not found in common directories

if __name__ == "__main__":
    libiconv_path = find_libiconv_dll()

    if libiconv_path:
        print(f"libiconv.dll found at: {libiconv_path}")
    else:
        print("libiconv.dll not found in common directories.")
