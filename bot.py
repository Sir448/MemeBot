# -*- coding: utf-8 -*-
"""
Created on Sat May 30 14:29:04 2020

@author: Chris
"""

import discord
from discord.ext import commands
from mutagen.mp3 import MP3
from math import ceil
import asyncio
from random import randint

import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


playing = False

# token = open("token.txt", "r").read()
token = os.getenv("TOKEN")

images = {
        "o kawaii koto":"OKawaiiKoto.jpg",
        "shocked pikachu":"ShockedPikachu.jpg",
        "imma head out":"ImmaHeadOut.jpg",
        "sayonara":"Sayonara.jpg",
        "i am superior":"ButIAmSuperior.png",
        "i don\'t think i will":"IDontThinkIWill.png",
        "i don\'t feel so good":"IDontFeelSoGood.png",
        "never forgive the japanese":"IllNeverForgetTheJapanese.png",
        "visible confusion":"VisibleConfusion.png",
        "man of culture":"ManOfCulture.jpg",
        "aqua crying":"AquaCrying.gif",
        "aqua screaming":"AquaScreaming.jpg",
        "tom confused":"TomConfused.jpg",
        "jesus?":"jesus.jpg",
        "mike-sulley":"Mike-Sulley.jpg",
        "shocked kevin":"ShockedKevin.jpg",
        "yell at cat":"YellAtCat.jpg",
        "buns":"Buns.png",
        "speech 100":"Speech100.jpg",
        "illusion 100":"Illusion100.jpg",
        "destruction 100":"Destruction100.jpg",
        "chika frustrated":"ChikaFrustrated.png",
        "breathing is fun":"BreathingIsFun.jpg",
        "patrick red eyes":"PatrickRedEyes.jpg",
        "cola":"Cola.png",
        "chika beats ishigami":"ChikaBeatsIshigami.gif",
        "eat this":"EatThis.png",
        "strange thing to ask":"StrangeThingToAsk.jpg",
        "chika panic":"ChikaPanic.gif",
        "weakness disgusts me":"WeaknessDisgustsMe.jpg",
        "t pose":"TPose.jpg",
        "the world shall know pain":"TheWorldShallKnowPain.jpg",
        "sad linus":"SadLinus.jpg",
        "hayasaka humiliation":"HayasakaHumiliation.jpg",
        "orgasm donor":"OrgasmDonor.png",
        "boi":"Boi.jpg",
        "mini keanu":"MiniKeanu.jpg",
        "sad keanu":"SadKeanu.png",
        "elon weed":"ElonWeed.gif",
        "blinking white guy":"BlinkingWhiteGuy.gif",
        "evil kermit":"EvilKermit.jpg",
        "none of my business":"NoneOfMyBusiness.jpg",
        "arthur fist":"ArthurFist.jpg",
        "i can\'t read":"ICantRead.jpg",
        "retarded spongebob":"RetardedSpongebob.jpg",
        "tired spongebob":"TiredSpongebob.jpg",
        "caveman spongebob":"CavemanSpongebob.png",
        "nezuko running":"NezukoRunning.gif",
        "confused spongebob":"ConfusedSpongebob.jpg",
        "alan calculating":"AlanCalculating.gif",
        "calculating":"Calculating.jpg",
        "300iq":"300IQ.jpg",
        "big brain":"BigBrain.jpg",
        "face palm":"FacePalm.jpg",
        "doubt":"Doubt.jpg",
        "f":"F.jpg",
        "what cost":"WhatCost.jpg",
        "what did it cost":"WhatDidItCost.jpg",
        "absolute win":"AbsoluteWin.jpg",
        "shrek":"Shrek.jpg",
        "pathetic":"Pathetic.jpg",
        "disappointed shinji":"DisappointedShinji.jpg",
        "sneak 100":"Sneak100.png",
        "joker dancing":"JokerDancing.jpg",
        "funeral dancing":"FuneralDancing.gif",
        "chika dancing":"ChikaDancing.gif",
        "konosuba dancing":"KonosubaDancing.gif",
        "komi dancing":"KomiDancing.gif",
        "here we go again":"HereWeGoAgain.jpg",
        "had to do it to em":"HadToDoItToEm.jpg",
        "supa hot fire":"SupaHotFire.gif",
        "leo clapping":"LeoClapping.gif",
        "clapping":"Clapping.gif",
        "shia labeouf clapping":"ShiaLabeoufClapping.gif",
        "jk i know face":"JKIKnowFace.jpg",
        "v smirk":"VSmirk.jpg",
        "changbin mom":"ChangbinMom.jpg",
        "suga police":"SugaPolice.jpg",
        "j-hope attack":"JHopeAttack.jpg",
        "disgusted sehun":"DisgustedSehun.jpg",
        "han tea":"HanTea.jpg",
        "changbin better":"ChangbinBetter.jpg",
        "do":"DO.jpg",
        "chika beats ishigami 2":"ChikaBeatsIshigami2.gif",
        "felix not caring":"FelixNotCaring.jpg",
        "changbin opinion":"ChangbinOpinion.jpg",
        "felix repeat":"FelixRepeat.jpg",
        "hyunjin awkward":"HyunjinAwkward.jpg",
        "chan interesting":"ChanInteresting.jpg",
        "people die if they are killed":"PeopleDieIfTheyAreKilled.png",
        "sadness and sorrow":"Swing.jpg",
        "all might noooo":"AllMightNOOOO.jpg",
        "first time":"FirstTime.jpg",
        "do it again":"DoItAgain.jpg",
        "you wouldn\'t get it":"YouWouldntGetIt.png"
        }

genres = {
    "images": {
        "anime":[
            "o kawaii koto",
            "sayonara",
            "i am superior",
            "never forgive the japanese",
            "man of culture",
            "aqua crying",
            "aqua screaming",
            "chika frustrated",
            "breathing is fun",
            "cola",
            "chika beats ishigami",
            "eat this",
            "strange thing to ask",
            "chika panic",
            "weakness disgusts me",
            "the world shall know pain",
            "hayasaka humiliation",
            "nezuko running",
            "pathetic",
            "disappointed shinji",
            "chika dancing",
            "konosuba dancing",
            "komi dancing",
            "chika beats ishigami 2",
            "people die if they are killed",
            "sadness and sorrow",
            "all might noooo"
            ],
        "kpop":[
            "jk i know face",
            "v smirk",
            "changbin mom",
            "suga police",
            "j-hope attack",
            "disgusted sehun",
            "han tea",
            "changbin better",
            "do",
            "felix not caring",
            "changbin opinion",
            "felix repeat",
            "hyunjin awkward",
            "chan interesting"
            ],
        "normie":[
            "shocked pikachu",
            "imma head out",
            "i don\'t think i will",
            "i don\'t feel so good",
            "visible confusion",
            "tom confused",
            "jesus?",
            "mike-sulley",
            "shocked kevin",
            "yell at cat",
            "buns",
            "speech 100",
            "illusion 100",
            "destruction 100",
            "patrick red eyes",
            "t pose",
            "sad linus",
            "orgasm donor",
            "boi",
            "mini keanu",
            "sad keanu",
            "elon weed",
            "blinking white guy",
            "evil kermit",
            "none of my business",
            "arthur fist",
            "i can\'t read",
            "retarded spongebob",
            "tired spongebob",
            "caveman spongebob",
            "confused spongebob",
            "alan calculating",
            "calculating",
            "300iq",
            "big brain",
            "face palm",
            "doubt",
            "f",
            "what cost",
            "what did it cost",
            "absolute win",
            "shrek",
            "sneak 100",
            "joker dancing",
            "funeral dancing",
            "here we go again",
            "had to do it to em",
            "supa hot fire",
            "leo clapping",
            "clapping",
            "shia labeouf clapping",
            "first time",
            "do it again",
            "you wouldn\'t get it"
            ]
        },
    "audio": {
        "anime":[],
        "kpop":[],
        "normie":[]
        }
    }

gifCount = 0
for i in images:
    if images[i][-4:] == ".gif":
        gifCount += 1

audio = {
        "you are already dead":"YouAreAlreadyDead.mp3",
        "to be continued":"ToBeContinued.mp3",
        "lick lick lick dub":"LickLickLickDub.mp3",
        "lick lick lick sub":"LickLickLickSub.mp3",
        "bruh":"bruh.mp3",
        "that\'s my opinion":"ThatsMyOpinion.mp3",
        "there is no meme":"ThereIsNoMeme.mp3",
        "ph intro":"PHIntro.mp3",
        "the next episode":"TheNextEpisode.mp3",
        "let\'s go":"LetsGo.mp3",
        "still d.r.e.":"StillD.R.E..mp3",
        "o kawaii koto":"OKawaiiKoto.mp3",
        "explosion":"Explosion.mp3",
        "waga na wa megumin":"WagaNaWaMegumin.mp3",
        "ahaha":"Ahaha.mp3",
        "videogames":"Videogames.mp3",
        "everybody\'s circulation":"EverybodysCirculation.mp3",
        "let\'s get ready to rumble":"LetsGetReadyToRumble.mp3",
        "sadness and sorrow":"SadnessAndSorrow.mp3",
        "batman transition":"BatmanTransition.mp3",
        "gang gang gang gang":"GangGangGangGang.mp3",
        "daddy chill":"DaddyChill.mp3",
        "what the hell is even that":"WhatTheHellIsEvenThat.mp3",
        "daddy chill 2":"DaddyChill2.mp3",
        "believe it":"BelieveIt.mp3",
        "don\'t worry bout it":"DontWorryBoutIt.mp3",
        "no diqk":"NoDiqk.mp3",
        "corona virus":"CoronaVirus.mp3",
        "why are you running":"WhyAreYouRunning.mp3",
        "oh my god":"OhMyGod.mp3",
        "corona time":"CoronaTime.mp3",
        "i wish i gave a fuck":"IWishIGaveAFuck.mp3",
        "supa hot fire":"SupaHotFire.mp3",
        "did i ask":"DidIAsk.mp3",
        "fbi open up":"FBIOpenUp.mp3",
        "default dance":"DefaultDance.mp3",
        "tokyo drift":"TokyoDrift.mp3",
        "kingsman country roads":"KingsmanCountryRoads.mp3",
        "i\'m gay":"ImGay.mp3"
        }

altCommands = {
        "shocked pikachu":["pikachu"],
        "i am superior":["superior"],
        "i don\'t think i will":["old capt", "capt"],
        "i don\'t feel so good":["spiderman snap","my baby tom holland"],
        "visible confusion":["obi-wan confused","obiwan confused"],
        "man of culture":["culture"],
        "aqua crying":["crying"],
        "aqua screaming":["screaming"],
        "speech 100":["speech"],
        "illusion 100":["illusion"],
        "destruction 100":["destruction"],
        "chika frustrated":["frustrated","chika frustration"],
        "breathing is fun":["breathing"],
        "cola":["i\'ll give you a cola"],
        "chika beats ishigami":["chika beating ishigami"],
        "eat this":["deku"],
        "strange thing to ask":["erwin"],
        "weakness disgusts me":["weakness","madara"],
        "the world shall know pain":["pain"],
        "hayasaka humiliation":["hayasaka humiliated","humiliation"],
        "mini keanu":["small keanu"],
        "elon weed":["elon high","high elon"],
        "blinking white guy":["blinking guy","confused white guy","confused guy"],
        "none of my business":["tea"],
        "retarded spongebob":["mocking spongebob"],
        "confused spongebob":["why"],
        "300iq":["200iq","300 iq", "200 iq"],
        "big brain":["markiplier"],
        "face palm":["picard"],
        "doubt":["press x to doubt","x"],
        "f":["press f to pay respects"],
        "what cost":["wario"],
        "what did it cost":["thanos"],
        "absolute win":["hulk","professor hulk", "prof hulk"],
        "pathetic":["asuka"],
        "disappointed shinji":["shinji"],
        "sneak 100":["sneak"],
        "joker dancing":["joker"],
        "funeral dancing":["funeral"],
        "komi dancing":["twice","what is love","twice dance"],
        "here we go again":["gta","ah shit, here we go again"],
        "supa hot fire":["i\'m about to end this man\'s whole career"],
        "clapping":["jaw drop","mind blown"],
        "shia labeouf clapping":["shia clapping","shia"],
        "j-hope attack":["jhope attack","j hope attack"],
        "chika beats ishigami 2":["chika beating ishigami 2"],
        "all might noooo":["all might no", "all might noo", "all might nooo", "all might nooooo", "noo", "nooo", "noooo", "nooooo"],
        "do it again":["i\'ll fuckin do it again", "i\'ll fucking do it again", "fuckin do it again", "fucking do it again"],
        "you are already dead":["omae wa mou shindeiru","already dead"],
        "lick lick lick dub":["lick dub"],
        "lick lick lick sub":["lick sub"],
        "that\'s my opinion":["opinion"],
        "there is no meme":["no meme"],
        "the next episode":["snoop dogg"],
        "still d.r.e.":["still dre","dre", "d.r.e."],
        "o kawaii koto":["how cute"],
        "explosion":["bakuretsu"],
        "waga na wa megumin":["megumin"],
        "everybody\'s circulation":["circulation"],
        "let's get ready to rumble":["fight"],
        "sadness and sorrow":["ss", "swing", "naruto swing"],
        "gang gang gang gang":["gang"],
        "what the hell is even that":["what the hell"],
        "don\'t worry bout it":["don\'t worry about it", "dw", "dw bout it"],
        "no diqk":["no dick"],
        "i wish i gave a fuck":["gave a fuck"],
        "why are you running":["running"],
        "fbi open up":["fbi"],
        "kingsman country roads":["kingsman","country roads"],
        "you wouldn\'t get it":["wouldn\'t get it"]
        }

altList = []
for i in altCommands:
    altList += list(altCommands[i])

altNames = {
        "that\'s my opinion":"That\'s My Opinion",
        "ph intro":"PH Intro",
        "let\'s go":"Let\'s Go",
        "i don\'t think i will":"I Don\'t Think I Will",
        "i don\'t feel so good":"I Don\'t Feel So Good",
        "i can\'t read":"I Can't Read",
        "i\'ll fucking do it again":"I\'ll Fucking Do It Again",
        "i\'ll fuckin do it again":"I\'ll Fuckin Do It Again",
        "everybody\'s circulation":"Everybody\'s Circulation",
        "let\'s get ready to rumble":"Let\'s Get Ready To Rumble",
        "don\'t worry bout it":"Don\'t Worry Bout It",
        "dw":"DW",
        "dw bout it":"DW Bout It",
        "fbi open up":"FBI Open Up",
        "don\'t worry about it":"Don\'t Worry About It",
        "jk i know face":"JK I Know Face",
        "do":"DO",
        "i\'ll give you a cola":"I\'ll Give You A Cola",
        "i\'m about to end this man\'s whole career":"I\'m About To End This Man\'s Whole Career",
        "i\'m gay":"I\'m Gay",
        "you wouldn\'t get it":"You Wouldn\'t Get It"
        }

images3 = {}
images2 = sorted(images)
for i in images2:
    images3[i] = images[i]
images = images3
del images3, images2

audio3 = {}
audio2 = sorted(audio)
for i in audio2:
    audio3[i] = audio[i]
audio = audio3
del audio3, audio2

genres["images"]["anime"].sort()
genres["images"]["kpop"].sort()
genres["images"]["normie"].sort()

presences = ["with fire", "Russian Roulette", "Pokemon Go", "Chopin – Ballade No. 1 in G minor", "SAO", "a dating sim", "gungi with Meurum", "Half Life 3"]

bot = commands.Bot(command_prefix=".")

bot.remove_command('help')


@bot.event
async def on_ready():
    await bot.change_presence( activity=discord.Game(name = presences[randint(0,len(presences) - 1)]))
    print(f'We have logged in as {bot.user}')
    
    

@bot.command()
async def i(ctx, *, arg):
    global picture, genre, gifOnly, msg
    if arg.lower() in images:
        await ctx.send(file = discord.File("Images/"+images[arg.lower()]))
    elif arg.lower() in altList:
        for i  in altCommands:
            if arg.lower() in altCommands[i]:
                picture = i
                break
        await ctx.send(file = discord.File("Images/"+images[picture]))
    elif "list" in arg.lower():
        genre = None
        if "anime" in arg.lower():
            genre = "anime"
        elif "kpop" in arg.lower():
            genre = "kpop"
        elif "normie" in arg.lower():
            genre = "normie"
        
        msg = ""
        if genre == None:
            for i in images:
                if images[i][-4:] == ".gif" or "gif" not in arg.lower():
                    if i in altNames:
                        msg += altNames[i] + "\n"
                    else:
                        msg += i.title() + "\n"
            if "gif" in arg.lower():
                embed = discord.Embed(title="List of GIFs",description=msg, color = 0x0042FF)
            else:
                embed = discord.Embed(title="List of Images",description=msg, color = 0x0042FF)
        else:
            for i in range(len(genres["images"][genre])):
                if images[genres["images"][genre][i]][-4:] == ".gif" or "gif" not in arg.lower():
                    if genres["images"][genre][i] in altNames:
                        msg += altNames[genres["images"][genre][i]] + "\n"
                    else:
                        msg += genres["images"][genre][i].title() + "\n"
            if "gif" in arg.lower():
                embed = discord.Embed(title="List of "+genre.title()+" GIFs",description=msg, color = 0x0042FF)
            else:
                embed = discord.Embed(title="List of "+genre.title()+" Images",description=msg, color = 0x0042FF)  
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(description="I don't have that image. Type `.i list` for a list of available images.", color = 0x0042FF)
        await ctx.send(embed=embed)
 


@bot.command()
async def a(ctx, *, arg):
    global playing, vc, voice, clip
    if playing == False:
        if arg.lower() == "list":
            msg = ""
            for i in audio:
                if i in altNames:
                    msg += altNames[i] + "\n"

                else:
                    msg += i.title() + "\n"
            embed = discord.Embed(title="List of Audio Clips",description=msg, color = 0xFF0000)
            await ctx.send(embed=embed)
        elif arg.lower() in audio:
            try:
                # await ctx.message.add_reaction('\N{THUMBS UP SIGN}')
                await ctx.message.add_reaction('✅')
                vc = ctx.message.author.voice.channel
                voice = await vc.connect()
                voice.play(discord.FFmpegPCMAudio(executable = "C:/FFmpeg/bin/ffmpeg.exe", source = "Audio/" + audio[arg.lower()]))
                if int(MP3("Audio/" + audio[arg.lower()]).info.length) > 59:
                    embed = discord.Embed(description="This audio clip is "+str(int(MP3("Audio/" + audio[arg.lower()]).info.length)//60)+":"+str(int(MP3("Audio/" + audio[arg.lower()]).info.length)%60)+". Use command `.a dc` to stop it.", color = 0xFF0000)
                    await ctx.send(embed=embed)
                playing = True
                duration = ceil(MP3("Audio/" + audio[arg.lower()]).info.length)
                counter = 0
                while duration > counter and playing == True:
                    await asyncio.sleep(1)
                    counter += 1
                await voice.disconnect()
                playing = False
            except:
                embed = discord.Embed(description="You are not connected to a voice channel", color = 0xFF0000)
                await ctx.send(embed=embed)
        elif arg.lower() in altList:
            for i  in altCommands:
                if arg.lower() in altCommands[i]:
                    clip = i
                    break
            try:
                await ctx.message.add_reaction('\N{THUMBS UP SIGN}')
                vc = ctx.message.author.voice.channel
                voice = await vc.connect()
                voice.play(discord.FFmpegPCMAudio(executable = "C:/FFmpeg/bin/ffmpeg.exe", source = "Audio/" + audio[clip]))
                print("1")
                if int(MP3("Audio/" + audio[clip]).info.length) > 59:
                    print("2")
                    embed = discord.Embed(description="This audio clip is "+str(int(MP3("Audio/" + audio[clip]).info.length)//60)+":"+str(int(MP3("Audio/" + audio[clip]).info.length)%60)+". Use command `.a dc` to stop it.", color = 0xFF0000)
                    print("3")
                    await ctx.send(embed=embed)
                playing = True
                duration = ceil(MP3("Audio/" + audio[clip]).info.length)
                counter = 0
                while duration > counter and playing == True:
                    await asyncio.sleep(1)
                    counter += 1
                await voice.disconnect()
                playing = False
            except:
                embed = discord.Embed(description="You are not connected to a voice channel", color = 0xFF0000)
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description="I don't have that audio clip. Type `.a list` for a list of available audio clips.", color = 0xFF0000)
            await ctx.send(embed=embed)
    elif arg.lower() == "dc" or arg.lower() == "disconnect":
        await ctx.message.add_reaction('\N{THUMBS UP SIGN}')
        playing = False
        await voice.disconnect()
    else:
        embed = discord.Embed(description="An audio clip is already being played", color = 0xFF0000)
        await ctx.send(embed=embed)

@bot.command()
async def m(ctx, *, arg):
    global playing, vc, voice, clip
    if playing == False:
        if arg.lower() == "list":
            msg = ""
            for i in audio:
                if i in images:
                    if i in altNames:
                        msg += altNames[i] + "\n"

                    else:
                        msg += i.title() + "\n"
            embed = discord.Embed(title="List of Image and Audio memes",description=msg, color = 0x8F00FF)
            await ctx.send(embed=embed)
        elif arg.lower() in audio and arg.lower() in images:
            try:
                vc = ctx.message.author.voice.channel
                voice = await vc.connect()
                voice.play(discord.FFmpegPCMAudio(executable = "C:/FFmpeg/bin/ffmpeg.exe", source = "Audio/" + audio[arg.lower()]))
                await ctx.send(file = discord.File("Images/"+images[arg.lower()]))
                if int(MP3("Audio/" + audio[arg.lower()]).info.length) > 59:
                    embed = discord.Embed(description="This audio clip is "+str(int(MP3("Audio/" + audio[arg.lower()]).info.length)//60)+":"+str(int(MP3("Audio/" + audio[arg.lower()]).info.length)%60)+". Use command `.a dc` to stop it.", color = 0x8F00FF)
                    await ctx.send(embed=embed)
                playing = True
                duration = ceil(MP3("Audio/" + audio[arg.lower()]).info.length)
                counter = 0
                while duration > counter and playing == True:
                    await asyncio.sleep(1)
                    counter += 1
                await voice.disconnect()
                playing = False
            except:
                embed = discord.Embed(description="You are not connected to a voice channel", color = 0x8F00FF)
                await ctx.send(embed=embed)
        elif arg.lower() in altList:
            for i  in altCommands:
                if arg.lower() in altCommands[i]:
                    clip = i
                    break
            if clip in audio and clip in images:
                try:
                    vc = ctx.message.author.voice.channel
                    voice = await vc.connect()
                    voice.play(discord.FFmpegPCMAudio(executable = "C:/FFmpeg/bin/ffmpeg.exe", source = "Audio/" + audio[clip]))
                    await ctx.send(file = discord.File("Images/"+images[clip]))
                    if int(MP3("Audio/" + audio[clip]).info.length) > 59:
                        embed = discord.Embed(description="This audio clip is "+str(int(MP3("Audio/" + audio[arg.lower()]).info.length)//60)+":"+str(int(MP3("Audio/" + audio[arg.lower()]).info.length)%60)+". Use command `.a dc` to stop it.", color = 0x8F00FF)
                        await ctx.send(embed=embed)
                    playing = True
                    duration = ceil(MP3("Audio/" + audio[clip]).info.length)
                    counter = 0
                    while duration > counter and playing == True:
                        await asyncio.sleep(1)
                        counter += 1
                    await voice.disconnect()
                    playing = False
                except:
                    embed = discord.Embed(description="You are not connected to a voice channel", color = 0x8F00FF)
                    await ctx.send(embed=embed)
            elif clip in audio:
                embed = discord.Embed(description="This meme only has an audio clip.", color = 0x8F00FF)
                await ctx.send(embed=embed)
            elif clip in images:
                embed = discord.Embed(description="This meme only has an image.", color = 0x8F00FF)
                await ctx.send(embed=embed)
        elif arg.lower() in audio:
            embed = discord.Embed(description="This meme only has an audio clip.", color = 0x8F00FF)
            await ctx.send(embed=embed)
        elif arg.lower() in images:
            embed = discord.Embed(description="This meme only has an image.", color = 0x8F00FF)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description="I don\'t have that meme. Type `.m list` for a list of available image and audio memes.", color = 0x8F00FF)
            await ctx.send(embed=embed)
    elif arg.lower() == "dc" or arg.lower() == "disconnect":
        await ctx.message.add_reaction('\N{THUMBS UP SIGN}')
        playing = False
        await voice.disconnect()
    else:
        embed = discord.Embed(description="An audio clip is already being played", color = 0x8F00FF)
        await ctx.send(embed=embed)

@bot.command()
async def alt(ctx, *, arg):
    if (arg.lower() in audio or arg.lower() in images) and arg.lower() in altCommands:
        for i in range(len(altCommands[arg.lower()])):
            if altCommands[arg.lower()][i] in altNames:
                    msg += altNames[altCommands[arg.lower()][i]] + "\n"
            else:
                msg += altCommands[arg.lower()][i].title() + "\n"
        if arg.lower() in altNames:
            embed = discord.Embed(title="Alternate Commands for "+altNames[arg.lower()],description=msg, color = 0x28DA0F)
        else:
            embed = discord.Embed(title="Alternate Commands for "+arg.title(),description=msg, color = 0x28DA0F)
        await ctx.send(embed=embed)
    elif arg.lower() in altList:
        for i in altCommands:
            if arg.lower() in altCommands[i]:
                clip = i
                break
        msg = ""
        if clip in altNames:
            msg += altNames[clip] + "\n"
        else:
            msg += clip.title() + "\n"
        for i in range(len(altCommands[clip])):
            if arg.lower() != altCommands[clip][i]:
                if altCommands[clip][i] in altNames:
                        msg += altNames[altCommands[clip][i]] + "\n"
                else:
                    msg += altCommands[clip][i].title() + "\n"
        if arg.lower() in altNames:
            embed = discord.Embed(title="Alternate Commands for "+altNames[arg.lower()],description=msg, color = 0x28DA0F)
        else:
            embed = discord.Embed(title="Alternate Commands for "+arg.title(),description=msg, color = 0x28DA0F)
        await ctx.send(embed=embed)
    elif arg.lower() in audio or arg.lower() in images:
        embed = discord.Embed(description="This meme does not have an alternate command", color = 0x28DA0F)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(description="I don't have that meme. Type `.i list` or `.a list` for a list of available memes.", color = 0x28DA0F)
        await ctx.send(embed=embed)

@bot.event
async def on_message(message):
    if message.content[:2] == "..":
        msg = list(message.content[2:])
        if message.author.nick != None:
            msg2 = message.author.nick + ": "
        else:
            msg2 = message.author.name + ": "
        for i in range(len(msg)):
            if i%2 == 0:
                msg2 += msg[i].lower()
            else:
                msg2 += msg[i].upper()
        await message.delete()
        await message.channel.send(msg2)
    elif message.content[:6] == ".anon.":
        print("{}: {}".format(message.author.name,message.content[6:]))
        msg = list(message.content[6:])
        msg2 = ""
        for i in range(len(msg)):
            if i%2 == 0:
                msg2 += msg[i].lower()
            else:
                msg2 += msg[i].upper()
        await message.delete()
        await message.channel.send(msg2)
    else:
        await bot.process_commands(message)


@bot.command()
async def count(ctx):
    embed = discord.Embed(description="We now have "+str(len(images))+" images including "+str(gifCount)+" gifs and "+str(len(audio))+" audio clips for a total of "+str(len(images)+len(audio))+" memes.", color = 0x939393)
    await ctx.send(embed=embed)


@bot.command()
async def cycle(ctx):
    await bot.change_presence( activity=discord.Game(name = presences[randint(0,len(presences) - 1)]))

@bot.command()
async def help(ctx):
    embed = discord.Embed(title = "Commands", color = 0x939393)
    embed.add_field(name="`.i [name of image]`", value="Requests an image", inline=False)
    embed.add_field(name="`.a [name of audio clip]`", value="Requests an audio clip", inline=False)
    embed.add_field(name="`.a disconnect` or `.a dc`", value="Stops audio clip", inline=False)
    embed.add_field(name="`.m [name of meme]`", value="Requests an image and audio meme", inline=False)
    embed.add_field(name="`.m disconnect` or `.m dc`", value="Stops audio clip", inline=False)
    embed.add_field(name="`.i list`", value="List of available images \nAdd `gif` for a list of gifs \nAdd a genre (`anime`,`kpop`,`normie`) for images of a specific genre", inline=False)
    embed.add_field(name="`.a list`", value="List of available audio clips", inline=False)
    embed.add_field(name="`.m list`", value="List of available image and audio memes", inline=False)
    embed.add_field(name="`.alt [name of meme]`", value="List of alternate names", inline=False)
    embed.add_field(name="`.count`", value="Count of how many memes are available", inline=False)
    await ctx.send(embed=embed)


bot.run(token)

