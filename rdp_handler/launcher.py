import os
import subprocess

from .logger import logger


def launch_thincast(rdp_file: str):
    # Possible paths for ThinCast client
    possible_paths = [
        '/usr/bin/thincast-client',  # Common Linux path
        '/usr/local/bin/thincast-client',
        '/Applications/Thincast Remote Desktop Client.app/Contents/MacOS/Thincast Remote Desktop Client'  # MacOS path
    ]

    thincast_path = None
    for path in possible_paths:
        if os.path.exists(path):
            thincast_path = path
            break

    if thincast_path is None:
        logger.error("ThinCast RDP client not found.")
        raise FileNotFoundError("ThinCast RDP client not found.")

    try:
        logger.info(f"Launching ThinCast client with RDP file: {rdp_file}")
        subprocess.Popen([thincast_path, rdp_file])
    except Exception as e:
        logger.error(f"Failed to launch ThinCast client: {e}")
        raise
