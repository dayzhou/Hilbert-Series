#!/usr/bin/env python
#
# Do statistics on Hilbert series data
# Date: 2014/01/24
# Version: 0.1

import os
from sympy.abc import T

N = ( 2, 3, 4, 5, 6, 7, 8, 9, 10 )

fromRootFolder = os.path.join( '..', 'generic-statistics' )
toRootFolder = os.path.join( '..', 'generic-statistics' )

def update_data( data, record ) :
	flag = 0
	for elem in data :
		if elem[:-1] == record[:-1] :
			elem[-1] += record[-1]
			flag = 1
			print 'SAME!'
			break
	if flag == 0 :
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
	data = []
	
	for n in N :
		print( n )
		
		file = open( os.path.join( fromRootFolder, 'n=%d.txt'%n ), 'r' )
		for i in range(2) : file.readline()
		for line in file :
			record = eval( line.strip( '\n').replace( '^', '**' ) )
			update_data( data, record )
		file.close()
	
	toFile = open( os.path.join( toRootFolder, 'total.txt' ), 'w' )
	toFile.write( 'FORMAT: [ DIMENSION, DEGREE, HILBERT-SERIES, COUNT ]\n\n' )
	for elem in sort( data ) :
		toFile.write( '%s\n' % str( elem ).replace( '**', '^' ) )
	toFile.close()
	
	print( 'DONE' )
