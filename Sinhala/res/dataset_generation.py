import json
import pandas as pd


df = pd.read_csv('sold_test.csv')

def get_offensive_words(row):
    tokens = row['tokens'].split()  # Split tokens
    rationales = json.loads(row['rationales'])  # Parse JSON array
    
    offensive_words = []
    for i, mark in enumerate(rationales):
        if mark == 1:
            offensive_words.append(tokens[i])
    
    return offensive_words

def extract_and_save_offensive_words(df, output_file='offensive_words.csv'):
    """Extract offensive words and save to CSV file."""
    offensive_words = []
    
    for idx, row in df.iterrows():
        if row['label'] == 'OFF':  # Only process offensive posts
            tokens = row['tokens'].split()
            rationales = json.loads(row['rationales'])
            
            for i, mark in enumerate(rationales):
                if mark == 1:
                    offensive_words.append(tokens[i])
    
    # Create DataFrame and save to CSV
    offensive_df = pd.DataFrame(offensive_words, columns=['word'])
    offensive_df.to_csv(output_file, index=False, encoding='utf-8')
    print(f"Offensive words saved to {output_file}")
    print(f"Total offensive words found: {len(offensive_df)}")
    return offensive_df