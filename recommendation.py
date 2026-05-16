from google import genai
from google.genai import errors
import os
import json
from shared.shared_vars import EnhancedEncoder
from dotenv import load_dotenv

os.environ['GRPC_VERBOSITY'] = 'NONE'
os.environ['GLOG_minloglevel'] = '2'

load_dotenv()

class error_message:
    def __init__(self,message):
        self.text=message
key=os.getenv("API_KEY")

client = genai.Client(api_key=key) 

def get_recommendation(fav, ingd, m, pref, adr):
    try:
        prompt = f"""Here is information about the user's favorite foods, the menu, ingredients of the items in the menu, additional preferences, and their allergies/dietary restrictions
        menu: {json.dumps(dict(m),separators=(',', ':'),cls=EnhancedEncoder)}
        Favorite Foods: {list(fav)}
        ingredients: {dict(ingd)}
        preferences: {pref}
        allergies/dietary restrictions: {list(adr)}
        TASK:
        Recommend a meal for breakfast,lunch,and dinner that is in the menu. If there is a dessert for that night, give your recommendation as well. Do not recommend any item that has an allergy or dietary restrction. Do not output anything that isn't the meal, information about the meal, and the reason why it was chosen
        """
        
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt
        )
    except errors.ServerError:
        return error_message("Model is busy, please try again.")
    except errors.ClientError:
        return error_message("Request limit exceeded, try again later")
    return response
