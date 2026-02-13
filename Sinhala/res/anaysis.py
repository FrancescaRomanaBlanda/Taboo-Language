import pandas as pd

def read_sold_test():
    df = pd.read_csv('../data/offensive_words_categorized.csv')
    print(df.dtypes)
    print(df.head())
    return df

def read_and_group_offensive_words(file_path='data/offensive_words_categorized.csv'):
    """Read offensive words file and group by category."""
    df = pd.read_csv(file_path)
    
    # Group by category
    grouped = df.groupby('Category')
    
    # Display groups
    print("\n=== Offensive Words Grouped by Category ===\n")
    for category, group in grouped:
        print(f"{category}:")
        print(f"  Count: {len(group)}")
        print(f"  Unique words: {group['word'].nunique()}")
        print(f"  Words: {group['word'].unique().tolist()[:10]}")  # Show first 10
        print()
    
    return grouped
def analyze_data(df):
   for index, value in df.iterrows()    :
    if value['label'] == "OFF":
            print("Offensive content detected.")
            print(value['text'])
            

def main():
    """Main function to execute all functions."""
    print("Starting analysis...")
    df = read_sold_test()
    analyze_data(df)
    grouped = read_and_group_offensive_words()
    print("Analysis complete!")

if __name__ == '__main__':
    main()