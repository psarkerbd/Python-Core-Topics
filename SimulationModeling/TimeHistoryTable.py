
from __future__ import print_function

# imported file will be on same directory 
# import ardeptime

from ardeptime import info

# file = open('Time History Table.py' , 'r');
# file.close;

# print info

# Time History Table
tht = {
    'event_no':[],
    'event_time':[],
    'event_type':[],
    'queue':[],
    'server_status':[]
}

numdtct = {};
altme = [];

# size take any one
size = len(info['arrival']);
#size = len(info['departure_time']);
#print size;
    
for i in range(size):
    tmp = info['departure'][i];
    numdtct.update({tmp: 'D'});
    altme.append(tmp);

for i in range(size):
    tmp = info['arrival'][i];
    numdtct.update({tmp: 'A'});
    altme.append(tmp);

# numdtct dictionary is already Sorted
    
#print(numdtct, end=' ');
#print('\n');

altme.append(0);

altme.sort();
#print(altme , end=' ');

#print(len(numdtct));

arr = 0;

tht['event_no'] += [1];
tht['event_time'] += [0];
tht['event_type'] += ['N'];
tht['queue'] += [0];
tht['server_status'] += ['Idle'];

for i in range(1 , len(altme)):
    tht['event_no'] += [i+1];
    curr = altme[i];
    tht['event_time'] += [curr];
    if(curr > 0):
        currtype = numdtct[curr];
    #print(curr , '->' , currtype, end='\n');
    if(currtype == 'A'):
        arr+=1;
        tht['event_type'] += ['A'];
    else:
        tht['event_type'] += ['D'];
        if(arr > 0):
            arr-=1;
        else:
            arr = 0;
    if(arr >= 1):
        tht['queue'] += [arr-1];
        tht['server_status'] += ['Busy'];
    else:
        tht['queue'] += [0];
        tht['server_status'] += ['Idle'];

#print(tht , end = '\n');

#print('Event no', '-'*3, 'Event time', '-'*3, 'Event type', '-'*3, 'Queue', '-'*3, 'Server status', end='\n');

# for i in range(len(tht['event_time'])):
#     print(tht['event_no'][i] , ' '*6 , '-'*3, tht['event_time'][i], ' '*9, '-'*3, tht['event_type'][i] , ' '*10, '-'*3,tht['queue'][i] , ' '*1, '-'*3, ' '*1, tht['server_status'][i] , end='\n')