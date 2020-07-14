import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (15,6)

#mac
mac_milliseconds = [27845, 14104, 7195, 4867, 3955, 2978]
mac_threads = [1,2,4,6,8,12]

#server
server_milliseconds = [36400,18259,9545,6540,4845,3342,2746,2358,2056,1857]
server_threads = [1,2,4,6,8,12,16,20,24,28]

plt.subplot(1, 2, 1)
plt.plot(mac_threads, mac_milliseconds, 'b', marker = 'o', markerfacecolor = 'cyan')

plt.xlabel('Number of processes')
plt.ylabel('Time in milliseconds')
plt.title('MacBook Pro')

plt.subplot(1, 2, 2)
plt.plot(server_threads, server_milliseconds, 'g', marker = '*', markerfacecolor = 'black')

plt.xlabel('Number of processes')
plt.ylabel('Time in milliseconds')
plt.title('FMI Server')

plt.suptitle('3000 members')

plt.show()