from ipaddress import ip_network

net = ip_network('172.16.160.0/255.255.240.0', 0)

k = 0
for ip in net:
    bin_ip = bin(int(str(ip).replace('.', '')))[2:]
    cnt_1 = bin_ip.count('1')
    
    if cnt_1 % 2 == 0:
        k += 1
print(k)
