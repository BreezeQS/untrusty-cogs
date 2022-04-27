from typing import Literal
import aiohttp
import asyncio
import time
import discord
from redbot.core import commands
from redbot.core.bot import Red
from redbot.core.config import Config

RequestType = Literal["discord_deleted_user", "owner", "user", "user_strict"]

class NekosBest(commands.Cog):
    """
    nekos.best API commands
    """
    BASE = "https://nekos.best/api/v2/"
    ICON = "https://nekos.best/favicon.png"

    def __init__(self, bot: Red) -> None:
        self.bot = bot
        self.config = Config.get_conf(
            self,
            identifier=332166608187293696,
            force_registration=True,
        )
        self.session = aiohttp.ClientSession(raise_for_status=True)

    def cog_unload(self):
        asyncio.create_task(self.session.close())


    async def red_delete_data_for_user(self, *, requester: RequestType, user_id: int) -> None:
        super().red_delete_data_for_user(requester=requester, user_id=user_id)

# Internals

    async def _api_call(self, route):
        """Calls the supplied route of nekos.best, returns url and if possible source url and anime name"""
        async with self.session.get(f"{self.BASE}{route}") as resp:
            json = await resp.json()
            url = json["results"][0]["url"]
            source_url = None
            anime_name = None

            if "source_url" in json["results"][0]:
                source_url = json["results"][0]["source_url"]

            if "anime_name" in json["results"][0]:
                anime_name = json["results"][0]["anime_name"]

            return url, source_url, anime_name

    async def _post_image(self, ctx, route):
        try:
            img = await self._api_call(route)
        except aiohttp.ClientResponseError:
            await ctx.send("There was an error trying to reach nekos.best, please try again later.")

        if await ctx.embed_requested():
            desc = ""
            if img[1]:
                desc += f"[**Source**]({img[1]})\n"
            if img[2]:
                desc += f"**Anime Name:** {img[2]}\n"
            
            embed = discord.Embed(colour=(await ctx.embed_color()))
            embed.set_image(url=img[0])
            embed.set_footer(text="Powered by nekos.best", icon_url=self.ICON)

            if desc:
                embed.description = desc
            
            await ctx.send(embed=embed)
            return

        desc = ""
        if img[1]:
            desc += f"**Source:** <{img[1]}>\n"
        if img[2]:
            desc += f"**Anime Name:**{img[2]}\n"
    
        desc += f"{img[0]}\n"
        await ctx.send(desc)

# Commands

    @commands.command()
    async def highfive(self, ctx):
        """Posts an image from the nekos.best highfive endpoint"""
        await self._post_image(ctx, "highfive")

    @commands.command()
    async def happy(self, ctx):
        """Posts an image from the nekos.best happy endpoint"""
        await self._post_image(ctx, "happy")

    @commands.command()
    async def sleep(self, ctx):
        """Posts an image from the nekos.best sleep endpoint"""
        await self._post_image(ctx, "sleep")

    @commands.command()
    async def laugh(self, ctx):
        """Posts an image from the nekos.best laugh endpoint"""
        await self._post_image(ctx, "laugh")

    @commands.command()
    async def bite(self, ctx):
        """Posts an image from the nekos.best bite endpoint"""
        await self._post_image(ctx, "bite")

    @commands.command()
    async def poke(self, ctx):
        """Posts an image from the nekos.best poke endpoint"""
        await self._post_image(ctx, "poke")

    @commands.command()
    async def tickle(self, ctx):
        """Posts an image from the nekos.best tickle endpoint"""
        await self._post_image(ctx, "tickle")

    @commands.command()
    async def kiss(self, ctx):
        """Posts an image from the nekos.best kiss endpoint"""
        await self._post_image(ctx, "kiss")

    @commands.command()
    async def wave(self, ctx):
        """Posts an image from the nekos.best wave endpoint"""
        await self._post_image(ctx, "wave")

    @commands.command()
    async def thumbsup(self, ctx):
        """Posts an image from the nekos.best thumbsup endpoint"""
        await self._post_image(ctx, "thumbsup")

    @commands.command()
    async def stare(self, ctx):
        """Posts an image from the nekos.best stare endpoint"""
        await self._post_image(ctx, "stare")

    @commands.command()
    async def cuddle(self, ctx):
        """Posts an image from the nekos.best cuddle endpoint"""
        await self._post_image(ctx, "cuddle")

    @commands.command()
    async def smile(self, ctx):
        """Posts an image from the nekos.best smile endpoint"""
        await self._post_image(ctx, "smile")

    @commands.command()
    async def baka(self, ctx):
        """Posts an image from the nekos.best baka endpoint"""
        await self._post_image(ctx, "baka")

    @commands.command()
    async def blush(self, ctx):
        """Posts an image from the nekos.best blush endpoint"""
        await self._post_image(ctx, "blush")

    @commands.command()
    async def think(self, ctx):
        """Posts an image from the nekos.best think endpoint"""
        await self._post_image(ctx, "think")

    @commands.command()
    async def pout(self, ctx):
        """Posts an image from the nekos.best pout endpoint"""
        await self._post_image(ctx, "pout")

    @commands.command()
    async def facepalm(self, ctx):
        """Posts an image from the nekos.best facepalm endpoint"""
        await self._post_image(ctx, "facepalm")

    @commands.command()
    async def wink(self, ctx):
        """Posts an image from the nekos.best wink endpoint"""
        await self._post_image(ctx, "wink")

    @commands.command()
    async def smug(self, ctx):
        """Posts an image from the nekos.best smug endpoint"""
        await self._post_image(ctx, "smug")

    @commands.command()
    async def cry(self, ctx):
        """Posts an image from the nekos.best cry endpoint"""
        await self._post_image(ctx, "cry")

    @commands.command()
    async def pat(self, ctx):
        """Posts an image from the nekos.best pat endpoint"""
        await self._post_image(ctx, "pat")

    @commands.command()
    async def dance(self, ctx):
        """Posts an image from the nekos.best dance endpoint"""
        await self._post_image(ctx, "dance")

    @commands.command()
    async def feed(self, ctx):
        """Posts an image from the nekos.best feed endpoint"""
        await self._post_image(ctx, "feed")

    @commands.command()
    async def shrug(self, ctx):
        """Posts an image from the nekos.best shrug endpoint"""
        await self._post_image(ctx, "shrug")

    @commands.command()
    async def bored(self, ctx):
        """Posts an image from the nekos.best bored endpoint"""
        await self._post_image(ctx, "bored")

    @commands.command()
    async def hug(self, ctx):
        """Posts an image from the nekos.best hug endpoint"""
        await self._post_image(ctx, "hug")

    @commands.command()
    async def slap(self, ctx):
        """Posts an image from the nekos.best slap endpoint"""
        await self._post_image(ctx, "slap")

    @commands.command()
    async def neko(self, ctx):
        """Posts an image from the nekos.best neko endpoint"""
        await self._post_image(ctx, "neko")

    @commands.command()
    async def kitsune(self, ctx):
        """Posts an image from the nekos.best kitsune endpoint"""
        await self._post_image(ctx, "kitsune")

    @commands.command()
    async def waifu(self, ctx):
        """Posts an image from the nekos.best waifu endpoint"""
        await self._post_image(ctx, "waifu")