# RecMeGPT

## Overview
This Python app provides media recommendations in response to user input. It fetches recommendations for videogames, music albums, films, TV shows, and books.


## Features
- Generates media recommendations for videogames, music albums, films, TV shows, and books.
- Recommendations are provided in a structured JSON format.
- Utilizes external APIs to fetch media recommendations.

## Installation
1. Clone the repository:
```sh
   git clone https://github.com/litepast/RecMeGPT.git
```

2. Navigate to the project folder
  ```sh
     cd RecMeGP
  ```

3. Create a new Virtual Environment
  ```sh
     python3 -m venv .venv
  ```
4. Install all the libraries from requirements.txt
  ```sh
     pip install -r requirements.txt
  ```
5. Create .env file with OpenAI APÏ
 ```sh
    OPENAI_API_KEY=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
  ```


## Usage


## Model Response

The app provides recommendations in a JSON format. The response includes:
    status: Indicates the success of the recommendation retrieval process (OK or NOK).
    header: A brief description of why the recommendations are suitable.
    recs: An array containing recommendations for videogames, music albums, films, TV shows, and books.

## YouTube Video on the app
  
 
   
