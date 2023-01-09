import pandas as pd

# Adding the facilities_data
facilities_data = f"facilities_data.csv"
facilities_df = pd.read_csv(facilities_data)

# displaying information about the facilities data
facilities_df.info()
