In this lab, I have used Python to perform a MapReduce program.
I was provided with an existing Mapper.py and a Reducer.py but it was for calculating the word count. 
We were given a task to change the files in a way where the URL_COUNT is calculated instead of the word count.

So i made my changes to Mapper.py and Reducer.py accordingly, used regex to identify url's be their scheme, etc.

and then it outputs the answer in this format:
<url>	1

After that, the output of the mapper.py goes to the reducer.py as an input and then this reducer function will aggregate the URLs together providing outputs in this format:

<url>	<count>

Also, this will only output those urls which are greater than 5.

(URLs under 5 will be skipped)

###Running the program

I ran the program locally using CSEL environment:
cat input/file01 input/file02 | python Mapper.py | sort | python Reducer.py

the output was as follows:

 /wiki/Doi_(identifier) 18
 /wiki/Google_File_System 6
 /wiki/ISBN_(identifier) 18
 /wiki/MapReduce 7
 /wiki/S2CID_(identifier) 14
 mw-data:TemplateStyles:r1129693374 7
 mw-data:TemplateStyles:r1238218222 121
 mw-data:TemplateStyles:r1295599781 33
 mw-data:TemplateStyles:r886049734 12

it showed me the output of all the urls >= 5 in the program.

After that, I ran the program on google console SSH with 2 worker nodes and 4 worker nodes:
The time difference recorded was as follows:
1 Master and 2 Workers : 
real 1m12.256s
user 0m15.823s
sys 0m1.166s

1 Master and 4 Workers:
real 1m38.984s 
user 0m19.669s
sys 0m1.822s

