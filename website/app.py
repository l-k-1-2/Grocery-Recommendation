from flask import Flask, render_template, request
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

app=Flask(__name__)

data=pd.read_csv("Groceries_dataset.csv")

def draw_result(user):
    user_id = user
    df3 = data.loc[data['Member_number'] == int(user_id)]
    transactions = [a[1]['itemDescription'].tolist() for a in list(df3.groupby(['Member_number','Date']))]
    te = TransactionEncoder()
    te_ary = te.fit(transactions).transform(transactions)
    transactions = pd.DataFrame(te_ary, columns=te.columns_)
    
    pf = transactions.describe()
    pf.iloc[0]-pf.iloc[3]   
    f = pf.iloc[0]-pf.iloc[3]
    a = f.tolist()
    b = list(f.index)
    item = pd.DataFrame([[a[r],b[r]]for r in range(len(a))], columns=['Count','Item'])
    item = item.sort_values(['Count'], ascending=False).head(50)
    
    freq_items = apriori(transactions, min_support=0.001, use_colnames=True)
    freq_items['length'] = freq_items['itemsets'].apply(lambda x: len(x))
    length = freq_items.iloc[-1]['length']
    l = freq_items.loc[freq_items['length'] == length]
    names=[]
    for i in l.itemsets:
        for j in i:
            if j not in names:
                names.append(j)
    return names

@app.route('/')
def hello():
    return render_template("home.html")

@app.route('/submit', methods=["POST"])
def login():
    if request.method == 'POST':
        user=request.form['custid']
        user=int(user)
        nm = draw_result(user)
        return render_template('result.html', data=nm)

if __name__ == "__main__":
    app.run(debug=True, port=4000)