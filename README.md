# Sentiment Analysis
Status: ongoing

## Overview
A repo to implement different ML models on sentiment analysis task on 10k fillings reports

## What are 10k fillings reports?
- Extensive financial report filing by public companies. 
- Release every year to the U.S Securities and Exchange Commission (SEC)
- Contain 100+ pages
  
### How to read a 10k report?
- There are 4 parts in a 10k.

Part I contains 4 items:
1. Business 
   - Risk Factors 
   - Unresolved 
2. Properties
3. Legal Proceedings
4. Mine Safety Disclosures

Part II contains 5 items:
5. Market for Registrant’s Common Equity, Related Stockholder Matters and Issuer Purchases of Equity Securities
6. Selected Financial Data
7. Management’s Discussion and Analysis of Financial Condition and Results of Operations
8. Quantitative and Qualitative Disclosures about Market Risk
9. Financial Statements and Supplementary Data, Controls and Procedures, Other Information

Part III contains 5 items:
10. Directors, Executive Officers and Corporate Governance
11. Executive Compensation
12. Security Ownership of Certain Beneficial Owners and Management and Related Stockholder Matters
13. Certain Relationships and Related Transactions, and Director Independence”
14. Principal Accountant Fees and Services

### What can we exploit from 10k data?
Research has shown that the sentiment meaning from 10ks are informative when making investing decision [link](https://poseidon01.ssrn.com/delivery.php?ID=971089017066125081097106102072084088004051077072079059077025092111001021027122020127011038049127007036048085122091000022013105024011023022080066078008010014068039018084073081024097116110099120105121075086005101118005097117074098105109021096118126&EXT=pdf&INDEX=TRUE).

The research by Azimi and Alabama on 7 billion words and 220 million sentences from the full text of all 10-K filings by U.S. public companies made during 1994-2017 shows that "Positive (negative) sentiment predicts higher (lower) abnormal return and lower (higher) abnormal trading volume around the 10-K filing date. The market overreacts to negative sentiment and underreacts to positive sentiment during the filing period. All of these effects are larger for negative sentiment than for positive sentiment. Positive sentiment also predicts higher future profitability, higher operating cash flow, lower cash holding, and lower financial leverage. Negative sentiment predicts these variables in the opposite direction."


## Models
### Simple logistic regression model
  - A very simple model. I use this to do some experiments with the data. Just don't implement this model.
  - Follow [this tutorial](https://towardsdatascience.com/a-beginners-guide-to-sentiment-analysis-in-python-95e354ea84f6)
  

### Using BERT and TensorFlow
  - Follow [this tutorial](https://towardsdatascience.com/sentiment-analysis-in-10-minutes-with-bert-and-hugging-face-294e8a04b671)- )
  - Use transfer learning and fine-tuning methods

### Using Stanford CoreNLP Model
  - Follow [this tutorial](https://towardsdatascience.com/natural-language-processing-using-stanfords-corenlp-d9e64c1e1024)
  - Implement at [sentiment-analysis-coreNLP.ipynb](https://github.com/AriNguyen/SentimentAnalysis/blob/master/sentiment-analysis-coreNLP.ipynb) 
  - Conclusion: 
  
### FinBERT model
  - Implement at [sentiment-analysis-FinBERT.ipynb](https://github.com/AriNguyen/SentimentAnalysis/blob/master/sentiment-analysis-FinBERT.ipynb)
  - Result
  - Conclusion

## Preprocess 10k data
https://towardsdatascience.com/nlp-preprocessing-with-nltk-3c04ee00edc0

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

