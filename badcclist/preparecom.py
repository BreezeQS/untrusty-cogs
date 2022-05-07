from typing import Iterable, List, Tuple
from redbot.core.utils.chat_formatting import escape
from redbot.core import commands

def PATCHED_prepare_command_list(
    ctx: commands.Context, command_list: Iterable[Tuple[str, dict]]
) -> List[Tuple[str, str]]:
    results = []
    for command, body in command_list:
        responses = body["response"]
        if isinstance(responses, list):
            result = ", ".join(responses)
        elif isinstance(responses, str):
            result = responses
        else:
            continue


        # Cut preview to 300 characters max, raised from 52 for glas
        if len(result) > 300:
            result = result[:297] + "..."
        # Replace newlines with spaces

        result = result.replace("\n", " ")
        # Escape markdown and mass mentions
        result = escape(result, formatting=True, mass_mentions=True)
        results.append((f"{ctx.clean_prefix}{command}", result))
    return results