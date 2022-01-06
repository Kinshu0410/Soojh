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


class InputPeerChannelFromMessage(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.InputPeer`.

    Details:
        - Layer: ``135``
        - ID: ``0xbd2a0840``

    Parameters:
        peer: :obj:`InputPeer <pyrogram.raw.base.InputPeer>`
        msg_id: ``int`` ``32-bit``
        channel_id: ``int`` ``64-bit``
    """

    __slots__: List[str] = ["peer", "msg_id", "channel_id"]

    ID = 0xbd2a0840
    QUALNAME = "types.InputPeerChannelFromMessage"

    def __init__(self, *, peer: "raw.base.InputPeer", msg_id: int, channel_id: int) -> None:
        self.peer = peer  # InputPeer
        self.msg_id = msg_id  # int
        self.channel_id = channel_id  # long

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "InputPeerChannelFromMessage":
        # No flags
        
        peer = TLObject.read(data)
        
        msg_id = Int.read(data)
        
        channel_id = Long.read(data)
        
        return InputPeerChannelFromMessage(peer=peer, msg_id=msg_id, channel_id=channel_id)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags
        
        data.write(self.peer.write())
        
        data.write(Int(self.msg_id))
        
        data.write(Long(self.channel_id))
        
        return data.getvalue()