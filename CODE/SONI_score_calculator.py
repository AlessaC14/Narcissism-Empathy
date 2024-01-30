import pandas as pd

excel_file_path = 'SONI FILE.xlsx' 

df = pd.read_excel(excel_file_path)

df['Approach affiliation'] = df['q4'] + df['q1'] + df['q12'] + df['q14'] + df['q17'] + df['q19'] + df['q21'] + df['q22'] + df['q26'] + df['q27'] + df['q31'] + df['q32']

df['Conflicted self-efficacy'] = df['q1'] + df['q7'] + df['q9'] + df['q11'] + df['q13'] + df['q29'] + df['q30'] + df['q33'] + df['q35'] + df['Question']

df['Conflicted affiliation'] = df['q6'] + df['q10'] + df['q16'] + df['q20'] + df['q25'] + df['q28'] + df['q36'] + df['q38']

df['Dismissive self-efficacy'] = df['q5'] + df['q15'] + df['q18'] + df['q23'] + df['q24'] + df['q37']

df.to_excel('SONI Analyzed Data.xlsx')