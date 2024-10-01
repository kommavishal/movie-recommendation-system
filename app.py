import streamlit as st
import pickle

def recommend(movie,movies_list):
    movie_index=movies_list[movies_list['title']==movie].index[0]
    distances=similarity[movie_index]
    r_list=sorted(enumerate(distances),reverse=True,key=lambda x:x[1])[1:6]
    recommended=[]
    for i in r_list:
        recommended.append(movies_list.iloc[i[0]].title)
    return recommended

movies_list=pickle.load(open('movies.pkl','rb'))
movie_list=movies_list['title'].values

similarity=pickle.load(open('similarity.pkl','rb'))




st.title('Movie recommender system')

selected_movie_name=st.selectbox(
    'which movie do you like',
    movie_list
)


if st.button('Recommend'):
    recommendations=recommend(selected_movie_name,movies_list)
    for i in recommendations:
        st.write(i)




# import streamlit as st
# import pickle
#
#
# def recommend(movie, movies_df, similarity_matrix):
#     # Find the index of the selected movie
#     movie_index = movies_df[movies_df['title'] == movie].index[0]
#
#     # Get the similarity scores for the selected movie
#     distances = similarity_matrix[movie_index]
#
#     # Sort the movies based on similarity scores
#     sorted_movies = sorted(enumerate(distances), reverse=True, key=lambda x: x[1])[1:6]
#
#     recommended = []
#     for i in sorted_movies:
#         # Append the title of the movie corresponding to the sorted index
#         recommended.append(movies_df.iloc[i[0]].title)
#
#     return recommended
#
#
# # Load movies data and similarity matrix
# movies_df = pickle.load(open('movies.pkl', 'rb'))
# movie_list = movies_df['title'].values
# similarity_matrix = pickle.load(open('similarity.pkl', 'rb'))
#
# st.title('Movie Recommender System')
#
# # Create a dropdown for selecting a movie
# selected_movie_name = st.selectbox(
#     'Which movie do you like?',
#     movie_list
# )
#
# # Display recommendations when the button is clicked
# if st.button('Recommend'):
#     recommendations = recommend(selected_movie_name, movies_df, similarity_matrix)
#     for movie in recommendations:
#         st.write(movie)
