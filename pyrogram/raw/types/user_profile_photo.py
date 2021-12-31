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


class UserProfilePhoto(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.UserProfilePhoto`.

    Details:
        - Layer: ``135``
        - ID: ``0x82d1f706``

    Parameters:
        photo_id: ``int`` ``64-bit``
        dc_id: ``int`` ``32-bit``
        has_video (optional): ``bool``
        stripped_thumb (optional): ``bytes``
    """

    __slots__: List[str] = ["photo_id", "dc_id", "has_video", "stripped_thumb"]

    ID = 0x82d1f706
    QUALNAME = "types.UserProfilePhoto"

    def __init__(self, *, photo_id: int, dc_id: int, has_video: Union[None, bool] = None, stripped_thumb: Union[None, bytes] = None) -> None:
        self.photo_id = photo_id  # long
        self.dc_id = dc_id  # int
        self.has_video = has_video  # flags.0?true
        self.stripped_thumb = stripped_thumb  # flags.1?bytes

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "UserProfilePhoto":
        flags = Int.read(data)
        
        has_video = True if flags & (1 << 0) else False
        photo_id = Long.read(data)
        
        stripped_thumb = Bytes.read(data) if flags & (1 << 1) else None
        dc_id = Int.read(data)
        
        return UserProfilePhoto(photo_id=photo_id, dc_id=dc_id, has_video=has_video, stripped_thumb=stripped_thumb)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.has_video else 0
        flags |= (1 << 1) if self.stripped_thumb is not None else 0
        data.write(Int(flags))
        
        data.write(Long(self.photo_id))
        
        if self.stripped_thumb is not None:
            data.write(Bytes(self.stripped_thumb))
        
        data.write(Int(self.dc_id))
        
        return data.getvalue()
