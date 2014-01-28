#!/usr/bin/env python
#
# Do statistics on Hilbert series data
# Date: 2014/01/24
# Version: 0.1

import os
from sympy.abc import T

NE = (
	(2, (3, 4, 5, 6) ),
	(3, (3, 4, 5, 6, 7) ),
	(4, (4, 5, 6, 7, 8) ),
	(5, (5, 6, 7, 8, 9) ),
	(6, (6, 7, 8, 9, 10) ),
	(7, (7, 8, 9, 10) ),
	(8, (8, 9, 10, 11) ),
	(9, (9, 10, 11, 12) ),
	(10, (10, 11, 12, 13) ),
)

fromRootFolder = 'statistics'
toFolder = 'statistics'

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
	if not os.path.exists( toFolder ) :
		os.mkdir( toFolder )
	elif not os.path.isdir( toFolder ) :
		os.remove( toFolder )
		os.mkdir( toFolder )
	
	for n, Edges in NE :
		print( n )
		data = []
		nFile = open( os.path.join( toFolder, 'n=%d'%n,  'total.txt' ), 'w' )
		nFile.write( 'FORMAT: [ DIMENSION, DEGREE, HILBERT-SERIES, COUNT ]\n\n' )
		
		for e in Edges :
			print( n, e )
			
			file = open( os.path.join( fromRootFolder, 'n=%d'%n, 'e=%d.txt'%e ), 'r' )
			for i in range(2) : file.readline()
			for line in file :
				record = eval( line.strip( '\n').replace( '^', '**' ) )
				update_data( data, record )
			file.close()
			
		for elem in data :
			nFile.write( '%s\n' % str( elem ).replace( '**', '^' ) )
	print( 'DONE' )
