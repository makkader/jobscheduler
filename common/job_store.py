import logging;
logger=logging.getLogger(__name__)

class JobStore:
    def __init__(self, db=None):
        pass
    
    def add_job(self,job=None):
        logger.info(f"Imagine job {job} is added to the DB.")
    
    def get_due_jobs(self):
        return ["JOB1","JOB2"] # due job list