# magic-folder
A script that will sort through all files in a specified directory and sort
them based on file-type and meta-data (where applicable). Use a `cron job` to
automatically run the script on a specific folder at pre-defined intervals.
The script will generate a log file detailing all file transaction performed
after each run.


## Task Breakdown
---
1. Use `glob` module to get a listing of each file in the directory. ..
...Assign the output from `glob` to a list
..*_(option): Get directory path from command line via `argv` from `sys`_
2. Use a generator function to pop items off the list one at a time and scan ..
...the last three characters to determine file extension
3. Sort files by arch-type ie. _Pictures_ , _Documents_ etc.
4. Perform a move operation on each file arch-type
5. Log all transactions to a file which will be backed up regularely