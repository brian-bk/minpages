# mny-pages

Works on linux. An abbreviated form a man-pages. 
You can easily edit mny-pages as you so choose.


INSTALLATION:
1.
	Change shebang (1st line of minyman.py) to point to python3
	This is already set up for most regular installations (/usr/bin/python3)
	Also make sure minyman.py is executable
		(~$ chmod +x minyman.py)
2.
	Add sym-link to minyman.py (with sudo/root)
		~$ ln -s /home/{user}/mny/minyman.py /usr/bin/mny
3.
	Edit first few lines of minyman.py:
=======
min-pages
=====
Works on linux. An abbreviated form a man-pages. 
You can easily edit mny-pages as you so choose.
-----

INSTALLATION:
-----
0. Change shebang (1st line of minyman.py) to point to python3
  *This is already set up for most regular installations (/usr/bin/python3)
  *Also make sure minyman.py is executable
  *(~$ chmod +x minyman.py)
0. Add sym-link to minyman.py (with sudo/root)
		~$ ln -s /home/{user}/mny/minyman.py /usr/bin/mny
0. Edit first few lines of minyman.py:
		i.[REQUIRED]:
			Change page_dir to a valid directory for the mny-pages.
			If needed create this directory.
		ii.[OPTIONAL]:
			Set default editor so it doesn't ask you every time

All done!
=======
------------------------------
Now you can create pages on your own, or use mny to 
create the pages as you go. You can even edit the mny mny-page,
to your liking. Whatever makes it easier to use.
