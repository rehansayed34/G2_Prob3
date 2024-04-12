# Automated Product Description Generation

## Overview

Automate the process of updating product descriptions on websites with the help of web scraping and Large Language Model (LLM) APIs. This project streamlines the creation of accurate and concise product descriptions by extracting information from provided URLs and utilizing pre-trained LLMs via their APIs.

## Approach

### Web Scraping:
Utilize Python with BeautifulSoup to extract product details from URLs.

### LLM APIs:
Leverage OpenAI GPT API or similar pre-trained LLMs to generate succinct descriptions directly from the extracted content.

## Tech Stack

- **Web Scraping:** Python with BeautifulSoup4
- **LLM APIs:** OpenAI GPT API or similar

## Usage

1. **Install Dependencies:** Ensure required libraries are installed.
    ```bash
    pip install streamlit==0.89.0 beautifulsoup4==4.10.0
    ```

2. **Run the Application:** Execute the provided Streamlit application.

3. **Input URL:** Enter the URL of the webpage containing product details.

4. **Process URL:** Click the button to initiate the web scraping and description generation process.

5. **View Generated Description:** The generated product description will be displayed.
