import pandas as pd

excel_file_path = 'FFNI FILE.xlsx'

df = pd.read_excel(excel_file_path)

df['Acclaim seeking'] = df['Question 1'] + df['Question 16'] + df['Question 31'] + df['Question 46']

df['Arrogance'] = df['Question 2'] + df['Question 17'] + df['Question 32'] + df['Question 47']

df['Authoritativeness'] = df['Question 3'] + df['Question 18'] + df['Question 33'] + df['Question 48']

df['Distrust'] = df['Question 4'] + df['Question 19'] + df['Question 34'] + df['Question 49']

df['Entitlement'] = df['Question 5'] + df['Question 20'] + df['Question 35'] + df['Question 50']

df['Exhibitionism'] = df['Question 6'] + df['Question 21'] + df['Question 36'] + df['Question 51']

df['Exploitativeness'] = df['Question 7'] + df['Question 22'] + df['Question 37'] + df['Question 52']

df['Grandiose fantasies'] = df['Question 8'] + df['Question 23'] + df['Question 38'] + df['Question 53']

df['Indifference'] = df['Question 9'] + df['Question 24'] + df['Question 39'] + df['Question 54']

df['Lack of empathy'] = df['Question 10'] + df['Question 25'] + df['Question 40'] + df['Question 55']

df['Manipulativeness'] = df['Question 11'] + df['Question 26'] + df['Question 41'] + df['Question 56']

df['Need for admiration'] = df['Question 12'] + df['Question 27'] + df['Question 42'] + df['Question 57']

df['Reactive anger'] = df['Question 13'] + df['Question 28'] + df['Question 43'] + df['Question 58']

df['Shame'] = df['Question 14'] + df['Question 29'] + df['Question 44'] + df['Question 59']

df['Thrill seeking'] = df['Question 15'] + df['Question 30'] + df['Question 45'] + df['Question 60']

df['Vulnerable Narcissism'] = df['Reactive anger'] + df['Shame'] + df['Need for admiration'] + df['Distrust']

df['Grandiose Narcissism'] = df['Indifference'] + df['Exhibitionism'] + df['Authoritativeness'] + df['Grandiose fantasies'] + df['Manipulativeness'] + df['Exploitativeness'] + df['Entitlement'] + df['Lack of empathy'] + df['Arrogance'] + df['Acclaim seeking'] + df['Thrill seeking']

df['Antagonism'] = df['Manipulativeness'] + df['Exploitativeness'] + df['Entitlement'] + df['Lack of empathy'] + df['Arrogance'] + df['Reactive anger'] + df['Distrust'] + df['Thrill seeking']

df['Extraversion'] = df['Acclaim seeking'] + df['Authoritativeness'] + df['Grandiose fantasies'] + df['Exhibitionism'] 

df['Total score'] = df['Acclaim seeking'] + df['Arrogance'] + df['Authoritativeness']  + df['Distrust'] + df['Entitlement'] + df['Exhibitionism'] + df['Exploitativeness'] + df['Grandiose fantasies'] + df['Indifference'] + df['Lack of empathy'] + df['Manipulativeness'] + df['Need for admiration'] + df['Reactive anger'] + df['Shame'] + df['Thrill seeking'] 


df.to_excel('FFNI Analyzed Data.xlsx') 







