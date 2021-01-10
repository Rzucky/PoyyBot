import discord
import asyncio
import requests
import random
import json
import time
import re
import linecache

#####################################################################################
############  Bot written to add fun features to Štosfender server
#########  Version 2.7.0
####### Python 3.8.4 and discord.py version 1.5.1
###### Author: zucc#4876

#actually not a bot but the Client but more permissions
bot = discord.Client() 


#dumb reason, it has to be defined before events
counter = 0
badpoyy = 0
goodpoyy = 0
srijeda = 1
peaky = 1
queen = 1

########kluki kompresor
############## betting game pomocu jsona
################ rodendani pomocu jsona
########################## on disconnect test sa spremanjem by writing message u svoj
################################### potentially reactions 
##################################### do the tenor shit
########### terry talk
################################ hit it and quit it u listu, procitati i onda random baci



@bot.event
async def on_ready():

	#Bot takes ~3-4s to startup
	print('PoyyBot online') 

	# 2 possible activites: Watching and Playing 
	#activity = discord.Activity(name='you pee :smirk:', type=discord.ActivityType.watching)
	#await bot.change_presence(activity=discord.Activity(name='you pee :smirk:', type=discord.ActivityType.watching))
	#await bot.change_presence(activity=discord.Game(name='poyy kolege ❤️'))

	# Setting `Listening ` status
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="old nostalgic songs"))

	#await bot.change_presence(activity=discord.Game(name='with Xmas decorations ❤️'))

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

	#if Yuki needs to be temporarely muted
	# if message.author.id == 663803129933856780:
	# 	return

	#if Dome needs to be temporarely muted
	# if message.author.id == 705332541439344671:
	# 	return

	#69420 special event
	if counter == 69420:
		if message.author.id == 782630417647796224 or message.author.id == 235088799074484224 or message.author.id == 234395307759108106 or message.author.id == 777942093208748033:
			counter -= 10
			return

		autor = '<@' + str(message.author.id) + '>'
		await message.channel.send(f'{autor} sent 69420th message. Teehee funny number nice. Good job! We getting high af!')
		await message.channel.send('https://tenor.com/view/bobux-gif-18603683')
		await message.channel.send('https://tenor.com/view/lizard-dancing-poggers-lizard-dance-poggers-gif-18527737')
		await message.channel.send('https://tenor.com/view/katie-nolan-69-golf-tougue-out-gif-12612419')
		return

	
	
	if message.channel.id == 782586423332175883:
		return

	#Bot shutdown procedure, only if it by me
	if (message.author.id == 305465501595729921 and message.content.lower() == 'poyy nane'):
		await message.channel.send('Nane time! *Upgrades people, upgrades*')
		with open('counter.txt', 'r+') as myfile:
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
		with open('counter.txt', 'r+') as myfile:
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

	#temporary varibles used for printing
	user = message.author
	kontent = message.content
	vrijeme = time.strftime('%X %x')


	#formatting the string for printing in terminal for bugfixing
	print(f"C: {counter} - Time: {vrijeme} - User: {user} - Message: {kontent}")

	#most used variable, puts the whole text in lowercase for easier checking
	kontent = message.content.lower()

	# #birthday reminder
	# lista = ['194728866420359168', '220986468686888960', '191918592487325697', '755524718760820878', '160789671599669248', '109554759488266240', '705332541439344671', '755825034219749497', '663803129933856780', '692064709108564015', '767857540360699904','218787234910961665', '224862746964000768','365962520680333314','305465501595729921']
	# for i in lista:
	# 	i = int(i)
	# 	user = await bot.fetch_user(i)
	# 	await user.send('Hej!\nUskoro je Jarzin rođendan pa ga nemoj propustiti :heart: \nYours truly, PoyyBot')
	# 	print(f'Uspjesno poslao poruku {i}')


#################################################################
### FUNCTIONS WITH +	and special 

	#formatting help command alphabetically 
	if(message.content == '+help'):

		await message.channel.send(embed=discord.Embed(title='Common functions', description= 
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

	if(message.content == '+help people'):

		await message.channel.send(
			"```" +
			"PoyyBot slike osoba: \n"+
			"   ❤️ chad ❤️      \n" + 
			"   ❤️ dome ❤️      \n" + 
			"   ❤️ GOD ❤️       \n" + 
			"   ❤️ jarza ❤️     \n" +
			"   ❤️ kluki ❤️     \n" + 
			"   ❤️ leica ❤️     \n" + 
			"   ❤️ nane ❤️      \n" + 
			"   ❤️ pasareta ❤️  \n" +
			"   ❤️ peace ❤️     \n" +
			"   ❤️ seky ❤️      \n" +
			"   ❤️ sexy ❤️      \n" +
			"   ❤️ smile ❤️     \n" +
			"   ❤️ synapsis ❤️  \n" +
			"   ❤️ štosdenfer ❤️\n" + 
			"   ❤️ yuki ❤️      \n" + 
			"   ❤️ wholesome ❤️ \n" +
			"   ❤️ +wholesome ❤️\n" +
			"   ❤️ zucc ❤️      \n" + 
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
			"   Peaky go tag Peace \n" +
			"   every time Štos is tagged \n" +
			"   owo/uwu small chance \n" +
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
		if hours >= 8 and hours <= 14:

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
	listaljudi = ['194728866420359168', '220986468686888960', '191918592487325697', '755524718760820878', '160789671599669248', '109554759488266240', '705332541439344671', '755825034219749497', '663803129933856780', '692064709108564015', '767857540360699904', '218787234910961665', '224862746964000768', '365962520680333314', '208207487025807360', '223441354259300352', '305465501595729921']

	if queen == 0 and hours >= 10 and hours <= 13:
		
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


#########################################
#######  +functions

	# String owofyer, changes using regex
	if message.content.startswith('+owo'):

		string = message.content
		string = re.sub(r'(?:r|l)', 'w', string)
		string = re.sub(r'(?:R|L)', 'W', string)
		string = re.sub(r'n([aeiou])', 'ny', string)
		string = re.sub(r'N([aeiou])', 'Ny', string)
		string = re.sub(r'N([AEIOU])', 'Ny', string)
		string = re.sub(r'(?:r|l)', 'w', string)
		string = re.sub(r'ove', 'uv', string)
		#5: is to remove +owo from the start
		await message.channel.send('<:uwu:774299564693520405>  ' + string[5:] + '  <:uwu:774299564693520405>' );
		return
	
	#send random cat gif, from CatAPI database
	if kontent == '+cat' or kontent == 'kot' or kontent == 'koty' or kontent == 'kotek':

		catGif = requests.get('http://thecatapi.com/api/images/get?format=src&type=gif')
		if catGif.status_code == 200:
			await message.channel.send(catGif.url)
		else:
			await message.channel.send('Site je down sorry :(')


	if (not random.randint(0, 300)):
		autor = '<@' + str(message.author.id) + '>'
		await message.channel.send(f'Nasumično si odabran(a) za jedan veliki hug {autor} :heart:, puno mi znacis i nadam se da ćeš imati dobar ostatak dana! <:uwuLove:779332074665541663>')
		await message.channel.send(f'{autor} https://media.giphy.com/media/ZQN9jsRWp1M76/giphy.gif')




##################################################
### TEXT CHECKERS WITH TEXT/EMOJI RESPONSES

	if (kontent == 'poyy' or kontent == 'pojj'):
		
		await message.channel.send('poyy  :heart:');
		await message.add_reaction('❤️')


	##### to be checked
	# if (('sad' in kontent) and not(':sad_pepe:' in kontent)):
	# 	await message.add_reaction('\U0001FAC2')

	if 'poyy' in kontent and not 'poyybot' in kontent:
		await message.channel.send('poyy  :heart:');
		await message.add_reaction('❤️')

	# if 'simp' in kontent:
	# 	await message.add_reaction(discord.utils.get(guildstos.emojis, name='pepe_simp'))

	if 'nane' in kontent or 'sleep' in kontent:
		kontent = kontent.replace('sleep', 'nane')
		await message.channel.send(file = discord.File(f'photos/{words}.png'))

	if 'hug' in kontent:
		#returns hug emoji if hug needed
		await message.channel.send('\U0001FAC2')

	if 'srijeda' in kontent:
		await message.channel.send('It is wednesday my dudes AAAAAAAAAAAAAAAAAAAAAAAAAAA')

	if 'oof' in kontent or 'o o f' in kontent:
		await message.add_reaction(discord.utils.get(guildstos.emojis, name='oof'))
		await message.channel.send(discord.utils.get(guildstos.emojis, name='oof'))

	if 'owo' in kontent or 'uwu' in kontent:
		if (random.randint(0,19)):
			emoji = discord.utils.get(guildstos.emojis, name='uwu')
			await message.channel.send(emoji)
		else:
			emoji = discord.utils.get(guildstos.emojis, name='daddy_uwu')
			await message.channel.send(emoji)


	if 'voli' in kontent:
		autor = '<@' + str(message.author.id) + '>'

		await message.channel.send(f"Volim te {autor} :heart:")

	if kontent == 'pogg' or kontent == 'poggers' or kontent == 'pog':
		await message.channel.send(discord.utils.get(guildstos.emojis, name='pog'))

	triggerwordZavodi = ["zpr", "zpm", "zpf", "zesoi", "zari", "ztel", "zoem", "zesa", "zvne", "zea", "zemris", "zkist"]

	for words in triggerwordZavodi:

		if words in kontent:
			words = words.upper()
			await message.channel.send(f'{words} makes me :face_vomiting:')
	

	######### Special for reviews
	if 'hvala poyy' in kontent:
		autor = '<@' + str(message.author.id) + '>'

		await message.channel.send(f"Nemaš frke srećo {autor}  <:uwuLove:779332074665541663> ")

		goodpoyy += 1
		return

	if 'bad poyy' in kontent:
		autor = '<@' + str(message.author.id) + '>'

		await message.channel.send(f"{autor} hates me... I'm sorry... :sob:  I hope one day you will love me... :cry:  ")

		badpoyy += 1
		return

##################################################
### PICTURE RESPONSES


	if '\U0001F449 \U0001F448' in kontent:
		#print('is for me')
		await message.channel.send(file = discord.File('photos/isforme.png'))

	###################################
	### Only specific word in message

	triggerwordsOnly = ['zucc', 'yuki', 'dome', 'peace', 'stosdenfer', 'jarza', 'kluki', 'leica', 'sexy', 'chad', 'makedonija']

	kontent = kontent.replace('š', 's')

	for words in triggerwordsOnly:

		if kontent == words:
			await message.channel.send(file = discord.File(f'photos/{words}.png'))


	####################################
	### Triggerword anywhere in message
	
	triggerwordAnywhere = ['uuuuuuuuu','juan', 'perhaps', 'wholesome', 'zabok', 'nibba', 'pasareta', 'cute', 'fersisa', 'ocean', 'aaaaaaaaa', 'big pp', 'gledec', 'stegovno', 'stegovna']

	kontent = kontent.replace(' ', '')
	kontent = kontent.replace('rock', 'gledec')
	kontent = kontent.replace('8400', 'gledec')
	kontent = kontent.replace('dekan', 'gledec')
	
	kontent = kontent.replace('motion', 'ocean')

	for words in triggerwordAnywhere:

		if words in kontent:
			await message.channel.send(file = discord.File(f'photos/{words}.png'))

	triggerwordsKurac = ["kurac", "kurca",  "kurcu", "kurčina", "kurcina"]

	if any(x in kontent for x in triggerwordsKurac):
		await message.channel.send(file=discord.File('photos/kurac.jpg'))


##################################################
### VIDEO RESPONSES

	triggerwordVideo = ['kings', 'milanovic', 'plenky', 'sotono', 'spinny', 'srpskipog', 'jacuseubit']

	kontent = kontent.replace('ubit cu se', 'jacuseubit')
	
	for words in triggerwordVideo:

		if kontent == words:
			await message.channel.send(file = discord.File(f'videos/{words}.mp4'))

	if kontent == 'motivacija':
		lista = ['breaking_news.mp4', 'deep_voice_pustite_ih.mp4', 'ne_brini_toliko.mp4', 'sreća.mp4', 'vi_ste_od_toga_jaci.mp4', 'vjeruj_u_sebe.mp4', 'voljeni.mp4']		
		video = random.choice(lista)
		await message.channel.send(file=discord.File(f'motivacija/{video}'))



##################################################
### PINGED PEOPLE
	

	#Only if peaky taggs peace
	if message.content == '<@692064709108564015>' and message.author.id == 755524718760820878:
		await message.channel.send(file = discord.File('photos/invertor.png'))


	if(len(message.mentions)):

		#Only when daddy owner is tagged, add daddy_buldge reaction
		if message.mentions[0].id == 365962520680333314:
			await message.add_reaction(discord.utils.get(guildstos.emojis, name='daddy_buldge'))

		#Only if someone responds to bots
		if message.mentions[0].id == 782630417647796224:
			await message.add_reaction('❤️')
			await message.add_reaction('\U0001F1F1')
			await message.add_reaction('\U0001F1FE')

	if 'bubi' in kontent:

		autor = '<@' + str(message.author.id) + '>'

		if(len(message.mentions)):

			if(len(message.mentions) == 1):

				iid = '<@' + str(message.mentions[0].id) + '>'
				await message.channel.send(f"{autor} really cares for {iid}   <:uwuLove:779332074665541663>   :heart:   <:uwu:774299564693520405>")

			elif(len(message.mentions) <= 5):

				iid = '<@' + str(message.mentions[0].id) + '>'
				output = f"{autor} really cares for {iid}"

				for i in range(1,len(message.mentions)):
					iid = '<@' + str(message.mentions[i].id) + '>'
					output += f" and {iid}" 

				output += f"   <:uwuLove:779332074665541663>   :heart:   <:uwu:774299564693520405>"
				await message.channel.send(output)



	##################################################
	### GIFS

	if 'nmg' in kontent:
		await message.channel.send('https://images-ext-2.discordapp.net/external/XxiQ3MWopOapikJ3p-jJ0wGaCjXzaeYXBvCr824Eu3w/https/i.picasion.com/gl/90/dLDc.gif')

	if 'bljuc' in kontent:
		await message.channel.send('http://i.picasion.com/gl/90/dLCV.gif')

	if 'gay' in kontent:
		await message.channel.send('https://tenor.com/view/gaaay-hagay-ha-gay-kenjeong-gif-5277255')

	if 'brazil' in kontent:
		await message.channel.send('https://tenor.com/view/brazil-youre-going-to-brazil-your-going-to-brazil-ur-going-to-brazil-gif-17868304')

	if 'yukihell' in kontent:
		await message.add_reaction(discord.utils.get(guildstos.emojis, name='yukiHell'))
		await message.channel.send('https://tenor.com/view/yuki-elmo-hands-up-fire-flames-gif-16709640');

	if 'crabrave' in kontent:
		await message.channel.send('https://tenor.com/view/crab-safe-dance-gif-13211112')

	if 'notinoti' in kontent:
		await message.channel.send(file=discord.File('videos/notinoti.gif'))

	if 'jojcek' in kontent:
		await message.channel.send('http://i.picasion.com/gl/90/dMcP.gif')

	##################################################
	### NITRO EMOTES
	
	triggerwordEmote = [':yukiHell:', ':catjam:', ':nipple_lick:', ':yuki_angry:']
	for words in triggerwordEmote:

		if words in kontent:
			words = words.replace(':','')
			await message.channel.send(discord.utils.get(guildstos.emojis, name=f'{words}'))



print('Starting program...')

bot.run('token')

