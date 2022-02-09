import logging;
logger=logging.getLogger(__name__)

class JobStore:
    def __init__(self, db=None):
        self._job_list=["JOB1","JOB2"] #initial dummy jobs
        
    
    def add_job(self,job):
        logger.info(f"Job {job} is added to the DB.")
        self._job_list.append(job)

    def get_due_jobs(self):
        return self._job_list # due job list