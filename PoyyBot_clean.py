import discord
import asyncio
import requests
import random
#import json
import time
import re
import linecache
from discord.ext import commands
# import io #import BytesIO
# from PIL import Image

#####################################################################################
############  Bot written to add fun features to Štosfender server
#########  Version 2.9.1
####### Python 3.8.4 and discord.py version 1.5.1
###### Author: zucc#4876

#help command removes the standard so we can overwrite it
#bot = discord.Client() 
bot = commands.Bot(command_prefix='+', help_command = None)

#dumb reason, it has to be defined before events
counter = 0
badpoyy = 0
goodpoyy = 0
srijeda = 1
peaky = 1
queen = 1

#########kluki kompresor
############## betting game pomocu jsona
################ rodendani pomocu jsona
########################## on disconnect test sa spremanjem by writing message u svoj
################################### potentially reactions 
##################################### do the tenor shit
############## is python random really random, graphical representation numpy? DONE
## random command
## on disconnect i on reconnect
#random teme
#fix fizicki
#fix emojie
#fix +help


@bot.event
async def on_ready():

	#Bot takes ~3-4s to startup
	print('PoyyBot online') 

	# 2 possible activites: Watching and Playing 
	#activity = discord.Activity(name='you pee :smirk:', type=discord.ActivityType.watching)
	#await bot.change_presence(activity=discord.Activity(name='the walls FUCKING SHAKE FFS', type=discord.ActivityType.watching))
	#await bot.change_presence(activity=discord.Game(name='poyy kolege ❤️'))

	# Setting `Listening ` status
	#await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.Streaming, name = 'Pweety Video', url="https://www.youtube.com/watch?v=EE-xtCF3T94"))
	#await bot.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))

	#counter counts total messages sent
	#badpoyy for 'bad poyy' command
	#goodpoyy for 'hvala poyy' command 
	global counter
	global badpoyy
	global goodpoyy
	global srijeda
	global peaky
	global queen
	
	#reading from the file, format is X Y Z for simpler reading
	with open('counter.txt', 'r+') as myfile:

		lista = myfile.readline()

		#splitting numbers into a list for a simpler handling
		lista = lista.split(' ')

		#printing each number 
		counter = int(lista[0])
		print(f'Counter: {counter}')
		badpoyy = int(lista[1])
		print(f'Badpoyy: {badpoyy}')
		goodpoyy = int(lista[2])
		print(f'Goodpoyy: {goodpoyy}')
		srijeda = int(lista[3])

		peaky = int(lista[4])
		hours = int(time.strftime('%H'))
		print(f'Peaky: {peaky}')

		queen = int(lista[5])
		print(f'Queen: {queen}')

		dan = time.strftime('%A')
		if dan == 'Wednesday':
			print(f'Isprintana srijeda:' + ('Yes' if srijeda == 1 else 'No'))
		elif dan == 'Thursday':
			srijeda = 0


@bot.event
async def on_disconnect():
	cenel = bot.get_channel(780881245499686932)
	#_k = '<@305465501595729921>'
	await cenel.send(f'zucc disconnectao sam se')


@bot.event
async def on_message(message):
	#probably not needed, but just in case
	global counter
	global badpoyy
	global goodpoyy
	global srijeda
	global peaky
	global queen
	
	#for each message sent on the server incrament by 1, including the PoyyBot
	counter += 1

	#Checking if the received message is by the bot to prevent recursion
	if message.author == bot.user:
		return

	#if štos needs to be temporarely muted
	if message.author.id == 365962520680333314:
		return

	if message.content.startswith('//'):
		return

	# if counter == 69420:
	# 	if message.author.id == 782630417647796224 or message.author.id == 235088799074484224 or message.author.id == 234395307759108106 or message.author.id == 777942093208748033:
	# 		counter -= 10
	# 		return

	# 	autor = '<@' + str(message.author.id) + '>'
	# 	await message.channel.send(f'{autor} sent 69420th message. Teehee funny number nice. Good job! We getting high af!')
	# 	await message.channel.send('https://tenor.com/view/bobux-gif-18603683')
	# 	await message.channel.send('https://tenor.com/view/lizard-dancing-poggers-lizard-dance-poggers-gif-18527737')
	# 	await message.channel.send('https://tenor.com/view/katie-nolan-69-golf-tougue-out-gif-12612419')
	# 	return



	if counter == 111111:
		if message.author.id == 782630417647796224 or message.author.id == 235088799074484224 or message.author.id == 234395307759108106 or message.author.id == 777942093208748033:
			counter -= 10
			return

		autor = '<@' + str(message.author.id) + '>'
		await message.channel.send(f"{autor} sent 111111th message. That's a lot of ones, just like this server <:kekw:774064416441892884>")
		await message.channel.send('https://tenor.com/view/hitmans-bodyguard-hitmans-bodyguard-gi-fs-samuel-l-jackson-time-tick-tock-gif-11022221')
		#await message.channel.send('https://tenor.com/view/lizard-dancing-poggers-lizard-dance-poggers-gif-18527737')
		#await message.channel.send('https://tenor.com/view/katie-nolan-69-golf-tougue-out-gif-12612419')
		await message.channel.send(f"jk jk, y'all are number 1 in my heart")
		return



	#ignoring kada channel just in case
	if message.channel.id == 782586423332175883:
		return

	#Bot shutdown procedure, only if it by me
	if (message.author.id == 305465501595729921 and message.content.lower() == 'poyy nane'):
		await message.channel.send('Nane time! *Upgrades people, upgrades*')
		with open('counter.txt', 'w') as myfile:
			#to remove the 'poyy nane' triggerword
			counter -= 1

			#saves the important numbers
			info = (f"{counter} {badpoyy} {goodpoyy} {srijeda} {peaky} {queen}")
			myfile.write(info)
			myfile.close()
			print("\n\n\n\n\n\n\n DATA SAVED \n\n\n\n\n\n\n")

			#closes the file and stops the program in the terminal
			raise KeyboardInterrupt

	if (message.author.id == 305465501595729921 and message.content.lower() == '+status'):
		print(f"\nCounter: {counter}\nBadpoyy: {badpoyy}\nGoodpoyy: {goodpoyy}\nSrijeda: {srijeda}\nPeaky: {peaky}\nQueen: {queen}")
		with open('counter.txt', 'w') as myfile:
			#to remove the 'poyy nane' triggerword
			counter -= 1

			#saves the important numbers
			info = (f"{counter} {badpoyy} {goodpoyy} {srijeda} {peaky} {queen}")
			myfile.write(info)
			print("\n\n DATA SAVED \n\n")
		return

	#Function that changes the counter amount so i don't have to manually do it
	if (message.author.id == 305465501595729921 and message.content.startswith('+counter')):
		msgg = message.content
		broj = int(msgg[9:])
		counter = broj


	#IMPORTANT: ID from the server for custom emotes
	guildstos = bot.get_guild(624602397204807681)
	guildmine = bot.get_guild(755531886956249098)
	guildfer  = bot.get_guild(650803962504675343)


	#temporary varibles used for printing
	user = message.author
	kontent = message.content
	vrijeme = time.strftime('%X')
	kanal = message.channel
	if str(kanal).startswith('Direct'):
		kanal = str(kanal)
		kanal = 'DM:   >>> ' + kanal[20:] + ' <<<'

	#formatting the string for printing in terminal for bugfixing
	print(f"C: {counter} - Time: {vrijeme} - Channel: {kanal} - User: {user} - Message: {kontent}")


	#most used variable, puts the whole text in lowercase for easier checking
	kontent = message.content.lower()

	#important to process all other commands which start with command_prefix='+'
	#doesn't need to pass through whole program with many checkers just to pass it to commands part
	_slika = message.content[1:]
	for comm in bot.commands:
		if _slika.startswith(str(comm)):
			await bot.process_commands(message)
			return


	# #birthday reminder
	# lista = ['194728866420359168', '220986468686888960', '191918592487325697', '755524718760820878', '160789671599669248', '109554759488266240', '705332541439344671', '755825034219749497', '663803129933856780', '692064709108564015', '767857540360699904','218787234910961665', '224862746964000768','365962520680333314','305465501595729921']
	# for i in lista:
	# 	i = int(i)
	# 	user = await bot.fetch_user(i)
	# 	await user.send('Hej!\nUskoro je Jarzin rođendan pa ga nemoj propustiti :heart: \nYours truly, PoyyBot')
	# 	print(f'Uspjesno poslao poruku {i}')

	matijacaBirthdayList = ['305465501595729921', '365962520680333314', '208207487025807360', '663803129933856780', '223441354259300352', '220986468686888960', '705332541439344671', '160789671599669248', '692064709108564015', '218787234910961665','229648988939223040', '191918592487325697', '194728866420359168', '755825034219749497', '755524718760820878', '109554759488266240', '767857540360699904','305465501595729921']
	YukiBirthdayList = ['305465501595729921','663803129933856780', '224862746964000768', '208207487025807360', '223441354259300352', '220986468686888960', '705332541439344671', '160789671599669248', '692064709108564015', '218787234910961665','229648988939223040', '191918592487325697', '194728866420359168', '755825034219749497', '755524718760820878', '109554759488266240', '767857540360699904','305465501595729921']
	if kontent == 'jkltest22' and message.author.id == 305465501595729921:
		for i in YukiBirthdayList:
			i = int(i)
			user = await bot.fetch_user(i)
			await user.send('Hej!\nIsprike što nisam javio ranije, danas je štosu rođendan! :heart: \nYours truly, PoyyBot')
			#await user.send('Sukladno sugestiji, važno je da naglasim da je rođendan sutra, za ~7 sati. :heart: \nPoyybot')
			print(f'Uspjesno poslao poruku {user.name}')



	if message.author.id == 305465501595729921 and message.content.startswith('+delete'):
		msg = message.content[8:]
		
		try:
			iid = int(msg)
		except:
			print('Wrong input')
		
		msg = await message.channel.fetch_message(iid)
		if msg.author.id != 782630417647796224:
			return

		await msg.delete()
		await message.delete()
		print(f'successfully deleted msg - {msg.content}')
		
		return

	if 'testt' in kontent and message.author.id == 305465501595729921:
		nekik = requests.get('https://picsum.photos/200/300', stream = True)
		# if catGif.status_code == 200:
		# 	await ctx.send(catGif.url)
		# else:
		# 	await ctx.send('Site je down sorry :(')
		# return

		if nekik.status_code == 200:
			print(nekik.content)
			nekik.raw.decode_content = True
			#bufr = io.BytesIO(nekik.content)
			#_slika = Image.frombuffer(bufr)
			image_data = nekik.content # byte values of the image
			#image = Image.frombytes('RGBA', (50,50), image_data, 'raw')
			image = Image.open(io.BytesIO(image_data))
			#image = Image.frombytes('RGBA', (200,300), image_data)
			#f = open("myfile.jpg", "rb")
			#f = io.BytesIO(bufr)

			await message.channel.send(file = image)


#################################################################
### FUNCTIONS WITH +	and special 

	#WIIIIIIIIIIIIIIIIIIIIIP
	if(message.content == '+help people'):

		await message.channel.send(
			"```" +
			"PoyyBot slike osoba: \n" +
			"   ❤️ chad ❤️       \n" + 
			"   ❤️ dome ❤️       \n" + 
			"   ❤️ GOD ❤️        \n" + 
			"   ❤️ jarza ❤️      \n" +
			"   ❤️ kluki ❤️      \n" + 
			"   ❤️ leica ❤️      \n" + 
			"   ❤️ nane ❤️       \n" + 
			"   ❤️ pasareta ❤️   \n" +
			"   ❤️ peace ❤️      \n" +
			"   ❤️ seky ❤️       \n" +
			"   ❤️ sexy ❤️       \n" +
			"   ❤️ smile ❤️      \n" +
			"   ❤️ synapsis ❤️   \n" +
			"   ❤️ štosdenfer ❤️ \n" + 
			"   ❤️ yuki ❤️       \n" +
			"   ❤️ waifu ❤️      \n" + 
			"   ❤️ wholesome ❤️  \n" +
			"   ❤️ +wholesome ❤️ \n" +
			"   ❤️ zucc ❤️       \n" + 
			"```")
		return

	if(message.content == '+help video'):

		await message.channel.send(
			"```" +
			"PoyyBot videos and GIFS: \n"+
			"   bljuc \n" +
			"   bunker \n" +
			"   brazil \n" +
			"   crab rave \n" +
			"   dome_angry\n" +
			"   fish \n" +
			"   gay \n" +
			"   jojcek \n" +
			"   ja cu se ubit \n" +
			"   kings \n" +
			"   milanovic \n" +
			"   motivacija \n" + 
			"   nmg \n" +
			"   noti noti \n" +
			"   plenky \n" +
			"   sekovno \n" +
			"   sotono \n" +
			"   spinny \n" +
			"   srpski pog \n"+
			"   važi \n" +
			"```")
		return

	if(message.content == '+help secret'):

		await message.channel.send(
			"```" +
			"PoyyBot secrets: \n"+
			"   do it motherfucker \n" +
			"   drunk Peace \n"+ 
			"   every time Štos is tagged \n" +
			"   GTFO \n" +
			"   HUG from Poyy \n" +
			"   kids \n" +
			"   kluki hug \n" +
			"   kluki S \n" +
			"   maurice \n" +
			"   Peaky go tag Peace \n" +
			"   p*yybot \n" +
			"   owo/uwu small chance \n" +
			"   sayonara_n1gga_cat \n" +
			"   srijeda \n" +
			"   volim te poyy \n" +
			"   youthrough \n" +
			"   yung jarza \n" +
			"   zucc dab \n" +
			"   1 bod \n" +
			"   007 or succ \n" +
			"   1000th message counter\n"+
			"potentially something else hehe... \n" +
			"```")
		return


###############################################
#### TIME CHECKERS

	#srijeda checker
	dan = time.strftime('%A')
	hours = int(time.strftime('%H'))
	minutes = int(time.strftime('%M'))
	day = time.strftime('%#d')
	month = int(time.strftime('%#m'))
	
	day = int(time.strftime('%#d'))

	#srijeda function utilizing strftime 
	if dan == 'Wednesday' and srijeda == 0:
		if hours >= 10:

			cenel = bot.get_channel(773940366499250227)
			await cenel.send('https://tenor.com/w0Xh.gif')
			await cenel.send('It is srijeda my drugovi REEEEEEEEEEEEEEEEEEEEEEEE')
			srijeda = 1
			return

	###peaky motivation function
	if month == 1 and peaky == 0:
		if hours >= 8 and hours <= 17:

			cenel = bot.get_channel(790215903823921182)

			await cenel.send('\U00002728')
			await cenel.send(file = discord.File(f'peaky/{day}.png'))
			await cenel.send('\U00002728')

			peaky = 1
			return

	#peaky reseter
	if peaky == 1 and hours >= 22:
		peaky = 0
		cenel = bot.get_channel(780881245499686932)
		_k = '<@305465501595729921>'
		await cenel.send(f'{_k} resetirao sam peaky')


	## queen of the day
	listaljudi = ['194728866420359168', '705332541439344671', '191918592487325697', '160789671599669248', '109554759488266240', '755825034219749497', '663803129933856780', '692064709108564015', '767857540360699904', '218787234910961665', '224862746964000768', '365962520680333314', '208207487025807360']
	#listaljudi = ['305465501595729921', '705332541439344671','755524718760820878','220986468686888960',]
	#listaljudi = ['194728866420359168',  '191918592487325697', '160789671599669248', '109554759488266240', '755825034219749497', '663803129933856780', '692064709108564015', '767857540360699904', '218787234910961665', '224862746964000768', '365962520680333314', '208207487025807360', '223441354259300352']
	
	#previous = ['705332541439344671', '755524718760820878', '223441354259300352', '218787234910961665', '663803129933856780', '220986468686888960', '191918592487325697', '109554759488266240','194728866420359168','692064709108564015','755825034219749497','224862746964000768','160789671599669248','767857540360699904','365962520680333314', '305465501595729921','208207487025807360']
	if queen == 0 and hours >= 10 and hours <= 17:
	
		queen = random.choice(listaljudi)
		queenstr = '<@' + queen + '>'
		queen = int(queen)
		
		cenel = bot.get_channel(773940366499250227)
		await cenel.send(f':sparkles: {queenstr} is QUEEN od the day! :crown:  YAAAS QUEEN SLAAAAY! :sparkles: ')
		return


	if queen != 0 and queen != 1 and hours >= 23:
		queen = 0
		cenel = bot.get_channel(780881245499686932)
		_k = '<@305465501595729921>'
		await cenel.send(f'{_k} resetirao sam queen')

	if message.author.id == queen:
		await message.add_reaction('\U0001F451')

	#custom queen selector
	# if message.content == 'testk2':
		
	# 	queen = '663803129933856780'
	# 	queenstr = '<@' + queen + '>'
	# 	queen = int(queen)
		
	# 	cenel = bot.get_channel(773940366499250227)
	# 	await cenel.send(f':sparkles: {queenstr} is QUEEN od the day! :crown:  YAAAS QUEEN SLAAAAY! :sparkles: ')
	# 	return


#########################################
#######  +functions


	## zvonko funkcija
	if message.content.startswith('+zvonko'):
		zvonko = ['bkvl', 'l a g a n o', 'lepo lepo', 'mnogo lepo', 'bude to tako nekada', 'tebra', 'Now I am become Death, the destroyer of Lopi!', "You can run, but you can't hide from SOA!"]
		out = random.choice(zvonko)
		await message.channel.send(out)
		return


	if message.content.startswith('+8ball'):
		_8ball = ['As I see it, yes.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again.', "Don’t count on it.", 'It is certain.', 'It is decidedly so.', 'Most likely.', 'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Outlook good.', 'Reply hazy, try again.', 'Signs point to yes.', 'Very doubtful.', 'Without a doubt.', 'Yes.', 'Yes – definitely.', 'You may rely on it.']

		autor = '<@' + str(message.author.id) + '>'
		response = random.choice(_8ball)
		print(response)
		async with message.channel.typing():
			await asyncio.sleep(1.5)

		await message.channel.send(embed=discord.Embed(title= 'Magic 8ball says:',description=f'{autor}, moj odgovor je -> **{response}**', color=0x000000))
		return

	if message.content.startswith('+smol'):
		string = message.content
		string = string[6:]
		autor = '<@' + str(message.author.id) + '>'
		lista='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
		smol = 'ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾᵠᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖᵠʳˢᵗᵘᵛʷˣʸᶻ'

		out = ""
		for i in string:
			try:
				slovo2 = lista.index(i)
				out += smol[slovo2]
			except:
				out += i

		out += f'\nᵇʸ: {autor}'

		await message.delete()
		await message.channel.send(out)
		return


	if message.content.startswith('+fensi'):
		string = message.content
		string = string[7:]
		autor = '<@' + str(message.author.id) + '>'

		# string = string.replace('A', '𝕬').replace('B', '𝕭').replace('C', '𝕮').replace('D', '𝕯').replace('E', '𝕰').replace('F', '𝕱').replace('G', '𝕲').replace('H', '𝕳').replace('I', '𝕴').replace('J', '𝕵').replace('K', '𝕶').replace('L', '𝕷').replace('M', '𝕸').replace('N', '𝕹').replace('O', '𝕺').replace('P', '𝕻').replace('Q', '𝕼').replace('R', '𝕽').replace('S', '𝕾').replace('T', '𝕿').replace('U', '𝖀').replace('V', '𝖁').replace('W', '𝖂').replace('X', '𝖃').replace('Y', '𝖄').replace('Z', '𝖅') \
		# 				.replace('a', '𝖆').replace('b', '𝖇').replace('c', '𝖈').replace('d', '𝖉').replace('e', '𝖊').replace('f', '𝖋').replace('g', '𝖌').replace('h', '𝖍').replace('i', '𝖎').replace('j', '𝖏').replace('k', '𝖐').replace('l', '𝖑').replace('m', '𝖒').replace('n', '𝖓').replace('o', '𝖔').replace('p', '𝖕').replace('q', '𝖖').replace('r', '𝖗').replace('s', '𝖘').replace('t', '𝖙').replace('u', '𝖚').replace('v', '𝖛').replace('w', '𝖜').replace('x', '𝖝').replace('y', '𝖞').replace('z', '𝖟')

		lista='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
		fensi='𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟'
		cur = 'Ą̷̹͖̲͓̥̞͐ͅB̶̼̻̳̫̩̫̳̿̔͗̚͘C̷̨̧̛͉͕͚͈̭̥̹̒̈̈̕D̴͉̗̤͕͙̠̀̒̄̾̓̎͘͠Ȅ̷̢̖͙̞̈̈́̈́̈̕͠F̴̨͓̲͔͇̤̪͇̑́̂͋̅G̵̢̡̨͖͉̥̖͙̅̂̑̒̚͜H̵̼̮͐̒̔̄̇̀̔I̴̺̭̳̹͕̤̫̣͒̽͋̋̀J̷̲̲̫̲̗͗̿̄̕ͅK̸͔̲̠̳̱͆̒̇͛̐͆͛͠Ḽ̸̥͇̜̳̪̀͝M̷͍̦͎̥̲͒̆N̶̯̗͓̟͐O̵̢̳̼̲͇̜̻̗͓̎͂͛̆͐͗̑͊P̶̦̱̻̯̭̪͍̙̣̯͌̀̀̀̃͛̅̕̚Q̶̨͉̖̤̯͇̩͆͒̐̅̓̑͑̌R̸͓͎̝̪̠͎̀̐͋͝S̵̙̭̉́́͐T̶̻͈̠̖̓ͅṴ̷̭͎̈́̉̅̌͂̕͜͜͝V̴̗̻̼̈̂̅̈͊̀̅͜W̷̖̥̮͕̭̣̫̳͉͑͋͜X̴̍̀̑͝ͅY̶̦̘̥͙͎̮͕̖̠̺̍̈́͛̋̉̑̑̐͑͝Z̷̢̛̪̲͍͎̤̜͕̬͋̅͜ą̷̛̳̥̯̖̒̇́͑̑̊̒̑͜͠ḃ̷̛̝̠̰̫̺̜̏͒̆̀͠c̴̡̨̹̪͉̍̏̾̆̚͜͝d̵̼̗͉͓̙̮̩͖̭͊̅̆͂̅̄̇̾͝e̶̠̞͇̘͇̼̱̓̓́̀͜f̸̛̰͂̊̉̓͆̉̿͘g̴̨̢̃͌͐͝h̵͈͔̼̰̩̺͓̫̣̉̀̋̀̅̇̊͘͜į̷̫̟͚̞͐̈́͜͠j̸̛̏͜k̵̢̖̭̭̤̹̖̿̉̏̐̎̑̉͐̆ͅĺ̵͙̺̲͓ṁ̸̛͕̣̺͉̗̘̓̍̑n̸̨̛̤͖̫͙̼̈́͂̀́͘o̶̙̩̖͚͎̹͇̦̘̙̎̆͂͝p̵͈͉͓̆̍̉̂̓̇̕͠q̶̧̣͔̻̮̟́̊͌̅̚͠r̴͔̹̯̪͎͐͆̿͋̓͛͐̈̈́̕s̶̪̋́̏̈́̽̉̓̒͌t̷̪̤͕̅͆́ů̵̯̣̩͉̰̆͛̍̈̔́͋́̓v̵̢̤̹͙͙͑͑̉͒̐̂͘͝w̸̧̞̭̖͚̲̅̐̚͘x̸͈̤̮̘͈̱͎̰̥̍̑́̓͘͜͝y̷͊́͑̂̋̋͘͜͠ż̷̯͉̣̩̲̯̈́͜'


		out = ""
		for i in string:
			try:
				slovo2 = lista.index(i)
				out += fensi[slovo2]
			except:
				out += i

		out += f'\n𝔟𝔶: {autor}'

		await message.delete()
		await message.channel.send(out)
		return


	#kluki randomizer since he is special
	if message.author.id == 220986468686888960:
		if (not random.randint(0, 150)):
			autor = '<@' + str(message.author.id) + '>'
			#klukicount = 0
			await message.channel.send(f'{autor} ja znam da ti mene najviše voliš na ovom serveru, ti imas posebno mjesto u mom ~~procesoru~~ srcu! :heart:')
			await message.channel.send(f'{autor} https://tenor.com/view/warm-hug-gif-10592083')


	if (not random.randint(0, 500)):
		autor = '<@' + str(message.author.id) + '>'
		await message.channel.send(f'Nasumično si odabran(a) za jedan veliki hug {autor} :heart:, puno mi znacis i nadam se da ćeš imati dobar ostatak dana! <:uwuLove:779332074665541663>')
		await message.channel.send(f'{autor} https://media.giphy.com/media/8tpiC1JAYVMFq/giphy.gif')


	if counter % 1000 == 0:
		## we dont want it to trigger on bots because it is not fun
		if message.author.id == 782630417647796224 or message.author.id == 235088799074484224 or message.author.id == 234395307759108106 or message.author.id == 777942093208748033:
			counter -= 10
			return

		k = counter // 1000
		autor = '<@' + str(message.author.id) + '>'
		await message.channel.send(f'{autor} je napisao/la vrlo specijalnu {k}000. poruku, WOOHOOOOO ')
		#await message.channel.send('AJMO DO 200k! <3')
		#await message.channel.send('https://tenor.com/view/excited-hockey-kid-yeah-gif-10474493')
		#await message.channel.send('https://tenor.com/view/pikachu-pokemon-love-happy-hearts-gif-16494752')
		#await message.channel.send('https://tenor.com/view/aw-cute-love-vibes-baby-yoda-star-wars-gif-16545548')
		#await message.channel.send('https://tenor.com/view/wee-woohoo-yay-baby-yoda-gif-18127486')
		#await message.channel.send('https://tenor.com/view/100-hundred-1000000-million-gif-13238033')
		#await message.channel.send('https://tenor.com/view/ansley-food-porn-harriott-kalman-gif-13660838')
		await message.channel.send('https://tenor.com/view/happy-corgi-cutie-pant-panting-gif-7525689')
		return


##################################################
### TEXT CHECKERS WITH TEXT/EMOJI RESPONSES
	######### Special for reviews

	#good reponse by bot, give +1 goodpoyy to rating
	if 'hvala poyy' in kontent:
		autor = '<@' + str(message.author.id) + '>'

		await message.channel.send(f"Nemaš frke srećo {autor}  <:uwuLove:779332074665541663> ")

		goodpoyy += 1
		return

	#bad reponse by bot, give +1 badpoyy to rating
	if 'bad poyy' in kontent:

		autor = '<@' + str(message.author.id) + '>'
		if message.author.id == 663803129933856780 or message.author.id == 755524718760820878:
			emoji = discord.utils.get(guildstos.emojis, name='sikeniggayouthought')
			await message.add_reaction(emoji)
			await message.channel.send(f"{autor} i know you don't, you love me :heart:")
			return

		await message.channel.send(f"{autor} hates me... I'm sorry... :sob:  I hope one day you will love me... :cry:  ")

		badpoyy += 1
		return

	#special response when addressing poyybot
	if 'volim te poyy' in kontent:
		autor = '<@' + str(message.author.id) + '>'
		goodpoyy += 1

		await message.channel.send(f"{autor} ja tebe volim više :heart:")
		return

	if (kontent == 'poyy' or kontent == 'pojj'):
		await message.channel.send('poyy  :heart:');
		await message.add_reaction('❤️')
		return


	if 'poyy' in kontent and not 'poyybot' in kontent:
		if(random.randint(0,50)):
			await message.channel.send('poyy  :heart:');
			await message.add_reaction('❤️')
			return
		else:
			await message.channel.send(file = discord.File('videos/sayonara_n1gga.webm'))

	if 'p*yybot' in kontent:
		autor = '<@' + str(message.author.id) + '>'
		await message.channel.send(f"{autor} WHY YOU DARE NOT MENTION MY NAME?!")

	if 'simp' in kontent:
		await message.add_reaction(discord.utils.get(guildstos.emojis, name='pepe_simp'))
		return

	# PoyyBot will always provide a hug
	if 'hug' in kontent:
		#returns hug emoji if hug needed
		await message.channel.send('\U0001FAC2')
		return

	#differet from srijeda checker, this is a text one
	if 'srijeda' in kontent:
		await message.channel.send('It is wednesday my dudes AAAAAAAAAAAAAAAAAAAAAAAAAAA')
		return

	if 'oof' in kontent or 'o o f' in kontent:
		await message.add_reaction(discord.utils.get(guildstos.emojis, name='oof'))
		await message.channel.send(discord.utils.get(guildstos.emojis, name='oof'))
		return

	#poggers has 50% chance to send loggers
	if kontent == 'pogg' or kontent == 'poggers' or kontent == 'pog':
		k = random.randint(0,2)
		if(k):
			await message.channel.send(file = discord.File('photos/loggers.png'))
		else:
			await message.channel.send(discord.utils.get(guildstos.emojis, name='pog'))
		return

	triggerwordZavodi = ["zpr", "zpm", "zpf", "zesoi", "zari", "ztel", "zoem", "zesa", "zvne", "zea", "zemris", "zkist"]

	for words in triggerwordZavodi:

		if words in kontent:
			words = words.upper()
			await message.channel.send(f'{words} makes me :face_vomiting:')
			return

	# #220986468686888960 = kluki, add S to his messages
	# if message.author.id == 220986468686888960:
	# 	await message.add_reaction('\U0001F1F8') #S

	#add BISH to yuki
	# if message.author.id == 663803129933856780:
	# 	await message.add_reaction('\U0001F171')
	# 	await message.add_reaction('\U0001F1EE')
	# 	await message.add_reaction('\U0001F1F8')
	# 	await message.add_reaction('\U0001F1ED')
	# 	return

	

	if message.content == '1': 
		k = random.randint(0,7)
		if(not k):
			await message.add_reaction('\U0001F1EF') #J
			await message.add_reaction('\U0001F1EA') #E
			await message.add_reaction('\U0001F171') #B
			await message.add_reaction('0️⃣') #O
			await message.add_reaction('\U0001F1FB') #V
			await message.add_reaction('\U0001F1E6') #A
			await message.add_reaction('\U0001F1F8') #S
		
		await message.add_reaction('1️⃣') #1
		await message.add_reaction('\U0001F1E7') #B
		await message.add_reaction('\U0001F1F4') #O
		await message.add_reaction('\U0001F1E9') #D
		return


	if "i'm" in kontent:
		index = kontent.find("i'm")
		part = kontent[index+4:]

		await message.channel.send(f"Hi {part}, **i'm dad** <:kekw:774064416441892884>")

		#print(kontent[index+4:])

	if "i am" in kontent:
		index = kontent.find("i am")
		part = kontent[index+5:]

		await message.channel.send(f"Hi {part}, **i am dad** <:kekw:774064416441892884>\nᵉ ⁿᵉᶜᵉˢ ˡᵒᵖᵒᵛᵉ")



##################################################
### PICTURE RESPONSES


	if '\U0001F449 \U0001F448' in kontent:
		#print('is for me')
		await message.channel.send(file = discord.File('photos/isforme.png'))


	###################################
	### Only specific word in message

	triggerwordsOnly = ['zucc','zucc dab', 'no u', 'babybrucos','get out', 'yuki', 'dome','peaky', 'peace', 'stosdenfer', 'jarza', 'kluki', 'leica', 'sexy', 'chad', 'makedonija', 'synapsis', 'jokes', 'seky', 'rok', 'kids', 'wholesome', 'take me out']

	kontent = kontent.replace('š', 's').replace('piki', 'peaky')

	for words in triggerwordsOnly:

		if kontent == words:

			if words == 'yuki':
				k = random.randint(0, 2)
				if(not k):
					words = words.replace('yuki', 'yukiwisperer')

			elif words == 'peace':
				k = random.randint(0, 2)
				if(not k):
					words = words.replace('peace', 'peace2')

			elif words == 'jarza':
				k = random.randint(0, 4)
				print(k)
				if(not k):
					words = words.replace('jarza', 'yungjarza')

			elif words == 'dome':
				k = random.randint(0, 4)
				print(k)
				if(not k):
					words = words.replace('dome', 'nobearddome')

			elif words == 'peaky':
				k = random.randint(0, 2)
				print(k)
				if(not k):
					await message.channel.send(file = discord.File(f'videos/smol.mp4'))
					return


			elif words == 'zucc':
				k = random.randint(0, 5)
				
				#random 10% chance for 007
				if(not k):
					if(random.randint(0, 1)):
						await message.channel.send('https://tenor.com/view/succ-meme-mr-succ-milk-boob-gif-18587671')
						return
					else:
						words = words.replace('zucc', '007')

			elif words == 'zucc dab':
				words = words.replace('zucc dab', 'zuccdab')

			elif words == 'get out':
				if(not random.randint(0,2)):
					words = 'getoutštos'
				else:
					words = words.replace('get out', 'getout')

			await message.channel.send(file = discord.File(f'photos/{words}.png'))
			return


	##random screenshots from camera voice 
	if 'smile' in kontent:
		_popis = ['alpha.png', 'alstrapon.png', 'anonimac.png', 'babyjuan.png', 'bendover.png', 'bodyBuilder.jpg', 'bruhdome.png', 'bruhkluki.png', 'cedevita.png', 'chaddome.png', 'chads.png', 'cowboy.png', 'cupic7.JPG', 'cupic_ispiti.png', 'cuteboi.png', 'dab.png', 'daddydone.png', 'daddyinsane.png', 'delet.jpg', 'domehead.png', 'domematija.png', 'domeyuki.png', 'domezucc.png', 'doubleheart.png', 'dripstos.jpg', 'drkas.png', 'drzse.png', 'dumbass.png', 'eat.png', 'edgar.png', 'fire.png', 'forme.png', 'ganggang.png', 'gecko.png', 'glu.png', 'god.png', 'hail.png', 'hair.jpg', 'hairless.jpg', 'happydome.png', 'heart.png', 'hideyowife.png', 'highboi.png', 'horny.png', 'hottuna.jpg', 'i was a bad girl.mp4', 'isforme.png', 'jackbox.png', 'jarzalea.png', 'jebemtimater.png', 'jump.png', 'kada.png', 'kkk.png', 'klukibrk.png', 'klukijarza.png', 'klukivlak1.jpg', 'klukivlak2.jpg', 'klukiyuki.png', 'klukizganac.png', 'klukizvonko.png', 'kosuljica.png', 'leadekica.jpg', 'leasynapsis.png', 'leayuki.png', 'leazucc.png', 'lightkluki.png', 'manyeyescursed.png', 'matijaca.png', 'matijaca2.png', 'mcdoggos.png', 'mcjarza.png', 'mckittys.png', 'mewvan.jpg', 'mlem.mp4', 'peacejarza.png', 'pisshulahopka.jpg', 'pizda.png', 'point.png', 'pov.png', 'prettyboi.png', 'scaryzucc.png', 'shitalot2.png', 'slonic.jpg', 'soa vidi sve.png', 'sus.png', 'swagsynapsis.png', 'synapsislea.png', 'synapsisyuki.png', 'synapsiszuc.png', 'tattooedpeace.jpg', 'tension.png', 'tiredkluki.png', 'trebal.jpg', 'vr.png', 'wedding.png', 'wholesome.png', 'wokejarza.png', 'wordscannotdescribehowperfectheis.jpg', 'yes.png', 'yuki.png', 'yukiDone.png', 'yukilea.png', 'yungdome2.png', 'yungdome3.png', 'yungdome4.png', 'yungyuki.png', 'zganac.png', 'zganac2.jpg', 'znanje.png', 'zuccbruhmoment.png', 'zuccchad.png', 'zuccpeace.png', 'žganac.png', 'žganaclana.png'] #,', 'peakycam.png'',''mladistos.png',','','','','',''

		_slika = random.choice(_popis)

		await message.channel.send(file = discord.File(f'smile/{_slika}'))
		return


	##random kluki screenshots
	if kontent == 'god':
		_klukipopis = ['aww.png', 'bluekluki.png', 'cat.jpg','chad.jpg', 'chad1.png', 'cutekluki.png', 'eyeskluki.jpg', 'god.png', 'kluki5.png', 'kluki6.png', 'klukicute.png', 'klukihot.jpg','klukijao.png','klukikiss.png', 'klukilove.png','klukiwtf.png','lightkluki.png','mete.png','prettykluki.jpg', 'Screenshot_1.png', 'Screenshot_2.png', 'smile.png', 'tiredkluki.png']

		_slika = random.choice(_klukipopis)

		await message.channel.send(file = discord.File(f'god/{_slika}'))
		return


	#cursed zvonko photos
	if 'cursed' in kontent:
		_cursedpopis = ['breath.png','cursedsmile.png','editaj.png','eyes.png','gledec.png','gledec2.png','gledeceye.png','gledeceye2.png','gledecheart.png','godpleaseburnusallwedonotdeservetoliveonthisworld.png','hairless.jpg','hee.png','kiklop.png','manyeyescursed.png','morejarza.png','nmg.png','no.png','radioactive.png','triple.png','what.jpg','why.png']

		_slika = random.choice(_cursedpopis)

		await message.channel.send(file = discord.File(f'cursed/{_slika}'))
		return

	#deepfried fotke by Dome
	if kontent == '+deepfried':
		_deepfriedpopis = ['dome.png','jarza.png','jarza3.png','leayuki.png','nane.png','peaky.png','peaky2.png','peaky3.png','synlea.png','synyuki.png','tuna.png','yuki.png','yungjarza.png','zganac.png','zvonko.png','zvonko2.png']

		_slika = random.choice(_deepfriedpopis)

		await message.channel.send(file = discord.File(f'deepfried/{_slika}'))
		return


	#photos from new year 2021.
	if kontent == '+wholesome':
		_newwholesomepopis = ['closeupyuki.jpg','doubledoggo.jpg','doubledoggo.jpg','drunkjarza.jpg','epicduo.jpg','firelea.jpg','fireworks.jpg','gentlmen.jpg','getout.png','happyjarza.jpg','happynewsynapsis.png','happyshookethyuki.jpg','happySmiles.jpg','happySquadCheers.jpg','happysynapsis.jpg','happytuna.jpg','jump.png','leachad.jpg','mcfireworks.png','oggypajki.jpg','panik.jpg','pixelatedlea.jpg','prayingtuna.jpg','returnofbruh.jpg','simps.jpg','sirshitalot.png','slightlydrunkjarza.jpg','slightlydrunkpeace.jpg','spiceyuki.jpg','squad.png','tuna&tuna.jpg','waves.jpg','year.png','zuccdab.png','zuccGoingHard.jpg','zuccInHisElement.jpg','zvonkohair.png']

		_slika = random.choice(_newwholesomepopis)

		await message.channel.send(file = discord.File(f'wholesome/{_slika}'))
		return


	if 'discrt' in kontent:
		_discrtpopis = ['anime.png','awwwwww.jpg', 'babybrucos.png', 'bonk.png', 'circlegang.jpg', 'jarunhepi.jpg', 'jarunskvat.jpg', 'kiss.png', 'kuhinjagang.jpg', 'meme1.png', 'meme2.png', 'meme3.png', 'meme4.png', 'meme5.png', 'meme6.jpg', 'meth.jpg', 'persuasion.jpg', 'rakija.png', 'surprised.jpg', 'tavatava.jpg', 'thelook.jpg', 'view.jpg', 'yukigoddess.png']

		_slika = random.choice(_discrtpopis)

		await message.channel.send(file = discord.File(f'discrt/{_slika}'))
		return


	####################################
	### Triggerword anywhere in message
	
	triggerwordAnywhere = ['aaaaaaaaa', 'big pp', 'bonk', 'cute', 'fersisa', 'fiz', 'getout', 'gledec', 'happy', 'juan', 'matan2', 'nane', 'nibba', 'ocean', 'pasareta', 'perhaps', 'poopyhead', 'stegovna', 'stegovno', 'terrified', 'uuuuuuuuu', 'vojko', 'waifu', 'wifey', 'wify', 'zabok', 'zebok']

	
	kontent = kontent.replace('rock', 'gledec').replace('8400', 'gledec').replace('dekan', 'gledec').replace('anonimac', 'poopyhead').replace('sleep', 'nane').replace('motion', 'ocean').replace('fer sisa', 'fersisa').replace('gtfo', 'getout').replace('z*bok', 'zebok').replace('zab*k', 'zebok')

	for words in triggerwordAnywhere:

		if words in kontent:
			if words == 'pasareta':
				if (not random.randint(0,2)):
					words = 'yukigoddess'

			elif words == 'bonk':
				if (not random.randint(0,2)):
					words = 'cyberbonk'

			await message.channel.send(file = discord.File(f'photos/{words}.png'))
			return


	#kurac photo
	triggerwordsKurac = ["kurac", "kurca",  "kurcu", "kurčina", "kurcina"]

	if any(x in kontent for x in triggerwordsKurac):
		await message.channel.send(file=discord.File('photos/kurac.jpg'))
		return

	#reacts with uwu photo by Yuki, but has  secret chance
	if ('owo' in kontent or 'uwu' in kontent):
		#stops bot from triggering when uwuLove emoji is in message


		if "<:uwuLove:779332074665541663>" in message.content:
			return
		# uwu has a 5% chance of triggering daddyUwu emoji instead
		else:
			if (random.randint(0,19)):
				await message.channel.send(file = discord.File('photos/uwu.png'))

			else:
				emoji = discord.utils.get(guildstos.emojis, name='daddy_uwu')
				await message.channel.send(emoji)
			return

##################################################
### VIDEO RESPONSES

	triggerwordVideo = ['kings', 'milanovic', 'plenky', 'sotono', 'spinny', 'srpskipog', 'jacuseubit', 'maurice', 'doit']

	kontent = kontent.replace('ubit cu se', 'jacuseubit').replace(' ', '').replace('dewit','doit')

	for words in triggerwordVideo:

		if kontent == words:

			await message.channel.send(file = discord.File(f'videos/{words}.mp4'))
			return

	#motivacija, by Vladimir Tintor
	if kontent == 'motivacija':
		lista = ['breaking_news.mp4', 'deep_voice_pustite_ih.mp4', 'ne_brini_toliko.mp4', 'sreća.mp4', 'vi_ste_od_toga_jaci.mp4', 'vjeruj_u_sebe.mp4', 'voljeni.mp4']		
		video = random.choice(lista)
		await message.channel.send(file=discord.File(f'videos/motivacija/{video}'))
		return

	#how bees are, probably should add beer, but it is funny
	if ('bee' in kontent) and not('been' in kontent):

		await message.channel.send('https://www.youtube.com/watch?v=SyPjwxHxbus&ab_channel=DaSassyOwl')
		return

##################################################
### PINGED PEOPLE
	

	#Only if peaky taggs peace
	if message.content == '<@692064709108564015>' and message.author.id == 755524718760820878:
		await message.channel.send(file = discord.File('photos/invertor.png'))
		return


	if message.content.startswith('+bad') and len(message.mentions):
		autor = '<@' + str(message.author.id) + '>'
		tagged = '<@' + str(message.mentions[0].id) + '>'
		embed = discord.Embed(description= f'{autor} thinks {tagged} was bad and needs to be punished',color=discord.Colour.purple())
		await message.channel.send(embed = embed.set_image(url="https://cdn.weeb.sh/images/H1eoWIDdb.gif"))
		return

	if(len(message.mentions)):

		#Only when daddy owner is tagged, add daddy_buldge reaction
		if message.mentions[0].id == 365962520680333314:
			await message.add_reaction(discord.utils.get(guildstos.emojis, name='trebalOvdjeKomeJebatB'))


		#voli but needs to be tagged
		if 'voli' in kontent:
			autor = '<@' + str(message.author.id) + '>'
			iid = '<@' + str(message.mentions[0].id) + '>'

			await message.channel.send(f":heart: {autor} voli {iid} :heart:")
			return

		#Only if someone responds to bots
		if message.mentions[0].id == 782630417647796224:
			await message.add_reaction('❤️')
			await message.add_reaction('\U0001F1F1')
			await message.add_reaction('\U0001F1FE')
			return


	#bubi function, it is possible to bubi up to 5 people, or just the one
	if 'bubi' in kontent:

		autor = '<@' + str(message.author.id) + '>'

		if(len(message.mentions)):

			if(len(message.mentions) == 1):

				iid = '<@' + str(message.mentions[0].id) + '>'
				await message.channel.send(f"{autor} really cares for {iid}   <:uwuLove:779332074665541663>   :heart:   <:uwu:774299564693520405>")
				return

			elif(len(message.mentions) <= 5):

				iid = '<@' + str(message.mentions[0].id) + '>'
				output = f"{autor} really cares for {iid}"

				for i in range(1,len(message.mentions)):
					iid = '<@' + str(message.mentions[i].id) + '>'
					output += f" and {iid}" 

				output += f"   <:uwuLove:779332074665541663>   :heart:   <:uwu:774299564693520405>"
				await message.channel.send(output)
				return


	##################################################
	### GIFS

	if 'nmg' in kontent:
		await message.channel.send('https://images-ext-2.discordapp.net/external/XxiQ3MWopOapikJ3p-jJ0wGaCjXzaeYXBvCr824Eu3w/https/i.picasion.com/gl/90/dLDc.gif')
		return

	if 'bljuc' in kontent:
		await message.channel.send('http://i.picasion.com/gl/90/dLCV.gif')
		return

	if 'jojcek' in kontent:
		await message.channel.send('http://i.picasion.com/gl/90/dMcP.gif')
		return

	if 'bunker' in kontent:
		await message.channel.send('https://images-ext-2.discordapp.net/external/NzP4X-Q3-ZwhHYlTuxXXBV2p7lXxXRPxzphtkyHBHXw/http/i.picasion.com/gl/90/dMFg.gif')
		return

	if 'važi' in kontent or 'vazi' in kontent:
		await message.channel.send('https://media.discordapp.net/attachments/771420916919304254/788147355143766016/dOvb.gif')
		return

	if 'gay' in kontent:
		if not '<:sikeniggayouthought:777509133720748044>' in kontent:
			await message.channel.send('https://tenor.com/view/gaaay-hagay-ha-gay-kenjeong-gif-5277255')
		return

	if 'fish' in kontent or 'gluglu' in kontent or 'tuna' in kontent:
		await message.channel.send('https://media.discordapp.net/attachments/773940366499250227/788890146891104306/blub.gif')
		return

	if 'brazil' in kontent:
		await message.channel.send('https://tenor.com/view/brazil-youre-going-to-brazil-your-going-to-brazil-ur-going-to-brazil-gif-17868304')
		return

	if 'yukihell' in kontent:
		await message.add_reaction(discord.utils.get(guildstos.emojis, name='yukiHell'))
		await message.channel.send('https://tenor.com/view/yuki-elmo-hands-up-fire-flames-gif-16709640');
		return

	if 'crabrave' in kontent:
		await message.channel.send('https://tenor.com/view/crab-safe-dance-gif-13211112')
		return

	if 'ubikurvu' in kontent:
		await message.channel.send('https://tenor.com/view/yay-oh-tom-and-jerry-jerry-sword-gif-149870452')
		return

	if 'sekovno' in kontent:
		await message.channel.send(file=discord.File('videos/sekovno.gif'))
		return

	if 'notinoti' in kontent:
		await message.channel.send(file=discord.File('videos/notinoti.gif'))
		return

	if ':dome_angry:' in kontent:
		await message.channel.send('https://cdn.discordapp.com/attachments/773940366499250227/790580101594742844/20201221_145931_001_1.gif')
		return


	jutra = ['youtrou', 'youtrough', 'jutro', 'youtrugh', 'youthrough', 'youthrou', 'yutreko', 'joutro', 'youtrhow' , 'dobrough', 'dobrou', 'jutar', 'hello', 'youghtrou']
	for words in jutra:
		if words in kontent:
			if(random.randint(0, 1)):
				await message.channel.send(discord.utils.get(guildstos.emojis, name='hello'))
				return
			await message.channel.send(discord.utils.get(guildstos.emojis, name='suhdude'))
			return


	##################################################
	### NITRO EMOTES
	
	if 'pavle' in kontent or 'pauq' in kontent:
		await message.channel.send(discord.utils.get(guildmine.emojis, name='pavlepauq'))
		return

	if 'dsg' in kontent:
		await message.channel.send(discord.utils.get(guildmine.emojis, name='dsg'))
		return

	if 'weirdchamp' in kontent:
		await message.channel.send(discord.utils.get(guildmine.emojis, name='WeirdChamp'))
		return

	if 'kommre' in kontent or 'kommie' in kontent:
		await message.channel.send(discord.utils.get(guildmine.emojis, name='kommre'))
		return

	triggerwordEmote = [':yukiHell:', ':catjam:', ':nipple_lick:', ':yuki_angry:']
	for words in triggerwordEmote:

		if words in kontent:
			words = words.replace(':','')
			await message.channel.send(discord.utils.get(guildstos.emojis, name=f'{words}'))

	return
	

#help command with main commands
@bot.command()
async def help(ctx):

	#formatting help command alphabetically 
	await ctx.send(embed=discord.Embed(title='Common functions', description= 
		"```" +
		"PoyyBot commands: \n"+
		"   +8ball              -for life dilemas \n" + 
		"   +cat                -najbolja funkcija\n" +
		"   +deepfried          -deepfried photos \n" + 
		"   +help people        -za slike specijalaca\n"+
		"   +help video         -popis videa i gifova\n"+
		"   +owo                -owofy text\n" +
		"   +peakify            -p e a k y i f y s  text\n" +
		"   +zvonko             -bude to tako nekada\n" +
		"   AAAAAAAAA           -AAAAAAAAAAAAAAA\n" + 
		"   bad poyy            -ako mrzite Poyya :( \n" +
		"   bee 				-how bees are\n" +
		"   bubi @tag           -we care for eachother \n" +
		"   cursed               -cursed Zvonko\n" +
		"   cute                -OwO \n"+
		"   FER SISA            -hehe svi znamo\n" + 
		"   gledec              -sexy dekan \n"+
		"   happy               -drunk Kluki\n" +
		"   hug                 -Poyy will always provide a hug\n"+
		"   hvala poyy          -ako volite Poyya\n" +
		"   Juan                -our dearest, za Yuki\n" + 
		"   jokes               -jokes on you im into that shit\n" +
		"   kurac/kurčina       -Charlie Oces malo?\n" +
		"   big PP              -chad Charlie\n" +   
		"   nibba               -hehe dark\n" +
		"   ocean               -ocean motion or something\n"+
		"   oof                 -rough       \n" +
		"   perhaps             -perhaps?\n"+
		"   pog                 -POGGERS\n" +
		"   poyy/pojj           -poyy kolege ❤️\n" + 
		"   👉👈               -is for me?\n"+
		"   premium emotovi ->  :yuki_angry:, :catjam:, :nipple_lick:,\n" +
		"   					:yukiHell:, :dome_angry: \n" + 		
		"   SIMP                -reaction \n" + 
		"   srijeda             -AAAAAAAAAAAAAAA\n" +
		"   stegovno            -kad se doxamo\n" +
		"   uuuuuuuuu           -kluki rage\n" +
		"   UwU/OwO             -one of the cutest emotes\n" + 
		"   volim               -PoyyBot vas uvijek voli\n" +
		"   Yukihell            -our permanent home\n" + 
		"   zabok               -Heaven\n"+
		"   zavod               -da se Kluki moze žaliti\n" + 
		"```", color=0x3366FF))
	return

#send random cat gif, from CatAPI database
@bot.command(aliases= ['kot', 'kotek', 'koty'])
async def cat(ctx):
	catGif = requests.get('http://thecatapi.com/api/images/get?format=src&type=gif')
	if catGif.status_code == 200:
		await ctx.send(catGif.url)
	else:
		await ctx.send('Site je down sorry :(')
	return

@bot.command()
async def facat(ctx):

	_k = requests.get('https://meowfacts.herokuapp.com/')
	_k = _k.text[9:-2]
	await ctx.send(embed=discord.Embed(description=_k, color=0xfe7448))
	return


@bot.command()
async def uleti(ctx):
	
	_k = random.randint(1,60)
	_line = linecache.getline('uleti.txt', _k)
	await ctx.send(_line)
	
	linecache.clearcache()
	return

@bot.command()
async def cum(ctx):
	_k = random.randint(1,110)
	_line = linecache.getline('cumandgo.txt', _k)
	embed = discord.Embed(title= _line,color=discord.Colour.green())
	await ctx.send(embed = embed)
	
	linecache.clearcache()
	return


@bot.command()
async def id(ctx, arg1, *args):
	if (not (ctx.author.id == 305465501595729921)):
		return
	msg = ''
	for arg in args:
		msg = msg + ' ' + arg

	user = await bot.fetch_user(int(arg1))

	await user.send(msg)
	print(f'>>> TO: {user.name} - {msg} <<<')
	return



###spreads text with spaces like: L o r e m  I p s u m
@bot.command()
async def peakify(ctx, *args):
	string = ''
	for arg in args:
		string = string + ' ' + arg

	string = string.replace(' ', ' \U00002728 ')
	string = list(string)
	out = ''
	for s in string:
		out += (str(s) + ' ')
	out += ' \U00002728'
	

	if len(out) <= 250:

		await ctx.send(embed=discord.Embed(title=out, color=0xb00b13))

	else:

		out1 = out[:1800]
		await ctx.send(embed=discord.Embed(description=out1, color=0xb00b13))

		if len(out) > 1800:

			out1 = out[1800:]
			await ctx.send(embed=discord.Embed(description=out1, color=0xb00b13))

	if str(ctx.channel).startswith('Direct'):
		print("Direct je, can't delete")
	else:
		await ctx.message.delete()
	return

# String owofyer, changes using regex
@bot.command()
async def owo(ctx, *args):
	string = ''
	for arg in args:
		string = string + ' ' + arg

	_lenny_list = ['(◕ᴥ◕)', '(人 ◕ω◕)', '^ↀᴥↀ^','(๑￫ܫ￩)', '(❍ᴥ❍ʋ)', '(✪‿✪)ノ', 'ʕ￫ᴥ￩ʔ', 'ʕ•ᴥ•ʔ', 'ʕ·ᴥ·ʔ', '(✿ヘᴥヘ)', '(ﾉ≧ڡ≦)', '(✾♛‿♛)', '( ͡°❥ ͡°)', '( ͡°👅 ͡°)', '꒒ ০ ⌵ ୧ ♡', '༼♥ ل͜ ♥༽','ʕ•̬͡•ʔ', '(๑•́ ω •̀๑)', 'ᵔᴥᵔ)','( っ´ω｀c)','( ^◡^)','╰(⸝⸝⸝´꒳`⸝⸝⸝)╯', '(♥ω♥ ) ~♪', '( ﾟ∀ﾟ)ﾉ【I LOVE U】', '(>^_^)><(^o^<)']
	string = re.sub(r'(?:r|l)', 'w', string)
	string = re.sub(r'(?:R|L)', 'W', string)
	string = re.sub(r'n([aeiou])', 'ny', string)
	string = re.sub(r'N([aeiou])', 'Ny', string)
	string = re.sub(r'N([AEIOU])', 'Ny', string)
	string = re.sub(r'(?:r|l)', 'w', string)
	string = re.sub(r'ove', 'uv', string)
	#5: is to remove +owo from the start
	
	out = random.choice(_lenny_list) + '  ' + string + '  ' + random.choice(_lenny_list)

	if len(out) <= 250:

		await ctx.send(embed=discord.Embed(title=out, color=0xffc0cb))

	else:

		out1 = out[:1800]
		await ctx.send(embed=discord.Embed(description=out1, color=0xffc0cb))

		if len(out) > 1800:

			out1 = out[1800:]
			await ctx.send(embed=discord.Embed(description=out1, color=0xffc0cb))

	if str(ctx.channel).startswith('Direct'):
		print("Direct je, can't delete")
	else:
		await ctx.message.delete()
	return



print('Starting program...')

bot.run('TOKEN')

