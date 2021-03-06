from discord.ext import commands
import discord
import random
import math
from rpggame import rpgplayer as rpgp, rpgconstants as rpgc, rpgweapon as rpgw, rpgarmor as rpga
from database import rpg as dbcon

money_sign = "¥"
SHOP_EMBED_COLOR = 0x00969b


class RPGGameActivities:
    def __init__(self, bot):
        self.bot = bot
        self.weapons = {}
        self.armors = {}
        print('RPGGameActivities started')

    async def send_shop_help_message(self, url: str, message: discord.Message):
        prefix = await self.bot._get_prefix(message)
        embed = discord.Embed(colour=SHOP_EMBED_COLOR)
        embed.set_author(name="Shop commands", icon_url=url)
        embed.add_field(name="Items",
                        value="Type '{}shop item' for a list of available items".format(prefix),
                        inline=False)
        embed.add_field(name="Weapons",
                        value="Type '{}shop weapon' for a list of available weapons".format(prefix),
                        inline=False)
        embed.add_field(name="Armor",
                        value="Type '{}shop armor' for the armor sold in this shop".format(prefix),
                        inline=False)
        embed.add_field(name="Restock", value="Weapons and armors refresh every hour".format(prefix),
                        inline=False)
        await self.bot.say(embed=embed)

    # {prefix}shop
    @commands.group(pass_context=1, help="Shop for valuable items!")
    async def shop(self, ctx):
        prefix = await self.bot._get_prefix(ctx.message)
        if ctx.invoked_subcommand is None and (
                ctx.message.content in ['{}shop help'.format(prefix), '{}shop'.format(prefix)]):
            if not await self.bot.pre_command(message=ctx.message, command='shop help'):
                return
            await self.send_shop_help_message(ctx.message.author.avatar_url, ctx.message)

    # {prefix}shop armor
    @shop.command(pass_context=1, aliases=["a", "armour"], help="Buy a shiny new suit of armor!")
    async def armor(self, ctx, *args):
        if not await self.bot.pre_command(message=ctx.message, command='shop armor'):
            return
        player = dbcon.get_player(ctx.message.author.id, ctx.message.author.display_name, ctx.message.author.avatar_url)
        if not await self.bot.rpggame.check_role(player.role, ctx.message):
            return
        if player.role == rpgc.names.get("role")[-1][0]:
            await self.bot.say("{}, A cat cannot possibly wear human armor...".format(ctx.message.author.mention))
            return
        if len(args) <= 0:
            embed = discord.Embed(colour=SHOP_EMBED_COLOR)
            embed.set_author(name="Shop Armory", icon_url=ctx.message.author.avatar_url)
            embed.add_field(name="Your money", value="{}{}".format(money_sign, player.money))
            start = max(0, player.get_level() - 5)
            for i in range(start, start + 10):
                a = self.armors.get(i)
                if a is None:
                    a = rpga.generateArmor(i * 1000)
                    self.armors[i] = a
                t = "Costs: {}".format(a.cost)
                if a.maxhealth != 0:
                    t += ", maxhealth: {}".format(a.maxhealth)
                if a.healthregen != 0:
                    t += ", healthregen: {}".format(a.healthregen)
                if a.money != 0:
                    t += ", money: {}%".format(a.money)
                embed.add_field(name=str(i) + ") " + a.name, value=t, inline=False)
            await self.bot.say(embed=embed)
            return
        try:
            armor = self.armors.get(int(args[0]))
        except ValueError:
            await self.bot.say("That is not an armor sold in this part of the country")
            return
        if armor is None:
            await self.bot.say("That is not an armor sold in this part of the country")
            return
        pa = player.armor
        if not player.buy_armor(armor):
            await self.bot.say("You do not have the money to buy the {}".format(armor.name))
            return
        t = "You have acquired the {} for {}{}".format(armor.name, money_sign, armor.cost)
        if pa.cost > 3:
            t += "\nYou sold your old armor for {}{}".format(money_sign, int(math.floor(0.25 * pa.cost)))
        dbcon.update_player(player)
        await self.bot.say(t)

    # {prefix}shop item
    @shop.command(pass_context=1, aliases=["i", "buy", "items"], help="Special knowledge on enemy weakpoints")
    async def item(self, ctx, *args):
        if not await self.bot.pre_command(message=ctx.message, command='shop item'):
            return
        player = dbcon.get_player(ctx.message.author.id, ctx.message.author.display_name, ctx.message.author.avatar_url)
        if not await self.bot.rpggame.check_role(player.role, ctx.message):
            return
        if len(args) <= 0:
            embed = discord.Embed(colour=SHOP_EMBED_COLOR)
            embed.set_author(name="Shop inventory", icon_url=ctx.message.author.avatar_url)
            embed.add_field(name="Your money", value="{}{}".format(money_sign, player.money))
            for i in sorted(rpgc.shopitems.values(), key=lambda l: l.cost):
                t = "Costs: {}{}".format(money_sign, i.cost)
                t += "\nYou can afford {} of this item".format(math.floor(player.money / i.cost))
                for e in i.benefit:
                    x = i.benefit.get(e)
                    t += "\n{}{}{}".format(e, x[0], x[1])
                embed.add_field(name=i.name, value=t, inline=False)
            await self.bot.say(embed=embed)
            return
        item = args[0].lower()
        if item in ["h", "hp"]:
            item = "health"
        if item in ["mh", "mhp"]:
            item = "maxhealth"
        elif item in ["d", "dam", 'dmg']:
            item = "damage"
        elif item in ["c", "crit"]:
            item = "critical"
        if item in ['maxhealth', 'health'] and player.role == rpgc.names.get("role")[-1][0]:
            await self.bot.say("{}, this stuff does not work on animals...".format(ctx.message.author.mention))
            return
        if item == "health" and player.health == player.maxhealth:
            await self.bot.say("You're already full HP")
            return
        item = rpgc.shopitems.get(item)
        if not item:
            await self.bot.say("Thats not an item sold here")
            return
        try:
            a = int(args[1])
        except ValueError:
            if args[1] in ['m', 'max']:
                a = math.floor(player.money / item.cost)
                m = int((player.maxhealth - player.health) / 25)
                if args[0] in ['h', 'hp', 'health'] and (player.money >= (m * item.cost)):
                    a = m
            else:
                a = 1
        except IndexError:
            a = 1
        if a < 0:
            await self.bot.say("Lmao, that sounds intelligent")
            return
        if player.buy_item(item, amount=a):
            await self.bot.say(
                "{} bought {} {} for {}{}".format(ctx.message.author.mention, a, item.name, money_sign, a * item.cost))
            dbcon.update_player(player)
        else:
            await self.bot.say("{} does not have enough money to buy {} {}\nThe maximum you can afford is {}".format(
                ctx.message.author.mention, a, item.name, math.floor(player.money / item.cost)))

    # {prefix}shop weapon
    @shop.command(pass_context=1, aliases=["w", "weapons"], help="Buy a shiny new weapon!")
    async def weapon(self, ctx, *args):
        if not await self.bot.pre_command(message=ctx.message, command='shop weapon'):
            return
        player = dbcon.get_player(ctx.message.author.id, ctx.message.author.display_name, ctx.message.author.avatar_url)
        if not await self.bot.rpggame.check_role(player.role, ctx.message):
            return
        if player.role == rpgc.names.get("role")[-1][0]:
            await self.bot.say("{}, how would you even use a weapon as a cat?".format(ctx.message.author.mention))
            return
        if len(args) <= 0:
            embed = discord.Embed(colour=SHOP_EMBED_COLOR)
            embed.set_author(name="Shop Weapons", icon_url=ctx.message.author.avatar_url)
            embed.add_field(name="Your money", value="{}{}".format(money_sign, player.money))
            start = max(0, player.get_level() - 5)
            for i in range(start, start + 10):
                w = self.weapons.get(i)
                if w is None:
                    w = rpgw.generate_weapon(i * 1000)
                    self.weapons[i] = w
                t = "Costs: {}".format(w.cost)
                if w.damage != 0:
                    t += ", damage + {}".format(w.damage)
                if w.weaponskill != 0:
                    t += ", weaponskill + {}".format(w.weaponskill)
                if w.critical != 0:
                    t += ", critical + {}".format(w.critical)
                embed.add_field(name=str(i) + ") " + w.name, value=t, inline=False)
            await self.bot.say(embed=embed)
            return
        try:
            weapon = self.weapons.get(int(args[0]))
        except ValueError:
            await self.bot.say("That is not a weapon sold in this part of the country")
            return
        if weapon is None:
            await self.bot.say("That is not an armor sold in this part of the country")
            return
        pw = player.weapon
        if not player.buy_weapon(weapon):
            await self.bot.say("You do not have the money to buy the {}".format(weapon.name))
            return
        t = "You have acquired the {} for {}{}".format(weapon.name, money_sign, weapon.cost)
        if pw.cost > 3:
            t += "\nYou sold your old weapon for {}{}".format(money_sign, int(math.floor(0.25 * pw.cost)))
        dbcon.update_player(player)
        await self.bot.say(t)

    # {prefix}train
    @commands.command(pass_context=1, aliases=["training"], help="Train your skills!")
    async def train(self, ctx, *args):
        if not await self.bot.pre_command(message=ctx.message, command='train'):
            return
        if len(args) <= 0:
            embed = discord.Embed(colour=SHOP_EMBED_COLOR)
            embed.set_author(name="Available Training", icon_url=ctx.message.author.avatar_url)
            for i in rpgc.trainingitems.values():
                embed.add_field(name=i.name, value="Minutes per statpoint: {}".format(i.cost), inline=False)
            await self.bot.say(embed=embed)
            return
        training = args[0]
        if training in ['ws', 'weapon']:
            training = "weaponskill"
        elif training in ['hp', 'h', 'health']:
            training = "maxhealth"
        training = rpgc.trainingitems.get(training)
        if not training:
            await self.bot.say("Thats not an available training")
            return
        try:
            a = int(args[1])
        except (ValueError, IndexError):
            a = math.ceil(rpgp.mintrainingtime / training.cost)

        player = dbcon.get_player(ctx.message.author.id, ctx.message.author.display_name, ctx.message.author.avatar_url)
        if not await self.bot.rpggame.check_role(player.role, ctx.message):
            return
        if player.role == rpgc.names.get("role")[-1][0] and training.name == 'maxhealth':
            await self.bot.say("{}, awww. So cute. A cat trying to fight a dummy".format(ctx.message.author.mention))
            return
        if player.busydescription != rpgp.BUSY_DESC_NONE:
            await self.bot.say("Please make sure you finish your other shit first")
            return
        c = ctx.message.channel
        if c.is_private:
            c = ctx.message.author
        time = math.ceil(a * training.cost)
        if not (rpgp.mintrainingtime <= time <= int(rpgp.maxtrainingtime + (0.5 * player.extratime))):
            await self.bot.say(
                "You can train between {} and {} points".format(math.ceil(rpgp.mintrainingtime / training.cost),
                                                                math.floor(int(rpgp.maxtrainingtime + (
                                                                        0.5 * player.extratime)) / training.cost)))
            return
        player.set_busy(rpgp.BUSY_DESC_TRAINING, time, c.id)
        player.buy_training(training, amount=a)
        dbcon.update_player(player)
        await self.bot.say(
            "{}, you are now training your {} for {} minutes".format(ctx.message.author.mention, training.name,
                                                                     int(math.ceil(a * training.cost))))

    # {prefix}work
    @commands.command(pass_context=1, aliases=["Work"], help="Work for some spending money!")
    async def work(self, ctx, *args):
        if not await self.bot.pre_command(message=ctx.message, command='work'):
            return
        try:
            time = int(args[0])
        except (ValueError, IndexError):
            time = rpgp.mintrainingtime

        player = dbcon.get_player(ctx.message.author.id, ctx.message.author.display_name, ctx.message.author.avatar_url)
        if not await self.bot.rpggame.check_role(player.role, ctx.message):
            return
        if player.role == rpgc.names.get("role")[-1][0]:
            await self.bot.say(
                "{}, I'm sorry, but we need someone with more... height...".format(ctx.message.author.mention))
            return
        if player.busydescription != rpgp.BUSY_DESC_NONE:
            await self.bot.say("Please make sure you finish your other shit first")
            return
        c = ctx.message.channel
        if c.is_private:
            c = ctx.message.author

        # Set busy time
        if not (rpgp.minworkingtime <= time <= (rpgp.maxworkingtime + player.extratime)):
            await self.bot.say("You can work between {} and {} minutes".format(rpgp.minworkingtime, (
                    rpgp.maxworkingtime + player.extratime)))
            return

        dbcon.set_busy(player.userid, math.ceil(time), c.id, rpgp.BUSY_DESC_WORKING)
        money = time * pow((player.get_level()) + 1, 1 / 2) * 120
        if player.role == rpgc.names.get('role')[0][0]:  # role == Peasant
            money *= 1.15
        dbcon.add_stats(player.userid, 'money', int(money))
        work = random.choice([
            'cleaning the stables',
            'sharpening the noble\'s weapon',
            'assisting the smith',
            'scaring crows',
            'a lewdly clothed maid',
            'collecting herbs',
            'writing tales and songs',
            'guarding the city gates',
            'gathering military intelligence',
            'summoning demons',
            'brewing potions',
            'chopping wood',
            'mining valuable ore'
        ])
        await self.bot.say("{}, you are now {} for {} minutes".format(ctx.message.author.mention, work, time))
