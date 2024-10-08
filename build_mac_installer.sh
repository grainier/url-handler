#!/bin/bash
set -e

# Install required libraries
python3 -m venv venv
source venv/bin/activate
pip3 install pyobjc
pip3 install pyinstaller
poetry install

# Clean previous builds
sudo rm -rf dist build RDPURLHandler.pkg package_root

# Clean previous installs
#sudo pkgutil --forget com.yourcompany.rdpurlhandler
#sudo rm -rf /Applications/RDPURLHandler.app ~/Applications/RDPURLHandler.app

# Build the application
pyinstaller RDPURLHandler.spec

# Create the package_root directory
mkdir -p package_root

# Copy the application into package_root
cp -R dist/RDPURLHandler.app package_root/

# Ensure scripts have correct permissions
chmod +x scripts/postinstall

# Build the installer package
pkgbuild \
  --root package_root \
  --identifier com.yourcompany.rdpurlhandler \
  --version 1.0.0 \
  --install-location /Applications \
  --component-plist assets/component.plist \
  --scripts scripts \
  RDPURLHandler.pkg

echo "Installer package built successfully: RDPURLHandler.pkg"
