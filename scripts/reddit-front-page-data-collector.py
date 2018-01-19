"""
Blake Bryant
Reddit front page title reader and data cleansing
"""


import praw
import WordCounter
import time
import sys
import os
import datetime
import cleanTitle

# Creates the reddit instance used to pull headlines from the front page
reddit = praw.Reddit(client_id='r0vxbQHE1IP0Ig', client_secret="YGKFlmNt_wJZbz3aze_qt4uWQfw",
                     password='bluelake', user_agent='Test script by /u/balake0813', username='FrontPageTitleReader')
WC = WordCounter.WordCounter()
# Checks the connection to Reddit
try:
    print('Trying connection...')
    if reddit.user.me() == 'FrontPageTitleReader':
        print('Connection to Reddit successful!')
except:
    print('ERROR: Possible no connection')

# TODO WRITE INTRODUCTION AND USAGE (possible README)


# GLOBAL VARIABLES
# Dictionary for storing word count
WORDS = {}
# List of all the headlines recorded
ALL_HEADLINES = []
# Skips the user prompts if True
QUICK_TEST = True
# Save file for all headlines before processing
HEADLINES_SAVE_FILE = 'AllHeadlines.txt'
# Minutes for submission refresh
if not QUICK_TEST:
    TIME_INTERVAL = input("Enter a positive whole number for the time interval in minutes for getting headlines: ")
    while not TIME_INTERVAL.isdigit() or int(TIME_INTERVAL) <= 0:
        TIME_INTERVAL = input("That is not an accepted response for the time interval. Please try again: ")
    TIME_INTERVAL = int(TIME_INTERVAL)
    DATA_FILE = input("Enter the name of the file (txt only) to be used or created: ")
    while DATA_FILE[len(DATA_FILE) - 4:] != '.txt':
        DATA_FILE = input("That's not a valid file name. Please try again: ")
else:
    TIME_INTERVAL = 10
    DATA_FILE = 'test.txt'
print("Time interval selected: " + str(TIME_INTERVAL) + " minutes")
print("File to be used for recording data: " + DATA_FILE)


# TODO write function for checking if the submissions are repeats
# TODO write function for outputting data into CSV
# TODO write function for SQLite database functionality (writing to database)


# Gets the headlines from the reddit front page. Returns the new headlines as list of strings.
def get_headlines():
    headlines = []
    new_headlines = 0
    for submission in reddit.front.hot():
        if submission.title not in ALL_HEADLINES:
            new_headlines += 1
            ALL_HEADLINES.append(submission.title)
            headlines.append(submission.title)
    print('# of new headlines since last check: ' + str(new_headlines))
    return headlines


def save_headlines(headlines):
    print("\n\nSaving headlines to '" + HEADLINES_SAVE_FILE + "'...")
    if os.path.isfile(HEADLINES_SAVE_FILE):
        f = open(HEADLINES_SAVE_FILE, 'r+')
        existing_headlines = f.readlines()
    else:
        f = open(HEADLINES_SAVE_FILE, 'w')
        existing_headlines = []
    new_headlines = 0
    for headline in headlines:
        if headline + "\n" not in existing_headlines:
            new_headlines += 1
            f.write(headline + "\n")
    print("Saved " + str(new_headlines) + " new headlines to '" + HEADLINES_SAVE_FILE + "'")
    f.close()

try:
    print("Checking Reddit every " + str(TIME_INTERVAL) + " seconds....")
    while True:
        start_time = time.time()
        #print("Current top ten of counted words: \n")
        #WC.print_df(10)
        # WC.save_df(DATA_FILE)
        print("Time elapsed to check for new headlines: " + str(round(time.time() - start_time, 3)) + " seconds.")
        for remaining in range(TIME_INTERVAL, -1, -1):
            sys.stdout.write("\r")
            sys.stdout.write("{:2d} seconds remaining...".format(remaining))
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.write("\r")
        sys.stdout.write("Checking for new headlines...\n")
        sys.stdout.flush()
except KeyboardInterrupt:
    print("Initializing shut down....")
    #save_headlines(ALL_HEADLINES)
    #WC.save_df(DATA_FILE)
    print("\n\nOh no. You killed me :(")
