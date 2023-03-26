import os
import random
import datetime


def prefix_url(url, prefix='deep'):
    files = []
    for file in os.listdir(url):
        if file.startswith(prefix):
            files.append(file)

    return files


def random_date_in_range(first_date, last_date):
    delta = (last_date - first_date)
    delta_in_days = delta.days

    random_days = random.randint(0, delta_in_days)

    random_date = first_date + datetime.timedelta(days=random_days)

    print(random_date)

    # random_date is monday
    if random_date.weekday() == 0:
        print("I have no vinagrette!")


if __name__ == "__main__":
    first_date = datetime.datetime.strptime('1940-1-4', "%Y-%m-%d").date()
    last_date = datetime.datetime.strptime('1967-11-22', "%Y-%m-%d").date()

    random_date_in_range(first_date, last_date)
