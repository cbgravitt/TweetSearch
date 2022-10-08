import requests
import os
import csv
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
token = os.getenv('BEARER_TOKEN')

#generates a header for urls based on token
def create_headers(token):
    headers = {"Authorization": "Bearer {}".format(token)}
    return headers

#generates a url for getting the tweets of the specified account
def create_id_url(id):
    url = 'https://api.twitter.com/2/users/' + id + '/tweets'
    return url

#returns the account's id based on username via the API
def get_id(username, headers):
    url = 'https://api.twitter.com/2/users/by?usernames=' + username
    response = requests.request("GET", url, headers=headers)
    response_j = response.json()
    return response_j['data'][0]['id']

#generates a .csv file from the data collected in main
def make_csv(data, username):
    csvFile = open("out.csv", "a", newline="", encoding='utf-8')
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(['Twitter Username', 'Tweet', 'Number of Hashtags'])
    for i in range(10):
        tweet = data[i]['text']
        count = 0
        for char in tweet:
            if char == "#":
                count += 1
        res = [username, tweet, count]
        csvWriter.writerow(res)
    csvFile.close()

def main():
    headers = create_headers(token)
    #username = input("Username")
    username = "@KingJames"
    id = get_id(username[1:], headers)
    url = create_id_url(id)
    response = requests.request("GET", url, headers=headers, params='exclude=retweets,replies')
    response_j = response.json()
    make_csv(response_j['data'], username)

if __name__ == '__main__':
    main()