import pexpect

def flushBuffer(delay,child):
		try:
			child.expect("ZzqQJjSh_Impossible_String", timeout = delay)
		except pexpect.TIMEOUT:
			pass
		child.buffer = child.string_type()
		return child.before


	

		
