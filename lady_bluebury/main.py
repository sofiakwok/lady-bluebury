import discord
import time

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('''So, Bluebury'''):
        time.sleep(0.5)
        await message.channel.send('Aye, I concur.  Thanketh god yond that’s all behind us.  How shouldst we bray out? \n')
    if message.content.startswith('''Let’s playeth a fat game of quiplash!'''):
        time.sleep(0.5)
        await message.channel.send('''Yond sounds excit'ment.  Anon, th're’s nay needeth to keepeth track of a “winn'r” 'r “los'r” - \n''')
    if message.content.startswith('''Nay, not at all -'''):
        time.sleep(0.5)
        await message.channel.send('''But I sayeth nay game is excit'ment without a dram competition.  Let’s sayeth mine own team shall beest on the hath left and yours shall beest on the right.''')
    if message.content.startswith('''Thee filthy, cheating dog!'''):
        time.sleep(0.5)
        await message.channel.send('''I couldst sayeth the same about thee''')
    if message.content.startswith('''God, I can’t believeth'''):
        time.sleep(0.5)
        await message.channel.send('''I bethink it’s timeth to did split again.''')
    if message.content.startswith("Welcome to the Bluebury channel!"):
        time.sleep(0.5)
        await message.channel.send('''Thy new goal: to did beat the oth'r side.  Starteth out by solving this shakespearean puzzle to receiveth in the humor: \n''')
        await message.channel.send('''https://docs.google.com/spreadsheets/d/1rWyyZAaC57aV6qq373dsVFxzh8XnZ3XWwcV3f_Or9eE/edit?usp=sharing''')
    if message.content.startswith('''Return to the main voice chat!'''):
        time.sleep(0.5)
        await message.channel.send('''Thee knoweth, these dram games art all well and valorous, but I bethink something m're satisfying wouldst beest going headeth to headeth.''')
    if message.content.startswith('''Final round!'''):
        time.sleep(0.5)
        await message.channel.send('''This hast been an excit'ment timeth.''')
    if message.content.startswith('''Nev'rtheless, I bethink'''):
        time.sleep(0.5)
        await message.channel.send('''Fine, whatev'r.''')


client.run('ODQ2NDk4NDM3MTI1NTA1MDI1.YKwZGg.BPysybIsTKKQNRV2De3h_ZiRxCo')
