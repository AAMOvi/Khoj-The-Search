import pandas as pd

# Step 1: Load dataset
df = pd.read_csv("Data/restaurants.csv", encoding="utf-8")

# Step 2: Keep only needed columns
columns_to_keep = ['name', 'address', 'rating', 'number_of_reviews', 'affluence']
df = df[columns_to_keep]

# Step 3: Clean ratings
df['rating'] = pd.to_numeric(df['rating'], errors='coerce').fillna(0)

# Step 4: Handle missing values
df = df.dropna(subset=['name', 'address'])

df['number_of_reviews'] = pd.to_numeric(df['number_of_reviews'], errors='coerce').fillna(0)
df['affluence'] = pd.to_numeric(df['affluence'], errors='coerce').fillna(0)

# Step 5: Remove extra spaces
df['name'] = df['name'].str.strip()
df['address'] = df['address'].str.strip()

# Step 6: Remove duplicates
df = df.drop_duplicates(subset=['name', 'address'])

# Step 7: Save cleaned dataset
df.to_csv("khoj_restaurants.csv", index=False)

print("Cleaned dataset saved as 'khoj_restaurants.csv'")
print("Cleaned dataset shape:", df.shape)