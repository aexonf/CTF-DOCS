import string
def check(char):
	s = "GOAHGHEEGSAEEHACEGULREPEEECEOKMKERFSESFRLKERUKTSVPMSSNHSKRFFAGIAPVETCNMDLVFHDAOGFLAFGSKEULMVOOWWCAHCRFVVNVHVCMSYELSPMIHHMODAUKHE" 
	if(char.upper() in s):
		pass
	else:
		print(char.upper())

alphabets = "abcdefghijklmnopqrstuvwxyz"
for c in alphabets:
	check(c)

