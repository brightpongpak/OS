import random
import math
# import 
import matplotlib.pyplot as plt


process_list1 = []
bust_time1 = []
process_list2 = []
bust_time2 = []
process_list3 = []
bust_time3 = []
map_process1 = {}
map_process2 = {}
map_process3 = {}
map_priority1 = {}
map_priority2 = {}
map_priority3 = {}
list_priority1 = []
list_priority2 = []
list_priority3 = []

def process1():
    for i in range(1,43):
        bust_time1.append(random.randint(2,8))
        process_list1.append(i)
    for i in range(43,55):
        bust_time1.append(random.randint(20,30))
        process_list1.append(i)     
    for i in range(55,61):
        bust_time1.append(random.randint(35,40))
        process_list1.append(i)
    random.shuffle(bust_time1)
    random.shuffle(process_list1)
    for i in range(0,60,1):
        map_process1[process_list1[i]] = bust_time1[i] 
    return map_process1

def process2():
    for i in range(1,13):
        bust_time2.append(random.randint(2,8))
        process_list2.append(i)
    for i in range(13,21):
        bust_time2.append(random.randint(20,30))
        process_list2.append(i)     
    for i in range(21,41):
        bust_time2.append(random.randint(35,40))
        process_list2.append(i)
    random.shuffle(bust_time2)
    random.shuffle(process_list2)
    for i in range(0,40,1):
        map_process2[process_list2[i]] = bust_time2[i] 
    return map_process2

def process3():
    for i in range(1,7):
        bust_time3.append(random.randint(2,8))
        process_list3.append(i)
    for i in range(7,12):
        bust_time3.append(random.randint(20,30))
        process_list3.append(i)     
    for i in range(12,21):
        bust_time3.append(random.randint(35,40))
        process_list3.append(i)
    random.shuffle(bust_time3)
    random.shuffle(process_list3)
    for i in range(0,20,1):
        map_process3[process_list3[i]] = bust_time3[i] 
    return map_process3


def priority1():
    for i in range(1,61):
        list_priority1.append(random.randint(1,20))
    random.shuffle(list_priority1)
    for i in range(0,60,1):
        map_priority1[i+1] = list_priority1[i]
    return map_priority1

def priority2():
    for i in range(1,41):
        list_priority2.append(random.randint(1,20))
    random.shuffle(list_priority2)
    for i in range(0,40,1):
        map_priority2[i+1] = list_priority2[i]
    return map_priority2

def priority3():
    for i in range(1,21):
        list_priority3.append(random.randint(1,20))
    random.shuffle(list_priority3)
    for i in range(0,20,1):
        map_priority3[i+1] = list_priority3[i]
    return map_priority3

def priorityScheduling1():
    map_Sequence = {}
    map_sorted = {}
    list_sorted = []
    list_value = []
    list_bus = []
    list_keyProcess = []
    waitTime = []
    list_ansBus = []
    for key,valueOfkey in sorted(priority1().items(), key = lambda item: item[1]):
        map_sorted[key] = valueOfkey
    for key,valueOfkey in map_sorted.items():
        list_sorted.append(key)
        list_value.append(valueOfkey)
    for key,valueOfkey in process1().items():
        list_keyProcess.append(key)
        list_bus.append(valueOfkey)
    for i in range(0,59,1):
        for j in range(0,59,1):
            if(list_keyProcess[i] == list_sorted[j]):
                list_ansBus.append(list_bus[i])
    for i in range(0,60,1):
        if(i == 0):
            waitTime.append(i)
        else:
            waitTime.append(waitTime[i-1]+list_value[i-1])
        # map_Sequence[i+1] = list_sorted[i]
    return waitTime

def priorityScheduling2():
    map_Sequence = {}
    map_sorted = {}
    list_sorted = []
    list_value = []
    list_bus = []
    list_keyProcess = []
    waitTime = []
    list_ansBus = []
    for key,valueOfkey in sorted(priority2().items(), key = lambda item: item[1]):
        map_sorted[key] = valueOfkey
    for key,valueOfkey in map_sorted.items():
        list_sorted.append(key)
        list_value.append(valueOfkey)
    for key,valueOfkey in process2().items():
        list_keyProcess.append(key)
        list_bus.append(valueOfkey)
    for i in range(0,39,1):
        for j in range(0,39,1):
            if(list_keyProcess[i] == list_sorted[j]):
                list_ansBus.append(list_bus[i])
    for i in range(0,40,1):
        if(i == 0):
            waitTime.append(i)
        else:
            waitTime.append(waitTime[i-1]+list_value[i-1])
        # map_Sequence[i+1] = list_sorted[i]
    return waitTime

def priorityScheduling3():
    map_Sequence = {}
    map_sorted = {}
    list_sorted = []
    list_value = []
    list_bus = []
    list_keyProcess = []
    waitTime = []
    list_ansBus = []
    for key,valueOfkey in sorted(priority3().items(), key = lambda item: item[1]):
        map_sorted[key] = valueOfkey
    for key,valueOfkey in map_sorted.items():
        list_sorted.append(key)
        list_value.append(valueOfkey)
    for key,valueOfkey in process3().items():
        list_keyProcess.append(key)
        list_bus.append(valueOfkey)
    for i in range(0,19,1):
        for j in range(0,19,1):
            if(list_keyProcess[i] == list_sorted[j]):
                list_ansBus.append(list_bus[i])
    for i in range(0,20,1):
        if(i == 0):
            waitTime.append(i)
        else:
            waitTime.append(waitTime[i-1]+list_value[i-1])
        # map_Sequence[i+1] = list_sorted[i]
    return waitTime


def FCFS():
    map_Sequence = {}
    list_key = []
    list_value = []
    waitTime = []
    for key,valueOfkey in process1().items():
        list_key.append(key)
        list_value.append(valueOfkey)
    for i in range(0,60,1):
        if(i == 0):
            waitTime.append(i)
        else:
            waitTime.append(waitTime[i-1]+list_value[i-1])
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
    list_value = []
    for key , valueOfkey in process1().items():
                map_data[key] = valueOfkey
                list_key.append(key)
                list_value.append(valueOfkey)
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


plt.plot(priorityScheduling1(), 'ro')
plt.plot(FCFS(), 'ro')
plt.plot(SJF(), 'ro')
plt.show()



