import streamlit as st
import pandas as pd
import os

# Function to load comments
def load_comments():
    if os.path.exists('comments.csv'):
        return pd.read_csv('comments.csv')
    else:
        return pd.DataFrame(columns=['Location', 'Comment'])

# Function to save a new comment
def save_comment(location, comment):
    df = load_comments()
    df = df.append({'Location': location, 'Comment': comment}, ignore_index=True)
    df.to_csv('comments.csv', index=False)

# Layout
st.sidebar.header("Add a Comment")
with st.sidebar.form(key='comment_form'):
    location = st.text_input("Location (e.g., URL section, description)")
    comment = st.text_area("Comment")
    submit_button = st.form_submit_button(label='Submit')
    if submit_button:
        save_comment(location, comment)

# Load and display comments
df_comments = load_comments()
if not df_comments.empty:
    st.sidebar.header("Comments")
    for index, row in df_comments.iterrows():
        st.sidebar.text(f"Location: {row['Location']}\nComment: {row['Comment']}\n---")

st.markdown("## Website View")
# Define the iframe HTML code with your URL
iframe_code = """
<iframe src="https://mediumslateblue-gnat-563477.hostingersite.com/" width="100%" height="600" frameborder="0"></iframe>
"""

# Use the st.markdown method to render the iframe in your Streamlit app
st.markdown(iframe_code, unsafe_allow_html=True)
