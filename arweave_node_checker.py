import requests
import json
from datetime import datetime
import time

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

starttime = time.time()
nodes_list = open('nodes.txt').read().split('\n')
nodes_count = int(len(nodes_list)/2)
i = 0
n = 1

print("=========================================================================")
print("Imported nodes:", nodes_count)
print("=========================================================================")

while True:
    while nodes_count > 0:
        node_ip = 'http://' + nodes_list[i] + ':1984'
        node_wallet = 'http://' + nodes_list[i] + ':1984' + '/wallet/' + nodes_list[i+1] + '/balance'
        node_info = json.loads(requests.get(node_ip).text)
        node_balance = requests.get(node_wallet)
        print("Node", n, "info:")
        print("IP:", nodes_list[i])
        print("Height:", node_info['height'])
        print("Current:", node_info['current'])
        print("Blocks:", node_info['blocks'])
        print("Peers:", node_info['peers'])
        print("Latency:", node_info['node_state_latency']/1000, "ms")
        print("Wallet:", nodes_list[i+1])
        print("Balance:", toFixed(node_balance.json()/1000000000000,5), "AR")
        print("-------------------------------------------------------------------------")
        nodes_count -= 1
        i += 2
        n += 1
    
    update = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("Last update:", update)
    print("=========================================================================")
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))
    nodes_list = open('nodes.txt').read().split('\n')
    nodes_count = int(toFixed(len(nodes_list)/2,0))
    i = 0
    n = 1
