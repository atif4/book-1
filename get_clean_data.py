# EDA pamages 
import pandas as pd
#load data
df = pd.read_csv("C:\\Users\\haier\\Downloads\\covid19_tweets.csv") 
df.dropna(inplace=True)
df.isnull().sum()
df=df.apply(lambda x: x.astype(str).str.lower()) # the whole dataset is converted into lowercase()
import neattext as nfx
def get_clean_data_column (new_column_name , column_name,df="C:\\Users\\haier\\Downloads\\covid19_tweets.csv"):
    df[new_column_name] = df[column_name].apply(nfx.remove_emojis)
    df[new_column_name] = df[new_column_name].apply(nfx.remove_numbers)
    df[new_column_name] = df[new_column_name].apply(nfx.remove_punctuations)
    df[new_column_name] = df[new_column_name].apply(nfx.remove_special_characters)
    df[new_column_name] = df[new_column_name].apply(nfx.remove_multiple_spaces)
    df[new_column_name] = df[new_column_name].apply(nfx.remove_stopwords)
    df[new_column_name] = df[new_column_name].apply(nfx.remove_urls)
    df[new_column_name] = df[new_column_name].apply(nfx.remove_visacard_addr)
    df[new_column_name] = df[new_column_name].apply(nfx.remove_terms_in_bracket)
    df[new_column_name] = df[new_column_name].apply(nfx.remove_street_address)
    df[new_column_name] = df[new_column_name].apply(nfx.remove_puncts)
    df[new_column_name] = df[new_column_name].apply(nfx.remove_postoffice_box)
    df[new_column_name] = df[new_column_name].apply(nfx.remove_phone_numbers)
    df[new_column_name] = df[new_column_name].apply(nfx.remove_html_tags)
    df[new_column_name] = df[new_column_name].apply(nfx.remove_currency_symbols)
    return df[new_column_name]
dict_names ={'cleaning_user_name':'user_name',
             'cleaning_user_location':'user_location',
             'cleaning_user_description':'user_description',
             'cleaning_text':'text',
             'cleaning_hashtags':'hashtags',
             'cleaning_source':'source'}
#this the loop in dictionary 
for i ,j in dict_names.items():
    #here i m call my custom function to clean the dataset
    get_clean_data_column(i,j,df="C:\\Users\\haier\\Downloads\\covid19_tweets.csv")