import ast
import os
import pandas as pd
import ast
#add categories to dataset
def read_data(v5_file, word_category_file):
    try:
        df = pd.read_csv(v5_file, on_bad_lines='skip')
        df_words = pd.read_csv(word_category_file, on_bad_lines='skip')
        return df, df_words
    except Exception as e:
        print("Error reading files:", e)
        return None, None

def update_categories(df, df_words):

    try:
        print("Updating categories...")

        # word -> category dictionary
        word_to_category = dict(zip(df_words['word'], df_words['Category']))

        for index, row in df.iterrows():

            # read offensive words
            try:
                offensive_words = ast.literal_eval(row['offensive_words'])
            except:
                offensive_words = []

            # read existing categories
            try:
                existing_categories = ast.literal_eval(row['category'])
            except:
                existing_categories = []

            new_categories = []

            for word in offensive_words:
                if word in word_to_category:
                    new_categories.append(word_to_category[word])

            # merge old + new categories
            merged_categories = list(set(existing_categories + new_categories))

            # update dataframe
            df.at[index, 'category'] = str(merged_categories)

            # debug
            print("Offensive Words:", offensive_words)
            print("Merged Categories:", merged_categories)
            print("--------------------------")

        return df

    except Exception as e:
        print("Error updating categories:", e)
        return df


def main():

    base_dir = os.path.dirname(__file__)
    os.chdir(base_dir)

    v5_file = os.path.normpath(
        os.path.join(base_dir, '..', 'data', 'processed_sold_dataset_v5.csv')
    )

    word_category_file = os.path.normpath(
        os.path.join(base_dir, '..', 'data', 'offensive_words_categorized.csv')
    )

    df, df_words = read_data(v5_file, word_category_file)

    if df is None:
        return

    df = update_categories(df, df_words)

    output_file = os.path.normpath(
        os.path.join(base_dir, '..', 'data', 'processed_sold_dataset_v6.csv')
    )

    df.to_csv(output_file, index=False)

    print("Finished! Saved to:", output_file)


if __name__ == "__main__":
    main()
