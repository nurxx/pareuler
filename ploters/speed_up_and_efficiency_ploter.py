import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (15,6)

speed_up = [1,539499/270889,539499/138477,539499/94115,539499/71571,539499/49249,539499/37735,539499/32145,539499/27833,539499/24540]
efficiency = [1,539499/270889/2,539499/138477/4,539499/94115/6,539499/71571/8,539499/49249/12,539499/37735/16,539499/32145/20,539499/27833/24,539499/24540/28]
ideal_speed_up = [1,2,4,6,8,12,16,20,24,28]
ideal_efficiency = [1,1,1,1,1,1,1,1,1,1]
server_threads = [1,2,4,6,8,12,16,20,24,28]

plt.subplot(1, 2, 1)
plt.plot(server_threads, speed_up, 'm', marker = 'o', markerfacecolor = 'red', label = 'S(n)')
plt.plot(server_threads, ideal_speed_up, 'y', marker = '*', markerfacecolor = 'green', label = 'Ideal S(n)')

plt.xlabel('Number of processes')
plt.ylabel('Speed-up')
plt.legend()
plt.title('Speed-up S(n)')


plt.subplot(1, 2, 2)
plt.plot(server_threads, efficiency, 'k', marker = 'o', markerfacecolor = 'yellow', label = 'E(n)')
plt.plot(server_threads, ideal_efficiency, 'b', marker = '*', markerfacecolor = 'cyan', label = 'Ideal E(n)')
plt.legend()

plt.xlabel('Number of processes')
plt.ylabel('Efficiency')
plt.title('Efficiency E(n)')
plt.show()