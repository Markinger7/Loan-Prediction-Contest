# Loan-Prediction-contest
Repo containing code for the Loan Prediction Practice Problem from <a href='https://datahack.analyticsvidhya.com/contest/practice-problem-loan-prediction-iii/#About'> Analytics Vidhya</a>.

### Description:
This hackathon aims to provide a professional setup to showcase your skills and compete with their peers, learn new things and achieve a steep learning curve.

### Problem
#### Predict Loan Eligibility for Dream Housing Finance company

Dream Housing Finance company deals in all kinds of home loans. They have presence across all urban, semi urban and rural areas. Customer first applies for home loan and after that company validates the customer eligibility for loan.

Company wants to automate the loan eligibility process (real time) based on customer detail provided while filling online application form. These details are Gender, Marital Status, Education, Number of Dependents, Income, Loan Amount, Credit History and others. To automate this process, they have provided a dataset to identify the customers segments that are eligible for loan amount so that they can specifically target these customers. 

### What did I do?
- EDA: explored the different features and checked effect on the variable of interest (loan_status)
- Cleaning: filled missing values
- Feature Engineering: created three new features from the numeric variables
- Model:
  - tested the folloing classifiers: LogisticRegression, KNeighborsClassifier, SVC, DecisionTreeClassifier, RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier and xgboost
  - LogisticRegression and AdaBoostClassifier performed the best (used cros validation to check consistency of both classifers)
  - Hyperparameter Tuning for LogisticRegression
- Final Model: LogisticRegression
  - C=100
  - max_iter=50
- Final Score in the contest: 0.78

### Python libaries
- numpy
- pandas
- matplotlib
- seaborn
- sklearn
