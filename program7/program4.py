import numpy as np
import pandas as pd
sales = np.array([12000, 15000, 10000, 18000, 20000])
df = pd.DataFrame({"Sales": sales})
print(df)
print("\nTotal:", np.sum(sales))
print("Average:", np.mean(sales))
print("Maximum:", np.max(sales))
print("Minimum:", np.min(sales))
print("Standard Deviation:", np.std(sales))