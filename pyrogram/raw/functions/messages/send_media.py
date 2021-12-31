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


class SendMedia(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``135``
        - ID: ``0xe25ff8e0``

    Parameters:
        peer: :obj:`InputPeer <pyrogram.raw.base.InputPeer>`
        media: :obj:`InputMedia <pyrogram.raw.base.InputMedia>`
        message: ``str``
        random_id: ``int`` ``64-bit``
        silent (optional): ``bool``
        background (optional): ``bool``
        clear_draft (optional): ``bool``
        reply_to_msg_id (optional): ``int`` ``32-bit``
        reply_markup (optional): :obj:`ReplyMarkup <pyrogram.raw.base.ReplyMarkup>`
        entities (optional): List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`
        schedule_date (optional): ``int`` ``32-bit``
        send_as (optional): :obj:`InputPeer <pyrogram.raw.base.InputPeer>`

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "media", "message", "random_id", "silent", "background", "clear_draft", "reply_to_msg_id", "reply_markup", "entities", "schedule_date", "send_as"]

    ID = 0xe25ff8e0
    QUALNAME = "functions.messages.SendMedia"

    def __init__(self, *, peer: "raw.base.InputPeer", media: "raw.base.InputMedia", message: str, random_id: int, silent: Union[None, bool] = None, background: Union[None, bool] = None, clear_draft: Union[None, bool] = None, reply_to_msg_id: Union[None, int] = None, reply_markup: "raw.base.ReplyMarkup" = None, entities: Union[None, List["raw.base.MessageEntity"]] = None, schedule_date: Union[None, int] = None, send_as: "raw.base.InputPeer" = None) -> None:
        self.peer = peer  # InputPeer
        self.media = media  # InputMedia
        self.message = message  # string
        self.random_id = random_id  # long
        self.silent = silent  # flags.5?true
        self.background = background  # flags.6?true
        self.clear_draft = clear_draft  # flags.7?true
        self.reply_to_msg_id = reply_to_msg_id  # flags.0?int
        self.reply_markup = reply_markup  # flags.2?ReplyMarkup
        self.entities = entities  # flags.3?Vector<MessageEntity>
        self.schedule_date = schedule_date  # flags.10?int
        self.send_as = send_as  # flags.13?InputPeer

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "SendMedia":
        flags = Int.read(data)
        
        silent = True if flags & (1 << 5) else False
        background = True if flags & (1 << 6) else False
        clear_draft = True if flags & (1 << 7) else False
        peer = TLObject.read(data)
        
        reply_to_msg_id = Int.read(data) if flags & (1 << 0) else None
        media = TLObject.read(data)
        
        message = String.read(data)
        
        random_id = Long.read(data)
        
        reply_markup = TLObject.read(data) if flags & (1 << 2) else None
        
        entities = TLObject.read(data) if flags & (1 << 3) else []
        
        schedule_date = Int.read(data) if flags & (1 << 10) else None
        send_as = TLObject.read(data) if flags & (1 << 13) else None
        
        return SendMedia(peer=peer, media=media, message=message, random_id=random_id, silent=silent, background=background, clear_draft=clear_draft, reply_to_msg_id=reply_to_msg_id, reply_markup=reply_markup, entities=entities, schedule_date=schedule_date, send_as=send_as)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 5) if self.silent else 0
        flags |= (1 << 6) if self.background else 0
        flags |= (1 << 7) if self.clear_draft else 0
        flags |= (1 << 0) if self.reply_to_msg_id is not None else 0
        flags |= (1 << 2) if self.reply_markup is not None else 0
        flags |= (1 << 3) if self.entities is not None else 0
        flags |= (1 << 10) if self.schedule_date is not None else 0
        flags |= (1 << 13) if self.send_as is not None else 0
        data.write(Int(flags))
        
        data.write(self.peer.write())
        
        if self.reply_to_msg_id is not None:
            data.write(Int(self.reply_to_msg_id))
        
        data.write(self.media.write())
        
        data.write(String(self.message))
        
        data.write(Long(self.random_id))
        
        if self.reply_markup is not None:
            data.write(self.reply_markup.write())
        
        if self.entities is not None:
            data.write(Vector(self.entities))
        
        if self.schedule_date is not None:
            data.write(Int(self.schedule_date))
        
        if self.send_as is not None:
            data.write(self.send_as.write())
        
        return data.getvalue()
