import pexpect
import time

def execute(child,commands):
	cmds = commands
	flushedStuff=''
	while not child.expect([r'.+', pexpect.EOF,pexpect.TIMEOUT], timeout=5):
		flushedStuff += child.match.group(0)
	child.expect(['configure terminal',pexpect.EOF,pexpect.TIMEOUT],timeout=60)
	for cmd in cmds:
			child.send(cmd)
			child.sendcontrol('m')
			child.sendcontrol('m')
	child.expect(['exit',pexpect.EOF,pexpect.TIMEOUT],timeout=60)
	print child.before
	return
