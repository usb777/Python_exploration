﻿title = '\nPython in easy steps\n'

for char in title : 
	print( char , end = ' ' )

for char in title :
	if char == 'y' :
		print( '*' , end = ' ' )
		continue
	print( char , end = ' ' )

for char in title :
	if char == 'y' :
		print( '*' , end = ' ' )
		pass
	print( char , end = ' ' )
