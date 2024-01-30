import pandas as pd

excel_file_path = "COMPASSION FILE.xlsx"

df = pd.read_excel(excel_file_path)

df['Kindness'] = df['Q2'] + df['Q6'] + df['Q10'] + df['Q14']

df['Common humanity'] = df['Q4'] + df['Q8'] + df['Q12'] + df['Q16']

df['Mindfulness'] = df['Q1'] + df['Q5'] + df['Q9'] + df['Q9']

df['Indifference'] = df['Q3'] + df['Q7'] + df['Q11'] + df['Q15']

df['TOTAL SCORE'] = df['Kindness'] + df['Common humanity'] + df['Mindfulness'] + df['Indifference']


df.to_excel('Compassion Analyzed Data.xlsx') 