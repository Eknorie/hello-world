import datetime

current_hour = datetime.datetime.now().hour

if 5 <= current_hour < 12:
    greeting_en = "Good morning"
    greeting_es = "Buenos días"
    greeting_fr = "Bonjour"
elif 12 <= current_hour < 18:
    greeting_en = "Good afternoon"
    greeting_es = "Buenas tardes"
    greeting_fr = "Bon après-midi"
else:
    greeting_en = "Good evening"
    greeting_es = "Buenas noches"
    greeting_fr = "Bonsoir"

print(f"{greeting_en}, Hello World")  # English
print(f"{greeting_es}, Hola Mundo")  # Spanish
print(f"{greeting_fr}, Bonjour le monde")  # French