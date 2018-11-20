import base64, os
import sys
import gzip

text_file = open("content.txt", "r")
lines = text_file.readlines()
content_str = str(lines[0])

encoded =  content_str.encode('ascii')
print(type(encoded))

def decode_base64(data):
    missing_padding = len(data) % 4
    if missing_padding != 0:
        data += b'='* (4 - missing_padding)
    return base64.decodestring(data)

with open(os.path.expanduser('test.txt'), 'wb') as f:
	# f.write(gzip.decompress(decode_base64(encoded)))
	f.write(decode_base64(encoded))


