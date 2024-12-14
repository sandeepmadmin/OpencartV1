import logging
import os.path


class Loggen():
    @staticmethod
    def logen():
        # path = os.path.abspath(os.curdir)+"\\logs\\automation.logs" # specify in fliname = path
        logging.basicConfig(filename='..\\logs\\automation.log', format='%(asctime)s: %(levelname)s: %(message)s:', datefmt='%m/%d/%y %I:%M:%S: %p')
        logger=logging.getLogger()
        logger.setLevel(logging.DEBUG)#detailed logs is given by DEBUG
        return logger