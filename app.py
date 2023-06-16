from flask import Flask, request, render_template, session
from matplotlib import pyplot as plt


## Langchain
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

import pandas as pd

from dotenv import load_dotenv
import os
# Load the .env file
load_dotenv()
# Now you can access the OPENAI_API_KEY as an environment variable
openai_api_key = os.getenv('OPENAI_API_KEY')
# Check if OPENAI_API_KEY was loaded correctly
if openai_api_key is not None:
    print("OPENAI_API_KEY was loaded correctly")
else:
    print("Failed to load OPENAI_API_KEY")





## check which model it is
# llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
llm = OpenAI(model_name="gpt-3.5-turbo", temperature=0)

# agent = create_csv_agent(llm, 'iMorning_test.csv', verbose=True)
agent = create_csv_agent(llm, 'iMorning_test.csv')


## Flask App
app = Flask(__name__)
app.secret_key = 'your secret key'
# app.secret_key = 'afsdfdsagfsgaregfdgvbarvf'


@app.route('/', methods=['GET', 'POST'])
def home():
    if 'history' not in session:
        session['history'] = []
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        user_input_adjusted = user_input + '(do not generate charts or tables; write all results in plain text)'
        answer = agent.run(user_input_adjusted)  # replace this with your actual LangChain agent call
        session['history'].append((user_input, answer))
        session.modified = True
        return render_template('home.html', history=list(reversed(session['history'])))
    return render_template('home.html', history=list(reversed(session['history'])))

if __name__ == '__main__':
    app.run(debug=True)

## Sample Questions
# - What is the YearToDate sales for each item_name?
# - Total YearToDate sales amount by vendor
# - Total YearToDate sales amount group by item_name, descending order
# - Total YearToDate sales amount by vendor, this year compared with last year, calculate percentage change
# - Percentage change in YearToDate sales for all items, compared with last year? Exclude items whose YearToDate sales from last year was 0 or null.


## Sample Results
# Question: Percentage change in YearToDate sales for all items, compared with last year? Exclude items whose YearToDate sales from last year was 0 or null.

# Answer: Average percentage change in YearToDate sales for all items, compared with last year (excluding items with YearToDate sales from last year as 0 or null): 13.98%

# Question: Total YearToDate sales amount by vendor, this year compared with last year, calculate percentage change

# Answer: Total YearToDate sales amount by vendor, this year compared with last year, calculate percentage change: - Supplier133: 43.44% - Supplier135: -3,826,975% - Supplier196: 168.31% - Supplier410: 24.40% - Supplier412: Infinity - Supplier426: 14.48%

# Question: Total YearToDate sales amount group by item_name, descending order

# Answer: The total YearToDate sales amount group by item_name, in descending order, is: Item602 2391217.37 Item604 2350357.46 Item603 628152.99 Item605 499407.17 Item601 251400.58 Item606 46294.16 Item610 44180.84 Item618 43559.14 Item607 39419.58 Item608 12062.95 Item609 5352.48 Item612 0.00 Item613 0.00 Item614 0.00 Item617 0.00 Item616 -2.77 Item611 -4.72 Item615 -11.19

# Question: Total YearToDate sales amount by vendor

# Answer: Supplier133: 83600.42, Supplier135: 499407.17, Supplier196: 2367770.12, Supplier410: 3270755.03, Supplier412: 43559.14, Supplier426: 46294.16

# Question: What is the YearToDate sales for each item_name?

# Answer: Item601 251400.58 Item602 2391217.37 Item603 628152.99 Item604 2350357.46 Item605 499407.17 Item606 46294.16 Item607 39419.58 Item608 12062.95 Item609 5352.48 Item610 44180.84 Item611 -4.72 Item612 0.00 Item613 0.00 Item614 0.00 Item615 -11.19 Item616 -2.77 Item617 0.00 Item618 43559.14 Name: YearToDate_Sales_ThisYear, dtype: float64