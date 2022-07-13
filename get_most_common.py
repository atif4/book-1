def get_most_common (token):
    most_common = get_tokens(token)
    user_info_df = pd.DataFrame(most_common.items(),columns=['words','score'])
    return user_info_df