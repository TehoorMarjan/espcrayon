from .colors import COLORS, EFFECTS

import httpx
import asyncio
import re
import unicodedata

type Color = tuple[int, int, int]
type Effect = str | None


class CrayonTwitchController:
    COOLDOWN = 60.0  # seconds

    _re_anycolor = re.compile(
        r"""
        ^\s*(
            # Match RGB format: r,g,b
            (
                (?P<rd>\d+)\s*,
                \s*(?P<gd>\d+)\s*,
                \s*(?P<bd>\d+)
            )
            |
            # Match Hex format: #RRGGBB
            \#(
                (?P<rh6>[0-9a-fA-F]{2})
                (?P<gh6>[0-9a-fA-F]{2})
                (?P<bh6>[0-9a-fA-F]{2})
            )
            |
            # Match short Hex format: #RGB
            \#(
                (?P<rh3>[0-9a-fA-F])
                (?P<gh3>[0-9a-fA-F])
                (?P<bh3>[0-9a-fA-F])
            )
            |
            # Match named color or effect
            (?P<name>\w+)
        )
        """,
        re.VERBOSE,
    )

    def __init__(self, base_url: str, token: str):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {token}",
            "content-type": "application/json",
        }
        self.last_requester: str | None = None

    def parse_color_param(self, param: str) -> tuple[Color, Effect]:
        """
        Parse a color parameter string and return the corresponding RGB color
        and effect.
        """
        if not (m := self._re_anycolor.match(param)):
            raise ValueError("Invalid color parameter format")
        if m["rd"] and m["gd"] and m["bd"]:
            r = int(m["rd"])
            g = int(m["gd"])
            b = int(m["bd"])
            effect = None
            if r > 255 or g > 255 or b > 255:
                raise ValueError("Color values must be between 0 and 255")
        elif m["rh6"] and m["gh6"] and m["bh6"]:
            r = int(m["rh6"], 16)
            g = int(m["gh6"], 16)
            b = int(m["bh6"], 16)
            effect = None
        elif m["rh3"] and m["gh3"] and m["bh3"]:
            r = int(m["rh3"] * 2, 16)
            g = int(m["gh3"] * 2, 16)
            b = int(m["bh3"] * 2, 16)
            effect = None
        elif m["name"]:
            name = (
                unicodedata.normalize("NFD", m["name"])
                .encode("ascii", "ignore")
                .decode("utf-8")
                .capitalize()
            )
            if name in COLORS:
                r, g, b = COLORS[name]
                effect = None
            elif name in EFFECTS:
                r, g, b = 0, 0, 0
                effect = name
            else:
                raise ValueError(f"Unknown color or effect name: {name}")
        else:
            raise ValueError("Invalid color parameter format")
        return (r, g, b), effect

    async def execute_light_effect(self, color: Color, effect: Effect) -> bool:
        r, g, b = color
        data = {
            "entity_id": "light.crayon_rgb_light",
            "effect": effect or "None",
            "brightness": 255,
        }
        if effect is None:
            data["rgb_color"] = [r, g, b]

        async with httpx.AsyncClient() as client:
            response = await client.post(
                self.base_url + "api/services/light/turn_on",
                headers=self.headers,
                json=data,
            )
            return response.status_code == httpx.codes.OK

    async def do_twitch_command(self, parameter: str, requester: str) -> str:
        if len(parameter) == 0:
            return "J'ai besoin d'un paramètre. -> !usage"
        
        # When a user requests a color change, prevent other users from
        # interfering for a cooldown period. Same user can change again
        # the color during the cooldown, but it will not reset the timer.
        if self.last_requester is not None:
            if self.last_requester != requester:
                return (
                    f"Attends un peu, {self.last_requester} vient juste de "
                    "changer la couleur."
                )
        else:
            asyncio.create_task(self.cooldown(requester))

        try:
            color, effect = self.parse_color_param(parameter)
        except ValueError:
            return "J'ai pas pu lire la couleur. -> !usage"

        success = await self.execute_light_effect(color, effect)
        if success:
            return "Et voilà !"
        else:
            return (
                "J'ai pas pu changer la couleur du crayon, mais c'est pas toi, "
                "c'est ma faute."
            )

    async def cooldown(self, requester: str):
        self.last_requester = requester
        await asyncio.sleep(self.COOLDOWN)
        self.last_requester = None