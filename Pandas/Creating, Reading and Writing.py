import pandas as pd #Importar pandas

#DataFrame
df_cvs = pd.read_csv()
df = pd.DataFrame({'Yes':[50,21], 'No':[131,2]}) #creación
print(df)

print(pd.DataFrame({'Bob': ['bob', 'esponga'], 'Sue': ['Din','Ya']}))

print(pd.DataFrame({'Bob': ['bob', 'esponga'], 'Sue': ['Din','Ya']}, index=['person 1', 'person 2']))

#Series
print(pd.Series([1,2,3,5,6,7,8]))

print(pd.Series())