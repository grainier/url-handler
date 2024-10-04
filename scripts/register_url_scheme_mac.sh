#!/bin/bash

# Path to your application bundle
APP_NAME="RDPURLHandler.app"
APP_PATH="/Applications/$APP_NAME"

# Check if the application exists at the specified path
if [ ! -d "$APP_PATH" ]; then
    echo "Application not found at $APP_PATH"
    echo "Please ensure that $APP_NAME is installed in the /Applications directory."
    exit 1
fi

# Register the application as the handler for 'rdp' URL scheme
echo "Registering $APP_NAME as the handler for rdp:// URLs."

# Use the lsregister command to update the Launch Services database
/System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework/Support/lsregister -f "$APP_PATH"

echo "Registration complete."

# Optional: Inform the user to log out and log back in (or restart) if necessary
echo "If the URL scheme is not recognized immediately, please log out and log back in, or restart your Mac."
