#!/bin/bash

echo "=== INSTALLATION AUTOMATISÉE LINUX/MACOS ==="

# Mettre à jour le système
sudo apt update -y && sudo apt upgrade -y

# Installer Python3 + pip si manquant
if ! command -v python3 &>/dev/null; then
  echo "[*] Installation de Python3..."
  sudo apt install -y python3
fi

if ! command -v pip3 &>/dev/null; then
  echo "[*] Installation de pip3..."
  sudo apt install -y python3-pip
fi

# Installer Git
if ! command -v git &>/dev/null; then
  echo "[*] Installation de Git..."
  sudo apt install -y git
fi

# Installer Node.js (via NodeSource)
if ! command -v node &>/dev/null; then
  echo "[*] Installation de Node.js LTS..."
  curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
  sudo apt install -y nodejs
fi

# Installer Jupyter et ipykernel
echo "[*] Installation de jupyter et ipykernel..."
pip3 install --upgrade pip
pip3 install jupyter ipykernel

echo "=== INSTALLATION TERMINEE ==="
