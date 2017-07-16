
from __future__ import print_function;

from TimeHistoryTable import altme, tht, numdtct

# print(altme , end='\n');
# print(tht, end='\n');

simstats = {
    'inter_event_time':[],
    'customer_queue':[],
    'server_uti':[]
}

for i in range(1 , len(altme)):
    x = altme[i];
    y = altme[i-1];
    diff = x - y;
    simstats['inter_event_time'] += [diff];
    simstats['customer_queue'] += [diff * tht['queue'][i-1]];
    if(tht['server_status'][i-1] == 'Busy'):
        simstats['server_uti'] += [diff * 1]
    else:
        simstats['server_uti'] += [diff * 0]

total = {};

# for key,list in dict.items()
for key,lis in simstats.items():
    total[key] = sum(lis);
#print(total)

print('Inter Event Time', '-'*2 , 'Customer Queue', '-'*2 , 'Server Utilization', end='\n');

for i in range(len(simstats['inter_event_time'])):
    print(simstats['inter_event_time'][i], ' '*14 , '-'*2, simstats['customer_queue'][i], ' '*12 , '-'*2, simstats['server_uti'][i], end='\n')
    
print('-'*40, '\n' ,total['inter_event_time'], ' '*15 , total['customer_queue'], ' '*15 , total['server_uti'])

#print('Inter Event Time = ', total['inter_event_time'], '\n', 'Customer Queue = ', total['customer_queue'], '\n', 'Server Utilization', total['server_uti']);