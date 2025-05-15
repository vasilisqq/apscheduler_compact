from apscheduler.schedulers.asyncio import AsyncIOScheduler

class C_scheduler():

    def __init__(self):
        self.scheduler = AsyncIOScheduler(timezone="Europe/Moscow")

    def start_sc(self):
        self.scheduler.start()

    def scheduled_task(func):
        def wrapper(self, trigger, time, **kwargs):
            self.scheduler.add_job(
                func,
                trigger,
                time,
                kwargs= {"self":self} | kwargs
            )
        return wrapper
    

    @scheduled_task
    async def hatch(self, triger, time, **kwargs):
        print("hello")

c_scheduler = C_scheduler()
