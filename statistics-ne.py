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

fromRootFolder = 'data'
toRootFolder = 'statistics'


def from_folder( n, e ) :
	return os.path.join( fromRootFolder, 'n=%d'%n, 'e=%d'%e )

def to_folder( n ) :
	return os.path.join( toRootFolder, 'n=%d'%n )

def update_data( data, record ) :
	flag = 0
	for elem in data :
		if elem[:-1] == record :
			elem[-1] += 1
			flag = 1
			break
	if flag == 0 :
		record.append( 1 )
		data.append( record )


if __name__ == '__main__' :
	for n, Edges in NE :
		print( n )
		nFolder = to_folder( n )
		
		if not os.path.exists( nFolder ) :
			os.mkdir( nFolder )
		elif not os.path.isdir( nFolder ) :
			os.remove( nFolder )
			os.mkdir( nFolder )
		
		for e in Edges :
			print( n, e )
			data = []
			eFolder = from_folder( n, e )
			eFile = open( os.path.join( nFolder, 'e=%d.txt' % e ), 'w' )
			eFile.write( 'FORMAT: [ DIMENSION, DEGREE, HILBERT-SERIES, COUNT ]\n\n' )
			
			for filename in os.listdir( eFolder ) :
				file = open( os.path.join( eFolder, filename ), 'r' )
				for line in file :
					record = eval( line.strip( '\n').replace( '{', '[' ).replace( '}', ']' ).replace( '^', '**' ) )
					update_data( data, record )
			
			for elem in data :
				eFile.write( '%s\n' % str( elem ).replace( '**', '^' ) )
	print( 'DONE' )
