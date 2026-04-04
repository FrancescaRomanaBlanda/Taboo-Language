import pandas as pd

# Load your dataset
df = pd.read_csv('Sinhala\data\processed_sold_dataset_v8.csv')

def classify_target(text):
    if pd.isna(text):
        return "UNT"
    
    text = str(text).lower()

    # 1. Keywords for Individual (IND)
    # Focus on singular pronouns and person-specific terms
    ind_keywords = ['තෝ', 'තමුසෙ', 'මූ', 'තී', 'මුසලයා', 'වේසි', 'පොන්නයා', 'බල්ලා']
    
    # 2. Keywords for Group (GRP)
    # Focus on religion, ethnicity, or collective entities
    grp_keywords = ['මුසල්මානුවන්', 'තම්බි', 'සිංහල', 'ආණ්ඩුව', 'දෙමල', 'දේශපාලුවො', 'එජාප']
    
    # 3. Keywords for Untargeted (UNT)
    # General profanity or abstract venting
    unt_keywords = ['හුත්ත', 'පක', 'කාලකන්නි', 'අපරාදේ']

    # Apply Logic
    if any(word in text for word in grp_keywords):
        return "GRP"
    elif any(word in text for word in ind_keywords):
        return "IND"
    elif any(word in text for word in unt_keywords):
        return "UNT"
    
    # Default if no keyword matches (can be set to OTH or left for manual review)
    return "UNT" 

# Apply the function ONLY from row 71 onwards (index 70)
# We use .iloc[70:] to select the range and update the column
df.loc[70:, 'target_type'] = df.iloc[70:]['text'].apply(classify_target)

# Save the updated file
df.to_csv('Sinhala\data\processed_sold_dataset_v9.csv', index=False, encoding='utf-8-sig')

print("Update complete! Rows 71+ have been processed.")