import logging
logging.basicConfig(format = '%(asctime)s: %(levelname)s: %(message)s',
                    datefmt= '%d %m %y-- %I:%M:%S:%p' ,level=logging.DEBUG)
logging.warning("This is a warning message")
logging.info("This is just an info message")
logging.error("error")