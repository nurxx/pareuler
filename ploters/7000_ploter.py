import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (15,6)
#mac
mac_milliseconds = [427227, 215118, 111708, 79320, 66319, 50474]
mac_threads = [1,2,4,6,8,12]

#server
server_milliseconds = [539499,270889,138477,94115,71571,49249,37735,32145,27833,24540]
server_threads = [1,2,4,6,8,12,16,20,24,28]

plt.subplot(1, 2, 1)
plt.plot(mac_threads, mac_milliseconds, 'y', marker = 'o', markerfacecolor = 'black')

plt.xlabel('Number of processes')
plt.ylabel('Time in milliseconds')
plt.title('MacBook Pro')

plt.subplot(1, 2, 2)
plt.plot(server_threads, server_milliseconds, 'r', marker = '*', markerfacecolor = 'blue')

plt.xlabel('Number of processes')
plt.ylabel('Time in milliseconds')
plt.title('FMI Server')

plt.suptitle('7000 members')

plt.show()