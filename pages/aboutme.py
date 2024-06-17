import streamlit as st

def show_about_me():
    st.markdown("# ABOUT ME")
    st.markdown("""
 I am a joyful and lively individual with a gentle and compassionate heart. Dancing and engaging in arts and crafts are among my favorite activities, as they allow me to express my creativity and bring me immense joy. Participating in pageants and organizing events are also passions of mine, as they not only boost my confidence but also provide a platform to showcase different facets of my personality. Through these experiences, I can connect with others, celebrate my achievements, and continuously grow as a person. These activities reflect my vibrant and dynamic nature, allowing me to shine and inspire those around me.
    """)

    st.markdown("---")

    st.image("pages/about_me_image.jpg")
    st.markdown("""
    Photo by [Your Name](https://example.com) on [Unsplash](https://unsplash.com)
    """)

    st.markdown("---")

    with st.expander("More about me"):
        st.markdown("""
       My journey in the Bachelor of Science in Information Systems (BSIS) has been a transformative experience, equipping me with a comprehensive understanding of both technical and business aspects of technology. Through rigorous coursework and practical projects, I have developed skills in system analysis, database management, and information technology, preparing me to bridge the gap between business needs and technological solutions.




        
        ### Personal Interests

        - **Dancing**
        - **Modeling**
        - **Arts and Drawing**
        
        ### Future Goals

       In five years, I aim to become a well-rounded performer, excelling in dancing and modeling while integrating my passion for the arts into my career. I envision myself participating in high-profile dance productions, fashion shows, and creating innovative art projects that blend movement, style, and creativity.
        """)

    st.markdown("---")

    st.info("Connect with me on [Facebook](https://web.facebook.com/queenie.seballos)")
    st.info("Visit my personal website [here](https://web.facebook.com/queenie.seballos)")

# Main function to run the app
def main():
    show_about_me()

if __name__ == "__main__":
    main()
