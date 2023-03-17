#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 13:59:43 2023

@author: pierre
"""

# import requests
from bs4 import BeautifulSoup
from selenium import webdriver

import pandas as pd

import time
from datetime import datetime
import os
#%%

url = "https://block.xyz/careers?business=TBD|Block|Cash%20App|Square&locations=British%20Columbia%2C%20Canada|Dublin%2C%20United%20Kingdom|Chisinau%2C%20Moldova%2C%20republic%20of|San%20Diego%2C%20United%20States|Seattle%2C%20United%20States|Berlin%2C%20United%20Kingdom|Amsterdam%2C%20Netherlands|Remote|Portland%20Metro%2C%20United%20States|Montreal%2C%20Canada|Barcelona%2C%20Ireland|Raleigh%2C%20United%20States|US%20-%20CA%20-%20%20NorCal%20Remote|Barcelona%2C%20Spain|Los%20Angeles%2C%20United%20States|Tokyo%2C%20Japan|Stockholm%2C%20Norway|Toronto%20or%20Vancouver%2C%20Canada|Warsaw%2C%20Norway|Dublin%2C%20Ireland|Toronto%2C%20Canada|Mountain%20View%2C%20United%20States|Berlin%2C%20Norway|Portland%20Metro%20%28Remote%29%2C%20United%20States|Ciudad%20de%20Mexico%2C%20Mexico|Manchester%2C%20United%20Kingdom|Melbourne%2C%20Australia|Oslo%2C%20Norway|Salt%20Lake%20City%2C%20United%20States|London%2C%20United%20Kingdom|Southern%20CA%20%28Remote%29%2C%20United%20States|Colorado%20Springs%2C%20United%20States|Barcelona%2C%20Norway|Berlin%2C%20Germany|Warsaw%2C%20Poland|Vancouver%2C%20Canada|Portland%2C%20United%20States|Mexico%20City%2C%20Mexico&roles=Supply%20Chain|Analytics|Data%20Science%20%26%20Machine%20Learning"


save_dir = '/media/terror/code/projects/blockcheck/'
previous_jobs = 'previous_df.csv'
os.chdir(save_dir)

driver = webdriver.Firefox()
driver.get(url)
time.sleep(3)
soup = BeautifulSoup(driver.page_source, 'html5lib')
driver.close()
#%%

# Find all job listings on the page
job_listings = soup.find_all('a', class_='JobList_link__yOMBM')


# get current job offers
current = dict()
for job in job_listings:
    current[job['href']] = {'title': job.find('div', class_='JobList_titleColumn__3oZrC').text, 
                        'business': job.find('div', class_='JobList_secondaryColumnSm__Ac1BT').text,
                        'location': [loc.text for loc in job.find('div', class_='JobList_locationsColumn__xrHQC')],
                        'date': datetime.now().strftime('%d/%m/%Y')}
 
current = pd.DataFrame.from_dict(current, orient='index')
current['date'] = pd.to_datetime(current.date, format="%d/%m/%Y")

found_new = False
# Read the old job listings from a file, if it exists
if os.path.exists(previous_jobs):
    previous = pd.read_csv(previous_jobs, index_col=0)
    # first print the ones not listed anymore
    for pi in previous.index:
        if pi not in current.index:
            print(f"REMOVED: {previous.loc[pi, 'title']}      ---    {pi}\n")
    # then print the new ones
    for ci in current.index:
        if ci not in previous.index:
            found_new = True
            print(f"NEW: {current.loc[ci,:]} \n")
    if not found_new:
        print('no new jobs listed')
    
else: 
    for ci in current.index:
        print(f"!!! NEW !!!:    {current.loc[ci,'title']}   ---   {current.loc[ci,'business']}\
\n{current.loc[ci,'location']}\n{current.loc[ci,'date']}\
\n{ci}\n")

# now we save the current as previous
current.to_csv(previous_jobs)

print(f"Checked at {datetime.now().strftime('%H:%M:%S %d/%m/%Y')}")
