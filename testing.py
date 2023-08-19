import streamlit as st
from hdbscan import HDBSCAN

def main():
    st.title('Test')
    a = HDBSCAN()
    st.write(a)

if __name__=='__main__':
    main()