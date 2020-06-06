import sys
import optparse
import requests

default_header_value = 'qwerty123'
header_word_list = 'header-list.txt'

parser = optparse.OptionParser()
parser.add_option('-u', '--url', dest='url')
(options, args) = parser.parse_args()

with open(header_word_list) as fp:
    line = fp.readline()
    line = line.rstrip("\n")
    while line:
        print("[+] Trying header: " + line)
        request_headers = {line : default_header_value}
        web_request = requests.get(options.url, headers=request_headers)
        if default_header_value in web_request.headers:
            print('[!] Found Header: ' + line + ":" + default_header_value)
            print('-------------------')
            if (default_header_value in web_request.text):
                print("[!!] Possible XXS")   
        line = fp.readline()
        line = line.rstrip("\n")