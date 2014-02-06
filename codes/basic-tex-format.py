#!/usr/bin/env python
#
# Rewrite statistic data files into TeX format
# Date: 2014/01/31
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

fromFolder = os.path.join( '..', 'basic-statistics' )
toFolder = os.path.join( '..', 'basic-tex' )
name = 'Hilbert-series-basic-case'

TEX_HEAD = r"""\documentclass[11pt]{article}

\setlength{\textwidth}{16cm}
\setlength{\textheight}{22cm}
\hoffset=-1.70cm
\voffset=-1.60cm

\usepackage{latexsym, graphicx}
\usepackage{amsmath, amssymb, bm}
\usepackage{hyperref}
\usepackage{longtable}

\renewcommand{\baselinestretch}{1.4}

\begin{document}

\begin{titlepage}
\begin{center}
\textbf{Collections of Hilbert Series Data} \\
\vspace{50mm}
Melissa Duncan\footnote{Email: m.duncan@maths.oxon.org}\\
Wei Gu\footnote{Email: guwei@mail.ustc.edu.cn} \\
Yang-Hui He\footnote{Email: hey@maths.ox.ac.uk} \\
Da Zhou\footnote{Email: zhouda@mail.ustc.edu.cn} \\
\vspace{4mm}
\end{center}
\end{titlepage}
"""

TEX_TAIL=r"""
\end{document}"""


def compile() :
	os.chdir( toFolder )
#	os.system( 'scite %s.tex' % name )
	os.system( 'latex %s.tex' % name )
	os.system( 'latex %s.tex' % name )
	os.system( 'dvips %s.dvi' % name )
	os.system( 'ps2pdf %s.ps' % name )
	os.system( 'evince %s.pdf' % name )
	os.system( 'cp %s.pdf ..' % name )


def reformat_expr( expr ) :
	expr = expr.replace( ' ', '' )		# remove spaces first
	i, length = 0, len( expr )

	newExpr = ''
	while i < length :
		if expr[i] != '^' and expr[i] != '*' :
			newExpr += expr[i]
			i += 1
		elif expr[i] == '*' :
			i += 1
		elif expr[i] == '^' :
			newExpr += '^{'
			i += 1
			if expr[i] == '(' :
				i += 1
				if expr[i] == '-' :
					newExpr += '-'
					i += 1
			while i < length and expr[i] in '0123456789' :
				newExpr += expr[i]
				i += 1
			if i < length and expr[i] == ')' :
				i += 1
			newExpr += '}'
	
	return newExpr


if __name__ == '__main__' :
	if not os.path.exists( toFolder ) :
		os.mkdir( toFolder )
	elif not os.path.isdir( toFolder ) :
		os.remove( toFolder )
		os.mkdir( toFolder )
	
	toFile = open( os.path.join( toFolder, name+'.tex' ), 'w' )
	toFile.write( TEX_HEAD )
	
	for n, Edges in NE :
		toFile.write( '\\section{\\underline{N=%d}}\n\n' % n )
		for e in Edges :
			toFile.write( '\\subsection{E=%d}\n\n' % e )
			
			table = r"""\begin{center}
\begin{longtable}{|c|c|p{80mm}|c|}
\caption{Quivers with %d Vertices and %d Edges} \\

\hline
\multicolumn{1}{|c|}{Dimension} & \multicolumn{1}{c|}{Degree}
& \multicolumn{1}{c|}{Hilbert Series} & \multicolumn{1}{c|}{Count} \\
\endfirsthead

\hline
\multicolumn{4}{|r|}{$\leftarrow$ Continued from previous page} \\
\hline
\multicolumn{1}{|c|}{Dimension} & \multicolumn{1}{c|}{Degree}
& \multicolumn{1}{c|}{Hilbert Series} & \multicolumn{1}{c|}{Count} \\
\endhead

\multicolumn{4}{|r|}{Continued on next page $\rightarrow$} \\
\hline
\endfoot

\hline
\endlastfoot
""" % ( n, e )

			fromFile = open( os.path.join( fromFolder, 'n=%d'%n, 'e=%d.txt'%e ), 'r' )
			for i in range(2) : fromFile.readline()
			for line in fromFile :
				record = eval( line.strip( '\n').replace( '^', '**' ) )
				record[2] = reformat_expr( str( record[2] ).replace( '**', '^' ) )
				table += '\hline\n%d & %d & \\rule{5mm}{0pt}$%s$ & %d \\\\\n' % ( record[0], record[1], record[2], record[3] )
			fromFile.close()
			table += '\\end{longtable}\n\\end{center}\n\n'
			
			toFile.write( table )
		toFile.write( '\\clearpage\n\n' )
	
	toFile.write( TEX_TAIL )
	toFile.close()
	
	compile()
	