# Full path and name to your csv file
csv_filepathname = "maggiecriqui/code/yelp_and_DDD/Final_csv.csv"
# Full path to your django project directory
your_djangoproject_home = "maggiecriqui/code/yelp_and_DDD"

import sys
import os

sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from yelp_info.models import Episode

import csv

dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')

for row in dataReader:
if row[0] != 'ZIPCODE': # Ignore the header row, import everything else
zipcode = ZipCode()
zipcode.zipcode = row[0]
zipcode.city = row[1]
zipcode.statecode = row[2]
zipcode.statename = row[3]
zipcode.save()