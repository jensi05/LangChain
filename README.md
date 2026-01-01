# AI Travel Planner

An intelligent travel planning application built with LangChain and Google Generative AI. This app generates personalized travel itineraries based on your preferences.

## Features

- **Customizable Travel Plans**: Generate travel itineraries based on:
  - Origin and destination cities
  - Number of days
  - Budget level (Low, Medium, High)
  - Travel style (Solo, Family, Couple, Friends)

- **AI-Powered Recommendations**: Uses Google's Gemini 2.5 Flash model to create detailed travel plans including:
  - Day-wise itineraries
  - Famous places to visit
  - Local food suggestions
  - Travel tips and recommendations

- **User-Friendly Interface**: Built with Streamlit for an intuitive web interface

## Prerequisites

- Python 3.11 or higher
- Google API Key for accessing Gemini models

## Installation

1. Create a virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
source .venv/bin/activate  # On macOS/Linux
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory and add your Google API key:
```
GOOGLE_API_KEY=your_api_key_here
```

## Usage

### Run the Travel Planner App

```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

### List Available Models

To view all available Google Generative AI models:

```bash
python list_models.py
```

## Project Structure

- `app.py` - Main Streamlit application for the AI Travel Planner
- `list_models.py` - Utility script to list available Google Generative AI models
- `requirements.txt` - Python package dependencies
- `.env` - Environment variables (create this file with your API key)

## Technologies Used

- **Streamlit** - Web application framework
- **LangChain** - Framework for building with LLMs
- **Google Generative AI** - Gemini models for content generation
- **Python-dotenv** - Environment variable management

## Configuration

The app uses the following configuration:
- Model: `gemini-2.5-flash`
- Temperature: 0.7 (balanced creativity and consistency)

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the MIT License.
