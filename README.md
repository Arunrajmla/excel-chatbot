# Data-Driven Chatbot for Excel Insights

A Flask-based chatbot designed to provide quick and accurate insights from an Excel dataset through natural language queries. This project simplifies data retrieval and analysis, enabling non-technical users to access key information without manual effort.

## Features

- **Natural Language Queries**: Ask questions like "What are the total sales?" or "What is the price of Product X?" and receive instant responses.
- **Dynamic Data Filtering**: Retrieve data based on categories, product names, or other attributes defined in the dataset.
- **Excel Data Integration**: Processes and interacts with Excel files using `pandas`, ensuring seamless data handling.
- **RESTful API**: Exposes an endpoint (`/ask`) to handle user queries and return JSON responses.
- **Built-in Error Handling**: Provides meaningful feedback for invalid or unsupported queries.

## Technologies Used

- **Programming Languages**: Python (Flask, Pandas)
- **Tools**: REST API, Excel

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Arunrajmla/excel-chatbot.git
   cd excel-chatbot
   ```

2. **Install Dependencies**:
   Make sure you have Python installed. Then, install the required libraries:
   ```bash
   pip install flask pandas openpyxl
   ```

3. **Prepare Your Dataset**:
   Place your Excel file in the project directory. Update the `data_file` variable in the code with the file's name:
   ```python
   data_file = 'your_data_file.xlsx'  # Replace with your Excel file name
   ```

4. **Run the Application**:
   Start the Flask server:
   ```bash
   python app.py
   ```
   The server will be available at `http://127.0.0.1:5000`.

5. **Test the API**:
   Use tools like Postman or curl to send a POST request to the `/ask` endpoint with a JSON payload:
   ```json
   {
       "question": "What are the total sales?"
   }
   ```

## Example Queries

- "What are the total sales?"
- "Show data for category Electronics."
- "What is the price of Product A?"

## Example Response

For a query like "What are the total sales?":
```json
{
    "answer": "The total sales are 12345."
}
```

## Key Highlights

- Simplifies workflows by enabling natural language interaction with data.
- Eliminates manual efforts for retrieving and analyzing data from Excel files.
- Scalable and adaptable for different datasets and business requirements.

## License

This project is open-source and available under the MIT License.

## Author

**Arunraj Katturaja**

Feel free to reach out for any questions or collaboration opportunities!
