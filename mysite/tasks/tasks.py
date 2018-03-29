from hist_price.models import *
from django_cron import CronJobBase, Schedule
import datetime
'''
class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1 # every 1 minutes

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'my_app.my_cron_job'

    def do(self):
        pass # do your thing here

        current_price = 9.9
        date='2018-03-29'
        p = PriceHistory(item=Item.objects.get(pk=1), price=current_price, date=date)
        p.save()
'''
def get_current_price(pid):
    return float(pid)/100

class UpdateHistoryPrice(CronJobBase):
    RUN_EVERY_MINS = 1

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'my_app.my_cron_job'

    def do(self):
        #for item in Item.objects.all():
            #if item.brand == 'GNC':
        i=Item.objects.get(pk=1)
        current_price = get_current_price(i.pid)
        time_tag = datetime.datetime.now().strtime("%Y-%m-%d")
        #p = PriceHistory(item=item, price=12.5, date=time_tag) 
        p = PriceHistory(item=i, price=current_price, date='2018-03-30')
        p.save()

