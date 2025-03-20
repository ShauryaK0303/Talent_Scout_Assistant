# TalentScout Hiring Assistant

An intelligent chatbot for initial candidate screening in the tech recruitment industry.

## Project Overview

TalentScout is an AI-powered hiring assistant designed to streamline the initial screening process for technical candidates. The chatbot collects essential information from candidates and generates relevant technical questions based on their declared tech stack.

### Key Features

- Collects candidate information (name, contact details, experience, etc.)
- Generates tailored technical questions based on the candidate's tech stack
- Maintains conversation context for a natural interaction
- Securely handles candidate data
- Provides a clean and intuitive user interface

## Installation Instructions

### Prerequisites

- Python 3.8+
- Gemini API key

### Setup

1. Clone the repository:
   ```
   git clone https://github.com/ShauryaK0303/talent_scout_assistant.git
   cd talent_scout_assistant
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your Gemini API key:
   ```
   GEMINI_API_KEY=your_openai_api_key_here
   ```

## Usage Guide

1. Start the application:
   ```
   streamlit run app.py
   ```

2. Open your web browser and navigate to the URL displayed in the terminal (typically http://localhost:8501)

3. The chatbot will guide you through the screening process, asking for your information and technical questions based on your expertise.

4. To end the conversation, simply type "goodbye", "exit", or "quit".

## Technical Details

### Libraries Used

- **Streamlit**: For building the web interface
- **Gemini API**: For generating intelligent responses
- **python-dotenv**: For managing environment variables

### Architecture

The application follows a modular structure:

- `app.py`: Main Streamlit application
- `config.py`: Configuration settings
- `utils/`: Utility functions for LLM interactions, prompt handling, and data processing
- `components/`: UI components for the chat interface

### Prompt Design

The prompt engineering approach focuses on:

1. **System Instructions**: Clear guidance for the LLM on its role and conversation flow
2. **Information Gathering**: Structured prompts to collect candidate information
3. **Technical Question Generation**: Contextual prompts that generate relevant technical questions based on the candidate's tech stack
4. **Conversation Management**: Maintaining context throughout the interaction

## Challenges & Solutions

### Challenge 1: Maintaining Conversation Context
- **Solution**: Implemented a session state mechanism in Streamlit to persist conversation history

### Challenge 2: Extracting Structured Information
- **Solution**: Used regex patterns to extract candidate information from natural language responses

### Challenge 3: Generating Relevant Technical Questions
- **Solution**: Created specialized prompts that focus the LLM on generating questions specific to the candidate's declared technologies

## Future Enhancements

- Sentiment analysis to gauge candidate engagement
- Multi-language support
- Integration with applicant tracking systems
- Enhanced data visualization for recruiters

## License

This project is licensed under the  License - see the LICENSE file for details.
