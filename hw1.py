import copy
import re
import collections

#import dictionary containing words whose word length is 16 or less
dic_16 = []
with open("dictionary.txt", 'r') as f:
    for line in f:
        line = line.replace("qu", "q")
        dic_16.append(line.replace("\n", ""))

#make a small dictionary that contains words which is consisted of  only given characters
def mk_new_dic(s):
    new_dic = []
    match = ''.join(sorted(set(s)))
    for v in dic_16:
        if re.search("[^"+match+"]", v) == None:
            new_dic.append(v)
    return new_dic

#make a list of words which can be the answer
def mk_match(new_dic, s):
    counter = collections.Counter(s)
    l = []
    for word in new_dic:
        if all(map(lambda items: word.count(items[0]) <= items[1], counter.items())) == True:
            l.append(word)
    return l

def point(word):
    if word == '':
        return 0
    count = 1
    c3 = re.findall("[jkqxz]", word)
    count += 3 * len(c3)
    c2 = re.findall("[cfhlmpvwy]", word)
    count += 2 * len(c2)
    c1 = re.findall("[^jkqxzcfhlmpvwy]", word)
    count += len(c1)
    return (count) ** 2

def mk_best_word(original):
    new_dic = mk_new_dic(original)
    word_list = mk_match(new_dic, original)
    if word_list == []:
        return "", 0
    d = {}
    for word in word_list:
        d[word] = point(word)
    d = sorted(d, key = lambda x : d[x], reverse = True)
    return d[0], point(d[0])

#receive16 characters
score = 0
for i in range(10):
    original = input().lower()
    original = original.replace("qu", "q")
    w, c = mk_best_word(original)
    score += c
    print(w, c)
    