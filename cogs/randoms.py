import random

import discord
from discord.ext import commands


class Randoms(commands.Cog):
    """
    Randomize between people, numbers or more!
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def randomrange(self, ctx, lower: int, upper: int):
        """Choose a random integer between given lower and upper bounds"""
        number = random.randint(lower, upper)
        await ctx.send(f"🎲 Twoja losowa liczba pomiędzy {lower} a {upper} to: {number}")

    @commands.command()
    async def randommember(self, ctx, role: discord.Role):
        """Choose a random member of given Discord role"""
        member = random.choice(role.members)
        await ctx.send(f"🎲 Wylosowana osoba to: {member}")


def setup(bot):
    bot.add_cog(Randoms(bot))
