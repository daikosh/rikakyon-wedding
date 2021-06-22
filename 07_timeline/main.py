import streamlit as st
from PIL import Image, ImageOps
import os
## Parameters ##


## functions ##
def initialization():
    pass

def main():
    initialization()

    ## Body ##
    options = ["1回生", "2回生", "3回生", "4回生"]
    st.select_slider("", options)

if __name__ == "__main__":
    main()
