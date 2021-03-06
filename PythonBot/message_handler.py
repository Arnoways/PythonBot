import constants
import datetime
import discord
import log
import random
import send_random
import string
from database import general as dbcon

NicknameAutoChange = False


def cl(x):
    return x.lower() if random.randint(0, 1) <= 0 else x.capitalize()


async def new(bot, message: discord.Message):
    if message.server.id in constants.s_to_ringels_whitelist and message.author.id == constants.DOGEid and "s" in message.content and await bot.pre_command(
            message=message, command='s_to_ringel_s', delete_message=False):
        await bot.send_message(message.channel, "*" + message.content.replace("s", "ß"))
        return
    if message.server.id not in constants.sponge_capitalization_blacklist and (
            message.author.id in bot.spongelist) and (random.randint(0, 4) <= 0) and (
            len(message.content) > 5) and await bot.pre_command(message=message, command='spongelist',
                                                                delete_message=False):
        await bot.send_message(message.channel, ''.join([cl(x) for x in message.content.lower()]))
        return
    if message.server.id not in constants.praise_the_sun_blacklist and message.content == "\\o/" and (
            datetime.datetime.utcnow() - bot.praise).seconds > (2 * 60) and await bot.pre_command(message=message,
                                                                                                  command='\\o/',
                                                                                                  delete_message=False):
        perms = message.channel.permissions_for(message.server.get_member(str(bot.user.id)))
        if not (perms.manage_messages and perms.attach_files):
            return
        await bot.delete_message(message)
        await send_random.file(bot, message.channel, "sun")
        bot.praise = datetime.datetime.utcnow()
        return
    if (message.server.id not in constants.ayy_lmao_blacklist or message.author.id == constants.NYAid) and (
            message.content.lower() == "ayy") and await bot.pre_command(message=message, command='ayy',
                                                                        delete_message=False):
        await bot.send_message(message.channel, "lmao")
        return
    if message.author.id in [constants.NYAid,
                             constants.TRISTANid] and message.content.lower() == "qyy" and await bot.pre_command(
        message=message, command='qyy', delete_message=False):
        await bot.send_message(message.channel, "kmao")
        return
    if message.content.lower() == "lmao" and message.author.id == constants.NYAid and await bot.pre_command(
            message=message, command='lmao', delete_message=False):
        await bot.send_message(message.channel, "ayy")
        return
    if message.server.id not in constants.lenny_blacklist and "lenny" in message.content.split(
            " ") and await bot.pre_command(message=message, command='response_lenny', delete_message=False):
        await bot.send_message(message.channel, "( ͡° ͜ʖ ͡°)")
        return
    if message.server.id not in constants.ded_blacklist and "ded" == message.content and await bot.pre_command(
            message=message, command='response_ded', delete_message=False):
        ml = list(bot.messages)
        m = ml.pop()
        while (m == message) or (m.channel != message.channel):
            if len(ml) == 0:
                return
            m = ml.pop()
        if (message.timestamp - m.timestamp).seconds > 60:
            await bot.send_message(message.channel, random.choice(constants.ded))
    if message.server.id not in constants.table_unflip_blacklist and message.content == "(╯°□°）╯︵ ┻━┻" and await bot.pre_command(
            message=message, command='tableflip', delete_message=False):
        await bot.send_message(message.channel, "┬─┬﻿ ノ( ゜-゜ノ)")
    if NicknameAutoChange:
        if message.author.id in [constants.NYAid, constants.LOLIid, constants.WIZZid] and message.author.permissions_in(
                message.channel).change_nickname and await bot.pre_command(message=message,
                                                                           command='nickname_auto_change',
                                                                           delete_message=False):
            if (len(message.content.split(" ")) > 2) and (message.server.name.lower() == "9chat"):
                if (message.content.split(" ")[0] == "i") and (message.content.split(" ")[1] == "am"):
                    try:
                        await bot.change_nickname(message.author, message.content.partition(' ')[2].partition(' ')[2])
                    except Exception:
                        pass
            if (len(message.content.split(" ")) > 1) and (message.server.name.lower() == "9chat"):
                if (message.content.lower().split(" ")[0] == "im") | (message.content.split(" ")[0] == "i'm"):
                    try:
                        await bot.change_nickname(message.author, message.content.partition(' ')[2])
                        print("Changed nickname")
                    except Exception:
                        pass
    if message.author.id in [constants.TRISTANid, constants.CHURROid] and "pls" in message.content.lower().split(" "):
        await bot.add_reaction(message, ":pepederp:302888052508852226")
    if message.author.id in bot.spamlist:
        if message.server.id == constants.NINECHATid:
            await bot.add_reaction(message, ":cate:290483030227812353")
            await bot.add_reaction(message, ":oldguy:292229250369716235")
            await bot.add_reaction(message, ":lewd:290790189125599233")
            await bot.add_reaction(message, ":haha:290486766169751553")
            await bot.add_reaction(message, ":what:290477388670959617")
            await bot.add_reaction(message, ":notlikethis:290790824676163584")
            await bot.add_reaction(message, ":wut:292659646014160908")
            await bot.add_reaction(message, ":ytho:290796028347809792")
            await bot.add_reaction(message, ":smug:358565714795298827")
            await bot.add_reaction(message, ":weebrage:290800474255261708")
            await bot.add_reaction(message, ":fetdoge:375987462553731073")
            await bot.add_reaction(message, ":pat:290789859663282176")
            await bot.add_reaction(message, ":nut:348350754974728193")
            await bot.add_reaction(message, ":hand:348350777661587466")
        else:
            await bot.add_reaction(message, "\u2764")

    if not (len(message.content) < 2 or (message.content[:2] == '<@') or (
            message.content[0].isalpha() and message.content[1].isalpha())):
        return

    if message.server.id not in constants.bot_talk_blacklist:
        await talk(bot, message)


async def talk(bot, message: discord.Message):
    if (bot.user in message.mentions or (len(
            set(message.content.lower().translate(str.maketrans('', '', string.punctuation)).split(" ")).intersection(
                {'biri', 'biribiri'})) > 0)) and await bot.pre_command(message=message, command='talk',
                                                                       delete_message=False):
        if 'prefix' in message.content.lower():
            await bot.send_message(message.channel,
                                   'My prefix is \'{}\', darling'.format(await bot._get_prefix(message)))
            return
        if (message.author.id in [constants.NYAid, constants.LOLIid, constants.WIZZid]) and \
                any(word in message.content.lower() for word in ['heart', 'pls', 'love']):
            await bot.send_message(message.channel, ":heart:")
            return
        if message.content[len(message.content) - 1] == "?":
            await bot.send_message(message.channel, random.choice(constants.qa))
            return
        else:
            await bot.send_message(message.channel, random.choice(constants.response))
            return


async def edit(message):
    if not message.author.bot:
        await log.message(message, "edited")


async def deleted(message):
    await log.message(message, "deleted")


async def new_pic(bot, message):
    if message.author.id == constants.NYAid:
        return
    for pic in message.attachments:
        await log.message(message, "pic", pic["url"])


STAR_EMBED_COLOR = 0xf9e000
STAR_EMOJI = '⭐'


def construct_embed_message(message: discord.Message, stars: int):
    m = 'A message received {} stars in {}'.format(stars, message.channel.mention)
    e = discord.Embed(colour=STAR_EMBED_COLOR)
    e.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
    if message.content:
        e.add_field(name='Message contents', value=message.content)
    if message.attachments:
        e.set_image(url=message.attachments[0].get('url'))
    e.set_footer(text='Message send at ' + message.timestamp.strftime("%Y-%m-%d %H:%M:%S"))
    return m, e


async def reaction(bot: discord.Client, reaction: discord.Reaction):
    if reaction.emoji == STAR_EMOJI:
        channel = dbcon.get_star_channel(reaction.message.server.id)
        if not channel:
            return
        channel = bot.get_channel(channel)

        stars = sum([x.count for x in reaction.message.reactions if x.emoji == STAR_EMOJI])
        embed_id = dbcon.get_star_message(reaction.message.id)
        m, e = construct_embed_message(reaction.message, stars)

        if embed_id:
            await bot.edit_message(await bot.get_message(channel, embed_id), new_content=m, embed=e)
            return

        i = (await bot.send_message(channel, content=m, embed=e)).id
        dbcon.update_star_message(reaction.message.id, i)
