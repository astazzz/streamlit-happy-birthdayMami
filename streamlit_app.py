from pathlib import Path
import json
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain

# Directories and file paths
THIS_DIR = Path(__file__).resolve().parent
CSS_FILE = THIS_DIR / "style" / "style.css"
ASSETS = THIS_DIR / "assets"
LOTTIE_ANIMATION = ASSETS / "animation_birthday.json"

# Function to load and display Lottie animation
def load_lottie_animation(file_path):
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except Exception as e:
        st.error(f"Error loading Lottie animation: {e}")
        return None

# Function to apply heart snowfall effect
def run_heart_animation():
    rain(emoji="❤️", font_size=30, falling_speed=5, animation_length="infinite")

# Function to get the name from query parameter
def get_person_name():
    query_params = st.experimental_get_query_params()
    return query_params.get("name", ["MAMI"])[0]

# Page Configurations
st.set_page_config(
    page_title="Happy Birthday",
    page_icon="🎂",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Run heart animation
run_heart_animation()

# Apply custom CSS
try:
    with open(CSS_FILE) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except Exception as e:
    st.error(f"Error loading CSS: {e}")

# Display header with personalized name
PERSON_NAME = get_person_name()
st.header(f"🎉🎂 Happy Birthday {PERSON_NAME}! 🎉🎂", anchor=False)

# Display Lottie animation
lottie_animation = load_lottie_animation(LOTTIE_ANIMATION)
if lottie_animation:
    st_lottie(lottie_animation, key="lottie-birthday", height=400)

# Personalized message
if PERSON_NAME.lower() == "mami":
    st.markdown(
        f"<h2 style='text-align: center; color: #ff69b4;'>🎂🎈🎁 {PERSON_NAME.upper()}, QUE TENGAS UN MUY FELIZ CUMPLEAÑOS!! 🎉🎉</h2>",
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        f"🎂🎈🎁 {PERSON_NAME}, que tengas un muy feliz cumpleaños!! 🎉🎉",
    )
