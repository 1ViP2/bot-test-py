import discord
import asyncio
import info
import random
import datetime
import time
import wikipedia
import wikipedia.exception

prefix = ".." 
token = info.seu_token()
client = discord.Client()
cor =0xC4D5AD
newUserMessage = "Olá seja bem vindo a testes"

@client.event
async def on_ready():


# Bot on
    print('-==Info==-')
    print(client.user.id)
    print(client.user.name)
    print('-========-')
    await client.change_presence(game=discord.Game(name='R.M, Use ..ajuda', type=1, url='https://www.twitch.tv/'),status='streaming')

@client.event
async def on_member_join(member):
    membros = len(member.server.members)
    canal = client.get_channel("477204900594319372")
    await client.send_message(canal, 'Olá {} . Bem vindo ao Servidor :european_castle: REINO MIX™ :european_castle: ! Consute as #:dart:regras , Se registre com as perguntas do #:pushpin:perguntas-registro , e responda no  #:paperclip:chat-registro , ou vá para uma Call Mix de Registro, aguardando um Registrador' .format(member.mention))
    await client.edit_channel(canal , topic=':regional_indicator_m: :regional_indicator_e: :regional_indicator_m: :regional_indicator_b: :regional_indicator_r: :regional_indicator_o: :regional_indicator_s: ❱ {}'.format(membros))

@client.event
async def on_member_remove(member):
    membros = len(member.server.members)
    canal = client.get_channel("477204900594319372")
    await client.send_message(canal, ':463459926669393930: **Sua luz nunca se apagará em nosso servidor, Obg {} ,volte sempre**  :395626929732190212:' .format(member.mention))
    await client.edit_channel(canal , topic=':regional_indicator_m: :regional_indicator_e: :regional_indicator_m: :regional_indicator_b: :regional_indicator_r: :regional_indicator_o: :regional_indicator_s: ❱ {}'.format(membros))

@client.event
async def on_message(message):



# Comando apagar
    if message.content.lower().startswith('..apagar'):
        tags = [r.name for r in message.author.roles]
        if not '✫CARRASCO✫' in tags:
            return await client.send_message(message.channel, '``Você não tem permissão para executar esse comando!``')
        try:
            limite = int(message.content[9:])
            await client.purge_from(message.channel, limit=limite)
            await client.send_message(message.channel, '{} mensagens foram apagadas com sucesso ,por {}'.format(limite,
                                                                                                                 message.author.mention))
        except:
            await client.send_message(message.channel, '``Eu não tenho permissão para apagar mensagens nesse canal.``')


# Comando sinfo
    if message.content.startswith('..sinfo'):
        user = message.author.name
        horario = datetime.datetime.now().strftime("%H:%M:%S")

        serverinfo_embed = discord.Embed(title="\n", description="Informações do servidor!!",
                                         color=0x2cff00)
        serverinfo_embed.set_thumbnail(url=message.server.icon_url)
        serverinfo_embed.add_field(name="Nome:", value=message.server.name, inline=True)
        serverinfo_embed.add_field(name="Dono:", value=message.server.owner.mention)
        serverinfo_embed.add_field(name="Cargos:", value=len(message.server.roles), inline=True)
        serverinfo_embed.add_field(name="Canais de texto:", value=len(
            [message.channel.mention for channel in message.server.channels if channel.type == discord.ChannelType.text]),
                                   inline=True)
        serverinfo_embed.add_field(name="Canais de voz:", value=len(
            [message.channel.mention for channel in message.server.channels if channel.type == discord.ChannelType.voice]),
                                   inline=True)
        serverinfo_embed.add_field(name="Membros:", value=len(message.server.members), inline=True)
        serverinfo_embed.add_field(name="Bots:", value=len([user.mention for user in message.server.members if user.bot]),
                                   inline=True)
        serverinfo_embed.add_field(name="Criado em:", value=message.server.created_at.strftime("%d %b %Y %H:%M"),
                                   inline=True)
        serverinfo_embed.add_field(name="Região:", value=str(message.server.region).title(), inline=True)
        serverinfo_embed.set_footer(text="Comando por {} - Hoje às {}".format(user, horario))
        await client.send_message(message.channel, embed=serverinfo_embed)

# Comando Wikipedia		
    @commands.command(pass_context=True)
    async def wiki(self, ctx, query: str = None):
        if query is None:
            return await self.bot.say("Oque eu devo procurar ?")
        try:
            q = wikipedia.page(query)
            summary = wikipedia.summary(query, sentences=5)
            wikipedia.set_lang('pt')

            embed = discord.Embed(title='Wikipedia:', description=f'{summary} \n\nPara mais informações [**clique aqui**]({q.url})', color=0x002eff)
            await self.bot.say(embed=embed)
        except wikipedia.exceptions.PageError:
            await self.bot.say("Não consegui achar nada com esse nome :/")

# Comando perguntar
    if message.content.lower().startswith('..perguntar'):
        user = message.author.name
        try:
            respostas = ['Sim', 'Não', 'Talvez']
            resposta = random.choice(respostas)
            mensagem = message.content[11:]
            horario = datetime.datetime.now().strftime("%H:%M:%S")
            embed = discord.Embed(color=cor)
            embed.add_field(name="Pergunta:", value='{}'.format(mensagem), inline=False)
            embed.add_field(name="Resposta:", value=resposta, inline=False)
            embed.set_footer(text="Comando por {} - Hoje às {}".format(user, horario))
            await client.send_message(message.channel, embed=embed)
        except:
            await client.send_message(message.channel, '``Você precisa perguntar alguma coisa!``')


# Comando membros
    if message.content.startswith('..membros'):
            user = message.author.name
            horario = datetime.datetime.now().strftime("%H:%M:%S")
            membros_embed = discord.Embed(title="\n", description="Total de membros no momento!",
                                             color=0xffe500)
            membros_embed.set_thumbnail(url=message.server.icon_url)
            membros_embed.set_footer(text="Comando por {} - Hoje às {}".format(user, horario))
            membros_embed.add_field(name="Membros no servidor:", value=len(message.server.members), inline=True)
            await client.send_message(message.channel, embed=membros_embed)


# Comando ajuda
    if message.content.startswith('..ajuda'):
            user = message.author.name
            horario = datetime.datetime.now().strftime("%H:%M:%S")
            membros_embed = discord.Embed(title="Esses são os comando do REINO MIX™", description="ㅤ\n"
                                                                                                  "..membros   |  Veja o tanto de membros no servidor.\n"
                                                                                                  "..perguntar |  Faça uma pergunta ao bot.\n"
                                                                                                  "..sinfo     |  Veja as informações do servidor.\n"
                                                                                                  "..ajuda     |  Veja a lista de comandos do hype.\n"
                                                                                                  "..beijar    |  Beije um membro.\n"
                                                                                                  "..nbeijo    |  Pare um beijo.\n"
                                                                                                  "ㅤ\n",
                                             color=cor)
            membros_embed.set_footer(text="Comando por {} - Hoje às {}".format(user, horario))
            await client.send_message(message.channel, embed=membros_embed)


# Comando astaff
    if message.content.startswith('..astaff'):
        tags = [r.name for r in message.author.roles]
        if not '⚔CORTE MIX⚔' in tags:
            return await client.send_message(message.channel, '``Você não tem permissão para executar esse comando!``')
        user = message.author.name
        horario = datetime.datetime.now().strftime("%H:%M:%S")
        membros_embed = discord.Embed(title="Esses são os comando staff do REINO MIX™",
                                          description="ㅤ\n"
                                                      "..apagar   |  Limpe o chat [✫CARRASCO✫].\n"
                                                      "..ban      |  Dar ban em um membro [✫CARRASCO✫].\n"
                                                      "..desban   |  Tira ban de um membro banido [✫CARRASCO✫].\n"
                                                      "..mutar    |  Muta um membro [◉CAÇADOR◉].\n"
                                                      "..desmutar |  Desmuta um membro mutado [◉CAÇADOR◉].\n"                                                                                                    
                                                      "..falar    |  O bot fala por você [◉CAÇADOR◉].\n"
                                                      "..finbox   |  O bot mandar mensagem no inbox do membro [✫CARRASCO✫].\n"
                                                      "ㅤ\n",
                                          color=0xff7600)
        membros_embed.set_footer(text="Comando por {} - Hoje às {}".format(user, horario))
        await client.send_message(message.channel, embed=membros_embed)
		

# Comando mutar
    if message.content.lower().startswith('..mutar'):
        tags = [r.name for r in message.author.roles]
        if not '◉CAÇADOR◉' in tags:
            return await client.send_message(message.channel, '``Você não tem permissão para executar esse comando!``')
        try:
            au = message.author.mention
            user = message.mentions[0]
            motivu = message.content[30:]
            horario = datetime.datetime.now().strftime("%H:%M:%S")
            cargo = discord.utils.get(message.author.server.roles, name='Usuario Mutado')
            embed = discord.Embed(title="Informações do mute:", description="ㅤ\n"
                                                                                            "O membro: {}\n"
                                                                                            "Foi mutado por: {}\n"
                                                                                            "Pelo motivo: {}\n"
                                                                                            "ㅤ".format(user.mention, au, motivu), color=0xff0000)
            embed.set_thumbnail(url="https://www.conferencecallsunlimited.com//images/uploads/images/14562969_s.jpg")
            embed.set_footer(text="Comando por {} - Hoje às {}".format(message.author, horario))
            embed.set_author(name=user)
            embed2 = discord.Embed(title="Informações do mute:", description="ㅤ\n"
                                                                                             "Você foi mutado por: {}\n"
                                                                                             "Pelo motivo: {}.\n"
                                                                                             "ㅤ".format(au, motivu), color=0x00ffdc)
            embed2.set_thumbnail(url="https://www.conferencecallsunlimited.com//images/uploads/images/14562969_s.jpg")
            embed2.set_footer(text="Comando por {} - Hoje às {}".format(message.author, horario))
            embed2.set_author(name=message.author)
            await client.add_roles(user, cargo)
            await client.send_message(client.get_channel("475719816867610626"), embed=embed)#Teste #475719816867610626 Reino#475721578571890688
            await client.send_message(user, embed=embed2)
        except:
            await client.send_message(message.channel, "``Você nao selecionou ninguem para mutar!``")

# Comando desmutar
    if message.content.lower().startswith('..desmutar'):
        tags = [r.name for r in message.author.roles]
        if not '◉CAÇADOR◉' in tags:
            return await client.send_message(message.channel, '``Você não tem permissão para executar esse comando!``')
        try:
            au = message.author.mention
            user = message.mentions[0]
            motivu = message.content[32:]
            horario = datetime.datetime.now().strftime("%H:%M:%S")
            cargo = discord.utils.get(message.author.server.roles, name='Usuario Mutado')
            embed = discord.Embed(title="Informações do desmute:", description="ㅤ\n"
                                                                                            "O membro: {}\n"
                                                                                            "Foi desmutado por: {}\n"
                                                                                            "Pelo motivo: {}\n"
                                                                                            "ㅤ".format(user.mention, au, motivu), color=0xff0000)
            embed.set_thumbnail(url="https://www.conferencecallsunlimited.com//images/uploads/images/14562969_s.jpg")
            embed.set_footer(text="Comando por {} - Hoje às {}".format(message.author, horario))
            embed.set_author(name=user)
            embed2 = discord.Embed(title="Informações do desmute:", description="ㅤ\n"
                                                                                             "Você foi desmutado por: {}\n"
                                                                                             "Pelo motivo: {}.\n"
                                                                                             "ㅤ".format(au, motivu), color=0x00ffdc)
            embed2.set_thumbnail(url="https://www.conferencecallsunlimited.com//images/uploads/images/14562969_s.jpg")
            embed2.set_footer(text="Comando por {} - Hoje às {}".format(message.author, horario))
            embed2.set_author(name=message.author)
            await client.remove_roles(user, cargo)
            await client.send_message(client.get_channel("475719816867610626"), embed=embed)#Teste #475719816867610626 Reino#475721578571890688
            await client.send_message(user, embed=embed2)
        except:
            await client.send_message(message.channel, "``Você nao selecionou ninguem para desmutar!``")


# Comando falar
    if message.content.startswith('..falar'):
        tags = [r.name for r in message.author.roles]
        if not '◉CAÇADOR◉' in tags:
            return await client.send_message(message.channel, '``Você não tem permissão para executar esse comando!``')
        try:
            falar = message.content[8:]
            await client.send_message(message.channel, "{}".format(falar))
            await client.delete_message(message)
        except:
            await client.send_message(message.channel, "``Você não falou nada!``")


# Comando finbox
    if message.content.lower().startswith('.finbox'):
        tags = [r.name for r in message.author.roles]
        if not '✫CARRASCO✫' in tags:
            return await client.send_message(message.channel, '``Você não tem permissão para executar esse comando!``')
        try:
            user = message.server.members
            falar = message.content[7:]
            await client.send_message(user, "{}".format(falar))
        except:
            await client.send_message(message.channel, "``Você nao selecionou ninguem para spama!``")


# Comando beijar
    if message.content.lower().startswith('..beijar'):
        try:
            membro = message.author.mention
            vitima = message.mentions[0]
            embed = discord.Embed(title="Informações do beijo:", description="ㅤ\n"
                                                               "O membro: {}\n"
                                                               "Beijou o(a): {}\n"
                                                               "ㅤ"
                                                               .format(membro, vitima), color=0xfd00ff)
            embed.set_image(url="https://media.giphy.com/media/BODYd97UpZ4Fq/giphy.gif")
            await client.send_message(message.channel, embed=embed)
        except:
            await client.send_message(message.channel, "``Você nao selecionou ninguem para beijar!``")


# Comando nbeijo
    if message.content.lower().startswith('..pbeijo'):
        try:
            membro = message.author.mention
            vitima = message.mentions[0]
            embed = discord.Embed(title="Informações da negação:", description="ㅤ\n"
                                                               "O membro: {}\n"
                                                               "Parou o beijou do(a): {}\n"
                                                               "ㅤ"
                                                               .format(membro, vitima.mention), color=0x2cff00)
            embed.set_image(url="http://3.bp.blogspot.com/-hoaoUyhmg0E/T5Mr10WmvhI/AAAAAAAABvY/e1b9tv5JSZ4/s1600/%23tapa+na+cara+dele+numa+briga.gif")
            await client.send_message(message.channel, embed=embed)
        except:
            await client.send_message(message.channel, "``Você nao selecionou ninguem pra parar o beijo!``")

#Comando lsbanneds
    if message.content.lower().startswith("..banidos"):
        x = await client.get_bans(message.server)
        xx = '\n'.join(["{0} ({0.id})".format(y) for y in x])
        embedban = discord.Embed(title="***Banidos:***", description=xx, color=0xdb709e)
        return await client.send_message(message.channel, embed=embedban)
			
# Comando ban
    if message.content.lower().startswith("..ban"):
        tags = [r.name for r in message.author.roles]
        if not '✫CARRASCO✫' in tags:
            return await client.send_message(message.channel, '``Você não tem permissão para executar esse comando!``')
        try:
            user = message.mentions[0]
            motivo = message.content[28:]
            horario = datetime.datetime.now().strftime("%H:%M:%S")
            embed = discord.Embed(title="Informações do ban:", description="ㅤ\n"
                                                                           "O membro: {}\n"
                                                                           "Foi banido por: {}\n"
                                                                           "Pelo motivo: {}\n"
                                                                           "ㅤ".format(user.mention, message.author.mention, motivo), color=0xffe500)
            embed.set_thumbnail(url="https://www.conferencecallsunlimited.com//images/uploads/images/14562969_s.jpg")
            embed.set_footer(text="Comando por {} - Hoje às {}".format(message.author, horario))
            embed.set_author(name=user)
            embed2 = discord.Embed(title="Informações do ban:", description="ㅤ\n"
                                                                            "Você foi banido por: {}\n"
                                                                            "Pelo motivo: {}.\n"
                                                                            "ㅤ".format(message.author.mention, motivo), color=0xff7600)
            embed2.set_thumbnail(url="https://www.conferencecallsunlimited.com//images/uploads/images/14562969_s.jpg")
            embed2.set_footer(text="Comando por {} - Hoje às {}".format(message.author, horario))
            embed2.set_author(name=message.author)

            await client.send_message(client.get_channel("475721578571890688"), embed=embed)
            await client.send_message(user, embed=embed2)
            await client.ban(user,delete_message_days=1)
        except:
            await client.send_message(message.channel, "``Você nao selecionou ninguem para dar ban!``")

# Comando unban
    if message.content.lower().startswith(prefix+"unban"):
        if message.author.server_permissions.ban_members:
            try:
                prefi = len(prefix) + 6
                use = message.content[prefi:]
                user2 = await client.get_user_info(user_id="{}".format(use))
                await client.unban(message.server,user2)
                await client.send_message(message.channel, "<@{}> desbanido do servidor".format(use))
            except discord.errors.HTTPException:
                try:
                    await client.send_message(message.channel, "O usuario {} não esta na lista de banido".format(user2.mention))
                except UnboundLocalError:
                    await client.send_message(message.channel, "ID do usuario esta errado")
            except discord.errors.NotFound:
                await client.send_message(message.channel, "ID do usuario esta errado!")
        else:
            await client.send_message(message.channel, "Você não tem permissão para executar essa comando")
			
# Comando membros
    if message.content.startswith("..desc"):
        canal = client.get_channel("476163919228960798")
        motivo = message.content[6:]
        await client.edit_channel(canal , topic=message.server.members)


	
client.run("NDc2NDczMjI0NzY3NzMzNzcx.Dk4XQg.zL9ZJcU1lbwiZIKp1HvVuDonWc0")
