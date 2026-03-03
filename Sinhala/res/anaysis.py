import os
import pandas as pd



def read_sold_test(file_path):
    # handle potential malformed rows gracefully
    try:
        df = pd.read_csv(file_path, on_bad_lines='skip')  # pandas >=1.3
    except TypeError:
        # fallback for older pandas versions
        df = pd.read_csv(file_path, error_bad_lines=False, warn_bad_lines=True)
    print(df.dtypes)
    print(df.head())
    return df

def read_and_group_offensive_words(file_path):
    """Read offensive words file and group by category."""
    try:
        df = pd.read_csv(file_path, on_bad_lines='skip')
    except TypeError:
        df = pd.read_csv(file_path, error_bad_lines=False, warn_bad_lines=True)
    
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
    # Iterate rows safely and report offensive entries
    for index, value in df.iterrows():
        if value.get('label') == "OFF":
            print("Offensive content detected.")
            print(value.get('text'))

def visualize_data(grouped):
    output_path = os.path.normpath(os.path.join(base_dir, '..', 'output', 'output.html'))

    output=pd.DataFrame(grouped.size(), columns=['Count'])
    output.to_html(output_path)

def main():
    try:
        # build path relative to this script so you won't get FileNotFoundError
        base_dir = os.path.dirname(__file__)
        file_path = os.path.normpath(os.path.join(base_dir, '..', 'data', 'offensive_words_categorized.csv'))

        df = read_sold_test(file_path)
        analyze_data(df)
        grouped = read_and_group_offensive_words(file_path)
        visualize_data(grouped)  # Pass the output path to the visualization function

        print("Analysis complete!", grouped)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    base_dir = os.path.dirname(__file__)

    main()