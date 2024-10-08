#!/bin/bash
set -e

# Install required libraries
sudo apt-get update
sudo apt-get install -y python3 python3-pip python3-venv python3-poetry
pip3 install pyinstaller
poetry install

# Define variables
APP_NAME=rdpurlhandler
VERSION=1.0.0
BUILD_DIR=build
PACKAGE_ROOT=$BUILD_DIR/package_root
DIST_DIR=dist

# Clean previous builds
rm -rf $BUILD_DIR $DIST_DIR

# Build the application
pyinstaller --onefile --name $APP_NAME rdp_handler/main.py

# Create the necessary directories for the Debian package
mkdir -p $PACKAGE_ROOT/usr/local/bin
mkdir -p $PACKAGE_ROOT/usr/share/applications
mkdir -p $PACKAGE_ROOT/DEBIAN

# Copy the application executable
cp $DIST_DIR/$APP_NAME $PACKAGE_ROOT/usr/local/bin/

# Copy the .desktop file
cp assets/rdpurlhandler.desktop $PACKAGE_ROOT/usr/share/applications/

# Create the control file for the Debian package
cat <<EOL > $PACKAGE_ROOT/DEBIAN/control
Package: $APP_NAME
Version: $VERSION
Section: utils
Priority: optional
Architecture: amd64
Depends: python3
Maintainer: Your Company <yourcompany@example.com>
Description: RDP URL Handler for Linux.
 This package installs RDP URL Handler, an RDP URL handler utility for Ubuntu.
EOL

# Set permissions
chmod -R 755 $PACKAGE_ROOT/usr/local/bin/$APP_NAME
chmod 644 $PACKAGE_ROOT/usr/share/applications/rdpurlhandler.desktop
chmod 755 $PACKAGE_ROOT/DEBIAN/control

# Build the Debian package
dpkg-deb --build $PACKAGE_ROOT $APP_NAME-$VERSION.deb

# Done
echo "Debian package built successfully: $APP_NAME-$VERSION.deb"
