import os

import pandas as pd

#remove duplicated offensive words and categories

def remove_duplicates():
    output_file=os.path.normpath(os.path.join(base_dir, '..', 'data', 'offensive_words_v3.csv'))

    file_path_words = os.path.normpath(os.path.join(base_dir, '..', 'data', 'offensive_words_v2.csv'))

    df = pd.read_csv(file_path_words, on_bad_lines='skip')
    words =df['word']
    print('original words:', len(words))
    unique_words = list(set(words))
    print('updated  words:', len(unique_words))
    offensive_df=pd.DataFrame(unique_words, columns=['word'])
    offensive_df.to_csv(output_file, index=False, encoding='utf-8')
    print(f"Offensive words saved to {output_file}")



def remove_duplicates_from_categories():
    output_file=os.path.normpath(os.path.join(base_dir, '..', 'data', 'offensive_words_categorized_v3.csv'))

    file_path_words = os.path.normpath(os.path.join(base_dir, '..', 'data', 'offensive_words_categorized_v2.csv'))


    df = pd.read_csv(file_path_words, on_bad_lines='skip')

    print('original words:', len(df))

    # remove duplicate words but keep their category
    # unique_df = df[['word', 'Category']].drop_duplicates(subset='word')
    unique_df = df.groupby('word')['Category'].apply(lambda x: list(set(x))).reset_index()

    print('updated words:', len(unique_df))

    unique_df.to_csv(output_file, index=False, encoding='utf-8')

    print(f"Offensive words saved to {output_file}")


if __name__=="__main__":
    base_dir = os.path.dirname(__file__)
    remove_duplicates_from_categories()