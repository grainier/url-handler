import os
import sys
import time

from rdp_handler.launcher import launch_thincast
from rdp_handler.logger import logger
from rdp_handler.parser import parse_rdp_url
from rdp_handler.rdp_generator import generate_rdp_file
from rdp_handler.registration import register_url_scheme


def main():
    # Registration code
    register_url_scheme()
    #
    # if len(sys.argv) < 2:
    #     logger.error("No URL provided.")
    #     sys.exit(1)
    #
    # url = sys.argv[1]
    # logger.info(f"Received URL: {url}")
    #
    # try:
    #     params = parse_rdp_url(url)
    #     logger.info(f"Parsed parameters: {params}")
    #
    #     temp_dir = os.path.join(os.path.expanduser('~'), '.rdpurlhandler', 'tmp')
    #     os.makedirs(temp_dir, exist_ok=True)
    #
    #     rdp_file = generate_rdp_file(params, temp_dir)
    #     logger.info(f"Generated RDP file at: {rdp_file}")
    #
    #     launch_thincast(rdp_file)
    #
    #     # Clean up the RDP file after a delay
    #     time.sleep(10)
    #     if os.path.exists(rdp_file):
    #         os.remove(rdp_file)
    #         logger.info(f"Removed RDP file: {rdp_file}")

    # except Exception as e:
    #     logger.error(f"An error occurred: {e}")
    #     sys.exit(1)
    pass


if __name__ == "__main__":
    main()
