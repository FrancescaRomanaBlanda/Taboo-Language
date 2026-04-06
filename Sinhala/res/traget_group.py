import pandas as pd

# Load your main dataset
df = pd.read_csv(r'Sinhala\data\processed_sold_dataset_v8.csv')

# Load keywords from CSVs
ind_keywords_df = pd.read_csv(r'Sinhala\data\offensive_words_v4_IND.csv')
grp_keywords_df = pd.read_csv(r'Sinhala\data\offensive_words_v4_GRP.csv')  # Assuming this file contains group keywords

# Convert keyword columns to lists and lowercase
ind_keywords = ind_keywords_df.iloc[:, 0].dropna().astype(str).str.lower().tolist()
grp_keywords = grp_keywords_df.iloc[:, 0].dropna().astype(str).str.lower().tolist()

# Untargeted keywords (kept hardcoded)
unt_keywords = ['හුත්ත', 'පක', 'කාලකන්නි', 'අපරාදේ']

def classify_target(text):
    if pd.isna(text):
        return "UNT"
    
    text = str(text).lower()

    if any(word in text for word in grp_keywords):
        return "GRP"
    elif any(word in text for word in ind_keywords):
        return "IND"
    elif any(word in text for word in unt_keywords):
        return "UNT"
    
    return "UNT"

# Apply the function to the entire dataset
df['target_type'] = df['text'].apply(classify_target)

# Save the updated dataset
df.to_csv(r'Sinhala\data\processed_sold_dataset_v9.csv', index=False, encoding='utf-8-sig')

print("Update complete! All rows have been processed.")
