print("lancement du bot...")
import json
import discord

from discord.utils import get

from discord.ext import commands
import random

from discord.ext.commands import has_permissions

bot = commands.Bot(command_prefix='!')
#prefix WTF bugatibugati
#prefix normal !


warnings = {}
idée = {}

#with open('idée.json', 'w') as infile:
    #idée = json.load(infile)

    #print(idée)
 #await bot.change_presence(status=discord.Status.idle,
  #  activity=discord.Game("!helpjc"))

#activity = discord.Game(name="!helpjc", type=3)
 #   await bot.change_presence(status=discord.Status.idle, activity=activity
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="!helpjc"))

    print("bot pret")


    print("coucou")

#actyvities = le plus bg des bot discord

@bot.event
async def on_raw_reaction_add(payload):
    emoji = payload.emoji.name
    canal = payload.channel_id
    message = payload.message_id
    roles = bot.get_guild(payload.guild_id).roles
    python_role = get(roles, name="python")
    membre = bot.get_guild(payload.guild_id).get_member(payload.user_id)

    if canal == 740829207898095627 and message == 740829995378802718 and emoji == "PythonPNGFile":

        print("grade ajoutée !")
        await membre.add_roles(python_role)
        await membre.send("tu obtient le grade python!")

@bot.event
async def on_raw_reaction_remove(payload):
    emoji = payload.emoji.name
    canal = payload.channel_id
    message = payload.message_id
    roles = bot.get_guild(payload.guild_id).roles
    python_role = get(roles, name="python")
    membre = bot.get_guild(payload.guild_id).get_member(payload.user_id)


    if canal == 740829207898095627 and message == 740829995378802718 and emoji == "PythonPNGFile":

        print("grade supprimé !")
        await membre.remove_roles(python_role)
        await membre.send("tu perds le grade python!")

#@bot.command()
#async def fortnite(ctx):
    #await ctx.send("aimes tu Fortnite? tape oui, non, ? ou "")
#réponse_utilisateur =

@bot.command()
async def infosjc(ctx):
    await ctx.send("Bonjour, Je suis un bot, On m'appelle JCBOT parce que.....\nBah parce que j'ai été crée par jcbevc t'es con ou quoi xD (je m'excuse pour cette insolance mais en même temps j'ai été programé comme ça)\nToi, oui toi, tu peut me parler en commançant tes message par un !")

@bot.command()
async def resaux_sociaux(ctx):
    await ctx.send("")

@bot.command()
async def trotroll(ctx):
    await ctx.send("")

#on client.on('message', message => {

             #   message.author.send("Bonjour, je suis ton bot");
              #  });

@bot.command()
async def hey_jcbot(ctx, membre : discord.Member):
    pseudo = membre.mention
    await ctx.send(f"hey {pseudo} ça va? moi je vais bien.\ntu peux faire !helpjc pour avoir la liste des commandes")



@bot.command()
async def helpjc(ctx):
    await ctx.send("les commandes sont pour l'instant :\n1 !bienvenue @pseudo\n2 !infosjc\n3 !idée\n4 !surpends_moi")
#!helpjcadmin(pour les admins)
@bot.command()
async def idée(ctx):
    await ctx.send("j'ai vraiment plus d'idée pour mon bot, si vous avez des idées pour rajouter des commandes je suis preneur.\nvous pouvez me donner des idées en mp")

#    with open('warnings.json', 'w') as outfile:
        #json.dump(warnings, outfile)
@bot.command()
async def monidée(ctx):


#@bot.command()
#@commands.has_permissions(administrator=True)
#async def helpjcadmin(ctx, payload):
    #canal = payload.channel_id
    #if canal == 666326950909837334:
        #await ctx.send("les commandes admins sont pour l'instant :\n1 !warn @pseudo")

#@helpjcadmin.error
#async def on_command_error(ctx, error):
    #if isinstance(error, commands.MissingPermissions):
        #await ctx.send("tu n'as pas les perms")


    @bot.command()
    async def regles(ctx):
        await ctx.send("les regles sont : va voir le #règlement")

#warning
@bot.command()
@commands.has_permissions(administrator=True)
async def warn(ctx, membre: discord.Member):
    pseudo = membre.mention
    id = membre.id

    if id not in warnings:
        warnings[id] = 0
        print("le menbre n'as aucun avertissement")
    warnings[id] += 1
    print("ajoute un avertissement", warnings[id], "/3")

    if warnings[id] == 3:
        warnings[id] = 0
        await membre.send("vous avez été éjecte du serveur ! trop d'avertissement!")
        await membre.kick()

    with open('warnings.json', 'w') as outfile:
        json.dump(warnings, outfile)

    await ctx.send(f"le membre {pseudo} a reçu une alerte ! attention a bien respecter les regles")

@warn.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("tu dois faire !warning @pseudo")

#@bot.command()
#async def motherlode(payload):
 #   membre = bot.get_guild(payload.guild_id).get_member(payload.user_id)
  #  id = membre.id
   # await membre.send("ton niveau de warn descends a 0")
    #warnings[id] = 0



@bot.command()
async def bienvenue(ctx, nouveau_membre:discord.Member):
    pseudo = nouveau_membre.mention
    await ctx.send(f"Bienvenue à {pseudo} sur le serveur discord ! n'oublie pas d'aller checker les règles dans le #règlement")

@bienvenue.error
async def on_command_error(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("la commande est : !bienvenue @pseudo")

#@bot.command()
#async def surpends_moi(ctx):
    #insolite = ["L’iPhone est 100 000 fois plus puissant que l’ordinateur d’Apollo 11:\nConcrètement, votre iPhone pourrait gérer 120 millions de missions lunaires simultanément.\n\nvoilà"]
    #await ctx.send(random.choice(insolite)

jeton = "NzM5OTIzOTU5MjQ3NTM2MTQ4.Xyhh4w.atjpfCdw723F4zGZHt5IBDXmt9g"

bot.run(jeton)

