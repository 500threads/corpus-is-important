# corpus-is-important

First please read this AWESOME blog by Ben Hawkes : https://blog.isosceles.com/how-to-build-a-corpus-for-fuzzing/
But there are two problems i faced. The content mime and corpus minimization. I am sharing my solution suggestions here so that you do not waste your time by dealing with these problems later.

## changing the last query

Content mime is great but if you are dealing with less-common file formats this query does not work.

```
SELECT url, warc_filename, warc_record_offset, warc_record_length
FROM ccindex.ccindex WHERE (crawl = 'CC-MAIN-2023-14') 
AND subset = 'warc' AND content_mime_detected = 'application/pdf';
```

In my current research i have to find a corpus with DGN files but the content mime is not "application/dgn" it is "application/octet-stream".
But we cant find DGN files this way right?
So the method i used here is finding urls with ending ".dgn". Here is example query:

```
SELECT url, warc_filename, warc_record_offset, warc_record_length
FROM ccindex.ccindex WHERE (crawl = 'CC-MAIN-2023-06')
AND subset = 'warc' AND url LIKE '%.dgn'
```

## download the csv

You need to download the output csv file.

## what is this python script

At the end of the blogpost Ben Hawkes gives us a script that downloads the files and tests for new coverage in the program.
But the problem here is i can't compile the target program myself since i dont have access to source code.
So if you are working with grey-box binaries, WinAFL has great python script to minimize corpus.
Of course before that we have to download the files to use in corpus minimization so you can use corpus_creator.py.
Dont forget to install dependencies first.

## working with grey-box binary in windows? here are the steps:
1-Read the blog above, do the instructions.\n
2-Download the CSV output.\n
3-Execute the corpus_creator.py\n
4-Use https://github.com/googleprojectzero/winafl/blob/master/winafl-cmin.py to minimize corpus. That's it.
