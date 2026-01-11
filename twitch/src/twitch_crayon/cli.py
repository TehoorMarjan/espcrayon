import asyncio
import os
import click

from dotenv import load_dotenv
from twitchAPI.chat import Chat, ChatCommand, EventData
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.twitch import Twitch
from twitchAPI.type import AuthScope, ChatEvent

from .crayon import CrayonTwitchController

load_dotenv()

APP_ID = os.environ["APP_ID"]
APP_SECRET = os.environ["APP_SECRET"]
TARGET_CHANNEL = os.environ["TARGET_CHANNEL"]
USAGE_URL = os.environ["USAGE_URL"]
TOKEN = os.environ["HATOKEN"]
BASE_URL = os.environ["HAURL"]

USER_SCOPE = [AuthScope.CHAT_READ, AuthScope.CHAT_EDIT]

crayon = CrayonTwitchController(base_url=BASE_URL, token=TOKEN)

# ## Twitch Chat Commands
async def crayon_command(cmd: ChatCommand):
    reply = await crayon.do_twitch_command(cmd.parameter)
    await cmd.reply(reply)

async def usage_command(cmd: ChatCommand):
    await cmd.reply(f"Utilisation du bot : {USAGE_URL}")

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
    token, refresh_token = await auth.authenticate()  # type: ignore
    await twitch.set_user_authentication(token, USER_SCOPE, refresh_token)

    # create chat instance
    chat = await Chat(twitch)

    # register the handlers for the events you want

    # listen to when the bot is done starting up and ready to join channels
    chat.register_event(ChatEvent.READY, on_ready)

    # you can directly register commands and their handlers
    chat.register_command("crayon", crayon_command)
    chat.register_command("usage", usage_command)

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
