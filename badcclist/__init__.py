from .preparecom import PATCHED_prepare_command_list

async def patch(bot):
    await bot.wait_until_red_ready()
    cog = bot.get_cog("CustomCommands")
    cog.prepare_command_list = PATCHED_prepare_command_list

async def setup(bot):
    loop = bot.loop
    loop.create_task(patch(bot))