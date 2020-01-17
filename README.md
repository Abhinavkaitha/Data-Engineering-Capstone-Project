# Table of Contents
1. [Project description](#Project-description)
2. [About the data](#About-the-data)
3. [Database Schema](#Database-Schema)
4. [Technologies used](#Technologies-used)
5. [Architecture](#Architecture)
6. [Airflow pipeline](#Airflow-pipeline)
7. [Challenges](#Challenges)
8. [Project File Structure](#Project-File-Structure)
9. [Run the project](#Run-the-project)
10. [Future Work](#Future-Work) 

# Project description

In 2019, the [global social penetration rate](https://www.statista.com/statistics/269615/social-network-penetration-by-region/) reached 45 percent, with East Asia and North America both having the highest penetration rate at 70 percent, followed by Northern Europe at 67 percent.([Statista](https://www.statista.com/topics/1164/social-networks/))

74% of consumers rely on social networks to help with their purchasing decisions.([awario](https://awario.com/blog/how-social-networks-influence-74-of-shoppers-for-their-purchasing-decisions-today/))

So, targeted advertisements play a key role in achieveing better returns on the money invested on ads. Various methos like attribution modeling, sentiment analysis, intent classification etc are combined to understand the users. Before using these different social media platforms, understanding the pulse of the users is quite important and this applies to every industry.

Studying how people feel about certain products in different regions will help us to customise the ads and target those regions during specific time in a day, month or year.

while fetching the tweets from twitter, we get the time stamp and also the location. We can give some keywords like coca cola, Dasani or Sprite etc to pull the tweets having these keywords related to coca cola products and study the pulse of the users about these products in different regions. This is not limited to just text data or response data(likes, retweets etc). Thanks to deep learning techniques, We can harvest the semtiment from emojis, pictures and videos as well.

This project focuses on the challenging phases of the Data Engineering part of the above mentioned analysis.
# About the data
Due to the limitations of standard twitter API, I used this [archive](https://archive.org/details/twitterstream?and%5B%5D=year%3A%222018%22) to fetch the twitter data. 

# Database Schema

# Technologies used
<img align="left" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Amazon_Web_Services_Logo.svg/512px-Amazon_Web_Services_Logo.svg.png" width=108>
<img align="left" src="https://upload.wikimedia.org/wikipedia/en/2/29/Apache_Spark_Logo.svg" width=108>
<img align="left" src="https://ncrocfer.github.io/images/airflow-logo.png" width=108>
<img align="left" src="https://cdn.sisense.com/wp-content/uploads/aws-redshift-connector.png" width=108>
<img align="left" src="https://braze-marketing-assets.s3.amazonaws.com/images/partner_logos/amazon-s3.png" width=140, height=45>
<img align="left" src="https://upload.wikimedia.org/wikipedia/commons/3/3c/Flask_logo.svg" width=140, height=45><br />

# Architecture
![Architecture](https://github.com/Abhinavkaitha/Data-Engineering-Capstone-Project/blob/master/Images/Screenshot%202020-01-16%20at%204.44.19%20PM.png)
# Airflow pipeline

# Challenges
- Storage and reading speeds optimised by Apache Parquet

- Data increase by 100x.
    - Redshift: read vs write

- Updating the data regularly

- Make it available to 100+ people

# Project File Structure

# Run the project

# Future Work

I want to extend this project to analyze the real time data using frame works like Apache Kafka. Since this project focuses on the Data Engineering part, I used simple machine learning models on text data to acheive the results. This can be extended to different data types like emojis, images and videos by buiding a robust database and analyze the data using deep learning techniques.
