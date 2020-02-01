import random
import math
# import 
import matplotlib.pyplot as plt


process_list = []
bust_time = []
map_process = {}
map_priority = {}
list_priority = []

def process1():
    for i in range(1,43):
        bust_time.append(random.randint(2,8))
        process_list.append(i)
    for i in range(43,55):
        bust_time.append(random.randint(20,30))
        process_list.append(i)     
    for i in range(55,61):
        bust_time.append(random.randint(35,40))
        process_list.append(i)
    random.shuffle(bust_time)
    random.shuffle(process_list)
    for i in range(0,60,1):
        map_process[process_list[i]] = bust_time[i] 
    return map_process

def priority():
    for i in range(1,61):
        list_priority.append(random.randint(1,20))
    random.shuffle(list_priority)
    for i in range(0,60,1):
        map_priority[i+1] = list_priority[i]
    return map_priority

def priorityScheduling():
    map_Sequence = {}
    map_sorted = {}
    list_sorted = []
    lsit_value = []
    waitTime = []
    for key,valueOfkey in sorted(priority().items(), key = lambda item: item[1]):
        map_sorted[key] = valueOfkey
    for key,valueOfkey in map_sorted.items():
        list_sorted.append(key)
        lsit_value.append(valueOfkey)
    for i in range(0,60,1):
        if(i == 0):
            waitTime.append(i)
        else:
            waitTime.append(waitTime[i-1]+lsit_value[i-1])
        # map_Sequence[i+1] = list_sorted[i]
    return waitTime

def FCFS():
    map_Sequence = {}
    list_key = []
    lsit_value = []
    waitTime = []
    for key,valueOfkey in process1().items():
        list_key.append(key)
        lsit_value.append(valueOfkey)
    for i in range(0,60,1):
        if(i == 0):
            waitTime.append(i)
        else:
            waitTime.append(waitTime[i-1]+lsit_value[i-1])
        # map_Sequence[i+1] = list_key[i]
    return waitTime

def SJF():
    map_Sequence = {}   
    map_sorted = {}
    list_sorted = []
    list_value = []
    waitTime = []
    for key,valueOfkey in sorted(process1().items(), key = lambda item: item[1]):
        map_sorted[key] = valueOfkey
    for key,valueOfkey in map_sorted.items():
        list_sorted.append(key)
        list_value.append(valueOfkey)
    for i in range(0,60,1):
        if(i == 0):
            waitTime.append(i)
        else:
            waitTime.append(waitTime[i-1]+list_value[i-1])
        # map_Sequence[i+1] = list_sorted[i]
    return waitTime

def RR():
    map_Sequence = {}
    list_completeKey = []
    map_data = {}
    waitTime = []
    list_key = []
    lsit_value = []
    for key , valueOfkey in process1().items():
                map_data[key] = valueOfkey
                list_key.append(key)
                lsit_value.append(valueOfkey)
    while 1:
        checking = []
        if(len(list_completeKey) != 60):
            for key , valueOfkey in map_data.items():
                map_data[key] = valueOfkey - 4
                if(map_data.get(key) <= 0):
                    list_completeKey.append(key)
                    checking.append(key)
            if(checking != []):
                for key in checking:
                    del map_data[key]
        else:
            break
    for i in range(0,60,1):
        map_Sequence[i+1] = list_completeKey[i]
    return map_Sequence


# plt.plot(priorityScheduling(), 'ro')
# plt.plot(FCFS(), 'ro')
# plt.plot(SJF(), 'ro')
# plt.show()





def info():
    ans = ((7/14)*(-(6/7)*math.log2(6/7))+((-1/7)*math.log2(1/7)))((7/14)*((-3/7)*math.log2(3/7))+((-4/7)*math.log2(4/7)))
    return ans

print(info())