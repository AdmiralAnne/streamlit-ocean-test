import streamlit as st
st.success("Collection of some resources and links where you can discover more about the Big Five model.")
with st.sidebar:
    st.success('Navigate to more pages using the above links ⬆️')
    

if st.button("Home"):
    st.switch_page("streamlit_app.py")
if st.button("Read more"):
    st.switch_page("pages/further_reading.py")
st.markdown("""

    1. [Simple Psychology - Big Five Personality](https://www.simplypsychology.org/big-five-personality.html)
    
    2. [Very well mind - How to Use the Big 5 Personality Traits](https://www.verywellmind.com/the-big-five-personality-dimensions-2795422)

    """
    )