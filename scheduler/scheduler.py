import time;
import sys;
import logging;
from threading import Event;
import threading;
import asyncio
from common.job_store import JobStore


from scheduler.job_receiver import JobReceiver

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger=logging.getLogger(__name__)

MAX_TIMEOUT=10


class Scheduler:
    def __init__(self):
         self._event = Event()
         self._job_store = JobStore()

    def start(self):
        
        logger.info("started")
        self.start_job_receiver()
        while True:
            logger.info("is waiting")
            self._event.wait(MAX_TIMEOUT)
            self._event.clear()
            self.process_job()
            

    def process_job(self):
        logger.info("processing job")
        duejobs=self._job_store.get_due_jobs()
        for job in duejobs:
            logger.info(f"sending job {job} to executor.")
            time.sleep(1)
        logger.info("sent all due job to the executors")
    
    def start_job_receiver(self):
        JobReceiver(self._event).start()
       

        

    