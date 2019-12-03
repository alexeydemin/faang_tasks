# Import libraries
import time
from datetime import datetime as dt

# Path to the host file, redirect to local host, list of websits to block
host_path = "/home/alex/hosts"
redirect = "127.0.0.1"
website_list = ["www.netflix.com","www.facebook.com"]

# Condition
while True:
    # Check for the current time
    n = dt.now()
    if dt(n.year, n.month, n.day, 8) < n < dt(n.year, n.month, n.day, 16):
        # Open file and read the content
        file = open(host_path, "r+")
        content = file.read()
        for website in website_list:
            if website in content:
                pass
            else:
                # Write the IP of localhost and name of the website to block
                file.write(redirect + " " + website + "\n")
    else:
        file = open(host_path, 'r+')
        content = file.readlines()
        # Take back pointer to starting of the file from the end of file
        file.seek(0)
        for line in content:
            # Please check explanation for this line
            if not any(website in line for website in website_list):
                file.write(line)
            file.truncate()
    time.sleep(5)
