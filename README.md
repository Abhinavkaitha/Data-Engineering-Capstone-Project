# Table of Contents
1. [Project description](#Project-description)
2. [About the data](#About-the-data)
3. [Database Schema](#Database-Schema)
4. [Architecture](#Architecture)
5. [Challenges](#Challenges)
6. [Project File Structure](#Project-File-Structure)
7. [Run the project](#Run-the-project)
8. [Future Work](#Future-Work) 

# Project description

In 2019, the [global social penetration rate](https://www.statista.com/statistics/269615/social-network-penetration-by-region/) reached 45 percent, with East Asia and North America both having the highest penetration rate at 70 percent, followed by Northern Europe at 67 percent. ([Statista](https://www.statista.com/topics/1164/social-networks/))

74% of consumers rely on social networks to help with their purchasing decisions. ([awario](https://awario.com/blog/how-social-networks-influence-74-of-shoppers-for-their-purchasing-decisions-today/))

So, targeted advertisements play a key role in achieving better returns on the money invested in ads. Various methods like attribution modeling, sentiment analysis, intent classification, etc are combined to understand the users. Before using these different social media platforms, understanding the pulse of the users is quite important and this applies to every industry.

Studying how people feel about certain products in different regions will help us to customize the ads and target those regions during a specific time in a day, month or year.

while fetching the tweets from twitter, we get the time stamp and also the location. We can give some keywords like coca-cola, Dasani or Sprite, etc to pull the tweets having these keywords related to coca-cola products and study the pulse of the users about these products in different regions. This is not limited to just text data or response data(likes, retweets, etc). Thanks to deep learning techniques, We can harvest the sentiment from emojis, pictures and videos as well.

This project focuses on the challenging phases of the Data Engineering part of the above-mentioned analysis.

# About the data
Due to the limitations of standard twitter API, I used this [archive](https://archive.org/details/twitterstream?and%5B%5D=year%3A%222018%22) to fetch the twitter data. 

# Database Schema
<img align="left" src="https://github.com/Abhinavkaitha/Data-Engineering-Capstone-Project/blob/master/Images/DB_table.png?raw=true" >

# Architecture
<img align="left" src="https://raw.githubusercontent.com/Abhinavkaitha/Data-Engineering-Capstone-Project/master/Images/Architecture.png" >

# Challenges
- Downloading and extrating 233 GB of twitter data from archive.org took forever.
	- Solution: Mount S3 to EC2 using S3fs fuse file system. Now S3 acts like a local directory to EC2 and you can dowload any amount of data directly to S3 from EC2. The configuration of EC2 can be as low as 1GB RAM.

- Preprocessing 233 GB JSON files
    - There are 36 columns in each JSON files, of which only 

- Updating the data regularly
	- Airflow DAG can be triggered everyday to take into account the newly updated data.

- Make it available to 100+ people
	- The final Dash app can be deployed on EC2 or aws beanstalk(which uses EC2 in background) to share the app with anyone. Currently I am using EC2 instance directly to deploy it.

# Project File Structure

# Run the project

# Future Work

I want to extend this project to analyze the real time data using frame works like Apache Kafka. Since this project focuses on the Data Engineering part, I used simple machine learning models on text data to acheive the results. This can be extended to different data types like emojis, images and videos by buiding a robust database and analyze the data using deep learning techniques.
