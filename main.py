import os
import platform
import subprocess
import tempfile
from colorama import Fore, Style, init

init(autoreset=True)

if platform.system() == "Windows":
    import winreg

def list_windows_startup_entries():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run")
    entries = []
    try:
        i = 0
        while True:
            entry_name, entry_value, entry_type = winreg.EnumValue(key, i)
            entries.append((i + 1, entry_name, entry_value))
            i += 1
    except OSError:
        pass
    winreg.CloseKey(key)
    return entries

def remove_windows_startup_entry(index, entries):
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)
    try:
        entry_name, entry_value = entries[index - 1][1], entries[index - 1][2]
        winreg.DeleteValue(key, entry_name)
        print(f"{Fore.GREEN}[+] Entry {entry_name} has been removed successfully.")

        if os.path.isfile(entry_value):
            os.remove(entry_value)
            print(f"{Fore.GREEN}[+] File '{entry_value}' has been deleted successfully.")
        else:
            print(f"{Fore.RED}[-] File '{entry_value}' not found or unable to delete.")
    except IndexError:
        print(f"{Fore.RED}[-] Invalid entry index.")
    except OSError as e:
        print(f"{Fore.RED}[-] Error removing entry: {e}")
    finally:
        winreg.CloseKey(key)

def list_linux_crontab_entries():
    try:
        output = subprocess.check_output(["crontab", "-l"], stderr=subprocess.STDOUT).decode('utf-8').strip()
        if output:
            entries = output.split("\n")
            return [(i + 1, entry) for i, entry in enumerate(entries)]
        else:
            return []
    except subprocess.CalledProcessError as e:
        if "no crontab" in e.output.decode('utf-8'):
            return []
        else:
            raise

def remove_linux_crontab_entry(index, entries):
    try:
        entry = entries[index - 1][1]
        all_entries = [e[1] for e in entries if e[1] != entry]

        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write("\n".join(all_entries).encode('utf-8'))
            tmp_file.write(b"\n")
            tmp_file_path = tmp_file.name

        subprocess.check_output(["crontab", tmp_file_path], stderr=subprocess.STDOUT)
        os.unlink(tmp_file_path)
        print(f"{Fore.GREEN}[+] Entry '{entry}' has been removed successfully.")
    except IndexError:
        print(f"{Fore.RED}[-] Invalid entry index.")
    except Exception as e:
        print(f"{Fore.RED}[-] Error removing crontab entry: {e}")

def main():
    os_name = platform.system()
    if os_name == "Windows":
        entries = list_windows_startup_entries()
        if not entries:
            print(f"{Fore.RED}[-] No startup entries found.")
        else:
            print(f"{Fore.GREEN}[+] Startup entries:")
            for index, name, value in entries:
                print(f"{Fore.YELLOW}{index}. {name}: {value}")

            print("\n")
            choice = int(input(f"{Fore.CYAN}[!] Enter the number of the entry you want to remove (0 to exit): {Style.RESET_ALL}"))
            if choice == 0:
                return
            elif 0 < choice <= len(entries):
                remove_windows_startup_entry(choice, entries)
            else:
                print(f"{Fore.RED}[-] Invalid choice.")
    elif os_name == "Linux":
        entries = list_linux_crontab_entries()
        if not entries:
            print(f"{Fore.RED}[-] No crontab entries found.")
        else:
            print(f"{Fore.GREEN}[+] Crontab entries:")
            for index, entry in entries:
                print(f"{Fore.YELLOW}{index}. {entry}")

            print("\n")
            choice = int(input(f"{Fore.CYAN}[!] Enter the number of the entry you want to remove (0 to exit): {Style.RESET_ALL}"))
            if choice == 0:
                return
            elif 0 < choice <= len(entries):
                remove_linux_crontab_entry(choice, entries)
            else:
                print(f"{Fore.RED}[-] Invalid choice.")
    else:
        print(f"{Fore.RED}[-] Unsupported operating system: {os_name}")

if __name__ == "__main__":
    main()
