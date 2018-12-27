import http.client
import re
import collections
import operator

def getTranscript(num, debug = 0):
        conn = http.client.HTTPSConnection("www.explainxkcd.com")

        searched = r"<span.*?>\s*Transcript\s*</span>.*?</h\d>(.*?)<h\d>"
        #probably not the best way to do it but it works for:
        #1, 25, 180, 500, 1000, 1500, 1840
        
        conn.request("GET", "/wiki/index.php/"+str(num))
        
        site = conn.getresponse().read().decode("utf-8")
        if debug:
                print(site)
        m = re.search(searched, site, re.I | re.DOTALL)
        if m == None or m.lastindex == None:
                print("\rno transcript found for "+str(num))
                if debug:
                        print("no transcript found for "+str(num))
                return "";#no transcript found
		
        if debug:
                print(m.group(0)+"\n")
        desc = m.group(1)
        if debug:
                print(desc+"\n")
        desc = re.sub("<.*?>", "",desc) #remove html markups
        if debug:
                print(desc+"\n")
        desc = re.sub(r"\[.*?\]", "",desc) # remove [situation description]
        if debug:
                print(desc+"\n")
        desc = re.sub(r"\\n", " ",desc) # remove "\n"s
        if debug:
                print(desc+"\n")
        desc = re.sub("&#160.*", "",desc) #remove things like "add a comment" (at the end)
        if debug:
                print(desc+"\n")
        
        return desc

def splitWords(transcript):
        words = list()
        wordRegex = re.compile(r"\b(\w+)\b")
        for word in re.findall(wordRegex,transcript):
                #print(word)
                words.append(word)
        return words

class WordCounter:
        def __init__(self):
                self.counter = collections.OrderedDict()
        def add(self, word):
                if word in self.counter:
                        self.counter[word] += 1
                else:
                        self.counter[word] = 1

wordCounter = WordCounter()
first = 1
last = 2090
total = last-first+1

out_file = 'list.txt'

print(wordCounter.counter)
for i in range(first, last+1):
        print('\r%i out of %i done' % (i-first, total), end = '\r')
        transcript = getTranscript(i)
        words = splitWords(transcript)
        for word in words:
                wordCounter.add(word.lower())

print('\n%i out of %i done' % (last-first+1, total))
print('saving results to %s' % out_file)

stats = sorted(wordCounter.counter.items(),
                             key=operator.itemgetter(1),
                             reverse = True)
with open(out_file, 'w', encoding='utf-8') as f:
        for wordStat in stats:
                #print(wordStat)
                print(wordStat, file=f)
