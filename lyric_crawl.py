import urllib2
from bs4 import BeautifulSoup


response = urllib2.urlopen("http://phish.net/song/")
html = response.read()



soup = BeautifulSoup(html)
urls = []
for a in soup.find_all("a"):
    if "/history" in a['href']:
        urls.append("http://phish.net/song/" + a['href'].split('/')[2] + "/lyrics")

lyricDict = {}
songs = []
for url in urls:
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html)
    text = soup.find("blockquote")
    try:
        content = [unicode(item) for item in text.contents]
        artist = content[0]
        lyrics = "".join(content[6:len(content)])
        cleanLyrics = lyrics.replace("<br/>","")
        if "Anastasio" in artist or "McConnell" in artist or "Fishman" in artist or "Gordon" in artist:
            songs.append(cleanLyrics)

##        print cleanLyrics
    except:
        pass

f1 = open("lyrics/lyrics.txt", "w")
for item in songs:
    f1.write("%s\n" % item.encode('utf-8'))
f1.close()
