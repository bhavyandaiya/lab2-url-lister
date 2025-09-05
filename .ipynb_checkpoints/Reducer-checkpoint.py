#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

#initiate
current_url = None
current_count = 0

#input comes from STDIN
for line in sys.stdin:
    line = line.strip() #removes whitespaces leading n trailing
    if not line:
        continue

    #is every single input coming from mapper.py in the format: <url>   <count> ? if yes
    try:
        url, count_str = line.split('\t', 1)
    except:
        ValueError 
        continue

    #converts every <count> in the input to an integet. skips if failed
    try:
        count = int(count_str)
    except:
        continue
    #if current url in loop is same as one in new line, then add it to count
    if current_url == url:
        current_count += count

    else:
        if current_url is not None:
            print(f'{current_url}\t{current_count}') #prints <url>   <count> (updated)
        current_url = url #updates url
        current_count = count #updates the count of <url>

if current_url is not None:
    print(f'{current_url}\t{current_count}') #prints last url, because it doesnt print that in loop because after url 1 is finished, the loop will recognise the new url, but not print it