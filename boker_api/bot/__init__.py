# -*- coding: utf-8 -*-
"""
    boker_api.bot
    ~~~~~~~~~~~~~

    Contains discord bot class with all its methods
    Initializes bot
"""

import discord
import os
import csv
import asyncio

from typing import List, Union


class User():
    """ User object holding user id and chip number data

    Attributes:
        ident (str): discord user id formatted as <@id>
        chips (str): number of Poker Now chips that user has

    """

    def __init__(self, ident: str, chips: str):
        self.ident = ident
        self.chips = chips


def parseRankings(rankingcsv: bytes) -> List[User]:
    """Parses Poker Now rankings into array of User objects

    Takes .csv attachment from `!prc all` (from Poker Now Bot,
    retreived using discord.py)
    and parses it into an array of User objects containing their
    discord id and number of chips

    Args:
        rankingcsv (bytes): bytecode of ranking csv attachment
                            read using discord.attachment.read()

    Returns:
        List[User]: array of Users containing
                    their discord id and number of chips
    """

    lines = csv.DictReader(rankingcsv.decode('utf-8').splitlines())
    return [User(row[' player id'], row[' chips']) for row in lines]


async def moveFische(
    spaces: int, cycles: int, sleep: float,
    message: discord.message.Message
) -> None:
    """Makes >))'> animation in discord message

    >))'>
        >))'>
            <'((<
        <'((<
    >))'>

    Args:
        spaces (int):                       max number of spaces
                                            to add before fish
        cycles (int):                       number of cycles to
                                            run animation
        sleep (float):                      number of seconds to
                                            sleep between frames
        message (discord.message.Message):  fish message to edit
    """

    right_fische = '>))\'>'
    left_fische = '<\'((<'

    # skip first frame as original message contains it
    for i in range(1, 2 * cycles * spaces):
        await asyncio.sleep(sleep)

        it = i % (spaces * 2)

        if it < spaces:  # fish moving right
            await message.edit(  # `_ ` is a whitespace in discord
                content=(((it % spaces) * '_ _ _ _ ') + right_fische)
                )
        else:           # fish moving left
            await message.edit(
                content=(((spaces - (it % spaces)) * '_ _ _ _ ') + left_fische)
                )


class MyClient(discord.Client):
    """discord.py client
    """

    async def on_ready(self) -> None:
        """on log in print to console and change game state
        """
        print('Logged on as', self.user)
        await self.change_presence(
            activity=discord.Game(name='the bella fische >))\'>')
            )

    async def send_pcr(self) -> None:
        """Sends `!pcr all` to BOT_CHANNEL (to get Poker Now Bot to send balances)

        Fetches bot channel id from environment

        sends !pcr using discord.GroupChannel.send()
        """
        channel = self.get_channel(int(str(os.getenv('BOT_CHANNEL'))))
        await channel.send('!pcr all')

    async def rankings(
        self, message: discord.message.Message
    ) -> Union[List[User], None]:
        """Checks if message is Poker Now Bot sending chip rankings, then parses them

        Args:
            message (discord.message.Message): message to check

        Returns:
            Union[List[User], None]: A list of parsed Users with their balances
                                        or None
        """

        if (
            message.author.id == int(os.getenv('POKER_NOW_BOT_ID'))
            and message.content == 'All player rankings:'
        ):
            for att in message.attachments:
                rankings = await att.read()
                return parseRankings(rankings)
        return None

    async def hello_world(self, message: discord.message.Message) -> None:
        """Sends `world` if anyone sends `hello` in a channel

        Args:
            message (discord.message.Message): message to check
        """
        if message.content.lower() == 'hello':
            await message.channel.send('world')

    async def bella_fische(self, message: discord.message.Message) -> None:
        """Sends animated `fische >))'>` if anyone sends `bella` in a channel

        Args:
            message (discord.message.Message): message to check
        """
        if message.content.lower() == 'bella':
            await message.channel.send('fische')

            fische_message = await message.channel.send('>))\'>')

            # 5 spaces, 5 cycles, 0.5 seconds between frames
            await moveFische(5, 5, 0.5, fische_message)

    async def on_message(self, message: discord.message.Message):
        if message.author == self.user:
            return

        await self.hello_world(message)

        await self.rankings(message)

        await self.bella_fische(message)


# init bot
client = MyClient()
