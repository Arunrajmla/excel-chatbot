import pandas as pd
from flask import Flask, request, jsonify

# Load Excel Data
data_file = '2025 data.xlsx'  # Path to your Excel file
df = pd.read_excel(data_file)

# Initialize Flask App
app = Flask(__name__)


# Helper Function to Process Questions
def process_question(question, df):
    question = question.lower()

    # Example: Fetch Total Sales
    if "total sales" in question:
        total_sales = df['user_count'].sum()
        return f"The total sales are {total_sales}."

    # Example: Filter by Category
    elif "category" in question:
        category = question.split("category ")[-1]
        filtered_data = df[df['Category'].str.lower() == category]
        if filtered_data.empty:
            return f"No data found for category '{category}'."
        else:
            return filtered_data.to_dict(orient='records')

    # Example: Get Price for a Product
    elif "price of" in question:
        product_name = question.split("price of ")[-1]
        filtered_data = df[df['Product Name'].str.lower() == product_name]
        if not filtered_data.empty:
            price = filtered_data['Price'].values[0]
            return f"The price of {product_name} is {price}."
        else:
            return f"Product '{product_name}' not found."

    # Default Response
    return "Sorry, I didn't understand your question."


# Flask Endpoint for the Bot
@app.route('/ask', methods=['POST'])
def ask_bot():
    data = request.json
    question = data.get('question', '')

    # Process the question and get an answer
    answer = process_question(question, df)
    return jsonify({"answer": answer})


# Run the App
if __name__ == '__main__':
    app.run(debug=True)
