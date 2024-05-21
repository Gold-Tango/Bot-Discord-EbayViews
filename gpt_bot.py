import discord
import openai
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Récupérer les tokens
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Définir la clé API d'OpenAI
openai.api_key = OPENAI_API_KEY

# Créer une instance de client Discord avec les intents nécessaires
intents = discord.Intents.default()
intents.messages = True  # Activer l'intent pour les messages
intents.guilds = True    # Activer l'intent pour les informations de guildes
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!chat'):
        prompt = message.content[6:]  # Supprimer le préfixe '!chat' du message

        try:
            response = openai.ChatCompletion.create(
                model="text-davinci-003",  # Spécifier le modèle à utiliser
                messages=[{"role": "system", "content": "Vous êtes un assistant virtuel très utile."},
                          {"role": "user", "content": prompt}]
            )
            await message.channel.send(response.choices[0].message['content'])
        except Exception as e:
            await message.channel.send(f"Une erreur s'est produite: {e}")

client.run(DISCORD_TOKEN)