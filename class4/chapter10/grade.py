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
        if exercise103.avoids('feel','k') and sorted(exercise103.lowest_avoidance()) == sorted(['q', 'j', 'x', 'z', 'w']):
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
        if exercise104.uses_only('hello',['h','e','l','o','p']):
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
        if exercise105.answer2 == 42 and exercise105.uses_all('hello',['h','e','l','o']):
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
        if exercise106.is_abecedarian('abbcdef') and not exercise106.is_abecedarian('cndsfsd'):
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
        if 'bookkeeper' in exercise107.results:
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
    elif assignment == '10.8':
        if sorted(exercise108.results) == sorted([198888, 199999]):
            db['submitted'][assignment] = True
            submit('exercise108.py',exercise108.__author__)
            str_in = input("Exercise answer correct and submitted. Would you like to submit another? (y/n): ")
            if str_in.lower() == 'y':
                menu()
        else:
            str_in = input('The exercise answer was incorrect. Did you still want to submit it? (y/n): ')
            if str_in.lower() == 'y':
                db['submitted'][assignment] = True
                submitbad('exercise108.py',exercise108.__author__)
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