import subprocess
import sys

from .logger import logger


def launch_thincast(rdp_file: str):
    logger.info(f"Launching ThinCast client with RDP file: {rdp_file}")
    try:
        if sys.platform == 'darwin':
            # MacOS
            subprocess.Popen(["open", "-a", "Thincast Remote Desktop Client", rdp_file])
        else:
            # Debian
            subprocess.Popen(["thincast-client", rdp_file])
    except Exception as e:
        logger.error(f"Failed to launch ThinCast client: {e}")
        raise
