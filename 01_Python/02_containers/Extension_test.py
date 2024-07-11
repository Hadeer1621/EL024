import pyautogui
import time
import subprocess

# Function to open VSCode
def open_vscode():
    # Opens VSCode using the command line
    subprocess.Popen(['code'])
    time.sleep(5)  # Wait for VSCode to open

# Function to open the Extensions sidebar
def open_extensions_sidebar():
    pyautogui.hotkey('ctrl', 'shift', 'x')
    time.sleep(2)  # Wait for the Extensions sidebar to open

# Function to search and install an extension
def search_and_install_extension(extension_name):
    pyautogui.hotkey('ctrl', 'shift', 'p')
    time.sleep(1)
    pyautogui.write('Extensions: Install Extensions')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.write(extension_name)
    time.sleep(2)  # Wait for search results to appear
    pyautogui.press('enter')  # Select the first result
    time.sleep(5)  # Wait for the extension to install

# Main function to perform the tasks
def main():
    open_vscode()
    open_extensions_sidebar()
    
    extensions = [
        "llvm-vs-code-extensions.vscode-clangd",
        "razzmatazz.cplusplus-helper",
        "twxs.cmake",
        "ms-vscode.cmake-tools"
    ]
    
    for extension in extensions:
        search_and_install_extension(extension)
        time.sleep(2)  # Small pause before installing the next extension

if __name__ == "__main__":
    main()
