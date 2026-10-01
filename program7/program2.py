import pandas as pd
data = {
    "Product": ["Pen", "Book", "Bag", "Pencil"],
    "Sales": [1000, 2500, 4000, 800]
}
df = pd.DataFrame(data)
print(df)
print("\nTotal Sales:", df["Sales"].sum())
print("Average Sales:", df["Sales"].mean())