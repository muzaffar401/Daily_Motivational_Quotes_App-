import streamlit as st
import random
from datetime import datetime
import time
import json
import os

# Set page config
st.set_page_config(
    page_title="✨ Daily Motivation",
    page_icon="🌞",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Single JSON file for all quotes
QUOTES_FILE = "quotes_db.json"

def load_quotes():
    """Load quotes from JSON file or return empty dict if file doesn't exist"""
    if os.path.exists(QUOTES_FILE):
        try:
            with open(QUOTES_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            st.error("Error reading quotes file. Starting with empty quotes.")
            return {}
    return {}

def save_quotes(quotes):
    """Save quotes to JSON file"""
    with open(QUOTES_FILE, 'w') as f:
        json.dump(quotes, f, indent=4)

# Load all quotes from single file
quotes_db = load_quotes()

# Initialize session state for user quotes
if 'user_quotes' not in st.session_state:
    st.session_state.user_quotes = []

# Custom CSS for styling
def add_bg():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://wallpapers.com/images/high/beautiful-dark-night-with-shooting-stars-kc0lgr6rplku557j.webp");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        .quote-container {{
            background-color: rgba(255, 255, 255, 0.3);
            border-radius: 15px;
            padding: 25px;
            margin: 15px 0;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }}
        .header {{
            color: #4a4a4a;
            text-align: center;
            margin-bottom: 30px;
        }}
        .category-btn {{
            margin: 5px !important;
        }}

.stButton>button {{
    background-color: #3546ff;
    color: white;
    border-radius: 8px;
    padding: 10px 24px;
    border: none;
    font-weight: bold;
    transition: all .5s ease;
}}

.stButton>button:hover {{
    background-color: #3546ff;
    color: white;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    transform: scale(1.05);
    transition: all .5s ease;
}}

.stTextArea>div>div>textarea {{
    min-height: 100px;
}}

.stRadio>div {{
    display: flex;
    justify-content: center;
    gap: 20px;
}}

.stRadio>div>label {{
    padding: 8px 16px;
    border-radius: 20px;
    background-color: rgba(240, 242, 246,0.3);
    cursor: pointer;
    transition: background-color 0.3s ease-in-out;
}}

.stRadio>div>label:hover {{
    background-color: rgba(240, 242, 246,0.5);
}}

.stRadio>div>label[data-baseweb="radio"]>div:first-child {{
    margin-right: 8px;
}}

        
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg()

# App title
st.markdown("<h1 class='header'>✨ Daily Motivational Quotes</h1>", unsafe_allow_html=True)

# Quote of the Day section
st.markdown("## 🌞 Quote of the Day")
if quotes_db:
    all_quotes = [quote for category in quotes_db.values() for quote in category]
    if all_quotes:
        today = datetime.now().day
        quote_of_the_day = all_quotes[today % len(all_quotes)]
        st.markdown(f"<div class='quote-container'>📜 {quote_of_the_day}</div>", unsafe_allow_html=True)
    else:
        st.warning("No quotes available in the database.")
else:
    st.warning("No quote categories available. Please add some quotes first.")

# Random Quote Generator
st.markdown("## 🎲 Random Quote Generator")
if quotes_db:
    category = st.radio("Select a category:", list(quotes_db.keys()), horizontal=True)
    
    if st.button("Get Random Quote"):
        if quotes_db.get(category):
            selected_quote = random.choice(quotes_db[category])
            st.markdown(f"<div class='quote-container'>✨ {selected_quote}</div>", unsafe_allow_html=True)
        else:
            st.warning(f"No quotes available in the {category} category.")
else:
    st.warning("No quote categories available. Please add some quotes first.")

# Add Your Own Quote
st.markdown("## ✍️ Add Your Own Quote")
with st.form("quote_form"):
    # If quotes exist, show existing categories, otherwise allow new category
    if quotes_db:
        user_category = st.selectbox("Category", list(quotes_db.keys()))
    else:
        user_category = st.text_input("Category")
    
    user_quote = st.text_area("Your motivational quote")
    submitted = st.form_submit_button("Submit Quote")
    
    if submitted and user_quote:
        # Initialize category if it doesn't exist
        if user_category not in quotes_db:
            quotes_db[user_category] = []
        
        # Add quote and save
        quotes_db[user_category].append(user_quote)
        save_quotes(quotes_db)
        
        # Add to session state
        st.session_state.user_quotes.append((user_category, user_quote))
        
        st.success("Thanks for sharing your motivational quote!")
        time.sleep(1)
        st.rerun()

# Display User Quotes if any
if st.session_state.user_quotes:
    st.markdown("## 💖 Your Shared Quotes")
    for i, (cat, quote) in enumerate(st.session_state.user_quotes, 1):
        with st.container():
            st.markdown(f"<div class='quote-container'>🌟 {quote} <br><small>(Category: {cat})</small></div>", unsafe_allow_html=True)