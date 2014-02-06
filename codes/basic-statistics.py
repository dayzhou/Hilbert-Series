#!/usr/bin/env python
#
# Do statistics on Hilbert series data
# Date: 2014/01/24
# Version: 0.1

import os
import sympy
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

fromRootFolder = os.path.join( '..', 'basic-data' )
toRootFolder = os.path.join( '..', 'basic-statistics' )


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


def compare( a, b ) :
	if a[0] < b[0] :
		return -1
	elif a[0] > b[0] :
		return 1
	else :
		if a[1] < b[1] :
			return -1
		elif a[1] > b[1] :
			return 1
		else :
			return 0


def sort( data ) :
	length = len( data )
	
	i = 0
	while i < length - 1 :
		j = i + 1
		while j < length :
			if data[i][3] < data[j][3] :
				data[i], data[j] = data[j], data[i]
			j += 1
		i += 1
	
	return data


if __name__ == '__main__' :
	if not os.path.exists( toRootFolder ) :
		os.mkdir( toRootFolder )
	elif not os.path.isdir( toRootFolder ) :
		os.remove( toRootFolder )
		os.mkdir( toRootFolder )
	
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
				file = os.path.join( eFolder, filename )
				if filename[-1] == '~' :
					os.remove( file )
					print 'Removed "%s"' % file
					continue
				
				for line in open( file, 'r' ) :
					record = eval( line.strip( '\n').replace( '{', '[' ).replace( '}', ']' ).replace( '^', '**' ) )
					record[2] = sympy.factor( record[2] )
					update_data( data, record )
			
			for elem in sort( data ) :
				eFile.write( '%s\n' % str( elem ).replace( '**', '^' ) )
	print( 'DONE' )
