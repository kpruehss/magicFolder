#Problem nots and analysis
---

##Sort files by file type
Could I get filenames in full as a **list** and then split off the extension
and then sort them into **dict**? Doing that might cut down on the number of
read/write operations the program performs!

What would need to happen?

* get filenames
  * use `scandir()` on the invoking directory which returns an interator. Loop
through the iterator and split the filename and extension. Use conditionals
to assign extensions to their arch-type ie. .txt to Documents.
Then assign it all to a dictionary, using arch-types as key and the files as
values