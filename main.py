
import discord
from discord.ext import commands
import random
import asyncio
import os
from dotenv import load_dotenv

# gets the verification token from .env file for the bot to connect
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# sets the prefix for the bot commands, and gives it permision to get access to members and other stuff using the intents
intents = discord.Intents().all()
client = commands.Bot(command_prefix="&", intents=intents)

# sets up a global variable for curse loop
cursing = False

# when the bot runs it prints a message that is has gone online in the command prompt
@client.event
async def on_ready():

    print(f'{client.user.name} is online!')

# a simple command that responds when a user says "ayy" used to make sure that it's working
@client.command(
    help="A simple command that mentions you and says lmao.",
    brief="lmao"
)
async def ayy(ctx):

    await ctx.send(f"{ctx.message.author.mention} lmao")

# a command used for debugging makes the bot join plays a sound file and leaves
@client.command(
    help="Used for testing the voice connectivity and if the sound plays correctly; Bot owner only.",
    brief="OWNER: Used for testing sound"
)
@commands.is_owner()
async def testBruh(ctx):

    user = ctx.message.author
    voiceChannel = ctx.message.author.voice.channel
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    print(ctx.guild.voice_channels)
    print("Connected to voicechat!")
    await ctx.send("Connecting...")
    voice.play(discord.FFmpegPCMAudio("bruh.mp3"))
    await asyncio.sleep(3)
    await voice.disconnect()

# forces the bot to leave it's current voice channel
@client.command(
    help="Used for forcing the bot to leave the voice chat in case it is needed or gets stuck; Bot owner only.",
    brief="OWNER: Forces the bot to leave vc"
)
@commands.is_owner()
async def forceLeave(ctx):

    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
        await ctx.send("Leaving Voice Chat...")
    else:
        await ctx.send("I'm not connected to a voice channel right now.")

# the main command: marks a member that is currently in a voice channel, if it can join it will go into a while loop
# from where it joins in random intervals plays a soundfile and leaves untill a new mark is called or cleanse is called
@client.command(
    help="Curses a user, meaning that whenever they join a voice chat the bot joins them and says bruh randomly.",
    brief="joins to say bruh to the target randomly"
)
async def curse(ctx, user: discord.User):

    global cursing
    cursing = True
    await ctx.send("***UWU?*** ")
    mark = ctx.guild.get_member(user.id)

    while cursing:

            waitTime = random.randint(5,900)
            print(waitTime)
            await asyncio.sleep(waitTime)

            if (mark.voice != None and cursing):
                await mark.voice.channel.connect()
                print("Connected to voicechat!")
                voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
                voice.play(discord.FFmpegPCMAudio("bruh.mp3"))
                await asyncio.sleep(3)
                await voice.disconnect()



# a command similiar to curse with a much lower delay between individual joins: mainly used for debugging and testing
# however could still be used if you are feeling particularly cruel that day
# made it owner only for obvious reasons uwu
@client.command(
    help="Similar to curse, however with a much more frequent rate of joins; used for debugging but can be used normally; Bot owner only.",
    brief="OWNER: curse but stronger"
)
@commands.is_owner()
async def curseEvil(ctx, user: discord.User):

    global cursing
    cursing = True
    await ctx.send("***UWU?*** ")
    mark = ctx.guild.get_member(user.id)

    while cursing:

        waitTime = random.randint(5, 15)
        print(waitTime)
        await asyncio.sleep(waitTime)

        if (mark.voice != None and cursing):
            await mark.voice.channel.connect()
            print("Connected to voicechat!")
            voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
            voice.play(discord.FFmpegPCMAudio("bruh.mp3"))
            await asyncio.sleep(3)
            await voice.disconnect()


# this command turns off the while loop of the curse command; made it admin only for added chaos
@client.command(
    help="gets user rid of the curse; Administrator only.",
    brief="ADMIN:gets rid of the curse"
)
@commands.has_permissions(administrator=True)
async def cleanse(ctx):

    await ctx.send("*A poor soul has been rid of the mark of the uwu...*")
    global cursing
    cursing = False
    print("Stopped Targetting")

# shuts down the bot
@client.command(
    help="Shuts down the bot; Bot owner only.",
    brief="OWNER: Shut down"
)
@commands.is_owner()
async def kill(ctx):

    await ctx.send("*i'm sowwy...*")
    client.close()

# error handling that responds in chat when an error is encountered
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter all the required arguments.")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("I do not have permision to do that, Please update my permistions")
    elif isinstance(error, commands.errors.CommandNotFound):
        await ctx.send("owo? Unknown command.")
    else:
        await ctx.send("*Uwu i did a fuwuky uppy.* Unknown Error please go yell at @Simojian ```"f"{error}```")
        raise error

# runs the bot using it's token
client.run(TOKEN)