import pandas as pd

# Load the Excel dataset
df = pd.read_excel("jee_cutoffs.xlsx")

# Display top rows
print("\n🧠 First 5 Rows:\n", df.head())

# Show all column names
print("\n🗂️ Columns:\n", df.columns)

# Show values of important filters
print("\n📚 Categories (Seat Types):", df['Seat Type'].unique())
print("🚻 Gender Pools:", df['Gender'].unique())
print("🏫 Institutes:", df['Institute'].unique())
print("📚 Branches:", df['Academic Program Name'].unique())

