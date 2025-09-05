#!/usr/bin/env python
"""reducer.py"""

#!/usr/bin/env python
import sys

current_url = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    url, count = line.split('\t')
    count = int(count)

    if current_url == url:
        current_count += count
    else:
        if current_url and current_count > 5:
            print(f"{current_url}\t{current_count}")
        current_url = url
        current_count = count

# Print the last URL if count > 5
if current_url == url and current_count > 5:
    print(f"{current_url}\t{current_count}")
