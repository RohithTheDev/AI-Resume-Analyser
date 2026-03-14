# AI Resume Analyser

An AI-powered web application that analyzes resumes using Google's Gemini AI to provide constructive feedback and improvement suggestions.

## Features

- Upload PDF or text resume files
- AI analysis focusing on content clarity, skill presentation, experience description, and job-specific improvements
- User-friendly Streamlit interface
- Free to use with Google Gemini API

## Requirements

- Python 3.12 or higher
- Google AI API key (free tier available)
- Internet connection for AI analysis

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/RohithTheDev/ai-resume-analyser.git
   cd ai-resume-analyser
   ```

2. Install dependencies using uv (recommended):
   ```bash
   uv sync
   ```

   Or using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add your Google AI API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

   Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey).

## Usage

1. Activate the virtual environment:
   ```bash
   uv run streamlit run main.py
   ```

   Or if using pip:
   ```bash
   streamlit run main.py
   ```

2. Open your browser to `http://localhost:8501`

3. Upload your resume (PDF or TXT format)

4. Optionally enter the job role you're applying for

5. Click "Analyse Resume" to get AI-powered feedback

## How It Works

1. **File Upload**: Users upload their resume in PDF or text format
2. **Text Extraction**: The app extracts text content from the uploaded file using PyPDF2 for PDFs
3. **AI Analysis**: The extracted text is sent to Google's Gemini 2.5 Flash model with a structured prompt
4. **Feedback Generation**: The AI analyzes the resume based on:
   - Content clarity and impact
   - Skill presentation
   - Experience description
   - Job-specific improvements
5. **Results Display**: Constructive feedback and recommendations are displayed in the app

## Project Structure

```
ai-resume-analyser/
├── main.py              # Main Streamlit application
├── pyproject.toml       # Project configuration and dependencies
├── README.md            # This file
├── .gitignore           # Git ignore rules
├── .env                 # Environment variables (API keys)
└── .venv/               # Virtual environment (created by uv/pip)
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source. Please check the license file for details.

## Disclaimer

This tool provides AI-generated suggestions and should be used as a supplement to professional career advice. Always review and customize feedback based on your specific situation.