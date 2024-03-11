import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

full_data = pd.read_csv('7_climate_data.csv')

df = pd.DataFrame
df = full_data.head()
pd.plotting.scatter_matrix(df, alpha=0.2)

fig, axs = plt.subplots(ncols=7, nrows=2, figsize=(20, 10))
index = 0
axs = axs.flatten()
for k,v in full_data.items():
    sns.histplot(v, ax=axs[index])
    index += 1
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=5.0)

sns.pairplot(df)
sns.heatmap(df.corr().abs(), annot=True)

