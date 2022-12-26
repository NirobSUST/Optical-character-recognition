
# Optical Character Recognition

Streamlit-based web application to perform OCR on input images


## License

[MIT](https://choosealicense.com/licenses/mit/)

  
## Installation

Install instructions
```bash
  git clone https://github.com/NirobSUST/Optical-character-recognition
  cd Optical-character-recognition
  pip install -r requirements.txt
```

    
## Run Locally

This project has been tested using Ubuntu 18.04.5

Open Streamlit webapp
```bash
streamlit run app.py
```

Launch very basic Tkinter UI
```bash
python gui.py 
```

 * main.py 
    
    Parameters: 
    
     * gpu: bool (default False)
     * img_path: required
```bash
python main.py --gpu --img_path
```
  
#### On the streamlit app:
Enable/Disable GPU usage accordingly.
Choose an input image, the output will be the same image with highlighted boxes of your text, and a paragraph of the detected text with the relative boxes.

In main.py the output will be the same as the streamlit app, but it will be saved in output/

You will have a folder of your experiment, where you'll find the text-highlighted image, plus two text files for your text and your boxes 

#### On the tkinter UI:

As of now, it works with images only, and the output is the same as in main.py
