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


class UpdateChannelParticipant(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``135``
        - ID: ``0x985d3abb``

    Parameters:
        channel_id: ``int`` ``64-bit``
        date: ``int`` ``32-bit``
        actor_id: ``int`` ``64-bit``
        user_id: ``int`` ``64-bit``
        qts: ``int`` ``32-bit``
        prev_participant (optional): :obj:`ChannelParticipant <pyrogram.raw.base.ChannelParticipant>`
        new_participant (optional): :obj:`ChannelParticipant <pyrogram.raw.base.ChannelParticipant>`
        invite (optional): :obj:`ExportedChatInvite <pyrogram.raw.base.ExportedChatInvite>`
    """

    __slots__: List[str] = ["channel_id", "date", "actor_id", "user_id", "qts", "prev_participant", "new_participant", "invite"]

    ID = 0x985d3abb
    QUALNAME = "types.UpdateChannelParticipant"

    def __init__(self, *, channel_id: int, date: int, actor_id: int, user_id: int, qts: int, prev_participant: "raw.base.ChannelParticipant" = None, new_participant: "raw.base.ChannelParticipant" = None, invite: "raw.base.ExportedChatInvite" = None) -> None:
        self.channel_id = channel_id  # long
        self.date = date  # int
        self.actor_id = actor_id  # long
        self.user_id = user_id  # long
        self.qts = qts  # int
        self.prev_participant = prev_participant  # flags.0?ChannelParticipant
        self.new_participant = new_participant  # flags.1?ChannelParticipant
        self.invite = invite  # flags.2?ExportedChatInvite

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "UpdateChannelParticipant":
        flags = Int.read(data)
        
        channel_id = Long.read(data)
        
        date = Int.read(data)
        
        actor_id = Long.read(data)
        
        user_id = Long.read(data)
        
        prev_participant = TLObject.read(data) if flags & (1 << 0) else None
        
        new_participant = TLObject.read(data) if flags & (1 << 1) else None
        
        invite = TLObject.read(data) if flags & (1 << 2) else None
        
        qts = Int.read(data)
        
        return UpdateChannelParticipant(channel_id=channel_id, date=date, actor_id=actor_id, user_id=user_id, qts=qts, prev_participant=prev_participant, new_participant=new_participant, invite=invite)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.prev_participant is not None else 0
        flags |= (1 << 1) if self.new_participant is not None else 0
        flags |= (1 << 2) if self.invite is not None else 0
        data.write(Int(flags))
        
        data.write(Long(self.channel_id))
        
        data.write(Int(self.date))
        
        data.write(Long(self.actor_id))
        
        data.write(Long(self.user_id))
        
        if self.prev_participant is not None:
            data.write(self.prev_participant.write())
        
        if self.new_participant is not None:
            data.write(self.new_participant.write())
        
        if self.invite is not None:
            data.write(self.invite.write())
        
        data.write(Int(self.qts))
        
        return data.getvalue()
