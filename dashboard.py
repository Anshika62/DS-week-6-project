import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import os

# Load CSV
df = pd.read_csv("sales_data.csv")

# Convert Date
df['Date'] = pd.to_datetime(df['Date'])

# ===============================
# SEABORN PLOTS
# ===============================

sns.set(style="whitegrid")

# Sales by Product
plt.figure(figsize=(6,4))
sns.barplot(data=df, x='Product', y='Total_Sales')
plt.title("Total Sales by Product")
plt.tight_layout()
plt.show()

# ===============================
# INTERACTIVE DASHBOARD (FIXED)
# ===============================

# Aggregate data (IMPORTANT)
product_sales = df.groupby(['Product', 'Region'])['Total_Sales'].sum().reset_index()

# Create folder if not exists
os.makedirs("visualizations", exist_ok=True)

fig = px.bar(
    product_sales,
    x='Product',
    y='Total_Sales',
    color='Region',
    title='Interactive Sales Dashboard'
)

# Save HTML
fig.write_html("visualizations/interactive_dashboard.html")

print("✅ Interactive dashboard created successfully!")
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import os

# Load CSV
df = pd.read_csv("sales_data.csv")

# Convert Date
df['Date'] = pd.to_datetime(df['Date'])

# ===============================
# SEABORN PLOTS
# ===============================

sns.set(style="whitegrid")

# Sales by Product
plt.figure(figsize=(6,4))
sns.barplot(data=df, x='Product', y='Total_Sales')
plt.title("Total Sales by Product")
plt.tight_layout()
plt.show()

# ===============================
# INTERACTIVE DASHBOARD (FIXED)
# ===============================

# Aggregate data (IMPORTANT)
product_sales = df.groupby(['Product', 'Region'])['Total_Sales'].sum().reset_index()

# Create folder if not exists
os.makedirs("visualizations", exist_ok=True)

fig = px.bar(
    product_sales,
    x='Product',
    y='Total_Sales',
    color='Region',
    title='Interactive Sales Dashboard'
)

# Save HTML
fig.write_html("visualizations/interactive_dashboard.html")

print("✅ Interactive dashboard created successfully!")
