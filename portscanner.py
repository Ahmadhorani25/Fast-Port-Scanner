import concurrent.futures
import socket

target_ip = "127.0.0.1"
def port_scan(portnum): #Here is the scanning process
    s=socket.socket(socket.AF_INET , socket.SOCK_STREAM) #Setting that ipv4 is used and using TCP
    s.settimeout(0.5) #Socket connection timeout 0.5 second for each scan
    result=s.connect_ex((target_ip, portnum)) #Checking if port is open if open result = 0
    if result==0:
        print(f"Port {portnum} is open")
    s.close()

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor: #This is the tool in which it maximizes the speed of the code execution by scanning 100 ports in parallel;
    executor.map(port_scan, range(1, 1025))