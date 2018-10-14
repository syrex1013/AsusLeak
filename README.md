# AsusLeak        
Proof of Concept of AsusLeak Vulnerability.                   
**CVE-2018-18287**         

# How to use      

AsusLeak.py         
`python AsusLeak.py -ip 192.168.1.1`        
`192.168.1.X HOSTNAME`        
`192.168.1.X HOSTNAME`  
`Time data:`                
`Sun, 14 Oct 2018 12:44:06 +0200(317023 secs since boot)`                   

# How it works        

Main router login page 192.168.1.1/Main_Login.asp discloses DHCP leaf information giving ip and hostname of hosts in network.               
It also leaks current time and date which can help in identifying location.

# Router information        

Router: RT-AC58U
Vendor: ASUS
Firmware version: 3.0.0.4.380_6516
    
