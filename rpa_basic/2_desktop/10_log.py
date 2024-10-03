import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s")

logging.debug("1")
logging.info("2")
logging.warning("3")
logging.error("4")
logging.critical("5")
