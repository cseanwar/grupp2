#!/usr/bin/python3

import datetime
import tarfile
import os.path

cuttent_time = datetime.datetime.now()
if cuttent_time.month == 1:
   pre_month = cuttent_time.replace(year=cuttent_time.year - 1, month=12)
else:
    days = 0
    while True:
        try:
            pre_month = cuttent_time.replace(month=cuttent_time.month - 1, day=cuttent_time.day - days)
            break
        except ValueError:
           days += 1

# Pick cuttent year from cuttent_time
des_year = pre_month.strftime("%Y")

# Pick cuttent month from cuttent_time
des_month = pre_month.strftime("%m")

# Source fle
file_name = "/var/log/removed_users_" + des_year + "-" + des_month + ".txt"

# Destination file
zipped_file = "/var/log/removed_users_" + des_year + "-" + des_month


with tarfile.open(f"{zipped_file}.tar.gz", "w:gz") as tar:
    tar.add(file_name)

# To delete a file
if os.path.exists(file_name):
     os.remove(file_name)
