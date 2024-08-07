import streamlit as st
import requests

st.title("PyGame - A Video Game Database")

base_url = "http://127.0.0.1:5000/"  

st.write("### Available REST API Endpoints")
st.code("""
GET /games
GET /games/<game_id>
POST /games
PUT /games/<game_id>
DELETE /games/<game_id>
""")

# Show All Games
if st.button("Show All Games"):
    response = requests.get(base_url + 'games')
    if response.status_code == 200:
        st.write(response.json())
    else:
        st.error(f"Error: {response.status_code}")

# Add a Game
st.write("### Add a Game")
name = st.text_input("Name")
platform = st.text_input("Platform")
year_of_release = st.number_input("Year of Release", step=1)
genre = st.text_input("Genre")
na_sales = st.number_input("NA Sales")
eu_sales = st.number_input("EU Sales")
jp_sales = st.number_input("JP Sales")
other_sales = st.number_input("Other Sales")
critic_score = st.number_input("Critic Score")
user_score = st.text_input("User Score")
rating = st.text_input("Rating")

if st.button("Add Game"):
    new_game = {
        "Name": name,
        "Platform": platform,
        "Year_of_Release": year_of_release,
        "Genre": genre,
        "NA_sales": na_sales,
        "EU_sales": eu_sales,
        "JP_sales": jp_sales,
        "Other_sales": other_sales,
        "Critic_Score": critic_score,
        "User_Score": user_score,
        "Rating": rating
    }
    response = requests.post(base_url + 'games', json=new_game)
    if response.status_code == 201:
        st.success("Game added successfully!")
    else:
        st.error(f"Error: {response.status_code}")
