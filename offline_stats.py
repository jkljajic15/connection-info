import re
import os
import sys
from tqdm import tqdm
from datetime import datetime

# Total offline time: 01:51.20 for: 2020-09-27
# Total offline time: 00:00.26 for: 2020-09-28
# Total offline time: 04:05.00 for: 2020-10-08

def unique(lst): 
  
    unique_lst = [] 
      
    for x in lst: 
        if x not in unique_lst: 
            try:
                # enforcing a correct format of dates (if there is an unexpected shutdown, log file can have a line with questionmarks)
                datetime.strptime(x, '%Y-%m-%d')
                unique_lst.append(x) 
            except:
                pass
    return unique_lst


def time_delta(lst, line):
    start_time = ''.join(re.findall(r'\d\d:\d\d\.\d\d', lst[0]))
    end_time = ''.join(re.findall(r'\d\d:\d\d\.\d\d', line))
    time_format = '%H:%M.%S'
    delta = datetime.strptime(end_time, time_format) - datetime.strptime(start_time, time_format)
    return delta


def getlogdata(filename):
    lst = []
    try:
        with open(filename) as f:
            for line in tqdm(f, desc = 'Getting log data...'):
                lst.append(line)
    except Exception as e:
        print(e)

    return lst

 
lst = getlogdata('log.txt')
dates = [ x.split()[0] for x in tqdm(lst, desc= 'Grabbing dates...')]
dates = unique(dates)


online_lst=[]
offline_lst=[]
total_offline = datetime.strptime('00:00.00', '%H:%M.%S')


def print_offline_stats(next_line):
    global offline_lst
    global total_offline
    if 'online' in next_line and len(offline_lst) != 0:

                time = time_delta(offline_lst, next_line)
                print(offline_lst[0][:19])
                print(offline_lst[-1][:19])
                print(f'\t Offline for {time}')
                total_offline += time
                offline_lst = []


def print_online_stats(next_line):
    global online_lst
    global total_offline
    if 'offline' in next_line and len(online_lst) != 0:

                time = time_delta(online_lst, next_line)
                print(online_lst[0].strip('\n'))
                print(online_lst[-1].strip('\n'))
                print(f'\t Offline for {time}')
                total_offline += time
                online_lst = []



total_offline_by_date = []

original_out = sys.stdout

# if os.path.exists("total.txt"):
#   os.remove("total.txt")

with open('offline.txt', 'w') as f, open('total.txt', 'w') as t:

    sys.stdout = f
    for date in tqdm(dates, desc=f'Writing to offline.txt...'):
        day = [x for x in lst if date in x]
        
        for k in range(len(day)): # tqdm(range(len(day)), desc='Writing daily data to offline.txt')

            if 'offline' in day[k]:
                offline_lst.append(day[k])
                try:
                    
                    next = day[k+1]

                    # ignoring less than 4 consecutive request time out or unreachable packets
                    if 'online' in next and len(offline_lst) < 4:   
                        offline_lst = []
                        k += 1
                    print_offline_stats(next)
                except Exception as e:
                    if len(offline_lst) < 4:
                        print_offline_stats(day[-1])
                    offline_lst = []
                    print(e)
        
        total_offline =  total_offline.strftime('%H:%M.%S')
        total_offline_by_date.append(f'Total offline time: {total_offline} for: {date}')
        print(f'\nTotal offline time: {total_offline} for: {date}\n')
        print('======================================================\n')
        total_offline = datetime.strptime('00:00.00', '%H:%M.%S')
    
    sys.stdout = t
    for x in tqdm(total_offline_by_date, desc='Writing to total.txt...'):
        print(x)
    

    sys.stdout = original_out


print('Program finished. Check offline.txt and total.txt for more information.')
input('Press enter to exit.')