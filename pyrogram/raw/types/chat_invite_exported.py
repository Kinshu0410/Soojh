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


class ChatInviteExported(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.ExportedChatInvite`.

    Details:
        - Layer: ``135``
        - ID: ``0xab4a819``

    Parameters:
        link: ``str``
        admin_id: ``int`` ``64-bit``
        date: ``int`` ``32-bit``
        revoked (optional): ``bool``
        permanent (optional): ``bool``
        request_needed (optional): ``bool``
        start_date (optional): ``int`` ``32-bit``
        expire_date (optional): ``int`` ``32-bit``
        usage_limit (optional): ``int`` ``32-bit``
        usage (optional): ``int`` ``32-bit``
        requested (optional): ``int`` ``32-bit``
        title (optional): ``str``

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`messages.ExportChatInvite <pyrogram.raw.functions.messages.ExportChatInvite>`
    """

    __slots__: List[str] = ["link", "admin_id", "date", "revoked", "permanent", "request_needed", "start_date", "expire_date", "usage_limit", "usage", "requested", "title"]

    ID = 0xab4a819
    QUALNAME = "types.ChatInviteExported"

    def __init__(self, *, link: str, admin_id: int, date: int, revoked: Union[None, bool] = None, permanent: Union[None, bool] = None, request_needed: Union[None, bool] = None, start_date: Union[None, int] = None, expire_date: Union[None, int] = None, usage_limit: Union[None, int] = None, usage: Union[None, int] = None, requested: Union[None, int] = None, title: Union[None, str] = None) -> None:
        self.link = link  # string
        self.admin_id = admin_id  # long
        self.date = date  # int
        self.revoked = revoked  # flags.0?true
        self.permanent = permanent  # flags.5?true
        self.request_needed = request_needed  # flags.6?true
        self.start_date = start_date  # flags.4?int
        self.expire_date = expire_date  # flags.1?int
        self.usage_limit = usage_limit  # flags.2?int
        self.usage = usage  # flags.3?int
        self.requested = requested  # flags.7?int
        self.title = title  # flags.8?string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "ChatInviteExported":
        flags = Int.read(data)
        
        revoked = True if flags & (1 << 0) else False
        permanent = True if flags & (1 << 5) else False
        request_needed = True if flags & (1 << 6) else False
        link = String.read(data)
        
        admin_id = Long.read(data)
        
        date = Int.read(data)
        
        start_date = Int.read(data) if flags & (1 << 4) else None
        expire_date = Int.read(data) if flags & (1 << 1) else None
        usage_limit = Int.read(data) if flags & (1 << 2) else None
        usage = Int.read(data) if flags & (1 << 3) else None
        requested = Int.read(data) if flags & (1 << 7) else None
        title = String.read(data) if flags & (1 << 8) else None
        return ChatInviteExported(link=link, admin_id=admin_id, date=date, revoked=revoked, permanent=permanent, request_needed=request_needed, start_date=start_date, expire_date=expire_date, usage_limit=usage_limit, usage=usage, requested=requested, title=title)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.revoked else 0
        flags |= (1 << 5) if self.permanent else 0
        flags |= (1 << 6) if self.request_needed else 0
        flags |= (1 << 4) if self.start_date is not None else 0
        flags |= (1 << 1) if self.expire_date is not None else 0
        flags |= (1 << 2) if self.usage_limit is not None else 0
        flags |= (1 << 3) if self.usage is not None else 0
        flags |= (1 << 7) if self.requested is not None else 0
        flags |= (1 << 8) if self.title is not None else 0
        data.write(Int(flags))
        
        data.write(String(self.link))
        
        data.write(Long(self.admin_id))
        
        data.write(Int(self.date))
        
        if self.start_date is not None:
            data.write(Int(self.start_date))
        
        if self.expire_date is not None:
            data.write(Int(self.expire_date))
        
        if self.usage_limit is not None:
            data.write(Int(self.usage_limit))
        
        if self.usage is not None:
            data.write(Int(self.usage))
        
        if self.requested is not None:
            data.write(Int(self.requested))
        
        if self.title is not None:
            data.write(String(self.title))
        
        return data.getvalue()
