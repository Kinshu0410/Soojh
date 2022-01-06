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


class SearchResultsPositions(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.messages.SearchResultsPositions`.

    Details:
        - Layer: ``135``
        - ID: ``0x53b22baf``

    Parameters:
        count: ``int`` ``32-bit``
        positions: List of :obj:`SearchResultsPosition <pyrogram.raw.base.SearchResultsPosition>`

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`messages.GetSearchResultsPositions <pyrogram.raw.functions.messages.GetSearchResultsPositions>`
    """

    __slots__: List[str] = ["count", "positions"]

    ID = 0x53b22baf
    QUALNAME = "types.messages.SearchResultsPositions"

    def __init__(self, *, count: int, positions: List["raw.base.SearchResultsPosition"]) -> None:
        self.count = count  # int
        self.positions = positions  # Vector<SearchResultsPosition>

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "SearchResultsPositions":
        # No flags
        
        count = Int.read(data)
        
        positions = TLObject.read(data)
        
        return SearchResultsPositions(count=count, positions=positions)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags
        
        data.write(Int(self.count))
        
        data.write(Vector(self.positions))
        
        return data.getvalue()