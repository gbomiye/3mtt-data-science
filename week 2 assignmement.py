import pandas as pd

data = {
    'Name': ['Alice', 'Bayo', 'Dapo'],
    'Age': [25, 20, 4, 8],
    'Country': ['USA', 'UK', 'Canada', 'Australia']
}
df = pd.DataFrame(data)
print(df)