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


class ChatParticipants(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.ChatParticipants`.

    Details:
        - Layer: ``135``
        - ID: ``0x3cbc93f8``

    Parameters:
        chat_id: ``int`` ``64-bit``
        participants: List of :obj:`ChatParticipant <pyrogram.raw.base.ChatParticipant>`
        version: ``int`` ``32-bit``
    """

    __slots__: List[str] = ["chat_id", "participants", "version"]

    ID = 0x3cbc93f8
    QUALNAME = "types.ChatParticipants"

    def __init__(self, *, chat_id: int, participants: List["raw.base.ChatParticipant"], version: int) -> None:
        self.chat_id = chat_id  # long
        self.participants = participants  # Vector<ChatParticipant>
        self.version = version  # int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "ChatParticipants":
        # No flags
        
        chat_id = Long.read(data)
        
        participants = TLObject.read(data)
        
        version = Int.read(data)
        
        return ChatParticipants(chat_id=chat_id, participants=participants, version=version)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags
        
        data.write(Long(self.chat_id))
        
        data.write(Vector(self.participants))
        
        data.write(Int(self.version))
        
        return data.getvalue()
