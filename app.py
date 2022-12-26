import streamlit as st 
import numpy as np
from PIL import Image
import tempfile
import cv2
import numpy as np

from ocr.text_reader import OCR_Reader
from webapp.app_utils import demo
from webapp.pages import Page, Pages_View

st.set_page_config(page_title="Optical character recognition", layout="wide")

class OCR_App_Page(Page):
    def __init__(self):
        Page.__init__(self, "Optical character recognition")
        st.sidebar.subheader("Parameters:")
        self.gpu = st.sidebar.checkbox("Enable GPU usage")
        self.reader = OCR_Reader(gpu=self.gpu)
    
    def dispatch(self):
        st.header("OCR")
        option = st.sidebar.radio('What do you prefer?', options = ['Custom images'])

        if option == 'Custom images':
            content = st.sidebar.file_uploader("Choose a content image", type=['png', 'jpg', 'jpeg'])
            if content:
                image = np.asarray(Image.open(content).convert('RGB'))
                try:
                    image, text, boxes = self.reader.read_text(image)
                    st.image(image)

                    cols = st.columns(2)
                    cols[0].subheader("Extracted text")
                    for line in text:
                        cols[0].text(line)  

                    cols[1].subheader("Extracted boxes")
                    for box in boxes:
                        cols[1].text(box)
                except:
                    st.error("I'm sorry, something went wrong. Maybe no text was detected, try another image.")        
            else:
                st.warning("Please choose a valid image file")
        else:
            st.subheader("Invalid Image!")
            
pages_view = Pages_View()
pages_view.add_page(OCR_App_Page())


def main(page_name):
    pages_view.get_page_by_name(page_name).dispatch()


if __name__ == "__main__":
    
    page_name = st.sidebar.selectbox("Select page:", options=pages_view.get_pages_name())
    main(page_name)