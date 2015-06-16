import sys
import os
from yelp_info.models import Episode
import csv

# Full path and name to your csv file
csv_filepathname = "/Users/maggiecriqui/code/yelp_and_DDD/FINAL_csv.csv"
# Full path to your django project directory
your_djangoproject_home = "/Users/maggiecriqui/code/yelp_and_DDD"



sys.path.append(your_djangoproject_home)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'


dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')

for row in dataReader:
    if row[0] != 'Season': # Ignore the header row, import everything else
        episode = Episode()
        episode.season = row[0]
        episode.resaurant_title = row[1]
        episode.city = row[2]
        episode.state = row[3]
        episode.business_id = row[4]
        episode.restaurant = row[5]
        episode.rating = row[6]
        episode.save()