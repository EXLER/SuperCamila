from discord.ext import commands


class Miscellaneous(commands.Cog):
    """
    Miscellaneous commands to help with simple and repetitive tasks.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def format(self, ctx, message_id, syntax):
        """Format message of given ID with given syntax.
        Keep in mind it only looks for the message in the channel you called the command"""
        channel = ctx.channel
        msg = await channel.fetch_message(message_id)
        if not msg:
            await ctx.send("❌ Nie znaleziono wiadomości o podanym ID w tym kanale!")
            return

        msg_content = msg.content
        await msg.delete()
        await ctx.send(content=f"```{syntax}\n{msg_content}```")


def setup(bot):
    bot.add_cog(Miscellaneous(bot))
