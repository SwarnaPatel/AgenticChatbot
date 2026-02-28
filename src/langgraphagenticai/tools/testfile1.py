import logging
logging.basicConfig(level=logging.INFO,filename="log.log",filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")
x=2
logging.info(f"The value of x is: {x}") 
logger = logging.getLogger(__name__)
logger.info("This is an info message from the logger.") 

try:
    1/0
except ZeroDivisionError as e:
    logging.exception("An error occurred: Division by zero Swarna")       
logging.debug("debug")
logging.info("info")
logging.warning("warning")  
logging.error("error")
logging.critical("critical")
