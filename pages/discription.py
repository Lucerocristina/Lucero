import streamlit as st

def show_app_description():
    st.markdown("# APP DESCRIPTION")

    st.markdown("""
    Welcome to my Streamlit application portfolio. Here, I showcase three compelling projects that highlight my expertise and passion for machine learning and data science.
    """)

    st.markdown("## Machine Learning Applications")

    st.markdown("### Crop Prediction 🌾")
    st.markdown("""
    This application uses advanced machine learning models to predict crop yields by examining historical data, weather trends, and soil conditions. Its goal is to help farmers make informed decisions for better crop planning and management.
    """)

    st.markdown("### Sentiment Analyzer 😊")
    st.markdown("""
    The sentiment analyzer employs NLP methods to analyze and categorize text sentiment. This helps businesses understand customer feedback, social media sentiment, and review sentiments to gain useful insights for action.
    """)

    st.markdown("### Image Classification 🖼️")
    st.markdown("""
    
This app employs advanced deep learning models to categorize images into specific groups, enabling functions such as identifying objects, recognizing faces, and analyzing medical images. Explore the potential of image recognition with this interactive tool.
    """)

    st.markdown("---")

    st.info("Explore each application to witness demonstrations and gain a deeper understanding of the underlying technology.")
    st.info("Connect with me on [Facebook](https://www.facebook.com/reyann.bolhano) for collaborations and discussions.")

# Main function to run the app
def main():
    show_app_description()

if __name__ == "__main__":
    main()
