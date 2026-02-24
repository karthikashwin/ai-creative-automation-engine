import streamlit as st
from batch_generator import run_campaign

st.set_page_config(page_title="AI Creative Automation Engine", layout="centered")

st.title("AI Creative Automation Engine")
st.write("Generate AI-powered marketing campaign assets automatically.")

campaign_name = st.text_input("Campaign Name", "fantasy_puzzle_launch")
base_theme = st.text_area("Base Theme", "Fantasy puzzle mobile game with magical characters")
num_images = st.slider("Number of Images", 1, 10, 3)

if st.button("Generate Campaign"):
    st.write("Generating images... Please wait.")
    
    run_campaign(
        campaign_name=campaign_name,
        base_theme=base_theme,
        num_images=num_images
    )

    st.success("Campaign generation complete! Check your campaigns folder.")