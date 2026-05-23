import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'Product': ['TV', 'Laptop', 'Phone', 'TV'],  # 4 item
    'Region': ['East', 'West', 'East', 'West'],  # 4 item  
    'Sales': [1200, 1500, 800, 1300]             # 4 item
}
df = pd.DataFrame(data)
print(df)

# Bikin grafik biar bisa masuk GitHub
df.groupby('Product')['Sales'].sum().plot(kind='bar')
plt.title('Total Sales by Product')
plt.savefig('sales_chart.png')
plt.show()