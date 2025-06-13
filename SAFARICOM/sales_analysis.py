import pandas as pd

def analyze_sales(df):
    df['total_revenue'] = df['price'] * df['quantity_sold']

    top_products = df.nlargest(3, 'total_revenue').drop_duplicates(subset='product')

    avg_priceper_category = df.groupby('category')['price'].mean().Round(2)

    return{
        'top_products':top_products,
        'avg_priceper_category': avg_priceper_category
    }