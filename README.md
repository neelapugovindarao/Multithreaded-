 Features


Concurrent downloads using ThreadPoolExecutor (up to 3 simultaneous downloads)
Simulated download time based on file size
Random failure simulation to mimic real-world network errors
Download summary showing success and failure counts


example output
Starting Downloads...

Starting download: file1.zip
Starting download: file2.mp4
Starting download: file3.pdf
Completed: file3.pdf
Starting download: file4.jpg
Failed: file1.zip
Completed: file2.mp4
...

Download Summary:

Successful: 4
Failed: 1
