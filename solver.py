from pwn import *
spells = dict(wqe='DEAFENINGBLAST',qqq='COLDSNAP', qqe='ICEWALL', qee='FORGESPIRIT', eee='SUNSTRIKE', wqq='GHOSTWALK', wee='CHAOSMETEOR', wwq='TORNADO', wwe='ALACRITY', www='EMP')
ip = ''
port = ''
r = remote(ip, port)
while True:
	try:
		data = r.recvuntil("What")
		d1 = data.strip().split(" ")
		kk = [d1[0][:1],d1[1][:1],d1[2][:1]]
		kk.sort(reverse=True)
		kf = (kk[0]+kk[1]+kk[2]).lower()
		print(kf,spells[kf])
		r.sendline(spells[kf])
		print(r.recv())
	except EOFError:
		print(r.recv())
		exit()
