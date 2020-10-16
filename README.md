# connection-info
Console app for checking and monitoring connection and offline time

After having a lot of problems with my ISP, i have decided to write this program.

**connection_info.pyw** [more on pyw](https://stackoverflow.com/questions/9705982/pythonw-exe-or-python-exe)) pings googles dns server and based on the response writes it to a log.txt file as online or offline (if request timed out or host unreachable). It is a while loop thats constantly running and pings are sent every second.

It can be made to run on startup simply by copying a shortcut to a Startup folder (have tried it on Windows). To get to Startup folder type **shell:startup** into run (windows key + r).

**offline_stats.py** processes the data from log file and extracts all instances where there are 3 or more consecutives offline lines, writes that to offline.txt and adds up total offline time by day and writes that to total.txt. Every time **offline_stats.py** is run it owerwrites the offline and total files.

After about 800k lines (arround 12 days of data) in log file, it is 23MB in size.
