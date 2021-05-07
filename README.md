# Sentiment Analysis
Status: ongoing

## Overview
A repo to implement different ML models on sentiment analysis task on 10k fillings reports

## What is 10k fillings reports?
- Extensive financial report filing by ... companies
- Release every year
- Contain 100+ pages

## Models
- Simple logistic regression model
  - A very simple model. I use this to do some experiments with the data. Just don't implement this model.
  - Follow [this tutorial](https://towardsdatascience.com/a-beginners-guide-to-sentiment-analysis-in-python-95e354ea84f6)
    

- Using BERT and TensorFlow
  - Follow [this tutorial](https://towardsdatascience.com/sentiment-analysis-in-10-minutes-with-bert-and-hugging-face-294e8a04b671)- )
  - Use transfer learning and fine-tuning methods

- Using Stanford CoreNLP Model
  - Follow this tutorial


##  Setting up
Activate virtual environment
```shell
cd Desktop/PROJECTS
source env_python_3/bin/activate
```

## Preprocess 10k data
https://towardsdatascience.com/nlp-preprocessing-with-nltk-3c04ee00edc0

## Result


## Conclusion


## Resolving Errors
### Cannot import seaborn in jupyter notebook
```python
import sys
print(sys.path)
sys.path.append('/Users/aringuyen/Desktop/PROJECTS/env_python_3/lib/python3.8/site-packages')
```

### No module named wordcloud
https://stackoverflow.com/questions/47298070/importerror-no-module-named-wordcloud

### Install scikit-learn
```shell
/usr/local/opt/python@3.9/bin/python3.9 -m pip install scikit-learn
```

### TypeError: expected string or bytes-like object
- Resole: run jupyter in Pycharm (problems in sys.path)

## Simple logistic regression modelg

