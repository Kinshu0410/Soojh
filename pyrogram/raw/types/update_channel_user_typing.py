#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-2021 Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Union, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class UpdateChannelUserTyping(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``135``
        - ID: ``0x8c88c923``

    Parameters:
        channel_id: ``int`` ``64-bit``
        from_id: :obj:`Peer <pyrogram.raw.base.Peer>`
        action: :obj:`SendMessageAction <pyrogram.raw.base.SendMessageAction>`
        top_msg_id (optional): ``int`` ``32-bit``
    """

    __slots__: List[str] = ["channel_id", "from_id", "action", "top_msg_id"]

    ID = 0x8c88c923
    QUALNAME = "types.UpdateChannelUserTyping"

    def __init__(self, *, channel_id: int, from_id: "raw.base.Peer", action: "raw.base.SendMessageAction", top_msg_id: Union[None, int] = None) -> None:
        self.channel_id = channel_id  # long
        self.from_id = from_id  # Peer
        self.action = action  # SendMessageAction
        self.top_msg_id = top_msg_id  # flags.0?int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "UpdateChannelUserTyping":
        flags = Int.read(data)
        
        channel_id = Long.read(data)
        
        top_msg_id = Int.read(data) if flags & (1 << 0) else None
        from_id = TLObject.read(data)
        
        action = TLObject.read(data)
        
        return UpdateChannelUserTyping(channel_id=channel_id, from_id=from_id, action=action, top_msg_id=top_msg_id)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.top_msg_id is not None else 0
        data.write(Int(flags))
        
        data.write(Long(self.channel_id))
        
        if self.top_msg_id is not None:
            data.write(Int(self.top_msg_id))
        
        data.write(self.from_id.write())
        
        data.write(self.action.write())
        
        return data.getvalue()