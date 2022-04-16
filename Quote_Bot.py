# bot.py
from email import message
import os
import random
import discord
from discord import file

import asyncio
from datetime import datetime, timedelta
import time
import sched

#from dotenv import load_dotenv

# 1
from discord.ext import commands

#load_dotenv()
TOKEN = "OTY0NzIxMzk4MTQyNjA3Mzcw.Ylow0A.2OqDTsUNsO8CUIZYpFJg82wIr_A"
#TOKEN = "INSERT_TOKEN_HERE"     
# 2
bot = commands.Bot(command_prefix='""')
#Testing 1, 2, 3, 4

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='roll_dice', help='Simulates rolling dice. Input in form "roll_dice X Y" X is number of dice to be rolled, and Y is the number of sides on those dice. Max is 69')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    if number_of_dice > 69:
        number_of_dice = 69
    if number_of_sides > 31415:
        number_of_sides = 31415
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))


@bot.command(name='quote', help='Format as \'""quote "QUOTE" USER\' which will add QUOTE to the user\'s quotes')
async def game_list(ctx, quote = "None", user = "None"):

    author_name = str(user)
    windows_file_author_name = author_name.strip('<')
    windows_file_author_name = windows_file_author_name.strip('>')
    guild = ctx.message.guild.name
    date_time = str(ctx.message.created_at)
        
    # Parent Directories  
    parent_dir = "c:/Users/hellotheredoriyah/OneDrive/ALS_Laptop/Documents/Programming/Discord_Bots/QuoteBot/Quote_Lists/"
    #parent_dir = "c:/Users/dasha/Github/Firstbot/Quote_Bot/Quote_Lists/"
    
    parent_dir += guild
    within_parent_dir = parent_dir + "/"
    try:  
            os.mkdir(parent_dir) 
            print("Directory '% s' created for server" % guild)
    except OSError as error:  
        print(error)  


    open_file = open(within_parent_dir + windows_file_author_name + "_quotes.txt", "a")
# open_file.write(fmt.format(message))
    open_file.write('"' + quote + '"- ' + user + " at " + date_time)
    open_file.write("\n")
    open_file.close()
    # user_game_dictionary[author_name] = game
    # user_game_dictionary[author_name] += ' Test'
    await ctx.channel.send(quote + " successfully added to " + user + "\'s list")
    # print(user_game_dictionary[author_name])

@bot.command(name='user', help='Sends a random quote from specified user, format as \'""user USER\'')
async def game_list(ctx, user = "None"):

    author_name = str(user)
    windows_file_author_name = author_name.strip('<')
    windows_file_author_name = windows_file_author_name.strip('>')
    guild = ctx.message.guild.name
    file_length = 0
        
    # Parent Directories  
    parent_dir = "c:/Users/hellotheredoriyah/OneDrive/ALS_Laptop/Documents/Programming/Discord_Bots/QuoteBot/Quote_Lists/"
    #parent_dir = "c:/Users/dasha/Github/Firstbot/Quote_Bot/Quote_Lists/"
    
    parent_dir += guild
    within_parent_dir = parent_dir + "/"
    try:  
            os.mkdir(parent_dir) 
            print("Directory '% s' created for server" % guild)
    except OSError as error:  
        print(error)  


    with open(within_parent_dir + windows_file_author_name + "_quotes.txt", "r") as f:
        lines = f.readlines()
    file_length = len(lines) 
    random_quote = random.choice(range(0, file_length))
    lines_stripped = []
    for line in lines:
        stripped = line.replace("\n", "")
        lines_stripped.append(stripped)
    print(lines_stripped)
    await ctx.channel.send(lines_stripped[random_quote])
    # else:
    #     await ctx.channel.send('User has no games listed')

@bot.command(name='random', help='Sends a random quote from any user')
async def game_list(ctx):

    guild = ctx.message.guild.name
    dir_length =  0
    file_length = 0
        
    # Parent Directories  
    parent_dir = "c:/Users/hellotheredoriyah/OneDrive/ALS_Laptop/Documents/Programming/Discord_Bots/QuoteBot/Quote_Lists/"
    #parent_dir = "c:/Users/dasha/Github/Firstbot/Quote_Bot/Quote_Lists/"
    
    parent_dir += guild
    within_parent_dir = parent_dir + "/"
    try:  
            os.mkdir(parent_dir) 
            print("Directory '% s' created for server" % guild)
    except OSError as error:  
        print(error)  

    path_dir = os.listdir(parent_dir)
    print(path_dir)
    dir_length = len(path_dir)
    random_user = random.choice(range(0, dir_length))
    i = 0
    for user in path_dir:
        if i == random_user:
            with open(within_parent_dir + user, "r") as f:
                lines = f.readlines()
            file_length = len(lines)
            random_quote = random.choice(range(0, file_length))
            lines_stripped = []
            for line in lines:
                stripped = line.replace("\n", "")
                lines_stripped.append(stripped)
            print(lines_stripped)
            await ctx.channel.send(lines_stripped[random_quote])
        i += 1
    
@bot.command(name='tally', help='Counts up all the quotes for each user')
async def game_list(ctx):

    guild = ctx.message.guild.name
    no_rankings = [0]
    name_rankings = ["placeholder"]
    file_length = 0
        
    # Parent Directories  
    parent_dir = "c:/Users/hellotheredoriyah/OneDrive/ALS_Laptop/Documents/Programming/Discord_Bots/QuoteBot/Quote_Lists/"
    #parent_dir = "c:/Users/dasha/Github/Firstbot/Quote_Bot/Quote_Lists/"
    
    parent_dir += guild
    within_parent_dir = parent_dir + "/"
    try:  
            os.mkdir(parent_dir) 
            print("Directory '% s' created for server" % guild)
    except OSError as error:  
        print(error)  

    path_dir = os.listdir(parent_dir)
    print(path_dir)
    for user in path_dir:
        with open(within_parent_dir + user, "r") as f:
            lines = f.readlines()
        file_length = len(lines)
        await ctx.channel.send("<" + user.strip("_quotes.txt") + "> : " + str(file_length))
        # if file_length > no_rankings[0]:
        #     no_rankings.insert(0, file_length)
        #     name_rankings.insert(0, "<" + user + ">")
        # elif file_length < no_rankings[0]:
        #     no_rankings.insert(0, file_length)
        #     name_rankings.insert(0, "<" + user + ">")

@bot.command(name='tally_user', help='Counts up all the quotes for each user')
async def game_list(ctx, author):

    guild = ctx.message.guild.name
    file_length = 0
        
    # Parent Directories  
    parent_dir = "c:/Users/hellotheredoriyah/OneDrive/ALS_Laptop/Documents/Programming/Discord_Bots/QuoteBot/Quote_Lists/"
    #parent_dir = "c:/Users/dasha/Github/Firstbot/Quote_Bot/Quote_Lists/"
    
    parent_dir += guild
    within_parent_dir = parent_dir + "/"
    try:  
            os.mkdir(parent_dir) 
            print("Directory '% s' created for server" % guild)
    except OSError as error:  
        print(error)  

    path_dir = os.listdir(parent_dir)
    print(path_dir)
    for user in path_dir:
        if str(author) == "<" + user.strip("_quotes.txt") + ">":
            with open(within_parent_dir + user, "r") as f:
                lines = f.readlines()
            file_length = len(lines)
            await ctx.channel.send("<" + user.strip("_quotes.txt") + "> : " + str(file_length))




bot.run(TOKEN)
