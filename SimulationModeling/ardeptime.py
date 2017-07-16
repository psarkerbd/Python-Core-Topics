
from __future__ import print_function;

info = {
    'customer_no':[],
    'inter_arrival':[],
    'arrival':[],
    'service_durations':[],
    'departure':[]
}

# n = input('Enter number you want to take Inter arrival: ');
# print("Enter Inter arrival time:\n");

# for i in range(n):
#     x = input();
#     info['inter_arrival'] += [x];
    
# print("Enter Service durations:\n");

# for i in range(n):
#     x = input();
#     info['service_durations'] += [x];
    
# #print(info['inter_arrival'])

info['inter_arrival'] = [3, 3, 2, 1, 6, 2];
info['service_durations'] = [2, 4, 2, 2, 4, 3]

info['arrival'] += [info['inter_arrival'][0]];
info['departure'] += [info['inter_arrival'][0] + info['service_durations'][0]]

for i in range(1, len(info['inter_arrival'])):
    num = info['inter_arrival'][i] + info['arrival'][i-1];
    info['arrival'] += [num];
    if(info['departure'][i-1] > info['arrival'][i]):
        delay = info['departure'][i-1] - info['arrival'][i];
        delay += info['service_durations'][i] + info['arrival'][i];
    else:
        delay = info['arrival'][i] + info['service_durations'][i];
    info['departure'] += [delay];
#print(info['arrival']);
#print(info['departure']);