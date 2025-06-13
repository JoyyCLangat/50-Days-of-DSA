def clean_customer_data(df):
    #remove duplicates
    df_cleaned = df.drop_duplicates()

    #Handle missing ages
    df_cleaned = df_cleaned['age'].fillna(df_cleaned['age'].median())

    df_cleaned['email'] = df_cleaned['email'].str.lower().str.strip()
    
    #Convert to int
    df['age'] = df['age'].astype(int)

    # Flag invalid emails
    df_cleaned['valid_email'] = df_cleaned['email'].str.contains('@') & df_cleaned['email'].str.contains('.')

    return df_cleaned
