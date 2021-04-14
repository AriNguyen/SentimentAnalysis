"""
@brief read pdf file
@author Ari Nguyen
"""
import os
import textract
import PyPDF2
import pandas as pd
import nltk
from nltk.corpus import stopwords
from wordcloud import STOPWORDS, WordCloud


if __name__ == '__main__':
    data_folder_path = '/Users/aringuyen/Desktop/CAP/10k-Reports/'
    file_path = 'Starbuck-10k.pdf'
    full_file_path = os.path.join(data_folder_path, file_path)

    text = textract.process(full_file_path, method='pdfminer')

    # stop words

    print(text)


