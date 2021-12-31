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


class GetSearchResultsPositions(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``135``
        - ID: ``0x6e9583a3``

    Parameters:
        peer: :obj:`InputPeer <pyrogram.raw.base.InputPeer>`
        filter: :obj:`MessagesFilter <pyrogram.raw.base.MessagesFilter>`
        offset_id: ``int`` ``32-bit``
        limit: ``int`` ``32-bit``

    Returns:
        :obj:`messages.SearchResultsPositions <pyrogram.raw.base.messages.SearchResultsPositions>`
    """

    __slots__: List[str] = ["peer", "filter", "offset_id", "limit"]

    ID = 0x6e9583a3
    QUALNAME = "functions.messages.GetSearchResultsPositions"

    def __init__(self, *, peer: "raw.base.InputPeer", filter: "raw.base.MessagesFilter", offset_id: int, limit: int) -> None:
        self.peer = peer  # InputPeer
        self.filter = filter  # MessagesFilter
        self.offset_id = offset_id  # int
        self.limit = limit  # int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "GetSearchResultsPositions":
        # No flags
        
        peer = TLObject.read(data)
        
        filter = TLObject.read(data)
        
        offset_id = Int.read(data)
        
        limit = Int.read(data)
        
        return GetSearchResultsPositions(peer=peer, filter=filter, offset_id=offset_id, limit=limit)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags
        
        data.write(self.peer.write())
        
        data.write(self.filter.write())
        
        data.write(Int(self.offset_id))
        
        data.write(Int(self.limit))
        
        return data.getvalue()
