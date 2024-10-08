#!/bin/bash
set -e

# Install required libraries
sudo apt-get update
sudo apt-get install -y python3 python3-pip python3-venv python3-poetry
python3 -m venv venv
source venv/bin/activate
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
Depends: python3, desktop-file-utils
Maintainer: Your Company <yourcompany@example.com>
Description: RDP URL Handler for Linux.
 This package installs RDP URL Handler, an RDP URL handler utility for Ubuntu.
EOL

# Create the postinst script
cat <<EOL > $PACKAGE_ROOT/DEBIAN/postinst
#!/bin/bash
set -e

echo "Running post-installation script for $APP_NAME"

# Update the desktop database
if command -v update-desktop-database > /dev/null; then
    echo "Updating desktop database..."
    update-desktop-database /usr/share/applications
fi

# Update the MIME database
if command -v update-mime-database > /dev/null; then
    echo "Updating MIME database..."
    update-mime-database /usr/share/mime
fi

exit 0
EOL

# Set permissions
chmod 755 $PACKAGE_ROOT/DEBIAN/postinst
chmod 755 $PACKAGE_ROOT/usr/local/bin/$APP_NAME
chmod 644 $PACKAGE_ROOT/usr/share/applications/rdpurlhandler.desktop
chmod 644 $PACKAGE_ROOT/DEBIAN/control

# Build the Debian package
dpkg-deb --build $PACKAGE_ROOT $APP_NAME-$VERSION.deb

# Done
echo "Debian package built successfully: $APP_NAME-$VERSION.deb"
