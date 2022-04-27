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



    @commands.command()
    async def neko(self, ctx):
        await self._post_image(ctx, "neko")
    
    @commands.command()
    async def hug(self, ctx):
        await self._post_image(ctx, "hug")