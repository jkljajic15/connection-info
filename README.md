# connection-info
Console app for checking and monitoring connection and offline time

After having a lot of problems with my ISP, i have decided to write this program.

**connection_info.pyw** ([more on pyw](https://stackoverflow.com/questions/9705982/pythonw-exe-or-python-exe)) pings googles dns server and based on the response writes it to a log.txt file as online or offline (if request timed out or host unreachable). It is a while loop thats constantly running and pings are sent every second.

It can be made to run on startup simply by copying a shortcut to a Startup folder (have tried it on Windows). To get to Startup folder type **shell:startup** into run (windows key + r).

**offline_stats.py** processes the data from log file and extracts all instances where there are 3 or more consecutive offline lines, writes that to offline.txt and adds up total offline time by day and writes that to total.txt. Every time **offline_stats.py** is run it overwrites the offline and total files.

After about 800k lines (arround 12 days of data) in log file, it is 23MB in size.
## Prerequisits
1. Python 3 installed
2. tqdm package for progress bar (optional) - **pip install tqdm**
## Usage
1. Download zip file and extract it
2. If you want the program to run on startup copy the shortcut to Startup folder (optional)
3. Run **connection_info.pyw**
4. Run **offline_stats.py** at will to get more information from log file

## Screenshots
![Alt text](/screenshots/logtxt.png?raw=true "Optional Title")
![Alt text](/screenshots/offlinetxt.png?raw=true "Optional Title")
![Alt text](/screenshots/totaltxt.png?raw=true "Optional Title")
![Alt text](/screenshots/offlinestats.png?raw=true "Optional Title")
