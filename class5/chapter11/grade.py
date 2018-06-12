#!/usr/bin/env python3

import shelve
import urllib.request

chapter = "11"
exercises = ['11.1','11.2','11.3','11.4','11.5','11.6']
loadedList = []
db = shelve.open('chapter11.db', flag='c', writeback=True)
db['loaded'] = {}
if 'submitted' not in db:
    db['submitted'] = {}

try:
    import exercise111
    db['loaded']['11.1'] = True
except:
    db['loaded']['11.1'] = False
try:
    import exercise112
    db['loaded']['11.2'] = True
except:
    db['loaded']['11.2'] = False
try:
    import exercise113
    db['loaded']['11.3'] = True
except:
    db['loaded']['11.3'] = False
try:
    import exercise114
    db['loaded']['11.4'] = True
except:
    db['loaded']['11.4'] = False
try:
    import exercise115
    db['loaded']['11.5'] = True
except:
    db['loaded']['11.5'] = False
try:
    import exercise116
    db['loaded']['11.6'] = True
except:
    db['loaded']['11.6'] = False


db.sync()

def menu():
    while True:
        for exercise in loadedList:
            if exercise in db['submitted']:
                print('[x] Exercise ' + exercise)
            else:
                print('[ ] Exercise ' + exercise)
        print('    Enter q to exit')
        str_in = input('Exercise (e.g. 11.1): ')
        if str_in in loadedList:
            grade(str_in)
            break
        elif str_in.lower() == 'q':
            break
        else:
            print('Incorrect response. Only enter the exercise number. Example: "11.1" (no quotes).')
            
def grade(assignment):
    if assignment == '11.1':
        if "cattle" in exercise111.make_dict("words.txt"):
            db['submitted'][assignment] = True
            submit('exercise111.py',exercise111.__author__)
            str_in = input("Exercise answer correct and submitted. Would you like to submit another? (y/n): ")
            if str_in.lower() == 'y':
                menu()
        else:
            str_in = input('The exercise answer was incorrect. Did you still want to submit it? (y/n): ')
            if str_in.lower() == 'y':
                db['submitted'][assignment] = True
                submitbad('exercise111.py',exercise111.__author__)
                str_in = input("Exercise submitted. Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
            else:
                print('Assignment was not submitted')
                str_in = input("Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
    elif assignment == '11.2':
        id = exercise112.invert_dict({1:2,3:4})
        if 2 in id and 4 in id:
            db['submitted'][assignment] = True
            submit('exercise112.py',exercise112.__author__)
            str_in = input("Exercise answer correct and submitted. Would you like to submit another? (y/n): ")
            if str_in.lower() == 'y':
                menu()
        else:
            str_in = input('The exercise answer was incorrect. Did you still want to submit it? (y/n): ')
            if str_in.lower() == 'y':
                db['submitted'][assignment] = True
                submitbad('exercise112.py',exercise112.__author__)
                str_in = input("Exercise submitted. Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
            else:
                print('Assignment was not submitted')
                str_in = input("Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
    elif assignment == '11.3':
        if exercise113.ackermann(3, 4) == 125:
            db['submitted'][assignment] = True
            submit('exercise113.py',exercise113.__author__)
            str_in = input("Exercise answer correct and submitted. Would you like to submit another? (y/n): ")
            if str_in.lower() == 'y':
                menu()
        else:
            str_in = input('The exercise answer was incorrect. Did you still want to submit it? (y/n): ')
            if str_in.lower() == 'y':
                db['submitted'][assignment] = True
                submitbad('exercise113.py',exercise113.__author__)
                str_in = input("Exercise submitted. Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
            else:
                print('Assignment was not submitted')
                str_in = input("Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
    elif assignment == '11.4':
        t = [1, 2, 3, 4]
        if exercise114.has_duplicates([1,2,3,3]) == True:
            db['submitted'][assignment] = True
            submit('exercise114.py',exercise114.__author__)
            str_in = input("Exercise answer correct and submitted. Would you like to submit another? (y/n): ")
            if str_in.lower() == 'y':
                menu()
        else:
            str_in = input('The exercise answer was incorrect. Did you still want to submit it? (y/n): ')
            if str_in.lower() == 'y':
                db['submitted'][assignment] = True
                submitbad('exercise114.py',exercise114.__author__)
                str_in = input("Exercise submitted. Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
            else:
                print('Assignment was not submitted')
                str_in = input("Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
    elif assignment == '11.5':
        if "ad" in exercise115.rotate_pair("words.txt"):
            db['submitted'][assignment] = True
            submit('exercise115.py',exercise115.__author__)
            str_in = input("Exercise answer correct and submitted. Would you like to submit another? (y/n): ")
            if str_in.lower() == 'y':
                menu()
        else:
            str_in = input('The exercise answer was incorrect. Did you still want to submit it? (y/n): ')
            if str_in.lower() == 'y':
                db['submitted'][assignment] = True
                submitbad('exercise115.py',exercise115.__author__)
                str_in = input("Exercise submitted. Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
            else:
                print('Assignment was not submitted')
                str_in = input("Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
    elif assignment == '11.6':
        if "llama" in exercise116.find_homophones("words.txt"):
            db['submitted'][assignment] = True
            submit('exercise116.py',exercise116.__author__)
            str_in = input("Exercise answer correct and submitted. Would you like to submit another? (y/n): ")
            if str_in.lower() == 'y':
                menu()
        else:
            str_in = input('The exercise answer was incorrect. Did you still want to submit it? (y/n): ')
            if str_in.lower() == 'y':
                db['submitted'][assignment] = True
                submitbad('exercise116.py',exercise116.__author__)
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