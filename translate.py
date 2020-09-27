import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'great-firewall-translator.json'
from google.cloud import translate_v2 as translate

class Translator():
    def __init__(self):
        self.client = translate.Client()
        self.target = 'zh-CN'
        
    def to_chinese(self, text, source_language='en'):
#         if isinstance(text, six.binary_type):
#             text = text.decode("utf-8")
        
        # Text can also be a sequence of strings, in which case this method
        # will return a sequence of results for each text.
        result = self.client.translate(text, target_language='zh-CN', source_language=source_language)
        return result['translatedText']
