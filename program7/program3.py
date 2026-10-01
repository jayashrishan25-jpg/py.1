import pandas as pd
data = {
    "Product": ["Laptop", "Mobile", "Tablet", "Printer"],
    "Sales": [50000, 70000, 30000, 20000]
}
df = pd.DataFrame(data)
highest = df.loc[df["Sales"].idxmax()]
print(df)
print("\nHighest Selling Product:")
print(highest)