
<!-- Banner -->
<div align="center">
  <img width="1115" height="628" alt="suicixdalEXE Banner" src="https://github.com/user-attachments/assets/7c9f1163-9d9e-440b-a3d1-512789438d13" />
</div>

<h1 align="center">🔧 suicixdalEXE</h1>
<p align="center">
  <strong>Advanced Multi-Feature Security Tool Suite</strong><br>
  <em>Educational and research purposes only</em>
</p>

<!-- Badges -->
<div align="center">
  
  ![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
  ![License](https://img.shields.io/github/license/xdrew87/suicixdalEXE?style=for-the-badge)
  ![Last Commit](https://img.shields.io/github/last-commit/xdrew87/suicixdalEXE?style=for-the-badge)
  ![GitHub Stars](https://img.shields.io/github/stars/xdrew87/suicixdalEXE?style=for-the-badge&logo=github)
  ![GitHub Issues](https://img.shields.io/github/issues/xdrew87/suicixdalEXE?style=for-the-badge)
  ![GitHub Forks](https://img.shields.io/github/forks/xdrew87/suicixdalEXE?style=for-the-badge)
  
</div>

---

## ⚠️ Important Disclaimer

> **WARNING**: This tool is provided **for educational and research purposes only**.

- ❌ The author assumes **no responsibility** for any misuse or damage caused by this program
- ⚖️ Users are responsible for complying with all applicable laws and regulations
- 🎓 Intended for cybersecurity education, ethical hacking courses, and authorized penetration testing
- 🔐 Only use on systems you own or have explicit permission to test

**Attribution**: Phone number functionality adapted from [GhostTrack](https://github.com/HunxByts/GhostTrack)

---

## ✨ Features

- 🌐 **Network & IP Tools**: Includes an IP Tracker, Public IP display, IP Pinger, IP Blacklist Check, and a specialized TCP Paping Tool.
- 🕵️ **OSINT & Reconnaissance**: Perform comprehensive lookups for Phone Numbers, Usernames, Email Breaches, and US ZIP Codes.
- 📱 **Social Media OSINT**: Track usernames across 20+ platforms and fetch public Instagram profile data using `instaloader`.
- 🛡️ **Security Focused**: Built with security education in mind, providing tools for ethical hacking and penetration testing practice.
- 🔐 **Secure API Key Management**: API keys are stored in an external `config.json` file to prevent accidental exposure.
- 🎨 **User-Friendly Interface**: A clean, color-coded, and easy-to-navigate command-line interface.

---

## 📋 Requirements

- **Python**: 3.8 or higher
- **Operating System**: Linux (Debian-based), Windows, macOS
- **Dependencies**: Listed in `requirements.txt`
- **Internet Connection**: Required for most features

---

## 📌 Latest Release - Version 2.0

### ✨ New Features
- ✅ **Instagram Lookup**: Added a new module to fetch public Instagram profile data.
- ✅ **IP Blacklist Check**: Check if an IP is listed on abuse databases.
- ✅ **ZIP Code Lookup**: Added a utility to find information about US ZIP codes.
- ✅ **Secure Configuration**: API keys are now managed via `config.json`.
- ✅ **UI Overhaul**: The menu has been redesigned for better clarity and ease of use.

### 🚀 Improvements
- 🚀 Enhanced performance and reliability
- 🎨 Better user interface and experience
- 📚 Comprehensive documentation updates
- 🛡️ Security improvements and bug fixes

---

## 🛠️ Installation Guide

### 🐧 Linux (Debian/Ubuntu)

```bash
# Update system packages
sudo apt update && sudo apt upgrade -y

# Install required packages
sudo apt install git python3 python3-pip -y

# Clone the repository
git clone https://github.com/xdrew87/suicixdalEXE.git
cd suicixdalEXE

# Install Python dependencies
pip3 install -r requirements.txt

# Run the tool
python3 suicixdalEXE.py
```

### 📱 Termux (Android)

```bash
# Update packages
pkg update && pkg upgrade -y

# Install required packages
pkg install git python

# Clone the repository
git clone https://github.com/xdrew87/suicixdalEXE.git
cd suicixdalEXE

# Install Python dependencies
pip install -r requirements.txt

# Run the tool
python suicixdalEXE.py
```

### 🪟 Windows

```powershell
# Install Python from python.org if not already installed
# Install Git from git-scm.com if not already installed

# Clone the repository
git clone https://github.com/xdrew87/suicixdalEXE.git
cd suicixdalEXE

# Install Python dependencies
pip install -r requirements.txt

# Run the tool
python suicixdalEXE.py
```

### 🍎 macOS

```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install required packages
brew install python git

# Clone the repository
git clone https://github.com/xdrew87/suicixdalEXE.git
cd suicixdalEXE

# Install Python dependencies
pip3 install -r requirements.txt

# Run the tool
python3 suicixdalEXE.py
```

---

## ⚙️ Configuration

To use features that rely on external APIs, you must create a `config.json` file in the root directory of the project.

1.  Create a file named `config.json`.
2.  Copy and paste the template below into the file.
3.  Replace the placeholder values with your actual API keys.

```json
{
    "abuseipdb_api_key": "your_abuseipdb_api_key_here",
    "hibp_api_key": "your_hibp_api_key_here"
}
```

> **Important**: Add `config.json` to your `.gitignore` file if it's not already there to prevent your keys from being committed to version control.

The following features require API keys:
- **Email Breach Check**: Requires a Have I Been Pwned (HIBP) API key.
- **IP Blacklist Check**: Requires an AbuseIPDB API key.

---

## 📖 Usage

### Quick Start

1. **Navigate** to the suicixdalEXE directory
2. **Run** the main script: `python3 suicixdalEXE.py`
3. **Follow** the interactive menu prompts
4. **Select** the desired functionality from the available options

### Command Line Options

```bash
# Display help information
python3 suicixdalEXE.py --help

# Run in verbose mode
python3 suicixdalEXE.py --verbose

# Specify output directory
python3 suicixdalEXE.py --output /path/to/output
```

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### 🐛 Reporting Bugs

- Use the [GitHub Issues](https://github.com/xdrew87/suicixdalEXE/issues) page
- Include detailed reproduction steps
- Provide system information and error logs

### 🔧 Development Setup

```bash
# Fork the repository on GitHub
# Clone your fork
git clone https://github.com/yourusername/suicixdalEXE.git
cd suicixdalEXE

# Create a new branch for your feature
git checkout -b feature/your-feature-name

# Install development dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt  # if available

# Make your changes and test thoroughly
# Submit a pull request
```

### 📝 Guidelines

- Follow existing code style and conventions
- Add appropriate documentation and comments
- Include tests for new functionality
- Ensure all security considerations are addressed

---

## 📞 Contact & Support

<div align="center">

### 🌐 Social Media

[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/xlsuixideix)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/mlag)
[![Discord](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com)

**Discord Username:** `galmx`

</div>

### 📧 Support

- 🐛 **Bug Reports**: Use GitHub Issues
- 💬 **General Questions**: Discord or Instagram DM
- 🔒 **Security Issues**: Contact privately through Discord

---

## 📜 License

This project is licensed under the **GNU General Public License v3.0**. See the `LICENSE` file for more details.

---

## 🙏 Acknowledgments

- 📱 Phone functionality adapted from [GhostTrack](https://github.com/HunxByts/GhostTrack)
- 🌟 Thanks to all contributors and users
- 🛡️ Special thanks to the cybersecurity community

---

<div align="center">

**⭐ If you find this tool useful, please consider starring the repository! ⭐**

Made with ❤️ for the cybersecurity community

</div>
