# Regular expression to extract URLs in href="URL"
import re
url_pattern = re.compile(r'href="([^"]+)"')

for line in sys.stdin:
    line = line.strip()
    urls = url_pattern.findall(line)
    for url in urls:
        print(f"{url}\t1")
