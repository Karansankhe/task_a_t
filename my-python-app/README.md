# My Python App

This project is a Smart Document QA Assistant that allows users to upload documents, ask questions, and receive answers in their preferred language. The application utilizes various APIs for document processing, translation, and text-to-speech functionalities.

## Project Structure

```
my-python-app
├── src
│   ├── main.py               # Entry point of the application
│   ├── config.py             # Configuration settings and environment variable loading
│   ├── ui.py                 # User interface handling with Streamlit
│   ├── document_processing.py # Functions for processing uploaded documents
│   ├── qa.py                 # Question-answering functionality
│   ├── translation.py         # Translation handling
│   ├── tts.py                # Text-to-speech functionality
│   ├── utils.py              # Utility functions
│   └── types
│       └── __init__.py       # Custom types and data structures
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd my-python-app
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

5. **Set up environment variables:**
   Create a `.env` file in the root directory and add your API keys:
   ```
   GOOGLE_API_KEY=<your_google_api_key>
   SARVAM_API_KEY=<your_sarvam_api_key>
   ```

## Usage

To run the application, execute the following command:
```
streamlit run src/main.py
```

Open your web browser and navigate to `http://localhost:8501` to access the application.

## Features

- Upload and process PDF and image documents.
- Ask questions about the uploaded documents.
- Receive answers in your preferred language.
- Translate answers and generate voice output.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.