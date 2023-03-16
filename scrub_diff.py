#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 13:59:43 2023

@author: pierre
"""

import requests
from bs4 import BeautifulSoup

def scrape_job_listings(url):
    # Send an HTTP request to the website
    response = requests.get(url)
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all job listings on the page
    job_listings = soup.find_all('a', class_='job-title-link')
    
    # Create a set to store the old job listings
    old_jobs = set()
    
    # Read the old job listings from a file, if it exists
    try:
        with open('old_jobs.txt', 'r') as f:
            for line in f:
                title, url = line.strip().split('\t')
                old_jobs.add((title, url))
    except FileNotFoundError:
        pass
    
    # Create a set to store the new job listings
    new_jobs = set()
    
    # Extract the title and URL for each job listing
    for job in job_listings:
        title = job.text.strip()
        url = job['href']
        new_jobs.add((title, url))
    
    # Find the new job listings
    new = new_jobs - old_jobs
    
    # Find the removed job listings
    removed = old_jobs - new_jobs
    
    # Write the new job listings to a file
    with open('new_jobs.txt', 'w') as f:
        for title, url in new:
            f.write(f"{title}\t{url}\n")
    
    # Write the current job listings to the old job listings file
    with open('old_jobs.txt', 'w') as f:
        for title, url in new_jobs:
            f.write(f"{title}\t{url}\n")
    
    # Return the new and removed job listings
    return new, removed