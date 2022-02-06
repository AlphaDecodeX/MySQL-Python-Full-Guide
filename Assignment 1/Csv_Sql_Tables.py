import ast
import pandas as pd
import MySQLdb
# Python Code to make SQL tables from csv Files
# Three tables are in main use --> movies, genres_movies, companies_movies

def object_to_list(pd_df):
    x = ast.literal_eval(pd_df)
    return x

# '[{}, {}]' --> [{}, {}]

db = MySQLdb.connect(host="localhost", user="root", passwd="1552454fghLPSK@$")

c = db.cursor()

c.execute("CREATE DATABASE IF NOT EXISTS moviesDb")
c.execute("USE moviesDb")
# -----------------------------------------------------
# Creating genres_movies table (id, genre, movie)
c.execute("DROP TABLE IF EXISTS genres_movies") # Drop the table if already exists
# Create a table if not exists

c.execute("CREATE TABLE IF NOT EXISTS genres_movies (ID INT(255), genre VARCHAR(20), movie VARCHAR(90))")

# Converting specific columns movies titles and genres into specific datastructures
# Initially genres column contained strings, so string object converted to list using object_to_list() function.

df = pd.read_csv("movies_info.csv")
movies_genres = df[['original_title', 'genres']]

movies_genres['genres'] = movies_genres['genres'].apply(lambda x: object_to_list(x))

# Creating the SQL table genres_movies in the form (ID, genre, movie_name)
for index, row in movies_genres.iterrows():
#     print(row['genres'])
#     print(row['original_title'])
    for genre in row['genres']:
#         print(genre['id'], row['original_title'])
        sql = "INSERT INTO genres_movies (id, genre, movie) VALUES (%s, %s, %s)"
        val = (genre['id'], genre['name'], row['original_title'])
        c.execute(sql, val)
        db.commit()
# -----------------------------------------------------
# Creating companies_movies table (id, production_company, movie)
c.execute("DROP TABLE IF EXISTS companies_movies") # Drop the table if already exists
# Create a table if not exists

c.execute("CREATE TABLE IF NOT EXISTS companies_movies (ID INT(255), company VARCHAR(500), movie VARCHAR(90))")
# Converting specific columns movies production companies and movies into specific datastructures
# Initially production_companies column contained strings, so string object converted to list using object_to_list() function.

df = pd.read_csv("movies_info.csv")
movies_companies = df[['original_title', 'production_companies']]

movies_companies['production_companies'] = movies_companies['production_companies'].apply(lambda x: object_to_list(x))
# Creating the SQL table companies_movies in the form (ID, company, movie_name)
for index, row in movies_companies.iterrows():
#     print(row['production_companies'])
#     print(row['original_title'])
    for company in row['production_companies']:
        
        sql = "INSERT INTO companies_movies (id, company, movie) VALUES (%s, %s, %s)"
        val = (company['id'], company['name'], row['original_title'])
        c.execute(sql, val)
        db.commit()

# Creating a Major Table (budget, id, popularity, release_date, revenue, runtime, original_title, vote_average, vote_count)
major_table = df[['id', 'original_title', 'budget', 'revenue', 'popularity', 'runtime', 'vote_average', 'vote_count', 'release_date']]
c.execute("DROP TABLE IF EXISTS movies") # Drop the table if already exists
# Create a table if not exists

c.execute("CREATE TABLE IF NOT EXISTS movies (id INT, movie VARCHAR(90), budget INT, revenue BIGINT, popularity FLOAT, runtime INT, vote_average INT, vote_count INT, release_date DATE)")

import math
# Handling Nan values
def runtime_replace(x):
    if math.isnan(x):
        return 0
    return x

def date_replace(x):
    try:
        if math.isnan((x)):
            return 0
    except Exception as e:
        return x

major_table['runtime'] = major_table['runtime'].apply(runtime_replace)
major_table['release_date'] = major_table['release_date'].apply(date_replace)

# Creating the SQL table companies_movies in the form (ID, company, movie_name)

for index, row in major_table.iterrows():
#     print(row['production_companies'])
#     print(row['original_title'])
        sql = "INSERT INTO movies (id, movie, budget, revenue, popularity, runtime, vote_average, vote_count, release_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (row['id'], row['original_title'], row['budget'], row['revenue'], row['popularity'], row['runtime'], row['vote_average'], row['vote_count'], row['release_date'])
        c.execute(sql, val)
        db.commit()

db.close()