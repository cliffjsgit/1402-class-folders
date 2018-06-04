#!/usr/bin/env python3

import shelve

exercises = ['91','92','93','94','95','96','97','98']
loadedList = []
db = shelve.open('chapter9.db', flag='c', writeback=True)
db['loaded'] = {}

try:
    import exercise91
    db['loaded']['91'] = True
except:
    db['loaded']['91'] = False
try:
    import exercise92
    db['loaded']['92'] = True
except:
    db['loaded']['92'] = False
try:
    import exercise93
    db['loaded']['93'] = True
except:
    db['loaded']['93'] = False
try:
    import exercise94
    db['loaded']['94'] = True
except:
    db['loaded']['94'] = False
try:
    import exercise95
    db['loaded']['95'] = True
except:
    db['loaded']['95'] = False
try:
    import exercise96
    db['loaded']['96'] = True
except:
    db['loaded']['96'] = False
try:
    import exercise97
    db['loaded']['97'] = True
except:
    db['loaded']['97'] = False
try:
    import exercise98
    db['loaded']['98'] = True
except:
    db['loaded']['98'] = False
    
db.sync()

for exercise in exercises:
    if db['loaded'][exercise]:
        loadedList.append(exercise)

db.close()

print(loadedList)