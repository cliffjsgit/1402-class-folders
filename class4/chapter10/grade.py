#!/usr/bin/env python3

import shelve
import urllib.request

chapter = "10"
exercises = ['10.1','10.2','10.3','10.4','10.5','10.6','10.7','10.9','10.10','10.11','10.12']
loadedList = []
db = shelve.open('chapter10.db', flag='c', writeback=True)
db['loaded'] = {}
if 'submitted' not in db:
    db['submitted'] = {}

try:
    import exercise101
    db['loaded']['10.1'] = True
except:
    db['loaded']['10.1'] = False
try:
    import exercise102
    db['loaded']['10.2'] = True
except:
    db['loaded']['10.2'] = False
try:
    import exercise103
    db['loaded']['10.3'] = True
except:
    db['loaded']['10.3'] = False
try:
    import exercise104
    db['loaded']['10.4'] = True
except:
    db['loaded']['10.4'] = False
try:
    import exercise105
    db['loaded']['10.5'] = True
except:
    db['loaded']['10.5'] = False
try:
    import exercise106
    db['loaded']['10.6'] = True
except:
    db['loaded']['10.6'] = False
try:
    import exercise107
    db['loaded']['10.7'] = True
except:
    db['loaded']['10.7'] = False
try:
    import exercise109
    db['loaded']['10.9'] = True
except:
    db['loaded']['10.9'] = False
try:
    import exercise1010
    db['loaded']['10.10'] = True
except:
    db['loaded']['10.10'] = False
try:
    import exercise1011
    db['loaded']['10.11'] = True
except:
    db['loaded']['10.11'] = False
try:
    import exercise1012
    db['loaded']['10.12'] = True
except:
    db['loaded']['10.12'] = False


db.sync()

def menu():
    while True:
        for exercise in loadedList:
            if exercise in db['submitted']:
                print('[x] Exercise ' + exercise)
            else:
                print('[ ] Exercise ' + exercise)
        print('    Enter q to exit')
        str_in = input('Exercise (e.g. 10.1): ')
        if str_in in loadedList:
            grade(str_in)
            break
        elif str_in.lower() == 'q':
            break
        else:
            print('Incorrect response. Only enter the exercise number. Example: "10.1" (no quotes).')
            
def grade(assignment):
    if assignment == '10.1':
        if exercise101.nested_sum([[1,2],[3,4]]) == 10:
            db['submitted'][assignment] = True
            submit('exercise101.py',exercise101.__author__)
            str_in = input("Exercise answer correct and submitted. Would you like to submit another? (y/n): ")
            if str_in.lower() == 'y':
                menu()
        else:
            str_in = input('The exercise answer was incorrect. Did you still want to submit it? (y/n): ')
            if str_in.lower() == 'y':
                db['submitted'][assignment] = True
                submitbad('exercise101.py',exercise101.__author__)
                str_in = input("Exercise submitted. Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
            else:
                print('Assignment was not submitted')
                str_in = input("Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
    elif assignment == '10.2':
        if exercise102.cum_sum([1, 2, 3]) == [1, 3, 6]:
            db['submitted'][assignment] = True
            submit('exercise102.py',exercise102.__author__)
            str_in = input("Exercise answer correct and submitted. Would you like to submit another? (y/n): ")
            if str_in.lower() == 'y':
                menu()
        else:
            str_in = input('The exercise answer was incorrect. Did you still want to submit it? (y/n): ')
            if str_in.lower() == 'y':
                db['submitted'][assignment] = True
                submitbad('exercise102.py',exercise102.__author__)
                str_in = input("Exercise submitted. Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
            else:
                print('Assignment was not submitted')
                str_in = input("Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
    elif assignment == '10.3':
        if exercise103.middle([1, 2, 3, 4]) == [2,3]:
            db['submitted'][assignment] = True
            submit('exercise103.py',exercise103.__author__)
            str_in = input("Exercise answer correct and submitted. Would you like to submit another? (y/n): ")
            if str_in.lower() == 'y':
                menu()
        else:
            str_in = input('The exercise answer was incorrect. Did you still want to submit it? (y/n): ')
            if str_in.lower() == 'y':
                db['submitted'][assignment] = True
                submitbad('exercise103.py',exercise103.__author__)
                str_in = input("Exercise submitted. Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
            else:
                print('Assignment was not submitted')
                str_in = input("Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
    elif assignment == '10.4':
        t = [1, 2, 3, 4]
        if exercise104.chop(t) == None and t == [2,3]:
            db['submitted'][assignment] = True
            submit('exercise104.py',exercise104.__author__)
            str_in = input("Exercise answer correct and submitted. Would you like to submit another? (y/n): ")
            if str_in.lower() == 'y':
                menu()
        else:
            str_in = input('The exercise answer was incorrect. Did you still want to submit it? (y/n): ')
            if str_in.lower() == 'y':
                db['submitted'][assignment] = True
                submitbad('exercise104.py',exercise104.__author__)
                str_in = input("Exercise submitted. Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
            else:
                print('Assignment was not submitted')
                str_in = input("Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
    elif assignment == '10.5':
        if exercise105.is_sorted([1, 2, 2]) and not exercise105.is_sorted(['b', 'a']):
            db['submitted'][assignment] = True
            submit('exercise105.py',exercise105.__author__)
            str_in = input("Exercise answer correct and submitted. Would you like to submit another? (y/n): ")
            if str_in.lower() == 'y':
                menu()
        else:
            str_in = input('The exercise answer was incorrect. Did you still want to submit it? (y/n): ')
            if str_in.lower() == 'y':
                db['submitted'][assignment] = True
                submitbad('exercise105.py',exercise105.__author__)
                str_in = input("Exercise submitted. Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
            else:
                print('Assignment was not submitted')
                str_in = input("Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
    elif assignment == '10.6':
        if exercise106.is_anagram('abba', 'baba') and not exercise106.is_anagram('lol', 'kol'):
            db['submitted'][assignment] = True
            submit('exercise106.py',exercise106.__author__)
            str_in = input("Exercise answer correct and submitted. Would you like to submit another? (y/n): ")
            if str_in.lower() == 'y':
                menu()
        else:
            str_in = input('The exercise answer was incorrect. Did you still want to submit it? (y/n): ')
            if str_in.lower() == 'y':
                db['submitted'][assignment] = True
                submitbad('exercise106.py',exercise106.__author__)
                str_in = input("Exercise submitted. Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
            else:
                print('Assignment was not submitted')
                str_in = input("Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()  
    elif assignment == '10.7':
        if exercise107.has_duplicates([4, 7, 2, 7, 3, 8, 9 ]) and not exercise107.has_duplicates(['b', 'd', 'a', 't']):
            db['submitted'][assignment] = True
            submit('exercise107.py',exercise107.__author__)
            str_in = input("Exercise answer correct and submitted. Would you like to submit another? (y/n): ")
            if str_in.lower() == 'y':
                menu()
        else:
            str_in = input('The exercise answer was incorrect. Did you still want to submit it? (y/n): ')
            if str_in.lower() == 'y':
                db['submitted'][assignment] = True
                submitbad('exercise107.py',exercise107.__author__)
                str_in = input("Exercise submitted. Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
            else:
                print('Assignment was not submitted')
                str_in = input("Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
    elif assignment == '10.9':
        fin = open("words.txt")
        li = []
        for line in fin:
            word = line.strip()
            li.append(word)
        if exercise109.version1("words.txt") == li and exercise109.version2("words.txt") == li:
            db['submitted'][assignment] = True
            submit('exercise109.py',exercise109.__author__)
            str_in = input("Exercise answer correct and submitted. Would you like to submit another? (y/n): ")
            if str_in.lower() == 'y':
                menu()
        else:
            str_in = input('The exercise answer was incorrect. Did you still want to submit it? (y/n): ')
            if str_in.lower() == 'y':
                db['submitted'][assignment] = True
                submitbad('exercise109.py',exercise109.__author__)
                str_in = input("Exercise submitted. Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
            else:
                print('Assignment was not submitted')
                str_in = input("Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
    elif assignment == '10.10':
        if exercise1010.in_bisect(['aa', 'alien', 'allen', 'zymurgy'], 'alien') == 1:
            db['submitted'][assignment] = True
            submit('exercise1010.py',exercise1010.__author__)
            str_in = input("Exercise answer correct and submitted. Would you like to submit another? (y/n): ")
            if str_in.lower() == 'y':
                menu()
        else:
            str_in = input('The exercise answer was incorrect. Did you still want to submit it? (y/n): ')
            if str_in.lower() == 'y':
                db['submitted'][assignment] = True
                submitbad('exercise1010.py',exercise1010.__author__)
                str_in = input("Exercise submitted. Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
            else:
                print('Assignment was not submitted')
                str_in = input("Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
    elif assignment == '10.11':
        fin = open("words.txt")
        li = []
        for line in fin:
            word = line.strip()
            li.append(word)
        if ['aa', 'aa'] in exercise1011.reverse_pair(li):
            db['submitted'][assignment] = True
            submit('exercise1011.py',exercise1011.__author__)
            str_in = input("Exercise answer correct and submitted. Would you like to submit another? (y/n): ")
            if str_in.lower() == 'y':
                menu()
        else:
            str_in = input('The exercise answer was incorrect. Did you still want to submit it? (y/n): ')
            if str_in.lower() == 'y':
                db['submitted'][assignment] = True
                submitbad('exercise1011.py',exercise1011.__author__)
                str_in = input("Exercise submitted. Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
            else:
                print('Assignment was not submitted')
                str_in = input("Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
    elif assignment == '10.12':
        fin = open("words.txt")
        li = []
        for line in fin:
            word = line.strip()
            li.append(word)
        if ['ah', 'as', 'aahs'] in exercise1012.interlock(li) and ['pee', 'ors', 'pi', 'poperies'] in exercise1012.three_way_interlock(li):
            db['submitted'][assignment] = True
            submit('exercise1012.py',exercise1012.__author__)
            str_in = input("Exercise answer correct and submitted. Would you like to submit another? (y/n): ")
            if str_in.lower() == 'y':
                menu()
        else:
            str_in = input('The exercise answer was incorrect. Did you still want to submit it? (y/n): ')
            if str_in.lower() == 'y':
                db['submitted'][assignment] = True
                submitbad('exercise1012.py',exercise1012.__author__)
                str_in = input("Exercise submitted. Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
            else:
                print('Assignment was not submitted')
                str_in = input("Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
    else:
        print('This should not have happened. Let your instructor know.')
    db.sync()
            
def submit(file,name):
    with open(file,'rb') as fin:
        assignment = fin.read()
        url = 'https://1402-answer-repo.s3.amazonaws.com/assignments/'+name+'/'+chapter+'/'+file
        req = urllib.request.Request(url.replace(' ',''), data=assignment, method='PUT')
        urllib.request.urlopen(req)

def submitbad(file,name):
    with open(file,'rb') as fin:
        assignment = fin.read()
        url = 'https://1402-answer-repo.s3.amazonaws.com/assignments/'+name+'/'+chapter+'/incorrect/'+file
        req = urllib.request.Request(url.replace(' ',''), data=assignment, method='PUT')
        urllib.request.urlopen(req)
            
def main():
    for exercise in exercises:
        if db['loaded'][exercise]:
            loadedList.append(exercise)
    
    print('The following exercises have been loaded: ' + ', '.join(loadedList) + '. Which would you like to grade?')
    menu()


main()

db.close()