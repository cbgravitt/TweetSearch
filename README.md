# TweetSearch
Leveraging Twitter API to show a user's recent tweets as a .csv file.

# How to Use
Launch using python then enter the username (including the @ symbol) of the desired user when prompted. The user's ten most recent tweets will be stored in a file called "out.csv" for you to look at. Data in the file includes username, the text of the tweet itself, and the number of hashtags used. NOTE: This does not include retweets and replies, only original tweets.

# IMPORTANT: TOKEN
To use this program, you need access to the twitter API. To do so, go to their website and apply for credentials. It takes less than 10 minutes. Once you have your credentials, put your Bearer Token in a .env file with the label used in the code ("BEARER_TOKEN"). Once that's set it'll work just fine.
