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


class DestroySessionNone(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.DestroySessionRes`.

    Details:
        - Layer: ``135``
        - ID: ``0x62d350c9``

    Parameters:
        session_id: ``int`` ``64-bit``

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`DestroySession <pyrogram.raw.functions.DestroySession>`
    """

    __slots__: List[str] = ["session_id"]

    ID = 0x62d350c9
    QUALNAME = "types.DestroySessionNone"

    def __init__(self, *, session_id: int) -> None:
        self.session_id = session_id  # long

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "DestroySessionNone":
        # No flags
        
        session_id = Long.read(data)
        
        return DestroySessionNone(session_id=session_id)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags
        
        data.write(Long(self.session_id))
        
        return data.getvalue()