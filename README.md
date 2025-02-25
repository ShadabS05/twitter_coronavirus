# Coronavirus twitter analysis

This is an assignment I worked on during my Big Data Course (CSCI-143) At Claremont McKenna College.

The goals of the assignment were to practice the following skills.

1. work with large scale datasets
2. work with multilingual text
3. use the MapReduce divide-and-conquer paradigm to create parallel code

## Process

Using a dataset that contains all geotagged tweets that were sent in 2020 (there are about 1.1 billion tweets), I ran the MapReduce procedure for efficient large scale parallel processing. My goal was to use a MapReducer to provide critical insights on statistics regarding tweets, locations, and trending topics during the pandemic which was represented through Twitter's use of HashTags. In doing so, we are able to understand what was happening on Twitter during the pandemic, what certain trends were, and plenty more information that can be extremely beneficial and insightful when analyzing our actions during the pandemic. The files have been pre-partitioned into the tweets per day and based on country/language, so the first step I worked on was mapping.

### Map

During the mapping process, I created a map python file, which consisted of looping through each file, going through all of the lines within the file, if a tweet had used a certain hashtag, then it will increase the count of that hashtag within a dictionary, along with other important information such as what language it was in/what country it was from depending on which file was inputted. 

### Reduce

Next, for the Reduce process, I wrote a Python file that takes the input from the map.py file, and reduces them together, which created an element-wise addition of all the counts. This outputted us a single .lang/.country file with the sums of all the files, depending on which files were inputted.

### Viaualize

Then, for the visualize step, I used matplotlib to plot whatever information that needed to be plot. For instance, I did the following plots: The for the number of tweets that used #코로나바이러스 and what country those tweets were from. The number of tweets that used #코로나바이러스 and what language the tweet was written in. The number of tweets that used #coronavirus and what country those tweets were from. The number of tweets that used #coronavirus and what language those tweets were written in.

<img src=outputs/country_korean.png width=100% />
<img src=outputs/lang_korean.png width=100% />
<img src=outputs/country_coronavirus.png width=100% />
<img src=outputs/lang_coronavirus.png width=100% />

### Alternative Reduce

I also worked on one final plot where I analyzed four different hashtags, and the count of those hashtags over the years. To make this plot, I had to alter my reduce file so that it contains the hashtag, the day, and the count for the number of tweets that used that hashtag that day. To do so, I used a a dictionary with the hashtag as the key, and a list with a size of 366, where the value at each index corresponds to the number of hashtags used on that index's day. After looping through each file with our different reduction, and using a similar plotting technique, I was left with the following plot:

<img src=outputs/alt_reduce.png width=100% />

Overall, by changing the reduction, we are able to derive new information from this dataset, and it is interesting to see the results we can get by altering our methods.

