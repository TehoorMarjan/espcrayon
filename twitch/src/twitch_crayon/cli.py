import asyncio
import os
import re
import unicodedata

import click
import httpx
from dotenv import load_dotenv
from twitchAPI.chat import Chat, ChatCommand, ChatMessage, ChatSub, EventData
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.twitch import Twitch
from twitchAPI.type import AuthScope, ChatEvent

from .colors import COLORS, EFFECTS

type Color = tuple[int, int, int]

load_dotenv()

APP_ID = os.environ["APP_ID"]
APP_SECRET = os.environ["APP_SECRET"]
USER_SCOPE = [AuthScope.CHAT_READ, AuthScope.CHAT_EDIT]
TARGET_CHANNEL = os.environ["TARGET_CHANNEL"]
TOKEN = os.environ["HATOKEN"]
BASE_URL = os.environ["HAURL"]

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "content-type": "application/json",
}

_re_rgbparam = re.compile(r"^\s*(?P<r>\d+)\s*,\s*(?P<g>\d+)\s*,\s*(?P<b>\d+)")
_re_hexparam = re.compile(
    r"^\s*#(?P<r>[0-9a-fA-F]{2})(?P<g>[0-9a-fA-F]{2})(?P<b>[0-9a-fA-F]{2})"
)
_re_hexparam2 = re.compile(
    r"^\s*#(?P<r>[0-9a-fA-F])(?P<g>[0-9a-fA-F])(?P<b>[0-9a-fA-F])"
)
_re_nameparam = re.compile(r"^\s*(?P<name>\w+)$")


def parse_color_param(param: str) -> tuple[Color, str] | None:
    if m := _re_rgbparam.match(param):
        r = int(m["r"])
        g = int(m["g"])
        b = int(m["b"])
        if r > 255 or g > 255 or b > 255:
            return None
    elif m := _re_hexparam.match(param):
        r = int(m["r"], 16)
        g = int(m["g"], 16)
        b = int(m["b"], 16)
    elif m := _re_hexparam2.match(param):
        r = int(m["r"] * 2, 16)
        g = int(m["g"] * 2, 16)
        b = int(m["b"] * 2, 16)
    elif m := _re_nameparam.match(param):
        name = (
            unicodedata.normalize("NFD", m["name"])
            .encode("ascii", "ignore")
            .decode("utf-8")
            .capitalize()
        )
        if name in COLORS:
            return COLORS[name], "None"
        elif name in EFFECTS:
            return (0, 0, 0), name
        return None
    else:
        return None
    return (r, g, b), "None"


async def crayon_send_command(color: Color, effect: str):
    r, g, b = color
    data = {
        "entity_id": "light.crayon_rgb_light",
        "effect": effect,
        "brightness": 255,
    }
    if effect == "None":
        data["rgb_color"] = [r, g, b]
    async with httpx.AsyncClient() as client:
        response = await client.post(
            BASE_URL + "api/services/light/turn_on", headers=HEADERS, json=data
        )
        return response.status_code == httpx.codes.OK

# ## Twitch Chat Commands

# this will be called whenever the !reply command is issued
async def test_command(cmd: ChatCommand):
    if len(cmd.parameter) == 0:
        await cmd.reply("you did not tell me what to reply with")
    else:
        await cmd.reply(f"{cmd.user.name}: {cmd.parameter}")

async def crayon_command(cmd: ChatCommand):
    if len(cmd.parameter) == 0:
        await cmd.reply(f"Please provide a color parameter.")
        return
    color_effect = parse_color_param(cmd.parameter)
    if color_effect is None:
        await cmd.reply(f"Invalid color parameter.")
        return
    success = await crayon_send_command(*color_effect)
    if success:
        await cmd.reply(f"Crayon color changed!")
    else:
        await cmd.reply(f"Failed to change crayon color.")

# This will be called when the event READY is triggered, which will be on
# bot start
async def on_ready(ready_event: EventData):
    print("Bot is ready for work, joining channels")
    # join our target channel, if you want to join multiple,
    # either call join for each individually
    # or even better pass a list of channels as the argument
    await ready_event.chat.join_room(TARGET_CHANNEL)
    # you can do other bot initialization things in here

# this is where we set up the bot
async def run():
    # set up twitch api instance and add user authentication with some scopes
    twitch = await Twitch(APP_ID, APP_SECRET)
    auth = UserAuthenticator(twitch, USER_SCOPE)
    token, refresh_token = await auth.authenticate()
    await twitch.set_user_authentication(token, USER_SCOPE, refresh_token)

    # create chat instance
    chat = await Chat(twitch)

    # register the handlers for the events you want

    # listen to when the bot is done starting up and ready to join channels
    chat.register_event(ChatEvent.READY, on_ready)

    # you can directly register commands and their handlers,
    # this will register the !reply command
    chat.register_command("reply", test_command)
    chat.register_command("crayon", crayon_command)

    # we are done with our setup, lets start this bot up!
    chat.start()

    # lets run till we press enter in the console
    try:
        input("press ENTER to stop\n")
    finally:
        # now we can close the chat bot and the twitch api client
        chat.stop()
        await twitch.close()


@click.command()
def main():
    """Start the Twitch Crayon program."""
    click.echo("Starting Twitch Crayon...")

    # lets run our setup
    asyncio.run(run())


if __name__ == "__main__":
    main()
