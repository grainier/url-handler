import logging
import os
from pathlib import Path

# Determine log directory
if os.name == 'posix':
    if 'Darwin' in os.uname().sysname:
        # MacOS log directory
        log_dir = Path.home() / 'Library' / 'Logs' / 'RDPURLHandler'
    else:
        # Linux log directory
        log_dir = Path.home() / '.rdpurlhandler' / 'logs'
else:
    # Default to current directory
    log_dir = Path.cwd() / 'logs'

log_dir.mkdir(parents=True, exist_ok=True)
log_file = log_dir / 'rdp_url_handler.log'

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file, mode='a'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
