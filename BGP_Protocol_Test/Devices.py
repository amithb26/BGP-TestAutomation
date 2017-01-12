import pexpect
import getdata
import time
import execute
import sys
import clear_buffer


class Devices:

	def connect(self,Device):

		device_data = getdata.get_data()
		IP_add = device_data['Device_Details'][Device]['ip_add']
		Port_no = device_data['Device_Details'][Device]['port']
		Password = device_data['Device_Details'][Device]['pwd']	
		hostname = device_data['Device_Details'][Device]['Hostname']
		child = pexpect.spawn('telnet ' + IP_add + ' ' + Port_no)
		child.sendcontrol('m')
		child.sendcontrol('m')
		clear_buffer.flushBuffer(5,child)
		child.sendcontrol('m')
		child.sendcontrol('m')		
		child.sendcontrol('m')
		flag = child.expect(['Router>','Router#',hostname+'>',hostname+'#',pexpect.EOF,pexpect.TIMEOUT],timeout=50)
		

		if (flag == 0 or flag == 1  or flag == 2  or flag == 3):
		       
			
			self.Login(Device,child)

		if flag == 4:
			
			return False

		if flag == 5:
			
			self.connect(Device)

		return child
		
	def Login(self,Device,child):
			
		child.sendcontrol('m')
		device_data = getdata.get_data()
		hostname = device_data['Device_Details'][Device]['Hostname']
		Password = device_data['Device_Details'][Device]['pwd']
		clear_buffer.flushBuffer(5,child)
		child.sendcontrol('m')
		flag = child.expect(['Router>','Router#',hostname+'>',hostname+'#',pexpect.EOF,pexpect.TIMEOUT],timeout=50)
		
		if flag == 0 or flag == 2:
			child.send('enable')
			child.sendcontrol('m')
			
			child.send(Password)
			child.sendcontrol('m')
			clear_buffer.flushBuffer(5,child)
			child.sendcontrol('m')
			child.sendcontrol('m')
			child.sendcontrol('m')
			flag1 = child.expect([hostname+'>',hostname+'#','Router#',pexpect.EOF,pexpect.TIMEOUT],timeout=50)
		
			if flag1 == 0:
				self.Login(Device,child)

		return


	def set_IP(self,Device,Links,Action):
		
		child = self.connect(Device)

		if (child):
			device_data = getdata.get_data()
			hostname = device_data['Device_Details'][Device]['Hostname']
			clear_buffer.flushBuffer(5,child)
			child.sendcontrol('m')
			flag = child.expect([hostname+'>',hostname+'#','Router\>','Router\#',pexpect.EOF,pexpect.TIMEOUT],timeout=50)		
			print 'flag=%d' % flag

			if (flag == 4 or flag == 5):
				print "Expected prompt not present"
				child.sendcontrol('m')
		
			if (flag == 0 or flag == 2):
				self.Login(Device,child)
				flag=1


			if (flag == 1 or flag == 3):

				if Action == 'configure':

					if (isinstance(Links,list)):

						for Lnk in Links:

							interface = device_data['Link_Details'][Lnk][Device]
							interface_add = device_data['Device_Details'][Device][interface]
							configs = """	
							configure terminal
							interface %s
							ip address %s 
							no shutdown				
							exit
							exit
							""" % (interface,interface_add)
							commands = configs.split('\n')
							execute.execute(child,commands)
							child.sendcontrol('m')
							
					else:
						interface = device_data['Link_Details'][Lnk][Device]
						interface_add = device_data['Device_Details'][Device][interface]
						configs = """ 	
						configure terminal
						interface %s
						ip address %s 
						no shutdown					
						exit
						exit
						""" % (interface,interface_add)
						commands = configs.split('\n')
						execute.execute(child,commands)
						child.sendcontrol('m')
						child.sendline('exit')
					        child.sendcontrol('m')
					
				else:
					if (isinstance(Links,list)):

						for Link in Links:

							interface = device_data['Link_Details'][Link][Device]
							interface_add = device_data['Device_Details'][Device][interface]
							unconfig = """ 	
							configure terminal
							interface %s
							no ip address %s 
							shutdown					
							exit
							exit
							""" % (interface,interface_add)
							commands = unconfig.split('\n')
							execute.execute(child,commands)
							child.sendline('exit')
							child.sendcontrol('m')
		
					else:
						interface = device_data['Link_Details'][Link][Device]
						interface_add = device_data['Device_Details'][Device][interface]
						unconfig = """ 	
						configure terminal
						interface %s
						no ip address %s 
						shutdown					
						exit
						exit
						""" % (interface,interface_add)
						commands = unconfig.split('\n')
						execute.execute(child,commands)
						child.sendcontrol('m')
		
			return True
		else:	
			
			return False
	
	def set_loopback(self,Device,Action):

		device_data = getdata.get_data()
		hostname = device_data['Device_Details'][Device]['Hostname']
		ip_add = device_data['Device_Details'][Device]["ip_add"]
		child = self.connect(Device)
		if child != False:
			clear_buffer.flushBuffer(5,child)
			child.sendcontrol('m')
			child.sendcontrol('m')
			child.sendcontrol('m')
			child.expect([hostname+'\#',pexpect.EOF,pexpect.TIMEOUT],timeout=60)
			child.sendcontrol('m')
			LO_interface_add = device_data['Device_Details'][Device]['lo']
			if Action == 'set':
			
				configs = """
					configure terminal
					interface %s
					ip address %s 					
					end
					exit
					""" % ('loopback0',LO_interface_add)
				commands = configs.split('\n')
				execute.execute(child,commands)
				child.sendcontrol('m')
		
			else:
				unconfig = """ 	
					configure terminal
					interface %s
					ip address 127.0.0.1 255.255.255.255
					end
					exit
					""" % ('loopback0')
				commands = unconfig.split('\n')
				execute.execute(child,commands)
				child.sendcontrol('m')
				child.sendcontrol('m')
				
 			return True 
		else:
			return False

			
	
	

		


		
dev =  Devices()

