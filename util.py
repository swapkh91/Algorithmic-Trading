import time
import datetime

def generate_past_n_days(numdays, start_date):
    """Generate N days until now, e.g., [20151231, 20151230]."""
    base = datetime.datetime.strptime(start_date, "%m/%d/%Y")
    date_range = [base + datetime.timedelta(days=x) for x in range(0, numdays)]
    return [x.strftime("%Y%m%d") for x in date_range]
