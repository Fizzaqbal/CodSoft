import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import pairwise_distances

movies = pd.read_csv('movies.csv')
ratings_movies = pd.read_csv('ratings.csv')

books = pd.read_csv('books.csv')
ratings_books = pd.read_csv('bratings.csv')
user_item_matrix_movies = ratings_movies.pivot_table(index='userId', columns='movieId', values='rating', fill_value=0)
user_item_matrix_books = ratings_books.pivot_table(index='userId', columns='bookId', values='rating', fill_value=0)

user_similarity_movies = 1 - pairwise_distances(user_item_matrix_movies, metric='cosine')
user_similarity_books = 1 - pairwise_distances(user_item_matrix_books, metric='cosine')

user_similarity_df_movies = pd.DataFrame(user_similarity_movies, index=user_item_matrix_movies.index, columns=user_item_matrix_movies.index)
user_similarity_df_books = pd.DataFrame(user_similarity_books, index=user_item_matrix_books.index, columns=user_item_matrix_books.index)

def get_movie_recommendations(user_id, num_recommendations=5):
    user_ratings_movies = user_item_matrix_movies.loc[user_id]
    similar_users_movies = user_similarity_df_movies[user_id].sort_values(ascending=False)
    similar_users_movies = similar_users_movies.drop(user_id)
    similar_users_ratings_movies = user_item_matrix_movies.loc[similar_users_movies.index]
    weighted_sum_movies = (similar_users_ratings_movies.T @ similar_users_movies).sort_values(ascending=False)
    already_rated_movies = user_ratings_movies[user_ratings_movies > 0].index
    recommended_movies = weighted_sum_movies.drop(already_rated_movies)
    top_recommendations_movies = recommended_movies.head(num_recommendations)
    top_movie_titles = movies[movies['movieId'].isin(top_recommendations_movies.index)]['title']
    return top_movie_titles

def get_book_recommendations(user_id, num_recommendations=5):
    user_ratings_books = user_item_matrix_books.loc[user_id]
    similar_users_books = user_similarity_df_books[user_id].sort_values(ascending=False)
    similar_users_books = similar_users_books.drop(user_id)
    similar_users_ratings_books = user_item_matrix_books.loc[similar_users_books.index]
    weighted_sum_books = (similar_users_ratings_books.T @ similar_users_books).sort_values(ascending=False)
    already_rated_books = user_ratings_books[user_ratings_books > 0].index
    recommended_books = weighted_sum_books.drop(already_rated_books)
    top_recommendations_books = recommended_books.head(num_recommendations)
    top_book_titles = books[books['bookId'].isin(top_recommendations_books.index)]['title']
    return top_book_titles

def main():
    user_id = int(input("Enter user ID: "))
    while True:
        choice = input("Enter 'M' for movie recommendations, 'B' for book recommendations, or 'Q' to quit: ").upper()
        if choice == 'M':
            recommendations = get_movie_recommendations(user_id)
            print(f"Movie Recommendations for User {user_id}:")
        elif choice == 'B':
            recommendations = get_book_recommendations(user_id)
            print(f"Book Recommendations for User {user_id}:")
        elif choice == 'Q':
            break  
        else:
            print("Invalid choice. Please enter 'M' for movie recommendations, 'B' for book recommendations, or 'Q' to quit.")

        for i, title in enumerate(recommendations, 1):
            print(f"{i}. {title}")

if __name__ == "__main__":
    main()
