#!/usr/bin/env python
"""mapper.py"""

import sys
import re
# Regular expression to extract URLs in href="URL"
pattern = re.compile(r'href="([^"]+)"')

for line in sys.stdin:
    line = line.strip()
    urls = pattern.findall(line)
    for url in urls:
      if url.startswith('#'): 
            continue
      print(f"{url}\t1")
