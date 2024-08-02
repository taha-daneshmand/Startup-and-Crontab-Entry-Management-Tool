# Startup and Crontab Entry Management Tool

![License](https://img.shields.io/github/license/taha-daneshmand/Startup-and-Crontab-Entry-Management-Tool)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen)

A cross-platform command-line tool to manage startup entries on Windows and crontab entries on Linux with colorized outputs for better readability.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Windows](#windows)
  - [Linux](#linux)
- [Example Output](#example-output)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This tool helps you list and remove startup entries on Windows and crontab entries on Linux. It uses colorized outputs for better readability and user experience.

## Features

- **List Startup Entries:** Lists all startup entries on Windows.
- **Remove Startup Entries:** Removes a specified startup entry on Windows.
- **List Crontab Entries:** Lists all crontab entries on Linux.
- **Remove Crontab Entries:** Removes a specified crontab entry on Linux.
- **Colorized Outputs:** Uses colorama to colorize outputs for better readability.

## Installation

### Prerequisites

- Python 3.8 or higher
- colorama

### Clone the Repository

```bash
git clone https://github.com/taha-daneshmand/Startup-and-Crontab-Entry-Management-Tool.git
cd Startup-and-Crontab-Entry-Management-Tool-tool
```

### Install Dependencies

```bash
pip install colorama
```

## Usage

### Windows

To list and remove startup entries on Windows:

```bash
python main.py
```

### Linux

To list and remove crontab entries on Linux:

```bash
python main.py
```

## Example Output

### Windows

```
[+] Startup entries:
1. ExampleEntry: C:\example\path\to\program.exe

[!] Enter the number of the entry you want to remove (0 to exit): 1
[+] Entry ExampleEntry has been removed successfully.
[+] File 'C:\example\path\to\program.exe' has been deleted successfully.
```

### Linux

```
[+] Crontab entries:
1. * * * * * /path/to/command

[!] Enter the number of the entry you want to remove (0 to exit): 1
[+] Entry '* * * * * /path/to/command' has been removed successfully.
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

Please make sure to update tests as appropriate.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
