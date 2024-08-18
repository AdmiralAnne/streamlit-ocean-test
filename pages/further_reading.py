import streamlit as st

# Success Message
st.success("Explore a curated collection of resources and links to deepen your understanding of the Big Five model.")

# Introductory Text
st.markdown("""
The Big Five Personality Model, also known as the OCEAN model, is a widely researched framework that describes human personality through five broad dimensions: Openness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism. Below, you'll find a list of useful articles, websites, and tools that provide valuable insights into these traits, as well as how they can be applied in various contexts like personal development, career growth, and mental health.
""")

# Resource List
st.markdown("""
### Educational Articles:
1. **[Simply Psychology - Big Five Personality](https://www.simplypsychology.org/big-five-personality.html)**  
   A comprehensive overview of the Big Five Personality Traits, including their definitions, significance, and implications in everyday life.

2. **[Very Well Mind - How to Use the Big Five Personality Traits](https://www.verywellmind.com/the-big-five-personality-dimensions-2795422)**  
   An informative guide on how to apply the Big Five traits in personal and professional settings.

3. **[Scontrino-Powell - Personality and Job Performance](https://scontrino-powell.com/blog/personality-and-job-performance)**  
   This article explores the relationship between personality traits and job performance, offering insights into how understanding the Big Five can enhance workplace dynamics.

### Interactive Tests and Tools:
4. **[Big Five Test - Test/Read More](https://bigfive-test.com/)**  
   Take the Big Five test yourself and get a personalized report on your OCEAN traits.

5. **[Truity - Individual Traits Test](https://www.truity.com/view/tests/big-five-personality)**  
   A popular platform offering a free Big Five personality test with detailed results and explanations.

### Research Papers:
6. **[The Wiley Handbook of Theoretical and Philosophical Psychology](https://onlinelibrary.wiley.com/doi/pdf/10.1002/9781118638279.app1)**  
   A more academic dive into the philosophical underpinnings and applications of the Big Five Personality Model.

7. **[Fetzer Institute - Big Five Inventory (BFI) PDF](https://fetzer.org/sites/default/files/images/stories/pdf/selfmeasures/Personality-BigFiveInventory.pdf)**  
   A detailed document that outlines the methodology and logic behind the Big Five Inventory (BFI) test.

""")

# Divider for clarity
st.divider()

# Further Recommendations and Features
st.markdown("""
### Additional Reading:
For those looking to dive deeper into the science behind the Big Five model, here are a few more recommendations:
- **[Handbook of Psychology, Volume 5, Personality and Social Psychology](https://www.pdfdrive.com/handbook-of-psychology-volume-5-personality-and-social-psychology-e20888869.html)**
- **[Me, Myself, and Us: The Science of Personality and the Art of Well-Being](https://www.pdfdrive.com/me-myself-and-us-the-science-of-personality-and-the-art-of-well-being-e166433821.html)**
- **more coming soon**
""")

# Sidebar with navigation and further links
with st.sidebar:
    st.success('Navigate through the sections above ⬆️')
    st.text(" ")
    st.info("**Follow us on social media:**")
    st.markdown("""
    - [Instagram](https://www.instagram.com/marjijamir)
    - [LinkedIn](https://www.linkedin.com/feed/)
    - [Github](https://github.com/AdmiralAnne)
    """)
