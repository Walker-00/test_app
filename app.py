import streamlit as st
import cv2
import numpy as np

st.set_option('deprecation.showPyplotGlobalUse', False)

def main():
    im = cv2.imread("./anime.jpg", 0)
    st.title("Test Edge detect Demo Project")
    st.sidebar.title("Test Edge detect Demo Project")
    st.sidebar.markdown("Choose Edge Detector")
    ed = st.sidebar.selectbox("Edge Detector", ("Sobel", "Laplacian", "Canny"))
    st.sidebar.markdown("##Default Kernal size is 5 by 5")
    ks = st.sidebar.selectbox("Kernal size for Gaussian", ("5 by 5", "3 by 3", "Default"))
    st.sidebar.markdown("##Recommend is 0")
    sx = st.sidebar.slider('Pick sigmaX value for Gaussian', 0, 10)
    st.sidebar.markdown("Recommend is 0")
    sy = st.sidebar.slider('Pick sigmaY value for Gaussian', 0, 10)
    t1 = st.sidebar.text_input('Enter threshold1 value:')
    t2 = st.sidebar.text_input('Enter threshold2 value: ')
    if st.sidebar.button("Done", key="done"):
        if ks == "5 by 5":
            k = (5, 5)
        elif ks == "3 by 3":
            k = (3, 3)
        elif ks == "Default":
            k = (5, 5)
        sm = cv2.GaussianBlur(src=im, ksize=k, sigmaX=int(sx), sigmaY=int(sy))
        if ed == "Sobel":
            sbx = cv2.Sobel(sm, cv2.CV_8U, 1, 0, ksize=5)
            sby = cv2.Sobel(sm, cv2.CV_8U, 0, 1, ksize=5)
            sb = cv2.bitwise_or(sbx, sby)
            cv2.imwrite("./out_put.jpg", sb)
            st.markdown("Original Photo")
            st.image("./anime.jpg")
            st.markdown("Output Photo")
            st.image("./out_put.jpg")
        elif ed == "Laplacian":
            lap = cv2.Laplacian(sm, cv2.CV_8U)
            cv2.imwrite("./out_put.jpg", lap)
            st.markdown("Original Photo")
            st.image("./anime.jpg")
            st.markdown("Output Photo")
            st.image("./out_put.jpg")
        elif ed == "Canny":
            can = cv2.Canny(sm, int(t1), int(t2))
            cv2.imwrite("./out_put.jpg", can)
            st.markdown("Original Photo")
            st.image("./anime.jpg")
            st.markdown("Output Photo")
            st.image("./out_put.jpg")
            
if __name__ == '__main__':
    main()
