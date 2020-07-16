import tweepy
import unicodecsv
import numpy as np
import pandas as pd
from tweepy import Cursor
from unidecode import unidecode


# Authentication and connection to Twitter API.
consumer_key = '5eq6TRJgT8yGDAf4ZTn3mpnq4'
consumer_secret = 'gl4ZmDVdPKNryE53EI5j5iZkyBOeyfZ0SpTBJD2FyJHylADRDS'
access_key = '1168836138225885184-mqWMfHrnsH4wHwoUk3TYlEHMtoEbFq'
access_secret = 'Iw4YAFO7gEPXtwxDWjrMQqbp7HA1t8boOlXVeZXwXN2y5'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


def getExceptionMessage(msg):
    words = msg.split(' ')
    errorMsg = ""
    for index, word in enumerate(words):
        if index not in [0,1,2]:
            errorMsg = errorMsg + ' ' + word
    errorMsg = errorMsg.rstrip("\'}]")
    errorMsg = errorMsg.lstrip(" \'")

    return errorMsg


def download_user(dl_user):
    try:    
        user_obj = api.get_user(dl_user)
        with open('result.csv', 'wb') as file:
            writer = unicodecsv.writer(file, delimiter = ',', quotechar = '"')
            # Write header row.
            
            writer.writerow(["id",
                            "id_str",
                            "Name",
                            "Username",
                            "Followers_count",
                            "Listed_count",
                            "Friends_count",
                            "Favorites_count",
                            "Created_at",
                            "Verified",
                            "Default_profile",
                            "Default_profile_image",
                            "Location",
                            "Statuses_count",
                            "Description",
                            "URL",
                            "Geo_enabled",
                        ])
            # Gather info specific to the current user.
            user_info = [user_obj.id,
                        user_obj.id_str,
                        user_obj.name,
                        user_obj.screen_name,
                        user_obj.followers_count ,
                        user_obj.listed_count,
                        user_obj.friends_count,
                        user_obj.favourites_count,
                        
                        user_obj.created_at,
                        user_obj.default_profile,
                        user_obj.default_profile,
                        user_obj.default_profile_image,
                        user_obj.location,
                        user_obj.statuses_count ,
                        user_obj.description,
                        user_obj.url,
                        user_obj.geo_enabled,
                        ]
            writer.writerow(user_info)
             # Show status if success
            print("Wrote tweets by %s to CSV." % dl_user)
    except tweepy.TweepError as e:
            print ("\n"+str(e.api_code) +":"+ getExceptionMessage(e.reason)+"\n")

