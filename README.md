# info-lstl

A bunch of things related to stuff we do in class.
Help is greatly appreciated.

## dropbox-fetch

It's supposed to recursively fetch files from a public dropbox.

Notes :
- The webpage scraping breaks every now and then
- It's in perl, e.g. I have no idea what I wrote

## rank.pl

Something that compares line rank range between two files

## siu.pl

Creates a DOT file (for graphviz) from a specific input

### Notes

- The program writes to a file named `file.gv`.

### Input
- first line is all the baseunits seperated by whitespace
- following lines are <unitsymbol> followed by their expression in baseunits (e.g. m.s-2)

### Example

![SI Units](http://i.imgur.com/5ZzgpEm.png)

### TODO

- Better debug output

## poem

Formats the poem in monospace and dumps whatever is after the poem delimiter.

### Usage
place `poem.css` in `/css/` (or modify the code to put it wherever you want)

### Input
- first line is title
- second line is author
- `---` is the poem end delimiter
