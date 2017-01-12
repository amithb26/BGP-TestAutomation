import pexpect
import getdata
import time
import execute
import Devices
import clear_buffer


def checking_operabilty(Device,command):
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
			#print 'flag =%d' % flag
			if flag==0 or flag==2:
				Dev.Login(Device,child)
				configs = """
				%s
				""" % (command)
				commands = configs.split('\n')
				execute.execute(child,commands)
			#	time.sleep(15)
				child.sendcontrol('m')
			#	print "BGP synchronization enabled in %s " % (Device)

			if flag == 1 or flag == 3:
				configs = """
				%s
				""" % (command)
				commands = configs.split('\n')
				execute.execute(child,commands)
			#	time.sleep(15)
				child.sendcontrol('m')
			#	print "BGP synchronization enabled in %s " % (Device)

			
			#else:
			#	print 'Expected prompt not found'

			return True
		
		else:
			return False


