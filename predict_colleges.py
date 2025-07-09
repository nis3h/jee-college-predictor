import pandas as pd

# Load data
df = pd.read_excel("jee_cutoffs.xlsx")

def predict_colleges(rank, category, gender, preferred_branch=None):
    # Step 1: Filter by category
    filtered_df = df[df['Seat Type'].str.lower() == category.lower()]

    # Step 2: Filter by gender
    gender_options = ['Gender-Neutral']
    if gender.lower() == "female":
        gender_options.append('Female-only')
    filtered_df = filtered_df[filtered_df['Gender'].isin(gender_options)]

    # Step 3: Filter by rank
    filtered_df = filtered_df[pd.to_numeric(filtered_df['Closing Rank'], errors='coerce') >= rank]

    # Step 4: Optional branch filter
    if preferred_branch:
        filtered_df = filtered_df[
            filtered_df['Academic Program Name'].str.lower().str.contains(preferred_branch.lower())
        ]

    # Step 5: Sort by Closing Rank (ascending = best colleges first)
    filtered_df = filtered_df.sort_values(by='Closing Rank')

    return filtered_df[['Institute', 'Academic Program Name', 'Seat Type', 'Gender', 'Closing Rank']]
