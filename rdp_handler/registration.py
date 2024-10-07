import os
import subprocess

from .logger import logger


def register_url_scheme():
    if os.name == 'posix':
        if 'Darwin' in os.uname().sysname:
            register_url_scheme_mac()
        else:
            register_url_scheme_linux()


def register_url_scheme_mac():
    # Path to the application bundle
    app_path = os.path.abspath(os.path.join(__file__, '..', '..', 'RDPURLHandler.app'))
    if not os.path.exists(app_path):
        # If not running from an app bundle, get the executable path
        app_path = os.path.abspath(os.path.join(__file__, '..', '..'))
    try:
        subprocess.run([
            '/System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework/Support/lsregister',
            '-f', "/Users/grainier/Github/url_handler/dist/RDPURLHandler.app"
        ], check=True)
        logger.info("Registered rdp:// URL scheme on MacOS.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to register URL scheme on MacOS: {e}")


def register_url_scheme_linux():
    # Path to the application executable
    app_executable = os.path.abspath(os.path.join(__file__, '..', 'main.py'))
    desktop_entry_name = 'rdpurlhandler.desktop'
    desktop_entry_path = os.path.expanduser(f'~/.local/share/applications/{desktop_entry_name}')

    # Create the .desktop file
    os.makedirs(os.path.dirname(desktop_entry_path), exist_ok=True)
    with open(desktop_entry_path, 'w') as f:
        f.write(f"""[Desktop Entry]
Name=RDP URL Handler
Exec={app_executable} %u
Type=Application
MimeType=x-scheme-handler/rdp;
NoDisplay=true
""")

    # Register the handler
    try:
        subprocess.run(['update-desktop-database', os.path.dirname(desktop_entry_path)], check=True)
        subprocess.run(['xdg-mime', 'default', desktop_entry_name, 'x-scheme-handler/rdp'], check=True)
        logger.info("Registered rdp:// URL scheme on Linux.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to register URL scheme on Linux: {e}")
