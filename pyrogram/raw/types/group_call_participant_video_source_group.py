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


class GroupCallParticipantVideoSourceGroup(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.GroupCallParticipantVideoSourceGroup`.

    Details:
        - Layer: ``135``
        - ID: ``0xdcb118b7``

    Parameters:
        semantics: ``str``
        sources: List of ``int`` ``32-bit``
    """

    __slots__: List[str] = ["semantics", "sources"]

    ID = 0xdcb118b7
    QUALNAME = "types.GroupCallParticipantVideoSourceGroup"

    def __init__(self, *, semantics: str, sources: List[int]) -> None:
        self.semantics = semantics  # string
        self.sources = sources  # Vector<int>

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "GroupCallParticipantVideoSourceGroup":
        # No flags
        
        semantics = String.read(data)
        
        sources = TLObject.read(data, Int)
        
        return GroupCallParticipantVideoSourceGroup(semantics=semantics, sources=sources)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags
        
        data.write(String(self.semantics))
        
        data.write(Vector(self.sources, Int))
        
        return data.getvalue()
