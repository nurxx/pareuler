import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (15,6)

#mac
mac_milliseconds = [145185, 73237, 37126, 25131, 20536, 15156]
mac_threads = [1,2,4,6,8,12]

#server
server_milliseconds = [188440,93894,48133,32997,26291,16877,13380,11383,9879,9091]
server_threads = [1,2,4,6,8,12,16,20,24,28]

plt.subplot(1, 2, 1)
plt.plot(mac_threads, mac_milliseconds, 'm', marker = 'o', markerfacecolor = 'yellow')

plt.xlabel('Number of processes')
plt.ylabel('Time in milliseconds')
plt.title('MacBook Pro')

plt.subplot(1, 2, 2)
plt.plot(server_threads, server_milliseconds, 'k', marker = '*', markerfacecolor = 'red')

plt.xlabel('Number of processes')
plt.ylabel('Time in milliseconds')
plt.title('FMI Server')

plt.suptitle('5000 members')

plt.show()