import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

import argparse

parser = argparse.ArgumentParser(description='Geolocation using embeddings')
parser.add_argument('input', type=str, help='Input file')
parser.add_argument('embeddings', type=str, help='Embeddings file')

args = parser.parse_args()

print('Reading embeddings...')
embeddings_df = pd.read_csv(args.embeddings, index_col=0)
print('Read: ', embeddings_df.shape)

print('Reading data...')
balanced_corpus_df = pd.read_csv(args.input, index_col=0)
print('Read: ', balanced_corpus_df.shape)

X_train, X_test, y_train, y_test = train_test_split(
    embeddings_df, balanced_corpus_df['area'], 
    test_size=0.05,
    random_state=2023
)
X_train, X_dev, y_train, y_dev = train_test_split(
    X_train, y_train,
    test_size=X_test.shape[0], 
    random_state=2023)

print('X_train', X_train.shape, 'y_train', y_train.shape)
print('X_test', X_test.shape, 'y_test', y_test.shape)

regressor = LogisticRegression()

scores = cross_val_score(regressor,
                         X_train,
                         y_train,
                         cv=5,
                         n_jobs=-1)

cv_score = scores.mean()
print(cv_score)

regressor = LogisticRegression()
regressor.fit(X_train, y_train)
preds = regressor.predict(X_test)
print(f'LogisticRegression\n{classification_report(y_test, preds)}')