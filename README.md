p align="center">
  <img src="https://img.shields.io/github/stars/Q-society/qsoc_scaner?style=for-the-badge&color=cyan">
  <img src="https://img.shields.io/github/forks/Q-society/qsoc_scaner?style=for-the-badge&color=green">
  <img src="https://img.shields.io/github/issues/Q-society/qsoc_scaner?style=for-the-badge&color=red">
</p>

<h1 align="center">🔮 Q Society Scanner v2.0 🔮</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Kali%20Linux-blue?style=flat-square&logo=kali-linux&logoColor=white">
  <img src="https://img.shields.io/badge/Platform-Termux-black?style=flat-square&logo=android&logoColor=green">
  <img src="https://img.shields.io/badge/Language-Python%203-yellow?style=flat-square&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Speed-5%20Seconds-red?style=flat-square&logo=speedtest&logoColor=white">
</p>

---

## ⚡ Matrix Overview
An ultra-fast, multithreaded OSINT Username Finder optimized for both **Kali Linux** and **Termux**. It utilizes a 50-thread concurrent pool engine to scan 200+ global platforms in less than 5 seconds.

██████╗     ███████╗ ██████╗  ██████╗██╗███████╗████████╗██╗   ██╗
██╔═══██╗    ██╔════╝██╔═══██╗██╔════╝██║██╔════╝╚══██╔══╝╚██╗ ██╔╝
██║   ██║    ███████╗██║   ██║██║     ██║█████╗     ██║    ╚████╔╝
██║   ██║    ╚════██║██║   ██║██║     ██║██╔══╝     ██║     ╚██╔╝

╚██████╔╝    ███████║╚██████╔╝╚██████╗██║███████╗    ██║      ██║

╚═════╝     ╚══════╝ ╚═════╝  ╚═════╝╚═╝╚══════╝    ╚═╝      ╚═╝
---

## 🚀 Installation & Core Matrix

### 🟢 Method 1: Kali Linux / Parrot OS
```bash
sudo apt update && sudo apt install git python3 python3-pip -y
git clone [https://github.com/Q-society/qsoc_scaner.git](https://github.com/Q-society/qsoc_scaner.git)
cd qsoc_scaner
pip3 install requests colorama
python3 qsoc_scanner.py
