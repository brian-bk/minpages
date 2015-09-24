Minpages
=========

Works on linux. An abbreviated form a man-pages. You can easily edit or add min-pages as you so choose.

## INSTALLATION:
--------
Two ways to install minpages:

1. Using pip
  * `pip install minpages`
2. Compile from source
  * `git clone https://github.com/brian-bk/minpages.git`
  * `cd minpages`
  * `python setup.py install`

Installation creates the executable `min`.
## USAGE
--------
Using minpages is really easy. A handful of default pages are created upon the first time running, and min will also by default copy them into `~/.minpages`.
  * To list all pages, type:
    * `min`
  * To view a specific page, type:
    * `min grep`
  * To edit a page (or create it), type:
    * `min grep -e`
  * You can delete a page too
    * `min grep -d`
  * View help:
    * `min -h` 
