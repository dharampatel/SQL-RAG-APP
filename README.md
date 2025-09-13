# Unlocking Knowledge with AI: Q&A App Using SQLite & Chroma DB

This project demonstrates how to build a Question & Answer (Q&A) application using **SQLite** for database management and **Chroma DB** for vector search capabilities. This Q&A app allows users to query knowledge stored in your custom database and retrieve accurate, context-based answers using AI-powered techniques.

### 🔍 **Overview**
In this project, we’ll walk through how to combine traditional relational databases (SQLite) with cutting-edge vector databases (Chroma DB) to create a simple yet powerful Q&A application that leverages AI for contextual retrieval. 

The system is designed to be extensible, allowing you to scale it with different data sources or enhance its capabilities with more advanced AI models.

---

### 🚀 **Features**

- **AI-Powered Q&A**: Answers are generated using AI models based on data stored in a relational database.
- **SQLite Integration**: Use SQLite for lightweight, efficient, and portable data storage.
- **Chroma DB Integration**: Store and retrieve data using Chroma DB’s vector search capabilities for better context-aware results.
- **Easy Setup**: Detailed steps for setting up and deploying the Q&A application.
- **Customizable**: You can modify the dataset or integrate other AI models to suit your needs.

---

### 📌 **Getting Started**

Follow these steps to get the Q&A app up and running locally:

#### 1. Clone the Repository
```bash
git clone https://github.com/dharampatel/SQL-RAG-APP.git
```

# Unlocking Knowledge with AI: Q&A App Using SQLite & Chroma DB

This project demonstrates how to build a Question & Answer (Q&A) application using **SQLite** for database management and **Chroma DB** for vector search capabilities. This Q&A app allows users to query knowledge stored in your custom database and retrieve accurate, context-based answers using AI-powered techniques.

### 🔍 **Overview**

In this project, we’ll walk through how to combine traditional relational databases (SQLite) with cutting-edge vector databases (Chroma DB) to create a simple yet powerful Q&A application that leverages AI for contextual retrieval.

The system is designed to be extensible, allowing you to scale it with different data sources or enhance its capabilities with more advanced AI models.

- - -

### 🚀 **Features**

*   **AI-Powered Q&A**: Answers are generated using AI models based on data stored in a relational database.
*   **SQLite Integration**: Use SQLite for lightweight, efficient, and portable data storage.
*   **Chroma DB Integration**: Store and retrieve data using Chroma DB’s vector search capabilities for better context-aware results.
*   **Easy Setup**: Detailed steps for setting up and deploying the Q&A application.
*   **Customizable**: You can modify the dataset or integrate other AI models to suit your needs.

- - -

### 📌 **Getting Started**

Follow these steps to get the Q&A app up and running locally:

#### 1\. Clone the Repository

```
git clone https://github.com/dharampatel/SQL-RAG-APP.git
cd SQL-RAG-APP
```

#### 2\. Install Dependencies

Make sure you have **Python 3.7+** installed. Create a virtual environment and install the required dependencies:

```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```

#### 3\. Set Up Database

Before running the app, you need to set up your **SQLite** database and the **Chroma DB** instance. Follow these steps:

*   **SQLite**: Create your SQLite database and populate it with data (details are in the `database.py`).
*   **Chroma DB**: Set up the Chroma DB configuration for vector storage (details in the `vectorStore.py`).

#### 4\. Running the Application

Once the setup is complete, you can start the application by running the following command:

```
python app.py
```

The app will launch locally on [http://127.0.0.1:5000/](http://127.0.0.1:5000/), and you can begin querying it.

- - -

### 🛠️ **Technologies Used**

*   **Python**: Programming language used for the app.
*   **SQLite**: Lightweight database for storing structured data.
*   **Chroma DB**: Vector database for storing and querying vectorized data.
*   **AI Models**: Utilized for generating context-based responses (details on model integration in `ai_model.py`).

- - -

### 📑 **File Structure**

```
/SQL-RAG-APP
│
├── /app.py               # Main application file
├── /database.py    # Script to set up SQLite database
├── /vectorStore.py     # Chroma DB configuration
├── /requirements.txt     # Python dependencies
├── /config.py          # AI model integration
└── /README.md            # This README file
```

- - -

### 💡 **How It Works**

*   **Data Ingestion**: Data is stored in the SQLite database, from where it’s extracted and vectorized using Chroma DB.
*   **Vector Search**: When a user asks a question, the system converts the query into a vector and performs a search in Chroma DB to find the closest match.
*   **AI Integration**: The retrieved data is then processed by the AI model to generate a relevant answer.

- - -

### 🔧 **Customization**

*   **Extend Database**: You can add more rows to the SQLite database to expand the knowledge base.
*   **Model Tuning**: If you're familiar with machine learning, feel free to experiment with different models for better Q&A performance.
*   **Deployment**: To deploy the app online, use platforms like Heroku, AWS, or DigitalOcean.

- - -

### 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

- - -

### 📚 **Resources**

*   [Medium Blog Post: Unlocking Knowledge with AI](https://medium.com/@dharamai2024/unlocking-knowledge-with-ai-a-step-by-step-guide-to-building-a-q-a-app-using-sqlite-chroma-db-c0974056d4d1)
*   [Chroma DB Documentation](https://www.trychroma.com/docs)
*   [SQLite Documentation](https://www.sqlite.org/docs.html)
