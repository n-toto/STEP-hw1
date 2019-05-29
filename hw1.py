import copy
import re
import collections

# Import dictionary containing words whose word length is 16 or less
dic_16 = []
with open("dictionary.txt", 'r') as f:
    for line in f:
        line = line.replace("qu", "q")
        dic_16.append(line.replace("\n", ""))

# Make a small dictionary that contains words consisting only of the given characters
def mk_new_dic(s):
    new_dic = []
    match = re.compile("[^"+s+"]")
    for v in dic_16:
        if re.search(match, v) == None:
            new_dic.append(v)
    return new_dic

# Make a list of words which only use the supplied letters.
def mk_match(new_dic, s):
    counter = collections.Counter(s)
    l = []
    for word in new_dic:
        if all(map(lambda items: word.count(items[0]) <= items[1], counter.items())) == True:
            l.append(word)
    return l

# Culculate the score for a word.
# The score for a given word is the square of the sum of its letter points plus a bonus point for not passing
# Letter point
# 'jxqxz' : 3, 'cfhlmpvwy' : 2, others : 1 point for each.
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
    return count ** 2

def mk_best_word(original):
    new_dic = mk_new_dic(original)
    word_list = mk_match(new_dic, original)
    if word_list == []:
        return "", 0
    score = {}
    for word in word_list:
        score[word.replace("q", "qu")] = point(word)
    score = sorted(score, key = lambda x : score[x], reverse = True)
    return score[0], point(score[0])

# Interactively read 16 letters 10 times.
score = 0
for i in range(10):
    original = input().lower()
    canonical = original.replace("qu", "q")
    w, c = mk_best_word(canonical)
    score += c
    print(w, c)
print(score)