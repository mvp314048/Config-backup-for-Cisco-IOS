from netmiko import ConnectHandler
import getpass
import sys
import time

##getting system date
day=time.strftime('%d')
month=time.strftime('%m')
year=time.strftime('%Y')
today=day+"-"+month+"-"+year

##initialising device
device = {
    'device_type': 'cisco_ios',
    }

##opening IP file
ipfile=open("iplist.txt")
print ("Script to take backup of devices, Please enter your credential")
device['username']=input("username:")
device['password']=getpass.getpass()

##taking backup
for line in ipfile:
 try:
     device['ip']=line.strip("\n")
     print("\n\nConnecting Device ",line)
     net_connect = ConnectHandler(**device)
     net_connect.enable()
     time.sleep(1)
     print ("Reading the running config ")

     #cmd = ['sh lldp neighbor' , 'sh info']
     #output = net_connect.send_config_set(cmd, delay_factor=2)
     
     #output = net_connect.send.config_set(cmd)
     #connection.send_config_set(config_commands)
     #config_commands = ['sh info' + str(n)]
     #output = net_connect.send_command_set(commands)
     #output = send_show_command(device, ['sh info', 'sh lldp neighbor'])
          
     output = net_connect.send_command('sh ver')
     output2 = net_connect.send_command('sh run')
     
     #print(output + output2)

     time.sleep(3)
     filename=device['ip']+'-'+today+".txt"
     saveconfig=open(filename,'w+')
     print("Writing configuration to file...")
     saveconfig.write(output + output2)
     saveconfig.close()
     time.sleep(2)
     net_connect.disconnect()
     print ("Configuration saved to file",filename)
 except:
           print ("Access to "+device['ip']+" failed,backup did not taken")

ipfile.close()
print ("\nAll device backup completed")
