from discord.ext import commands


class Misc:
    def __init__(self, my_bot):
        self.bot = my_bot
        print('Misc started')

    @commands.command(pass_context=1, help="Invite me to your own server")
    async def inviteme(self, ctx):
        if not await self.bot.pre_command(message=ctx.message, command='inviteme'):
            return
        await self.bot.say(
            "Here is a link to invite me:\nhttps://discordapp.com/api/oauth2/authorize?client_id=244410964693221377&permissions=472951872&scope=bot")

    @commands.command(pass_context=1, help="Join my masters discord server for anything")
    async def helpserver(self, ctx):
        if not await self.bot.pre_command(message=ctx.message, command='helpserver'):
            return
        await self.bot.say("A link to the past:\nhttps://discord.gg/KBxRd7x")

    @commands.command(pass_context=1, help="Vote for me, this increases my power!")
    async def vote(self, ctx):
        if not await self.bot.pre_command(message=ctx.message, command='vote'):
            return
        await self.bot.say("Give me some love:\nhttps://discordbots.org/bot/244410964693221377/vote")