def get_pnn_tweet(name_of_pnn):
    pnn_tweet = df[df['Sentiment']==name_of_pnn]['cleaning_text']
    return pnn_tweet

get_pnn_tweet('Natural').head(2)

get_pnn_tweet('Negative').head(2)

get_pnn_tweet('Positive').head(2)