from googletrans import Translator, LANGUAGES

song = '''
You say you love me, I say you crazy
We're nothing more than friends
You're not my lover, more like a brother
I known you since we were like ten, yeah
Don't mess it up, talking that shit
Only gonna push me away, that's it
When you say you love me, that make me crazy
Here we go again
''' #any song lyrics here

my_languages = ['en','ur','hi','mr','ar']

for language in my_languages:
    t = Translator().translate(song, dest= language)
    print(language + ' - ' + LANGUAGES[language])
    print(t.text)
    song = t.text
    print()
