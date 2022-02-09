import streamlit as st
import numpy as np

st.set_option('deprecation.showPyplotGlobalUse', False)

def main():
    st.title("Test")
    st.sidebar.title("Test")
    st.sidebar.subheader("Choose Print")
    t = st.sidebar.selectbox("Text", ("Hello", "Hi", "Walker?"))

    if t == "Hello":
        st.markdown("Hi")
    elif t == "Hi":
        st.markdown("Hello")
    elif t == "Walker?":
        st.markdown("Yep, I'm Walker!")

if __name__ == '__main__':
    main()
