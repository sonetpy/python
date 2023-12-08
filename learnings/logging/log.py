# You’ll see that the messages corresponding to warning, error, and critical are logged onto the console, whereas debug and info are not.
# This is because, by default, only messages corresponding to a logging level of warning and above are logged onto the console. 
# However, you can modify this by configuring the logger to start logging from a specific level of your choosing.
# Check learnings\logging\log_at_all_level.py to see logging at all levels

import logging
def main() -> None:
    logging.basicConfig(level=logging.INFO)

    logging.debug("A DEBUG Message")
    logging.info("An INFO")
    logging.warning("A WARNING")
    logging.error("An ERROR")
    logging.critical("A message of CRITICAL severity")

if __name__ == "__main__":
    main()
