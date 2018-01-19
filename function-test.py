import cleanTitle

f = open('AllHeadlines.txt', 'r+')
hls = f.readlines()

ct = cleanTitle.cleanTitle()
chls = []
for h in hls:
    chls.append(ct.clean(h))
for v in chls:
    print(str(v))