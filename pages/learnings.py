import streamlit as st

def show_learnings():
    st.markdown("# WHAT I HAVE LEARNED")

    st.markdown("""    
    
    Developing these applications has been rewarding, allowing me to delve into various aspects of machine learning and data science. Below are the significant learnings extracted from each project:
    """)

    st.markdown("## Crop Prediction 🌾")
    st.markdown("""
    - **Predictive Analytics**: Utilized classification algorithms to predict pest infestations in crops by analyzing historical data and environmental variables.
    - **Research and Development**: Gained valuable insights into agricultural methodologies and the critical role of data-driven choices in farming.
    - **Data Visualization**: I have developed expertise in crafting clear visual representations that convey intricate trends and patterns found in agricultural data.
    """)

    st.markdown("## Sentiment Analyzer 😊")
    st.markdown("""
    - **Natural Language Processing (NLP)**: Explored NLP techniques for text preprocessing, feature extraction, and sentiment analysis using libraries like NLTK and spaCy.
    - **Model Evaluation**: Learned methods to evaluate sentiment analysis models, including accuracy metrics and handling sentiment polarity variations.
    - **Application in Business**: Conducted studies on emerging agricultural technologies, exploring their potential to revolutionize yield optimization and sustainable farming practices.
    """)

    st.markdown("## Image Classification 🖼️")
    st.markdown("""
    - **Natural Language Processing**: Explored advanced methods in Natural Language Processing, employing models like BERT, GPT-3, and Transformer to handle tasks such as sentiment analysis and language generation.
    - **Reinforcement Learning**: Implemented Reinforcement Learning techniques, including Deep Q-Networks (DQN) and Policy Gradient methods, to address intricate decision-making challenges in environments like game simulations and robotics.
    - **Time Series Forecasting**: Applied LSTM and GRU networks in Time Series Forecasting to predict trends in domains such as financial markets, energy usage, and weather patterns, showcasing the effectiveness of neural networks in analyzing sequential data.
    """)

    st.markdown("---")

    st.info("These projects have furnished me with practical expertise in machine learning, encompassing data preprocessing, model evaluation, and domain-specific insights.. Connect with me on [Facebook](https://www.facebook.com/reyann.bolhano) to discuss more about these projects!")

# Main function to run the app
def main():
    show_learnings()

if __name__ == "__main__":
    main()
