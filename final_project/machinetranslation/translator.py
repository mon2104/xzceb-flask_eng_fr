import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

#apikey = os.environ['apikey']
apikey = "kxGI9iqBN6HIbG81WbBQkm8gpZRooMCe-BoeVksge6g_"
#url = os.environ['url']
url = "https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/12788802-2ecf-48a5-ba6f-6ed748f97892"
VERSION = '2018-05-01'

authenticator = IAMAuthenticator("kxGI9iqBN6HIbG81WbBQkm8gpZRooMCe-BoeVksge6g_")
language_translator = LanguageTranslatorV3(VERSION, authenticator)
language_translator.set_service_url("https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/12788802-2ecf-48a5-ba6f-6ed748f97892")

def english_to_french(english_text):
    if (english_text == None):
        french_text = None
    else:
        translation_response = language_translator.translate(text = english_text, model_id = 'en-fr')
        translation = translation_response.get_result()
        french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    if (french_text == None):
        english_text = None
    else:
        translation_response = language_translator.translate(text = french_text, model_id = 'fr-en')
        translation = translation_response.get_result()
        english_text = translation['translations'][0]['translation']
    return english_text
    