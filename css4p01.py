# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 19:40:23 2024

@author: Thabakgolo Letsau
"""

import pandas as pd

movie_data = pd.read_csv(r"C:\Users\Thabakgolo Letsau\Downloads\movie_dataset.csv")


# Rename columns with spaces
movie_data.columns = movie_data.columns.str.replace(' ', '_')

# Check for missing values
missing_values = movie_data.isnull().sum()

# Handle missing values (example: fill with mean for numerical columns)
movie_data['Revenue_(Millions)'].fillna(movie_data['Revenue_(Millions)'].mean(), inplace=True)

# Identify the highest rated movie
highest_rated_movie = movie_data.loc[movie_data['Rating'].idxmax()]

# Extract the movie title
highest_rated_movie_title = highest_rated_movie['Title']

# Calculate the average revenue
average_revenue = movie_data['Revenue_(Millions)'].mean()

# Print the result
print(f"The average revenue of all movies in the dataset is: {average_revenue:.2f} million dollars.")

# Filter movies from 2015 to 2017
filtered_movies = movie_data[(movie_data['Year'] >= 2015) & (movie_data['Year'] <= 2017)]

# Calculate the average revenue for the filtered movies
average_revenue_2015_to_2017 = filtered_movies['Revenue_(Millions)'].mean()

# Print the result
print(f"The average revenue of movies from 2015 to 2017 is: {average_revenue_2015_to_2017:.2f} million dollars.")

# Count the number of movies released in the year 2016
movies_2016_count = movie_data[movie_data['Year'] == 2016].shape[0]

# Print the result
print(f"The number of movies released in the year 2016 is: {movies_2016_count}.")

# Count the number of movies directed by Christopher Nolan
nolan_movies_count = movie_data[movie_data['Director'] == 'Christopher Nolan'].shape[0]

# Print the result
print(f"The number of movies directed by Christopher Nolan is: {nolan_movies_count}.")

# Count the number of movies with a rating of at least 8.0
high_rating_movies_count = movie_data[movie_data['Rating'] >= 8.0].shape[0]

# Print the result
print(f"The number of movies with a rating of at least 8.0 is: {high_rating_movies_count}.")

# ///

# Filter movies directed by Christopher Nolan
nolan_movies_ratings = movie_data[movie_data['Director'] == 'Christopher Nolan']['Rating']

# Calculate the median rating for Christopher Nolan's movies
median_rating_nolan_movies = nolan_movies_ratings.median()

# Print the result
print(f"The median rating of movies directed by Christopher Nolan is: {median_rating_nolan_movies:.2f}.")


#///

# Calculate the average rating for each year
average_rating_by_year = movie_data.groupby('Year')['Rating'].mean()

# Find the year with the highest average rating
year_highest_average_rating = average_rating_by_year.idxmax()

# Get the highest average rating
highest_average_rating = average_rating_by_year.max()

# Print the result
print(f"The year with the highest average rating is {year_highest_average_rating} with an average rating of {highest_average_rating:.2f}.")

#//

# Filter movies from 2006 to 2016
movies_2006_to_2016 = movie_data[(movie_data['Year'] >= 2006) & (movie_data['Year'] <= 2016)]

# Count the number of movies for each year
movies_count_2006 = movies_2006_to_2016[movies_2006_to_2016['Year'] == 2006].shape[0]
movies_count_2016 = movies_2006_to_2016[movies_2006_to_2016['Year'] == 2016].shape[0]

# Calculate the percentage increase
percentage_increase = ((movies_count_2016 - movies_count_2006) / movies_count_2006) * 100

# Print the result
print(f"The percentage increase in the number of movies made between 2006 and 2016 is: {percentage_increase:.2f}%.")

#//

from collections import Counter

# Extract and split the actors' names from the "Actors" column
all_actors = movie_data['Actors'].str.split(', ').explode()

# Count the occurrences of each actor
actor_counts = Counter(all_actors)

# Find the most common actor
most_common_actor = actor_counts.most_common(1)[0][0]

# Print the result
print(f"The most common actor in all the movies is: {most_common_actor}.")

#//
# Extract and split the genres from the "Genre" column
all_genres = movie_data['Genre'].str.split(', ').explode()

# Count the number of unique genres
unique_genres_count = all_genres.nunique()

# Print the result
print(f"The number of unique genres in the dataset is: {unique_genres_count}.")

#///

# Calculate the correlation matrix for numerical features
correlation_matrix = movie_data.corr()

# Print the correlation matrix
# print("Correlation Matrix:")
# print(correlation_matrix)

# Extract insights
insight_1 = "There is a positive correlation between 'Rating' and 'Metascore', suggesting that movies with higher ratings tend to have higher Metascores."
insight_2 = "The correlation between 'Rating' and 'Revenue_(Millions)' is moderate, indicating that successful movies, in terms of revenue, may have higher ratings."
insight_3 = "There is a weak negative correlation between 'Metascore' and 'Runtime_(Minutes)', implying that longer movies may not necessarily receive higher Metascores."
insight_4 = "No strong correlation is observed between 'Rating' and 'Year', indicating that the quality of movies is not strongly tied to the release year."
insight_5 = "The correlation between 'Revenue_(Millions)' and 'Year' is relatively weak, suggesting that the revenue of movies is not strongly influenced by the release year."

# Print insights
print("\nInsights:")
print(insight_1)
print(insight_2)
print(insight_3)
print(insight_4)
print(insight_5)





















