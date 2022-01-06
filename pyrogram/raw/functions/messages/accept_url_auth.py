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


class AcceptUrlAuth(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``135``
        - ID: ``0xb12c7125``

    Parameters:
        write_allowed (optional): ``bool``
        peer (optional): :obj:`InputPeer <pyrogram.raw.base.InputPeer>`
        msg_id (optional): ``int`` ``32-bit``
        button_id (optional): ``int`` ``32-bit``
        url (optional): ``str``

    Returns:
        :obj:`UrlAuthResult <pyrogram.raw.base.UrlAuthResult>`
    """

    __slots__: List[str] = ["write_allowed", "peer", "msg_id", "button_id", "url"]

    ID = 0xb12c7125
    QUALNAME = "functions.messages.AcceptUrlAuth"

    def __init__(self, *, write_allowed: Union[None, bool] = None, peer: "raw.base.InputPeer" = None, msg_id: Union[None, int] = None, button_id: Union[None, int] = None, url: Union[None, str] = None) -> None:
        self.write_allowed = write_allowed  # flags.0?true
        self.peer = peer  # flags.1?InputPeer
        self.msg_id = msg_id  # flags.1?int
        self.button_id = button_id  # flags.1?int
        self.url = url  # flags.2?string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "AcceptUrlAuth":
        flags = Int.read(data)
        
        write_allowed = True if flags & (1 << 0) else False
        peer = TLObject.read(data) if flags & (1 << 1) else None
        
        msg_id = Int.read(data) if flags & (1 << 1) else None
        button_id = Int.read(data) if flags & (1 << 1) else None
        url = String.read(data) if flags & (1 << 2) else None
        return AcceptUrlAuth(write_allowed=write_allowed, peer=peer, msg_id=msg_id, button_id=button_id, url=url)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.write_allowed else 0
        flags |= (1 << 1) if self.peer is not None else 0
        flags |= (1 << 1) if self.msg_id is not None else 0
        flags |= (1 << 1) if self.button_id is not None else 0
        flags |= (1 << 2) if self.url is not None else 0
        data.write(Int(flags))
        
        if self.peer is not None:
            data.write(self.peer.write())
        
        if self.msg_id is not None:
            data.write(Int(self.msg_id))
        
        if self.button_id is not None:
            data.write(Int(self.button_id))
        
        if self.url is not None:
            data.write(String(self.url))
        
        return data.getvalue()