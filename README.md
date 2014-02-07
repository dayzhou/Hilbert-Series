Hilbert-Series
=============
Feb. 7th, 2014
=============

This is the Hilbert series data for quiver gauge theories considered in this article:
(hyperlink...)
Below is an explanatory note on the files in this GitHub repository.

=============

-- "codes" directory:

the scripts used for handling data in data.tar.bz2 and statistics.tar.bz2 and generating the PDF files "Hilbert-series-basic-case.pdf" and "Hilbert-series-generic-case.pdf".

If you're interested in them, feel free to hack! I will not explain them here.

=============

-- "data.tar.bz2" file

The raw data files generated with Macaulay2, the Hilbert series data in them are not simplified, and are not sorted out in order. I compressed them because the original size are too big.

All the data in each ".txt" file are in this format:
{dimension, degree, Hilbert-series}
Each ".txt" file is for a particular quiver with specific number of nodes "n" and edges "e".

To download this file, click on its name and then click on "View Raw". To uncompress it, use this command on Linux:
	tar xvjpf data.tar.bz2

=============

-- "statistics.tar.bz2" file

This compressed file contains statistical data of the raw data. We counted the frequency of each combination - {dimension, degree, Hilber-series} for every (n, e) pair, and sorted them by frequency in descending order.

All data in each ".txt" file are in this format:
[dimension, degree, Hilbert-series, count]

=============

-- "Hilbert-series-basic-case.pdf" & "Hilbert-series-generic-case.pdf"

To make the data more readable, I put all the statistical data into TeX files. By using tables, they look nicer and are easy to compare with each other.
