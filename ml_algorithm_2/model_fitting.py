import pandas as pd
from tabulate import tabulate
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier

pdtabulate=lambda df:tabulate(df,headers='keys',tablefmt='psql')

input=pd.read_csv(r'E:\UMKCStudies\Thesis\ml_algorithm_2\bagofwords_output.csv',index_col=0)

naive_bayes=MultinomialNB()
logreg=LogisticRegression(solver='lbfgs',multi_class='multinomial',max_iter=1000)
supvec = svm.SVC(gamma='scale', decision_function_shape='ovo')
rdmfrst=RandomForestClassifier(n_estimators=100, max_depth=10)

x=input.drop(columns=['label'])
y=input['label']

x_train, x_test, y_train, y_test = train_test_split(x,y,random_state=42)

naive_bayes.fit(x_train,y_train)
predictions_nb=naive_bayes.predict(x_test)
logreg.fit(x_train,y_train)
predictions_lr=logreg.predict(x_test)
supvec.fit(x_train,y_train)
predictions_supvec=supvec.predict(x_test)
rdmfrst.fit(x_train,y_train)
predictions_rdmfrst=rdmfrst.predict(x_test)

scores=pd.DataFrame(columns=['Model','Accuracy score','Precision score','Recall score','F1 score'])
scores=scores.append({'Model':'Naive Bayes'},ignore_index=True)
scores.loc[scores['Model']=='Naive Bayes','Accuracy score']=accuracy_score(y_test, predictions_nb)
scores.loc[scores['Model']=='Naive Bayes','Precision score']=precision_score(y_test, predictions_nb,average='weighted')
scores.loc[scores['Model']=='Naive Bayes','Recall score']=recall_score(y_test, predictions_nb,average='weighted')
scores.loc[scores['Model']=='Naive Bayes','F1 score']=f1_score(y_test, predictions_nb,average='weighted')

scores=scores.append({'Model':'Logistic Regression'},ignore_index=True)
scores.loc[scores['Model']=='Logistic Regression','Accuracy score']=accuracy_score(y_test, predictions_lr)
scores.loc[scores['Model']=='Logistic Regression','Precision score']=precision_score(y_test, predictions_lr,average='weighted')
scores.loc[scores['Model']=='Logistic Regression','Recall score']=recall_score(y_test, predictions_lr,average='weighted')
scores.loc[scores['Model']=='Logistic Regression','F1 score']=f1_score(y_test, predictions_lr,average='weighted')

scores=scores.append({'Model':'Support Vector Classifier'},ignore_index=True)
scores.loc[scores['Model']=='Support Vector Classifier','Accuracy score']=accuracy_score(y_test, predictions_supvec)
scores.loc[scores['Model']=='Support Vector Classifier','Precision score']=precision_score(y_test, predictions_supvec,average='weighted')
scores.loc[scores['Model']=='Support Vector Classifier','Recall score']=recall_score(y_test, predictions_supvec,average='weighted')
scores.loc[scores['Model']=='Support Vector Classifier','F1 score']=f1_score(y_test, predictions_supvec,average='weighted')

scores=scores.append({'Model':'Random Forest'},ignore_index=True)
scores.loc[scores['Model']=='Random Forest','Accuracy score']=accuracy_score(y_test, predictions_rdmfrst)
scores.loc[scores['Model']=='Random Forest','Precision score']=precision_score(y_test, predictions_rdmfrst,average='weighted')
scores.loc[scores['Model']=='Random Forest','Recall score']=recall_score(y_test, predictions_rdmfrst,average='weighted')
scores.loc[scores['Model']=='Random Forest','F1 score']=f1_score(y_test, predictions_rdmfrst,average='weighted')

print(pdtabulate(scores))