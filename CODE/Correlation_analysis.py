import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame

import seaborn as sns
import matplotlib.pyplot as plt


excel_file_path = 'Correlation variables.xlsx'

df = pd.read_excel(excel_file_path)

df.corr()

sns.heatmap(df.corr());

#Size of heatmap
plt.figure(figsize=(16, 6))

heatmap = sns.heatmap(df.corr(), vmin=-1, vmax=1, annot=True, cmap='twilight')
heatmap.set_title('Correlation Heatmap', fontdict={'fontsize':18}, pad=12);

plt.savefig('heatmap.png', dpi=300, bbox_inches='tight')
