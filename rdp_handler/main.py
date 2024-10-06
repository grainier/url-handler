import os
import sys
import time

from rdp_handler.launcher import launch_thincast
from rdp_handler.logger import logger
from rdp_handler.parser import parse_rdp_url
from rdp_handler.rdp_generator import generate_rdp_file


def process_url(url):
    logger.info(f"Received URL: {url}")

    try:
        params = parse_rdp_url(url)
        logger.info(f"Parsed parameters: {params}")

        temp_dir = os.path.join(os.path.expanduser('~'), '.rdpurlhandler', 'tmp')
        os.makedirs(temp_dir, exist_ok=True)

        rdp_file = generate_rdp_file(params, temp_dir)
        logger.info(f"Generated RDP file at: {rdp_file}")

        launch_thincast(rdp_file)

        # Clean up the RDP file after a delay
        time.sleep(10)
        if os.path.exists(rdp_file):
            os.remove(rdp_file)
            logger.info(f"Removed RDP file: {rdp_file}")

    except Exception as e:
        logger.error(f"An error occurred: {e}", exc_info=True)
        sys.exit(1)


def main():
    if len(sys.argv) > 1:
        # URL is passed as a command-line argument
        url = sys.argv[1]
        process_url(url)
    else:
        # No URL passed via command line
        if sys.platform == 'darwin':
            logger.info("Running on Darwin")
            try:
                import objc
                from Foundation import NSObject
                from AppKit import NSApplication, NSApp

                class AppDelegate(NSObject):
                    def applicationDidFinishLaunching_(self, notification):
                        logger.info("Application did finish launching")

                    def application_openURLs_(self, app, urls):
                        logger.info("application_openURLs_ called")
                        for url in urls:
                            url_str = str(url.absoluteString())
                            logger.info(f"Received URL via application_openURLs_: {url_str}")
                            process_url(url_str)
                        # Log before termination
                        logger.info("Processing complete, terminating application")
                        # Exit the application after processing
                        NSApp.terminate_(self)

                app = NSApplication.sharedApplication()
                delegate = AppDelegate.alloc().init()
                app.setDelegate_(delegate)
                app.run()
            except Exception as e:
                logger.error(f"Exception in main: {e}", exc_info=True)
                sys.exit(1)
        else:
            # On other platforms, log an error if no URL is provided
            logger.error("No URL provided.")
            sys.exit(1)


if __name__ == "__main__":
    main()
