import googletrans
from googletrans import Translator

# print(googletrans.LANGUAGES)

class TranslatorCore(object):

    ourDefaultLang = 'ru'
    theirsDefaultLang = 'en'
    translator = Translator()

    def translate(self, text):
        translated = self.translator.translate(text, dest=self.theirsDefaultLang)
        if translated.src == 'en':
            translated = self.translator.translate(text, dest=self.ourDefaultLang)
        return translated.text
