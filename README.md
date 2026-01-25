# Text-to-SQL LLM App 🚀

An intelligent Streamlit application that converts natural language questions into SQL queries using Google's Gemini AI. Simply ask questions in plain English, and the app will generate and execute SQL queries against a student database, displaying results in an interactive format.

## ✨ Features

- **Natural Language to SQL**: Ask questions in plain English and get SQL queries automatically generated
- **AI-Powered**: Leverages Google's Gemini 3 Flash model for intelligent query generation
- **Interactive UI**: Clean and user-friendly Streamlit interface
- **Real-time Results**: Instantly see query results displayed in a formatted table
- **Student Database**: Pre-configured SQLite database with student information (name, class, section, marks)

## 🎯 Capabilities

The app can answer various types of questions about the student database:

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
- **Custom Queries**: Any question about students, classes, sections, or marks

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **AI Model**: Google Gemini 3 Flash Preview
- **Database**: SQLite
- **Data Processing**: Pandas
- **Language**: Python 3

## 📋 Prerequisites

- Python 3.7 or higher
- Google API Key for Gemini AI
- pip (Python package manager)

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
   - Add your Google API key:
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```
   - Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

5. **Initialize the database** (if not already done):
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

3. **Ask questions**:
   - Type your question in natural language in the input field
   - Click "Ask the question" button
   - View the generated SQL query result in the table below

## 📊 Database Schema

The application uses a SQLite database (`student.db`) with the following structure:

**STUDENT Table**:
- `NAME` (VARCHAR): Student's name
- `CLASS` (VARCHAR): Class name (e.g., "Data Science", "DevOps")
- `SECTION` (VARCHAR): Section identifier (A, B, C, etc.)
- `MARKS` (INT): Student's marks

## 🔧 Project Structure

```
text-to-sql_llm_app/
├── app.py              # Main Streamlit application
├── sql.py              # Database initialization script
├── student.db          # SQLite database file
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (create this)
└── README.md          # This file
```

## 💡 How It Works

1. **User Input**: User enters a natural language question
2. **AI Processing**: The question is sent to Google Gemini AI with a carefully crafted prompt
3. **SQL Generation**: Gemini generates an appropriate SQL query based on the question
4. **Query Execution**: The generated SQL is executed against the SQLite database
5. **Result Display**: Results are formatted as a pandas DataFrame and displayed in Streamlit

## 🎨 Example Workflow

```
User Question: "What is the average marks of the students?"
    ↓
AI Generates: SELECT AVG(MARKS) FROM STUDENT;
    ↓
Query Executed: Returns average marks value
    ↓
Display: Shows result in interactive table
```

## 🔒 Security Notes

- Never commit your `.env` file to version control
- Keep your Google API key secure and private
- The `.env` file should be listed in `.gitignore`

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📝 License

This project is open source and available for educational purposes.

## 🙏 Acknowledgments

- Google Gemini AI for the powerful language model
- Streamlit for the amazing framework
- The open-source community

---

**Made with ❤️ using Streamlit and Google Gemini AI**
