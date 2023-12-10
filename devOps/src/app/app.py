import streamlit as st
from datetime import datetime
from PIL import Image

st.set_page_config(layout="wide")
logo = Image.open("public/logo.webp")


# Function to display GitHub and Badge Images in the sidebar
def display_sidebar():
    st.sidebar.markdown(
        "[![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)"
    )

    # Badges from "Ileriayo/markdown-badges"
    st.sidebar.markdown(
        "![Kubernetes](https://img.shields.io/badge/kubernetes-326CE5.svg?&style=for-the-badge&logo=kubernetes&logoColor=white)"
    )
    st.sidebar.markdown(
        "![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?&style=for-the-badge&logo=PyTorch&logoColor=white)"
    )
    st.sidebar.markdown(
        "![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FFD43B?style=for-the-badge&logo=huggingface&logoColor=black)"
    )
    st.sidebar.markdown(
        "![logPai](https://img.shields.io/badge/logPai-FFD43B?style=for-the-badge&logo=logPai&logoColor=black)"
    )  # Placeholder as there's no official badge for logPai

    st.sidebar.markdown("### Work in Progress 🚧👷")
    st.sidebar.markdown("### Contact")
    st.sidebar.markdown("p4rlx-news@pm.me")
    st.divider()
    st.sidebar.markdown(
        "[### Github Link](https://github.com/snyata/deepField_logE)"
    )


# Main Page Layout
def main_page():
    today = datetime.now().strftime("%Y-%m-%d")
    st.title(f"Deep Field LogE - {today}")
    st.image(
        logo, use_column_width=True, clamp=True, caption="A Deep Field Audiato"
    )

    current_time = datetime.now().strftime("%H:%M:%S")
    st.write(f"Current Time: {current_time}")

    st.divider

    st.markdown("**HS** and **Nullzero**")

    placeholder = st.empty()
    if st.button("Receive Insights"):
        placeholder.text(
            "Insight Box: To be populated with data from the Model's GET endpoint when live."
        )

    st.markdown("### Live Dashboard")
    # df_placeholder = st.empty()
    # st.write(df_placeholder)

    st.markdown(
        """
    #### Project Explanation
    This project is about deploying and training models to Google Cloud Platform and monitoring them on-premises in Australia. The core functionality involves passing logs through a secure connection for processing by a model that is intermittently trained. The insights generated are then consumed by the ELK stack.
    """
    )

    st.markdown("### Updates")
    latest_commit = (
        "Latest commit message here"  # Placeholder for GitHub commit
    )
    st.text_area("Latest Commit from GitHub", latest_commit, height=100)


# Display the sidebar and main page content
display_sidebar()
main_page()
