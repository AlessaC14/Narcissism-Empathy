import pandas as pd

excel_file_path = 'neuroticism_file.xlsx' 

df = pd.read_excel(excel_file_path)

df['Neuroticism'] = df['Q9'] + df['Q24'] + df['Q39'] + ['Q54'] + df['Q55'] + df['Q56']

df.to_excel('NEUROTICISM_SCORE.xlsx')
