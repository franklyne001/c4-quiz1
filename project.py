# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 13:16:50 2024

@author: franklyne wekesa
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
file_path = 'movie_dataset.csv'
df = pd.read_csv(file_path)

# Display the first few rows
print(df.head())

# Check for missing values
print(df.isnull().sum())

# Handle missing values by filling with median for relevant columns
df['Revenue (Millions)'].fillna(df['Revenue (Millions)'].median(), inplace=True)
df['Metascore'].fillna(df['Metascore'].median(), inplace=True)

# Check again for missing values to ensure cleaning
print(df.isnull().sum())

# Highest rated movie
highest_rated_movie = df.loc[df['Rating'].idxmax(), ['Title', 'Rating']]
print(f"Highest Rated Movie: {highest_rated_movie['Title']}, Rating: {highest_rated_movie['Rating']}")

# Calculate and display average revenue
average_revenue = df['Revenue (Millions)'].mean()
print(f"The average revenue of all movies is {average_revenue:.2f} Million")

# Filter movies released between 2015 and 2017, then calculate and display average revenue
movies_2015_2017 = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]
average_revenue_2015_2017 = movies_2015_2017['Revenue (Millions)'].mean()
print(f"The average revenue of movies from 2015 to 2017 is {average_revenue_2015_2017:.2f} Million")

# Number of movies released in 2016
movies_2016_count = df[df['Year'] == 2016].shape[0]
print(f"The number of movies released in 2016 is {movies_2016_count}")

# Count movies directed by Christopher Nolan
nolan_movies_count = df[df['Director'] == 'Christopher Nolan'].shape[0]
print(f"The number of movies directed by Christopher Nolan is {nolan_movies_count}")

# Group by Year and calculate average Rating, then find the year with the highest average rating
average_ratings_per_year = df.groupby('Year')['Rating'].mean()
highest_avg_rating_year = average_ratings_per_year.idxmax()
print(f"The year with the highest average rating is: {highest_avg_rating_year}")

# Calculate percentage increase in movies between 2006 and 2016
movies_2006 = df[df['Year'] == 2006].shape[0]
movies_2016 = df[df['Year'] == 2016].shape[0]
percentage_increase = ((movies_2016 - movies_2006) / movies_2006) * 100
print(f"The percentage increase in number of movies made between 2006 and 2016 is: {percentage_increase:.2f}%")

# Separate Actors column into individual names, then filter and find most common actor
all_actors = df['Actors'].str.split(',').explode().str.strip()
target_actors = ['Mark Wahlberg', 'Bradley Cooper', 'Chris Pratt', 'Matthew McConaughey']
filtered_actors = all_actors[all_actors.isin(target_actors)]
most_common_actor = filtered_actors.value_counts().idxmax()
print(f"The most common actor among the choices is: {most_common_actor}")

# Split Genre column and calculate number of unique genres
all_genres = df['Genre'].str.split(',').explode().str.strip()
unique_genre_count = len(all_genres.unique())
print(f"The number of unique genres is: {unique_genre_count}")

# Correlation of numerical features with heatmap
numerical_features = df.select_dtypes(include=['float64', 'int64'])
correlation_matrix = numerical_features.corr()

#"""
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix of Numerical Features')
plt.show()
#"""


