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


class SecureValueErrorData(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.SecureValueError`.

    Details:
        - Layer: ``135``
        - ID: ``0xe8a40bd9``

    Parameters:
        type: :obj:`SecureValueType <pyrogram.raw.base.SecureValueType>`
        data_hash: ``bytes``
        field: ``str``
        text: ``str``
    """

    __slots__: List[str] = ["type", "data_hash", "field", "text"]

    ID = 0xe8a40bd9
    QUALNAME = "types.SecureValueErrorData"

    def __init__(self, *, type: "raw.base.SecureValueType", data_hash: bytes, field: str, text: str) -> None:
        self.type = type  # SecureValueType
        self.data_hash = data_hash  # bytes
        self.field = field  # string
        self.text = text  # string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "SecureValueErrorData":
        # No flags
        
        type = TLObject.read(data)
        
        data_hash = Bytes.read(data)
        
        field = String.read(data)
        
        text = String.read(data)
        
        return SecureValueErrorData(type=type, data_hash=data_hash, field=field, text=text)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags
        
        data.write(self.type.write())
        
        data.write(Bytes(self.data_hash))
        
        data.write(String(self.field))
        
        data.write(String(self.text))
        
        return data.getvalue()
