# Text-to-SQL LLM App 🚀

An intelligent Streamlit application that converts natural language questions into SQL queries using Google's Gemini AI. Simply ask questions in plain English, and the app will generate and execute SQL queries against your database, displaying results in an interactive format.

## ✨ Features

- **Natural Language to SQL**: Ask questions in plain English and get SQL queries automatically generated
- **AI-Powered**: Leverages Google's Gemini 3 Flash Preview model for intelligent query generation
- **Multi-Database Support**: Connect to SQLite or PostgreSQL/Amazon Redshift databases
- **Dynamic Schema Detection**: Automatically retrieves and uses database schema information for accurate query generation
- **Interactive UI**: Clean and user-friendly Streamlit interface with database type selection
- **Real-time Results**: Instantly see query results displayed in a formatted table
- **Student Database**: Pre-configured SQLite database with student information (name, class, section, marks)

## 🎯 Capabilities

The app can answer various types of questions about your database:

### Example Questions You Can Ask:

- **Count Queries**: "How many students are in the database?"
- **Aggregate Functions**: 
  - "What is the average marks of the students?"
  - "What is the total marks of the students?"
  - "What is the maximum marks of the students?"
  - "What is the minimum marks of the students?"
- **Top Performers**: "What are the students with the highest marks?"
- **Filtering**: "Show me all students in Data Science class"
- **Sorting**: "List students ordered by their marks"
- **Custom Queries**: Any question about your database tables and columns
- **PostgreSQL/Redshift Queries**: Supports complex queries with schema-qualified table names

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **AI Model**: Google Gemini 3 Flash Preview
- **Database Support**: 
  - SQLite (default)
  - PostgreSQL / Amazon Redshift
- **Database Libraries**: 
  - sqlite3 (for SQLite)
  - redshift-connector (for PostgreSQL/Redshift)
  - SQLAlchemy (for database operations)
- **Data Processing**: Pandas
- **Language**: Python 3

## 📋 Prerequisites

- Python 3.7 or higher
- Google API Key for Gemini AI
- pip (Python package manager)
- For PostgreSQL/Redshift: Database credentials (host, port, database name, username, password)

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd text-to-sql_llm_app
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv texttosqlproject
   source texttosqlproject/bin/activate  # On Windows: texttosqlproject\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Create a `.env` file in the root directory
   - Add your Google API key (required):
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```
   - For PostgreSQL/Redshift connections, also add:
     ```
     DB_USER=your_database_username
     DB_PASSWORD=your_database_password
     DB_HOST=your_database_host
     DB_PORT=your_database_port
     DB_NAME=your_database_name
     ```
   - Get your Google API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

5. **Initialize the SQLite database** (if using SQLite):
   ```bash
   python sql.py
   ```

## 🎮 Usage

1. **Start the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

2. **Open your browser**:
   - The app will automatically open at `http://localhost:8501`
   - Or manually navigate to the URL shown in the terminal

3. **Select Database Type**:
   - Use the sidebar to select between "sqllite" or "postgresql"
   - The app will automatically connect to the selected database type

4. **Ask questions**:
   - Type your question in natural language in the input field
   - Click "Ask the question" button
   - View the generated SQL query result in the table below

## 📊 Database Schema

### SQLite Database

The application includes a pre-configured SQLite database (`student.db`) with the following structure:

**STUDENT Table**:
- `NAME` (VARCHAR): Student's name
- `CLASS` (VARCHAR): Class name (e.g., "Data Science", "DevOps")
- `SECTION` (VARCHAR): Section identifier (A, B, C, etc.)
- `MARKS` (INT): Student's marks

### PostgreSQL/Redshift Database

The app supports PostgreSQL and Amazon Redshift databases. When connecting to PostgreSQL/Redshift:
- The app automatically detects schema information
- Supports schema-qualified table names (e.g., `legacy_dm.fact_live_product_sales`)
- Dynamically retrieves table and column information for accurate query generation

## 🔧 Project Structure

```
text-to-sql_llm_app/
├── app.py              # Main Streamlit application
├── db_connection.py    # Database connection class (supports SQLite and PostgreSQL/Redshift)
├── sql.py              # SQLite database initialization script
├── student.db          # SQLite database file
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (create this)
└── README.md          # This file
```

## 💡 How It Works

1. **Database Selection**: User selects database type (SQLite or PostgreSQL) from the sidebar
2. **Connection**: The app connects to the selected database using the `DatabaseConnection` class
3. **Schema Detection**: The app automatically retrieves schema information (tables and columns)
4. **User Input**: User enters a natural language question
5. **AI Processing**: The question is sent to Google Gemini AI with:
   - A carefully crafted prompt for SQL generation
   - Database schema information for context
   - Database-specific instructions (e.g., schema.table format for PostgreSQL)
6. **SQL Generation**: Gemini generates an appropriate SQL query based on the question and schema
7. **Query Execution**: The generated SQL is executed against the connected database
8. **Result Display**: Results are formatted as a pandas DataFrame and displayed in Streamlit

## 🎨 Example Workflow

```
User selects: SQLite database
    ↓
User Question: "What is the average marks of the students?"
    ↓
AI Generates: SELECT AVG(MARKS) FROM STUDENT;
    ↓
Query Executed: Returns average marks value
    ↓
Display: Shows result in interactive table
```

## 🔧 Database Connection Details

### SQLite Connection
- Automatically connects to `student.db` in the project root
- No additional configuration needed (after running `sql.py`)

### PostgreSQL/Redshift Connection
- Requires environment variables in `.env` file:
  - `DB_USER`: Database username
  - `DB_PASSWORD`: Database password
  - `DB_HOST`: Database host address
  - `DB_PORT`: Database port number
  - `DB_NAME`: Database name
- Uses `redshift-connector` library for connections
- Supports schema-qualified table names (e.g., `schema_name.table_name`)
- Currently configured for `legacy_dm` schema and `fact_live_product_sales` table (can be modified in `db_connection.py`)

## 🔒 Security Notes

- Never commit your `.env` file to version control
- Keep your Google API key and database credentials secure and private
- The `.env` file should be listed in `.gitignore`
- Use environment variables for all sensitive information

## 📦 Dependencies

The project requires the following Python packages (see `requirements.txt`):

- `streamlit`: Web application framework
- `google-generativeai`: Google Gemini AI integration
- `python-dotenv`: Environment variable management
- `sqlalchemy`: Database abstraction layer
- `psycopg2-binary`: PostgreSQL adapter
- `redshift-connector`: Amazon Redshift connection library
- `pandas`: Data manipulation (usually included with above)

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Add support for additional database types

## 📝 License

This project is open source and available for educational purposes.

## 🙏 Acknowledgments

- Google Gemini AI for the powerful language model
- Streamlit for the amazing framework
- The open-source community

---

**Made with ❤️ using Streamlit and Google Gemini AI**
