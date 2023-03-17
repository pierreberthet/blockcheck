#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 13:59:43 2023

@author: pierre
"""

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

import time
#%%

url = "https://block.xyz/careers?business=TBD|Block|Cash%20App|Square&locations=British%20Columbia%2C%20Canada|Dublin%2C%20United%20Kingdom|Chisinau%2C%20Moldova%2C%20republic%20of|San%20Diego%2C%20United%20States|Seattle%2C%20United%20States|Berlin%2C%20United%20Kingdom|Amsterdam%2C%20Netherlands|Remote|Portland%20Metro%2C%20United%20States|Montreal%2C%20Canada|Barcelona%2C%20Ireland|Raleigh%2C%20United%20States|US%20-%20CA%20-%20%20NorCal%20Remote|Barcelona%2C%20Spain|Los%20Angeles%2C%20United%20States|Tokyo%2C%20Japan|Stockholm%2C%20Norway|Toronto%20or%20Vancouver%2C%20Canada|Warsaw%2C%20Norway|Dublin%2C%20Ireland|Toronto%2C%20Canada|Mountain%20View%2C%20United%20States|Berlin%2C%20Norway|Portland%20Metro%20%28Remote%29%2C%20United%20States|Ciudad%20de%20Mexico%2C%20Mexico|Manchester%2C%20United%20Kingdom|Melbourne%2C%20Australia|Oslo%2C%20Norway|Salt%20Lake%20City%2C%20United%20States|London%2C%20United%20Kingdom|Southern%20CA%20%28Remote%29%2C%20United%20States|Colorado%20Springs%2C%20United%20States|Barcelona%2C%20Norway|Berlin%2C%20Germany|Warsaw%2C%20Poland|Vancouver%2C%20Canada|Portland%2C%20United%20States|Mexico%20City%2C%20Mexico&roles=Supply%20Chain|Analytics|Data%20Science%20%26%20Machine%20Learning"


# def scrape_job_listings(url):
# Send an HTTP request to the website
driver = webdriver.Firefox()
driver.get(url)
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# html = driver.page_source
time.sleep(time_sleep)
soup = BeautifulSoup(driver.page_source, 'html5lib')

#%%

# Find all job listings on the page
job_listings = soup.find_all('a', class_='JobList_link__yOMBM')

# Create a set to store the old job listings
old_jobs = set()

# Read the old job listings from a file, if it exists
try:
    with open('old_jobs.txt', 'r') as f:
        for line in f:
            title, url = line.strip().split('\t')
            old_jobs.add((title, url))
except FileNotFoundError:
    print("no previous file, creating one")
    # create one
    pass

# Create a set to store the new job listings
new_jobs = set()

for job in job_listings:
     print(job)
     print("\n")
     
     
# Extract the title and URL for each job listing
for job in job_listings:
    title = job.text.strip()
    url = job['href']
    new_jobs.add((title, url))

# Find the new job listings
new = new_jobs - old_jobs

# Find the removed job listings
removed = old_jobs - new_jobs
    
    # # Write the new job listings to a file
    # with open('new_jobs.txt', 'w') as f:
    #     for title, url in new:
    #         f.write(f"{title}\t{url}\n")
    
    # # Write the current job listings to the old job listings file
    # with open('old_jobs.txt', 'w') as f:
    #     for title, url in new_jobs:
    #         f.write(f"{title}\t{url}\n")
    
    # # Return the new and removed job listings
    # return new, removed