# Whova technical test

Tested on Python Version: 3.6.9

Make sure to have the following python libraries installed
 - sqlite3
 - xlrd

## To create the database
> python3 import_agenda.py agenda.xls
 
## To help with look up values in the database
> python3 lookup_agenda.py --help

![](https://github.com/achen173/Whova/blob/master/agenda_import/Pictures/example_help.JPG)

Example:
> python3 lookup_agenda.py 'Time Start' '08:45 AM'
> 
![](https://github.com/achen173/Whova/blob/master/agenda_import/Pictures/example_lookup.JPG)
