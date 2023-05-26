import pandas as pd
import requests
import config
"""
This's a ETL practice in python
Note:
    source: https://towardsdev.com/create-an-etl-pipeline-in-python-with-pandas-in-10-minutes-6be436483ec9
"""


#Extract from the moviedb
API_KEY = config.api_key
movies_list = []

for movie_id in range(550,556):
    #get requests from themoviedb
    url = 'https://api.themoviedb.org/3/movie/{}?api_key={}'.format(
    movie_id, API_KEY)
    
    movies_list.append(requests.get(url).json())
    
df_movies = pd.DataFrame.from_dict(movies_list)

print(df_movies.head())
print(df_movies.columns)
print(df_movies.genres)

#Tranform
# list of only columns for the analysis
list_columns = ['id','budget',  'imdb_id',
                'original_title', 'release_date', 'revenue', 'runtime']
genres_list = df_movies['genres'].tolist()

fit_genres_list = [item for sublist in genres_list for item in sublist]

print(df_movies[list_columns].head())

# get all genres into a list

# result = []

# for l in genres_list:
#     r = []
#     for d in l:
#         r.append(d['name'])
    
#     result.append(r)

#fit every genres from every movie
result = [ [dtn['name'] for dtn in lt] for lt in genres_list ]

df_movies = df_movies.assign(genres_all = result)

#genres dataframe
df_genres = pd.DataFrame.from_records(fit_genres_list).drop_duplicates()
print(df_genres.head())



list_columns.extend(df_genres['name'].to_list())

s = df_movies['genres_all'].explode()
df_movies = df_movies.join(pd.crosstab(s.index, s))

print(df_movies.head())

#working with datetime
df_movies['release_date'] = pd.to_datetime(df_movies['release_date'])
df_movies['day'] = df_movies['release_date'].dt.day
df_movies['month'] = df_movies['release_date'].dt.month
df_movies['year'] = df_movies['release_date'].dt.year
df_movies['day_of_week'] = df_movies['release_date'].dt.day_name()

list_time_columns = ['id', 'release_date',
                     'day', 'month', 'year', 'day_of_week']

print(df_movies[list_time_columns].head())

#Loat
df_movies[list_columns].to_csv('tbdb_movies.csv', index= False)
df_genres.to_csv('tbdb_genres.csv', index=False)
df_movies[list_time_columns].to_csv('tbdb_datetimes.csv', index = False)
