import sys
import os

# Point Python to the root directory of your project
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv

st.set_page_config(page_title="Anime Recommendation System", page_icon=":tv:", layout="wide")
load_dotenv()

@st.cache_resource
def init_pipeline():
    return AnimeRecommendationPipeline()

pipeline= init_pipeline()
st.title("Anime Recommendation System")
query=st.text_input("Enter your anime preferences or questions: light hearted anime with school setting.")
if query:
    with st.spinner("Fetching recommendations for you..."):
        response=pipeline.recommend(query)
        st.markdown("### Recommendations")
        st.write(response)

