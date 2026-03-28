import ast
import os
import pandas as pd

#fix relations -Add missing relations
#update label and length and list of offensive words
#create new dataset

def read_data(file_path, file_path_words):
    try:
        print("Reading data...")

        df = pd.read_csv(file_path, on_bad_lines='skip')
        df2 = pd.read_csv(file_path_words, on_bad_lines='skip')

        return df, df2

    except Exception as e:
        print("Error reading data:", e)
        return None, None

def fix_relations(df, df2):
    try:
        print("Fixing relations...")

        # Create fast lookup set of offensive words
        offensive_words_set = set(df2['word'].dropna().astype(str))

        # Drop old columns if they exist
        for col in ['rationales', 'offensive_words']:
            if col in df.columns:
                df = df.drop(columns=[col])

        df['rationales'] = ""
        df['offensive_words'] = ""

        for index, row in df.iterrows():

            try:
                # Convert string representation of list to actual list
                tokens = ast.literal_eval(row['tokens'])
            except Exception as e:
                print(f"Error parsing tokens at index {index}: {e}")
                tokens = []

            # Build rationales aligned with tokens
            rationales = ['1' if word in offensive_words_set else '0' for word in tokens]

            # Extract offensive words only
            offensive_in_row = [tokens[i] for i, mark in enumerate(rationales) if mark == '1']

            # Update dataframe
            df.at[index, 'rationales'] = str(rationales)
            df.at[index, 'offensive_words'] = str(offensive_in_row)
            df.at[index, 'off_word_count'] = len(offensive_in_row)
            if len(offensive_in_row) > 0:
                df.at[index, 'label'] = 'OFF'
            else:
                df.at[index, 'label'] = 'NOT'

            # Optional debug
            print("Tokens:", tokens)
            print("Rationales:", rationales)
            print("Offensive Words:", offensive_in_row)
            print('--------------------------')

        return df

    except Exception as e:
        print("Error fixing relations:", e)
        return df

def csv_to_excel():
    base_dir = os.path.dirname(__file__)
    os.chdir(base_dir)

    csv_file = os.path.normpath(
        os.path.join(base_dir, '..', 'data', 'processed_sold_dataset_v8.csv')
    )
    excel_file = os.path.normpath(
        os.path.join(base_dir, '..', 'data', 'processed_sold_dataset_v8_excel.xlsx')
    )
    # df = pd.read_csv(
    #     csv_file,
    #     encoding="utf-8",
    #     engine="python",
    #     on_bad_lines="skip"  # skips problematic rows safely
    # )
    #
    # # Save using openpyxl engine (Excel-friendly)
    # with pd.ExcelWriter(excel_file, engine="openpyxl") as writer:
    #     df.to_excel(writer, index=False)
    df = pd.read_csv(csv_file, encoding="utf-8", engine="python")

    # Convert everything to string (prevents Excel formulas)
    df = df.astype(str)

    # Save to Excel
    with pd.ExcelWriter(excel_file, engine="openpyxl") as writer:
        df.to_excel(writer, index=False)

    print("Conversion completed successfully!")

def delete_columns():
    base_dir = os.path.dirname(__file__)
    os.chdir(base_dir)
    csv_file = os.path.normpath(
        os.path.join(base_dir, '..', 'data', 'processed_sold_dataset_v7.csv')
    )
    df = pd.read_csv(
        csv_file,
        encoding="utf-8",
        engine="python",
        on_bad_lines="skip"  # skips problematic rows safely
    )
    df = df.drop(columns=["C14", "C15", "C16", "C17", "C18", "C19", "C20", "C21", "C22", "C23", "C24","C25","C26", "C27"])
    df.to_csv("processed_sold_dataset_v8.csv", index=False)


def base ():

    base_dir = os.path.dirname(__file__)
    os.chdir(base_dir)

    file_path = os.path.normpath(
        os.path.join(base_dir, '..', 'data', 'processed_sold_dataset_v4.csv')
    )

    file_path_words = os.path.normpath(
        os.path.join(base_dir, '..', 'data', 'offensive_words_v3.csv')
    )

    df, df2 = read_data(file_path, file_path_words)

    if df is None:
        return

    df3 = fix_relations(df, df2)

    output_path = os.path.normpath(
        os.path.join(base_dir, '..', 'data', 'processed_sold_dataset_v5.csv')
    )

    df3.to_csv(output_path, index=False)

    print("Finished. Saved to:", output_path)

def main():
 # delete_columns()
    csv_to_excel()


if __name__ == "__main__":
    main()
