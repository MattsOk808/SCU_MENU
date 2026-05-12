from google import genai
from google.genai import errors
import os
import json
from shared_vars import EnhancedEncoder
from dotenv import load_dotenv

os.environ['GRPC_VERBOSITY'] = 'NONE'
os.environ['GLOG_minloglevel'] = '2'

load_dotenv()

class error_message:
    def __init__(self,message):
        self.text=message
key=os.getenv("API_KEY")

client = genai.Client(api_key=key) 

def get_recommendation(fav, ingd, m, d):
    try:
        prompt = f"""Here is information about the user's favorite food, the menu, and ingredients of the items in the menu
        menu: {json.dumps(dict(m[d]),separators=(',', ':'),cls=EnhancedEncoder)}
        Favorite Foods: {list(fav)}
        ingredients: {dict(ingd)}
        TASK:
        Recommend a meal for breakfast,lunch,and dinner that is in the menu
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
