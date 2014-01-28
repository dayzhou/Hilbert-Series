#!/usr/bin/env python
#
# Do statistics on Hilbert series data
# Date: 2014/01/24
# Version: 0.1

import os
from sympy.abc import T

N = ( 2, 3, 4, 5, 6, 7, 8, 9, 10 )

fromRootFolder = 'statistics'
toRootFolder = 'statistics'

def update_data( data, record ) :
	flag = 0
	for elem in data :
		if elem[:-1] == record[-1] :
			elem[-1] += record[-1]
			flag = 1
			print 'SAME!'
			break
	if flag == 0 :
		data.append( record )


if __name__ == '__main__' :
	data = []
	toFile = open( os.path.join( toRootFolder, 'statistics.txt' ), 'w' )
	toFile.write( 'FORMAT: [ DIMENSION, DEGREE, HILBERT-SERIES, COUNT ]\n\n' )
	
	for n in N :
		print( n )
		
		file = open( os.path.join( fromRootFolder, 'n=%d'%n, 'total.txt' ), 'r' )
		for i in range(2) : file.readline()
		for line in file :
			record = eval( line.strip( '\n').replace( '^', '**' ) )
			update_data( data, record )
		file.close()
			
	for elem in data :
		toFile.write( '%s\n' % str( elem ).replace( '**', '^' ) )
	print( 'DONE' )
