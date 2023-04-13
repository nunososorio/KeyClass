# KeyClass: Text Classification based on Keywords

KeyClass is a web app that allows you to classify a text based on the presence of keywords that are characteristic for each category. You can upload a text file in doc, docx or pdf format and a keywords file in txt format. The app will extract the text and the keywords from the files and assign one or more categories to the text. The app will also plot a bar chart with the frequency of keywords for each category in the text. You can use this app to quickly and easily analyze your text and find out what topics or themes it covers.

## Installation

To run this app locally, you need to have Python 3 and pip installed on your system. You also need to install the following libraries:

- matplotlib

- nltk

- numpy

- pandas

- Pillow

- python-docx

- scipy

- streamlit

- textract

You can install them using the following command:

`pip install -r requirements.txt`

Alternatively, you can use a virtual environment such as conda or venv to create an isolated environment and install the dependencies there.

## Usage

To run this app locally, you need to clone this repository or download the zip file. Then, navigate to the directory where the app.py file is located and run the following command:

`streamlit run app.py`

This will launch the app in your browser and you will see a web interface like this:

![App interface](app.png)

On the left sidebar, you can upload your text file and choose your keywords option. You can either use the default keywords named REFLECT_PT that read from rkeywords.txt in the same directory as the script or upload your custom keywords file. The format of the keywords file should be as follows:

`Category: keyword1, keyword2, keyword3`

For example:

`Fruits: apple, banana, orange`

`Animals: dog, cat, bird`

`Colors: red, green, blue`

Once you upload both files, the app will display the text and the categories on the main panel. It will also show a bar chart with the frequency of keywords for each category in the text. You can use this information to understand what your text is about and how it relates to different categories.

## Demo

You can also try this app online using Streamlit Sharing. Just click on this link: [https://share.streamlit.io/username/keyclass/app.py](https://share.streamlit.io/username/keyclass/app.py)

You will see the same web interface as above and you can upload your files and see the results.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

This project was inspired by a teaching task to incentivate students improve their writing skills through feedback and reflection. The task was to classify a text based on six categories: Reflective Writing, Critical Thinking, Academic Writing, Personal Development, Professional Development and Learning Strategies.

The default keywords for each category were taken from [rkeywords.txt](rkeywords.txt), which was provided by Reflect.

The code for extracting text from different file formats was adapted from [textract](https://github.com/deanmalmgren/textract), a library that extracts text from any document.

The code for creating a web interface was adapted from [streamlit](https://github.com/streamlit/streamlit), a library that makes it easy to create beautiful data apps in Python.

The code for plotting a bar chart was adapted from [matplotlib](https://github.com/matplotlib/matplotlib), a library that provides comprehensive 2D plotting capabilities in Python.

The code for finding sentence similarity was adapted from [nltk](https://github.com/nltk/nltk), a library that provides natural language processing tools in Python.

The code for generating word embeddings was adapted from [gensim](https://github.com/RaRe-Technologies/gensim), a library that provides topic modeling and natural language processing tools in Python.
