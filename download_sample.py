import urllib2

url = "http://inspirefwtx.weebly.com/uploads/2/5/0/9/25099112/1656174_orig.jpg"

file_name = url.split('/')[-1]
u = urllib2.urlopen(url)
while True:
    buffer = u.read()
    if not buffer:
        break

    f = open(file_name, 'wb')
    f.write(buffer)
    f.close()
