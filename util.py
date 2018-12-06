import time
import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup

def generate_past_n_days(numdays, start_date):
    """Generate N days until now, e.g., [20151231, 20151230]."""
    base = datetime.datetime.strptime(start_date, "%m/%d/%Y")
    date_range = [base + datetime.timedelta(days=x) for x in range(0, numdays)]
    return [x.strftime("%Y%m%d") for x in date_range]

def get_soup_with_repeat(url, repeat_times=3, verbose=True):
    for i in range(repeat_times): # repeat in case of http failure
        try:
            time.sleep(np.random.poisson(3))
            response = urlopen(url)
            data = response.read().decode('utf-8')
            return BeautifulSoup(data, "lxml")
        except Exception as e:
            if i == 0:
                print(e)
            if verbose:
                print('retry...')
            continue
