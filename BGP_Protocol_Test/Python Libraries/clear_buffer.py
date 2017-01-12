import pexpect






def flushBuffer(delay,child):
		try:# Greedily read in all the incoming characters
			child.expect("ZzqQJjSh_Impossible_String", timeout = delay)
		except pexpect.TIMEOUT:
			pass
		# Clear local input buffer inside the spawn Class
		child.buffer = child.string_type()
		return child.before


	

		
