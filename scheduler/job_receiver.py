import time
import logging;
import threading;
logger=logging.getLogger(__name__)

class JobReceiver():
    def __init__(self, event):
        self._event=event
    def start(self):
        logger.info("started")
        x = threading.Thread(target=self.simulated_MQ)
        x.start()

    def simulated_MQ(self):
        #replace by pika, rabbitMQ client 
        
        i=0
        while i<10:
            i+=1
            logger.info("waiting for incoming job")
            time.sleep(3) 
            logger.info("got a job (simulated)")
            self._event.set()
            