# RecMeGPT

## Overview
RecMeGPTs delivers you media recommendations in response to your input! How many times have you played a videogame, watched a movie or show, read a book, listened to an album and kept an itch for more things based on the media, art and entertainment you just loved? I know I have! I watched 'Oppenheimer' and I loved it and went on a 3-week journey to read about the history of nuclear energy. That's the power good art can have on you. With that in mind, I channeled the power of ChatGPT to recommend videogames, music albums, films, TV shows and books based on the input of the user, with useful links to learn more about them.
It doesn't stop with entertainment, you can enter a theme or descriptor, something like 'Optimism' or 'Melancholy' and it will give you recommendations with that theme. So enjoy!


## Features
- Generates media recommendations for videogames, music albums, films, TV shows, and books.
- Provides links to learn more about each recommendation.

## Installation
1. Clone the repository:
```sh
git clone https://github.com/litepast/RecMeGPT.git
```
2. Navigate to the project folder
  ```sh
  cd RecMeGPT
  ```
3. Create a new Virtual Environment
  ```sh
  python -m venv .venv
  ```
4. Activate Virtual Environment (linux/windows)
  ```sh
  python -m venv .venv
  ```
  ```sh
  .venv\Scripts\activate.bat
  ```
5. Install all the libraries from requirements.txt
  ```sh
  pip install -r requirements.txt
  ```
6. Create a .env file with OpenAI APÏ
 ```sh
 OPENAI_API_KEY=Your_api_key
  ```

## Usage
1. Start the Jupyter Notebook server with either command on the project folder
   ```sh
    python -m notebook
   ```
   ```sh
      jupiter notebook
   ```
2. Open the notebook file
   Once the jupyer server is started (which might look something like http://localhost:8889/tree), open the `recmegpt_notebook.ipynb` file.

3. Run all cells
   Click on the 'Run All Cells' on the menu 'Run' so the libraries and modules are loaded

4. Enter your input and get the recommendations!
   At the bottom of cell #3, there will be a textbox and one button, something you like, or anything really, then click the button to try to get the recommendations powered by chatGPT! Each recommendation wil have a description and a link to a site where you can learn more about it.


## Model Response

The app provides recommendations in a JSON format. The response includes:
- status: Indicates the success of the recommendation retrieval process (OK or NOK).
- header: A brief description of why the recommendations are suitable.
- recs: An array containing recommendations for videogames, music albums, films, TV shows, and books, each with their title and a descrption

## YouTube Video with the project running
  
 
   
