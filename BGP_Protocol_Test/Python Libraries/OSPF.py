import pexpect
import getdata
import time
import execute
import Devices
import clear_buffer

class OSPF:


	
	def Configure_ospf(self,Device,process_id,Networks_connected,Area,Action):

		device_data = getdata.get_data()
		hostname = device_data['Device_Details'][Device]['Hostname']
		Dev = Devices.Devices()
		child = Dev.connect(Device)

		if (child):

			clear_buffer.flushBuffer(10,child)
			child.sendcontrol('m')
			child.sendcontrol('m')
			child.sendcontrol('m')
			flag = child.expect([hostname+'>',hostname+'#','Router\>','Router\#',pexpect.EOF,pexpect.TIMEOUT],timeout=50)
			if flag==0 or flag==2:
				Dev.Login(self,Device,child)
				if Action == 'enable':
					if (isinstance(Networks_connected,list)):
						for NID in Networks_connected:
								print NID
								configs = """
					 			configure terminal
								router ospf %s
								network %s area %s 
								exit
								exit
								""" % (process_id,NID,Area)
								commands = configs.split('\n')
								execute.execute(child,commands)
							
								child.sendcontrol('m')
		
						child.sendline('exit')
						child.sendcontrol('m')
			
					else:
						NID = Networks_connected
						configs = """
						configure terminal
						router ospf %s
						network %s area %s
						end
						""" % (process_id,NID,Area)
						commands = configs.split('\n')
						execute.execute(child,commands)
						child.sendcontrol('m')
			
				else:
					unconfig = """
					configure terminal
					no router ospf %s
					end 
					""" % (process_id,NID,Area)
					commands = configs.split('\n')
					execute.execute(child,commands)
					child.sendcontrol('m')
			
			if flag == 1 or flag == 3:
				if Action == 'enable':
					if (isinstance(Networks_connected,list)):
						for NID in Networks_connected:
								configs = """
								configure terminal
								router ospf %s
								network %s area %s 
								exit
								exit
								""" % (process_id,NID,Area)
								commands = configs.split('\n')
								execute.execute(child,commands)
								child.sendcontrol('m')
			
						child.sendline('exit')
						child.sendcontrol('m')
			
					else:
						NID = Networks_connected
						configs = """
						configure terminal
						router ospf %s
						network %s area %s
						end
						""" % (process_id,NID,Area)
						commands = configs.split('\n')
						execute.execute(child,commands)
						child.sendcontrol('m')
			

				else:
					unconfig = """
					configure terminal
					no router ospf %s
					end
					""" % (process_id,NID,Area)
					commands = configs.split('\n')
					execute.execute(child,commands)
					child.sendcontrol('m')
			
		        return True
		
		else:
			return False








