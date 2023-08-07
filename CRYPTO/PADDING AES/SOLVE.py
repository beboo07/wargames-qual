from pwn import *
import string
z=string.printable
#34.154.18.2 6953 
def encrypt(ct):

	r = remote("34.154.18.2", 6953)
	r.recvuntil(b'>')
	r.sendline(ct)
	return r.recvuntil(b'\n')
flag='ASCWG{'
while flag[-1] !='}':
	
	le=encrypt(flag.encode())
	l=len(le)
	g=flag
	for i in z:
		send=g+i
		cl=len(encrypt(send.encode()))
		if cl==l:
			flag+=i
			print(flag)
			break
#what i got at the end is ASCWG{S0o_M4ny_Cr1M3s_Y0u_H@v3_7o_1nV3s71g4Te_
#but the last value was random and couldn't get it because of the reconnection every time 
