import requests
import tablib

def find_nth(string, substring, n):
   if (n == 1):
       return string.find(substring)
   else:
       return string.find(substring, find_nth(string, substring, n - 1) + 1)

def extract_url(line):
    if not line.startswith('#Server'):
        return None
    end = find_nth(line, '/', 3) + 1
    if end <= 0:
        return None
    return line[10:end].strip()

def main():
    r = requests.get('https://www.archlinux.org/mirrorlist/?country=all&protocol=http&protocol=https&ip_version=4')
    lines = r.text.split('\n')
    for line in lines:
        url = extract_url(line)
        if not url:
            continue
        print(url, '\t', end='')
        r = requests.get(url)
        print(r.elapsed.total_seconds())

if __name__ == '__main__':
    main()
