# EDA pamages 
import pandas as pd
#load data
df = pd.read_csv("C:\\Users\\haier\\Downloads\\covid19_tweets.csv") 
df.dropna(inplace=True)
df.isnull().sum()
df=df.apply(lambda x: x.astype(str).str.lower()) # the whole dataset is converted into lowercase()
df
import neattext as nfx
def get_unique_value(column_id):
    #"These are unique value"
    unique_info = df[column_id].unique()
    return unique_info
def get_unique_info_count(column_id):
    #"This tells how many times a word is repeat or not"
    unique_info_count = df[column_id].value_counts()
    return  unique_info_count 
def get_unique_info_largest(column_id):
    #"Here top 30 values which repeated mostly")
    #plot the top value count 
    unique_info_largest = df[column_id].value_counts().nlargest(30)
    return unique_info_largest
columns_id_list=['user_name',
                 'user_location',
                 'user_description',
                 'user_created',
                 'user_followers',
                 'user_friends',
                 'user_favourites',
                 'user_verified', 
                 'date',
                 'text',
                 'hashtags',
                 'source',
                 'is_retweet']

for column_id_list in columns_id_list:
    get_unique_value(column_id_list)