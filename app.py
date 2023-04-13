# Import the libraries
import matplotlib.pyplot as plt
import streamlit as st
import os
import tempfile
from docx import Document

# Create a title and a sidebar
st.title("KeyClass: Text Classification based on Keywords")
st.markdown("by Nuno S. Osório")
st.sidebar.header("Upload your files")

# Define the file name and extension for the text file
text_file = st.sidebar.file_uploader("Choose a text file", type=["docx"])

# Define the option for the keywords file
option = st.sidebar.radio("Choose the keywords option", ["Default", "Custom"])

# Check if the option is default
if option == "Default":
    # Define the file name and extension for the default keywords file
    keywords_file = os.path.join(os.path.dirname(__file__), "rkeywords.txt")
else:
    # Define the file name and extension for the custom keywords file
    keywords_file = st.sidebar.file_uploader("Choose a custom keywords file", type=["txt"])

# Check if both files are uploaded or exist
if text_file is not None and keywords_file is not None:
    # Read the uploaded file content
    document = Document(text_file)
    text = '\n'.join([paragraph.text for paragraph in document.paragraphs])

    # Split the text into words and convert to lower case
    words = text.lower().split()

    # Initialize an empty dictionary to store the keywords and categories
    keywords = {}

    # Check if the option is default
    if option == "Default":
        # Open the default keywords file and read the lines
        with open(keywords_file, "r") as f:
            lines = f.readlines()
    else:
        # Read the lines from the custom keywords file
        lines = keywords_file.readlines()

    # Loop through the lines
    for line in lines:
        # Decode and strip the line if needed
        if isinstance(line, bytes):
            line = line.decode().strip()
        else:
            line = line.strip()
        # Split the line by colon and strip the whitespace
        category, words = line.split(":")
        category = category.strip()
        words = words.strip()
        # Split the words by comma and strip the whitespace
        words = [word.strip() for word in words.split(",")]
        # Add the category and words to the dictionary
        keywords[category] = words

    # Initialize an empty list to store the categories
    labels = []

    # Initialize an empty dictionary to store the frequencies
    freqs = {}

    # Loop through the keywords and categories
    for category, words in keywords.items():
        # Check if the text contains any keyword for each category
        if any(word in words for word in text.lower().split()):
            # Add the category to the list
            labels.append(category)
            # Count the frequency of keywords for each category in the text
            freq = sum([text.lower().split().count(word) for word in words])
            # Add the frequency to the dictionary
            freqs[category] = freq
            
    # Create a new string with highlighted keywords
    highlighted_text = text
    for category, words in keywords.items():
        for word in words:
            highlighted_text = highlighted_text.replace(word, '**' + word + '**')
            
    # Display the text and the categories
    st.subheader("Text extracted from the uploaded document:")
    st.write(text)
    st.subheader("Categories Keyword Analysis:")
    st.write(", ".join(labels))
   

    # Display the highlighted text using markdown
    st.markdown(highlighted_text)

    # Plot a bar chart with the frequencies of keywords for each category
    fig, ax = plt.subplots()
    ax.bar(freqs.keys(), freqs.values())
    ax.set_xlabel("Categories")
    ax.set_ylabel("Frequencies")
    ax.set_title("Frequency of keywords for each category in the text")
    st.pyplot(fig)

else:
    # Display a message if both files are not uploaded or exist
    st.write("Please upload or choose both files to start.")

    # Display a markdown text to explain the format of the keywords file
    st.sidebar.markdown("""
    ## Keywords File Format

    The keywords file should be a txt file with one line per category. Each line should have the following format:

    `Category: keyword1, keyword2, keyword3`
    """)
