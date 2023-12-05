import os
import json
import openai
from dotenv import load_dotenv

class RecMeGPT:
    """
    A class to interact with OpenAI's ChatGPT model with the purpose of getting several media and entertainment
    recommendations based of the input of the user.
    """

    def __init__(self):
        # Load environment variables from the .env file
        load_dotenv('config.env')

        # Retrieve the OPENAI_API_KEY environment variable
        self.api_key = os.getenv("OPENAI_API_KEY")

        # Set the retrieved API key for the OpenAI library
        openai.api_key = self.api_key

        # The first version of the prompt I fined tuned to come up with the result I wanted, very verbose but tried to be as clear as possible
        # 270 tokens approx.
        self.role_v1= """
        You are media and entertainment expert, you will receive an input from the user, which could be some other form of media they like
        or themes. You will recommend them 5 videogames, 5 music albums, 5 films, 5 movies and 5 books with have similar vibes, genres or themes.
        You will return this information in a JSON format, where the JSON has 3 initial parameters,
        The first is 'status', which will be set as "OK" if you can find all the recommendations.
        The second is the 'header', where you tell the user why they could like the recommendations, no more than 30 words.
        The third is the recommendations, set as "recs", as an array of 5 objects, each for every form of media (albums, games, movies, tv and books in that order),
        each of those objects will have another array of objects, representing the recommendations,
        each recommendation object will have 2 parameters, title and description. 
        The recommendation description will not be longer than 30 words.
        You will not skip any media for recommendations.
        In case the user input doesn't make sense or you cannot deliver all the recommendations, 
        make the recommendations set to an array empty, the header empty and the status as "NOK".
        """

        #second version of the prompt, tried to do it with less words (tokens) and used directly the json format I wanted
        #195 tokens approx.
        self.role_v2="""
        Given the user input, return a JSON with 5 recommendations of each media, the JSON will have the next format
        {
            "status": , /*set to "OK" all recommendations can be found and input makes sense, set as "NOK" otherwise */
            "header": , /*30 words or less as to you recommended this, set empty if status is "NOK"*/
            "recs": {                 
                /*
                Create 5 objects like this for albums, games, movies, tv and books:
                {"title:" /*include author or artists if it applies*/ , "description": /*cool description, 30 words or less*/}
                */
                /*music albums*/
                "albums": [
                ],
                /*Videogames*/
                "games": [                  
                ],
                "movies": [                   
                ],
                /*TV Shows*/
                "tv": [                   
                ],                
                "books": [                   
                ]
            }
        }
        """

    def request_recommendation(self, user_input, prompt_version=1):
        """
        Make a request to the OpenAI API to make the arguments.
        Args:
        - user_input (str): The input by the user representing what they like and want to get recommendations based off.
        - prompt_version (int, optional): the version of the prompt used as role in the gpt model, defaults as 1.

        Returns:
        - dict: The response content from the OpenAI API with the recommendations.
        """
        # Create a chat completion with the provided message and role
        try:
            if prompt_version == 1:
                role = self.role_v1
            elif prompt_version == 2:
                role = self.role_v2
            else:
                role = self.role_v1

            response = openai.chat.completions.create(
                model="gpt-3.5-turbo-1106",
                response_format={ "type": "json_object" },
                messages=[
                    {"role": "system", "content": role},
                    {"role": "user", "content": user_input}
                ]
            )
            return json.loads(response.choices[0].message.content)

        except Exception as e:
            # Set to data to false in case there was an exception
            print(e)
            return False
