import pexpect
import getdata
import time
import execute
import Devices
import clear_buffer

class IBGP:

	def Configure_IBGP(self,Device,AS_id,Interface,Action):

		device_data = getdata.get_data()
		hostname = device_data['Device_Details'][Device]['Hostname']
		Dev = Devices.Devices()
		child = Dev.connect(Device)

		if (child):

			clear_buffer.flushBuffer(10,child)
			child.sendcontrol('m')
			child.sendcontrol('m')
			child.sendcontrol('m')
			flag = child.expect([hostname+'>',hostname+'#','Router\>','Router\#',pexpect.EOF,pexpect.TIMEOUT],timeout=90)
			if flag==0 or flag==2:
				Dev.Login(Device,child)
				if Action == 'enable':
					if (isinstance(Interface,list)):
						for interface in Interface:
								configs = """
								configure terminal
								router bgp %d
								neighbor %s remote-as %d
								neighbor %s update-source loopback 0
								exit
								exit
								""" % (AS_id,interface,AS_id,interface)
								commands = configs.split('\n')
								execute.execute(child,commands)
								time.sleep(6)
								child.sendcontrol('m')
						child.sendline('exit')
						child.sendcontrol('m')
						
					else:
						interface = Interface
						configs = """
						configure terminal
						router bgp %d
						neighbor %s remote-as %d
						neighbor %s update-source loopback 0
						exit
						exit
						""" % (AS_id,interface,AS_id,interface)
						commands = configs.split('\n')
						execute.execute(child,commands)
						child.sendcontrol('m')
			
					

				else:
					unconfig = """
					configure terminal
					no router bgp %d
					exit
					exit
					""" % (AS_id)
					commands = configs.split('\n')
					execute.execute(child,commands)
					child.sendcontrol('m')
			

		
			if flag == 1 or flag == 3:
				if Action == 'enable':
					if (isinstance(Interface,list)):
						for interface in Interface:
								print interface
								configs = """
								configure terminal
								router bgp %d
								neighbor %s remote-as %d
								neighbor %s update-source loopback 0
								exit
								exit
								""" % (AS_id,interface,AS_id,interface)
								commands = configs.split('\n')
								execute.execute(child,commands)
								time.sleep(6)
								child.sendcontrol('m')
						child.sendline('exit')
						child.sendcontrol('m')
						
					else:
						interface = Interface
						configs = """
						configure terminal
						router bgp %d
						neighbor %s remote-as %d
						neighbor %s update-source loopback 0
						exit
						exit
						exit
						""" % (AS_id,interface,AS_id,interface)
						commands = configs.split('\n')
						execute.execute(child,commands)
						child.sendcontrol('m')

				else:
					unconfig = """
					configure terminal
					no router bgp %d
					exit
					exit
					""" % (AS_id)
					commands = configs.split('\n')
					execute.execute(child,commands)
					child.sendcontrol('m')

		        return True
		
		else:
			return False


	def enable_syn(self,Device,AS_id):
		
		
		device_data = getdata.get_data()
		hostname = device_data['Device_Details'][Device]['Hostname']
		Dev = Devices.Devices()
		child = Dev.connect(Device)
		if (child):

			clear_buffer.flushBuffer(10,child)
			child.sendcontrol('m')
			child.sendcontrol('m')
			child.sendcontrol('m')
			flag = child.expect([hostname+'>',hostname+'#','Router\>','Router\#',pexpect.EOF,pexpect.TIMEOUT],timeout=90)
			if flag==0 or flag==2:
				Dev.Login(Device,child)
				configs = """
				configure terminal
				router bgp %d
				synchronization
				end
				""" % (AS_id)
				commands = configs.split('\n')
				execute.execute(child,commands)
				child.sendcontrol('m')
			

			if flag == 1 or flag == 3:
				configs = """
				configure terminal
				router bgp %d
				synchronization
				end
				""" % (AS_id)
				commands = configs.split('\n')
				execute.execute(child,commands)
				child.sendcontrol('m')

			return True
		
		else:
			return False







	def Configure_EBGP(self,Device,AS_id,Interface,neighbor_AS_id,Action):

		device_data = getdata.get_data()
		hostname = device_data['Device_Details'][Device]['Hostname']
		Dev = Devices.Devices()
		child = Dev.connect(Device)

		if (child):

			clear_buffer.flushBuffer(10,child)
			child.sendcontrol('m')
			child.sendcontrol('m')
			child.sendcontrol('m')
			flag = child.expect([hostname+'>',hostname+'#','Router\>','Router\#',pexpect.EOF,pexpect.TIMEOUT],timeout=90)
			if flag==0 or flag==2:
				Dev.Login(Device,child)
				if Action == 'enable':
					if (isinstance(Interface,list)):
						for interface in Interface:
								configs = """
								configure terminal
								router bgp %d
								neighbor %s remote-as %d
								exit
								exit
								""" % (AS_id,interface,neighbor_AS_id)
								commands = configs.split('\n')
								execute.execute(child,commands)
								time.sleep(6)
								child.sendcontrol('m')
						child.sendline('exit')
						child.sendcontrol('m')
						
					else:
						interface = Interface
						configs = """
						configure terminal
						router bgp %d
						neighbor %s remote-as %d
						exit
						exit
						""" % (AS_id,interface,neighbor_AS_id)
						commands = configs.split('\n')
						execute.execute(child,commands)
						child.sendcontrol('m')
			
				else:
					unconfig = """
					configure terminal
					no router bgp %d
					exit
					exit
					""" % (AS_id)
					commands = configs.split('\n')
					execute.execute(child,commands)
					child.sendcontrol('m')
			
			if flag == 1 or flag == 3:
				if Action == 'enable':
					if (isinstance(Interface,list)):
						for interface in Interface:
			
								configs = """
								configure terminal
								router bgp %d
								neighbor %s remote-as %d
								exit
								exit
								""" % (AS_id,interface,neighbor_AS_id)
								commands = configs.split('\n')
								execute.execute(child,commands)
								child.sendcontrol('m')
						child.sendline('exit')
						child.sendcontrol('m')
						
					else:
						interface = Interface
						configs = """
						configure terminal
						router bgp %d
						neighbor %s remote-as %d
						exit
						exit
						""" % (AS_id,interface,neighbor_AS_id)
						commands = configs.split('\n')
						execute.execute(child,commands)
						child.sendcontrol('m')
			
				else:
					unconfig = """
					configure terminal
					no router bgp %d
					exit
					exit
					""" % (AS_id)
					commands = configs.split('\n')
					execute.execute(child,commands)
					child.sendcontrol('m')
			
		        return True
		
		else:
			return False


	def advertising_loopback(self,Device,AS_id,Interface,mask):
		device_data = getdata.get_data()
		hostname = device_data['Device_Details'][Device]['Hostname']
		Dev = Devices.Devices()
		child = Dev.connect(Device)
		if (child):

			clear_buffer.flushBuffer(10,child)
			child.sendcontrol('m')
			child.sendcontrol('m')
			child.sendcontrol('m')
			flag = child.expect([hostname+'>',hostname+'#','Router\>','Router\#',pexpect.EOF,pexpect.TIMEOUT],timeout=90)
			if flag==0 or flag==2:
				Dev.Login(Device,child)
				configs = """
				configure terminal
				router bgp %d
				network %s mask %s
				end
				""" % (AS_id,Interface,mask)
				commands = configs.split('\n')
				execute.execute(child,commands)
				child.sendcontrol('m')
			

			if flag == 1 or flag == 3:
				configs = """
				configure terminal
				router bgp %d
				network %s mask %s
				end
				""" % (AS_id,Interface,mask)
				commands = configs.split('\n')
				execute.execute(child,commands)
				child.sendcontrol('m')
			
			return True
		
		else:
			return False



	def redistribution(self,Device,AS_id,Process_id):
		 
		device_data = getdata.get_data()
		hostname = device_data['Device_Details'][Device]['Hostname']
		Dev = Devices.Devices()
		child = Dev.connect(Device)
		if (child):

			clear_buffer.flushBuffer(10,child)
			child.sendcontrol('m')
			child.sendcontrol('m')
			child.sendcontrol('m')
			flag = child.expect([hostname+'>',hostname+'#','Router\>','Router\#',pexpect.EOF,pexpect.TIMEOUT],timeout=90)
			if flag==0 or flag==2:
				Dev.Login(Device,child)
				configs = """
				configure terminal
				router ospf %d
				redistribute bgp %d subnets
				end
				""" % (Process_id,AS_id)
				commands = configs.split('\n')
				execute.execute(child,commands)
				child.sendcontrol('m')
			
			if flag == 1 or flag == 3:
				configs = """
				configure terminal
				router ospf %d
				redistribute bgp %d subnets
				end
				""" % (Process_id,AS_id)
				commands = configs.split('\n')
				execute.execute(child,commands)
				child.sendcontrol('m')
		
			return True
		
		else:
			return False


	def route(self,Device,AS_id,Interface):
		
		device_data = getdata.get_data()
		hostname = device_data['Device_Details'][Device]['Hostname']
		Dev = Devices.Devices()
		child = Dev.connect(Device)
		if (child):

			clear_buffer.flushBuffer(10,child)
			child.sendcontrol('m')
			child.sendcontrol('m')
			child.sendcontrol('m')
			flag = child.expect([hostname+'>',hostname+'#','Router\>','Router\#',pexpect.EOF,pexpect.TIMEOUT],timeout=90)
			if flag==0 or flag==2:
				Dev.Login(Device,child)
				configs = """
				configure terminal
				router bgp %d
				neighbor %s next-hop-self
				end
				""" % (AS_id,Interface)
				commands = configs.split('\n')
				execute.execute(child,commands)
				child.sendcontrol('m')
			

			if flag == 1 or flag == 3:
				configs = """
				configure terminal
				router bgp %d
				neighbor %s next-hop-self
				end
				""" % (AS_id,Interface)
				commands = configs.split('\n')
				execute.execute(child,commands)
				child.sendcontrol('m')
			
			return True
		
		else:
			return False





		




				

