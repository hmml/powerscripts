Power Scripts
=============
Various useful scripts mostly for OSX.

Scripts
=======

cleanpath.py
----------------
`$PATH` variable gets polluted over time. `cleanpath.py` searches for duplicates, invalid paths and outputs cleaned version. Encountered issues are printed to `stderr` and cleaned `$PATH` to `stdout`.

Usage:

	% echo $PATH
	/opt/local/bin:/opt/local/sbin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/bin:/usr/faulty

	% cleanpath.py
	Duplicated: /usr/bin
	Doesn't exist: /usr/faulty
	/opt/local/bin:/opt/local/sbin:/usr/bin:/bin:/usr/sbin:/sbin

	% CLEAN_PATH=`./cleanpath.py 2> /dev/null`
	% echo $CLEAN_PATH
	/opt/local/bin:/opt/local/sbin:/usr/bin:/bin:/usr/sbin:/sbin	


parallel.py
---------------
Run multiple commands (read from `stdin`) in parallel. Default number of processes equals to what Activity Monitor sees. Return values are printed at the end. However you can't tell which one belongs to which procesess. 

Usage:

	% parallel.py
	Pool size: 4
	date
	date
	^D
	Sat 25 Jan 2014 15:49:00 CET
	Sat 25 Jan 2014 15:49:00 CET
	[0, 0]


or just feed a file with commands into `parallel.py` and use 7 parallel processes:

	% parallel.py 7 < commands_to_execute.txt


License
=======
MIT