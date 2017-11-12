import pronounce

file = open('words.txt')
wlist = []

for line in file:
    wlist.append(line.strip())
    
def words_to_keys(wlist):
    dict1 = dict()
    index = 0
    for word in wlist:
        dict1[word] = index
        index += 1
    return dict1

# two dictionaries: pronounciation dict and keyword dict    
pro_dictionary = pronounce.read_dictionary(filename='c06d.txt')
key_words = words_to_keys(wlist)

# inverting the pronounication dict so that we can find have prounciations be the keys
# and create a list of words that have the same pronounciation
def invert_dict(d):
    inverse = dict()
    for key in d:
        value = d[key]
        inverse.setdefault(value, []).append(key)
    return inverse

new_dict = invert_dict(pro_dictionary)

for k, v in new_dict.items():
    if len(v) >= 3:
        if len(v[0]) >= 4:
            if v[0][1:] in v:
                if v[0][0] + v[0][2:] in v:
                    print(v)
        