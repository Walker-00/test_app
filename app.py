import streamlit as st
import cv2
import numpy as np

st.set_option('deprecation.showPyplotGlobalUse', False)

def main():
    st.title("Test Edge detect Demo Project")
    st.sidebar.title("Test Edge detect Demo Project")
    st.sidebar.markdown("##Default Kernal size is 5 by 5")
    ks = st.sidebar.selectbox("Kernal size for Gaussian", ("5 by 5", "7 by 3", "Default"))
    st.sidebar.markdown("##Recommend is 0")
    sx = st.sidebar.slider('Pick sigmaX value for Gaussian', 0, 10)
    st.sidebar.markdown("Recommend is 0")
    sy = st.sidebar.slider('Pick sigmaY value for Gaussian', 0, 10)
    st.sidebar.markdown('threshold1 value')
    t1 = st.sidebar.text_input('Enter threshold1 value:')

if __name__ == '__main__':
    main()
