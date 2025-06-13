def monthly_sales_summary(df):
    df['date'] = pd.to_datetime(df['date'])

    monthly_summary = df.groupby(df['date'].dt.to_period('M')).agg(
        total_sales=('sales_amount', 'sum'),
        avg_sales=('sales_amount', 'mean'),
        transaction_count=('sales_amount', 'count'),

    )
    return monthly_summary





























    