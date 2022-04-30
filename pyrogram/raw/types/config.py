#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
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
from typing import List, Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class Config(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.Config`.

    Details:
        - Layer: ``140``
        - ID: ``330B4067``

    Parameters:
        date: ``int`` ``32-bit``
        expires: ``int`` ``32-bit``
        test_mode: ``bool``
        this_dc: ``int`` ``32-bit``
        dc_options: List of :obj:`DcOption <pyrogram.raw.base.DcOption>`
        dc_txt_domain_name: ``str``
        chat_size_max: ``int`` ``32-bit``
        megagroup_size_max: ``int`` ``32-bit``
        forwarded_count_max: ``int`` ``32-bit``
        online_update_period_ms: ``int`` ``32-bit``
        offline_blur_timeout_ms: ``int`` ``32-bit``
        offline_idle_timeout_ms: ``int`` ``32-bit``
        online_cloud_timeout_ms: ``int`` ``32-bit``
        notify_cloud_delay_ms: ``int`` ``32-bit``
        notify_default_delay_ms: ``int`` ``32-bit``
        push_chat_period_ms: ``int`` ``32-bit``
        push_chat_limit: ``int`` ``32-bit``
        saved_gifs_limit: ``int`` ``32-bit``
        edit_time_limit: ``int`` ``32-bit``
        revoke_time_limit: ``int`` ``32-bit``
        revoke_pm_time_limit: ``int`` ``32-bit``
        rating_e_decay: ``int`` ``32-bit``
        stickers_recent_limit: ``int`` ``32-bit``
        stickers_faved_limit: ``int`` ``32-bit``
        channels_read_media_period: ``int`` ``32-bit``
        pinned_dialogs_count_max: ``int`` ``32-bit``
        pinned_infolder_count_max: ``int`` ``32-bit``
        call_receive_timeout_ms: ``int`` ``32-bit``
        call_ring_timeout_ms: ``int`` ``32-bit``
        call_connect_timeout_ms: ``int`` ``32-bit``
        call_packet_timeout_ms: ``int`` ``32-bit``
        me_url_prefix: ``str``
        caption_length_max: ``int`` ``32-bit``
        message_length_max: ``int`` ``32-bit``
        webfile_dc_id: ``int`` ``32-bit``
        phonecalls_enabled (optional): ``bool``
        default_p2p_contacts (optional): ``bool``
        preload_featured_stickers (optional): ``bool``
        ignore_phone_entities (optional): ``bool``
        revoke_pm_inbox (optional): ``bool``
        blocked_mode (optional): ``bool``
        pfs_enabled (optional): ``bool``
        tmp_sessions (optional): ``int`` ``32-bit``
        autoupdate_url_prefix (optional): ``str``
        gif_search_username (optional): ``str``
        venue_search_username (optional): ``str``
        img_search_username (optional): ``str``
        static_maps_provider (optional): ``str``
        suggested_lang_code (optional): ``str``
        lang_pack_version (optional): ``int`` ``32-bit``
        base_lang_pack_version (optional): ``int`` ``32-bit``

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`help.GetConfig <pyrogram.raw.functions.help.GetConfig>`
    """

    __slots__: List[str] = ["date", "expires", "test_mode", "this_dc", "dc_options", "dc_txt_domain_name", "chat_size_max", "megagroup_size_max", "forwarded_count_max", "online_update_period_ms", "offline_blur_timeout_ms", "offline_idle_timeout_ms", "online_cloud_timeout_ms", "notify_cloud_delay_ms", "notify_default_delay_ms", "push_chat_period_ms", "push_chat_limit", "saved_gifs_limit", "edit_time_limit", "revoke_time_limit", "revoke_pm_time_limit", "rating_e_decay", "stickers_recent_limit", "stickers_faved_limit", "channels_read_media_period", "pinned_dialogs_count_max", "pinned_infolder_count_max", "call_receive_timeout_ms", "call_ring_timeout_ms", "call_connect_timeout_ms", "call_packet_timeout_ms", "me_url_prefix", "caption_length_max", "message_length_max", "webfile_dc_id", "phonecalls_enabled", "default_p2p_contacts", "preload_featured_stickers", "ignore_phone_entities", "revoke_pm_inbox", "blocked_mode", "pfs_enabled", "tmp_sessions", "autoupdate_url_prefix", "gif_search_username", "venue_search_username", "img_search_username", "static_maps_provider", "suggested_lang_code", "lang_pack_version", "base_lang_pack_version"]

    ID = 0x330b4067
    QUALNAME = "types.Config"

    def __init__(self, *, date: int, expires: int, test_mode: bool, this_dc: int, dc_options: List["raw.base.DcOption"], dc_txt_domain_name: str, chat_size_max: int, megagroup_size_max: int, forwarded_count_max: int, online_update_period_ms: int, offline_blur_timeout_ms: int, offline_idle_timeout_ms: int, online_cloud_timeout_ms: int, notify_cloud_delay_ms: int, notify_default_delay_ms: int, push_chat_period_ms: int, push_chat_limit: int, saved_gifs_limit: int, edit_time_limit: int, revoke_time_limit: int, revoke_pm_time_limit: int, rating_e_decay: int, stickers_recent_limit: int, stickers_faved_limit: int, channels_read_media_period: int, pinned_dialogs_count_max: int, pinned_infolder_count_max: int, call_receive_timeout_ms: int, call_ring_timeout_ms: int, call_connect_timeout_ms: int, call_packet_timeout_ms: int, me_url_prefix: str, caption_length_max: int, message_length_max: int, webfile_dc_id: int, phonecalls_enabled: Optional[bool] = None, default_p2p_contacts: Optional[bool] = None, preload_featured_stickers: Optional[bool] = None, ignore_phone_entities: Optional[bool] = None, revoke_pm_inbox: Optional[bool] = None, blocked_mode: Optional[bool] = None, pfs_enabled: Optional[bool] = None, tmp_sessions: Optional[int] = None, autoupdate_url_prefix: Optional[str] = None, gif_search_username: Optional[str] = None, venue_search_username: Optional[str] = None, img_search_username: Optional[str] = None, static_maps_provider: Optional[str] = None, suggested_lang_code: Optional[str] = None, lang_pack_version: Optional[int] = None, base_lang_pack_version: Optional[int] = None) -> None:
        self.date = date  # int
        self.expires = expires  # int
        self.test_mode = test_mode  # Bool
        self.this_dc = this_dc  # int
        self.dc_options = dc_options  # Vector<DcOption>
        self.dc_txt_domain_name = dc_txt_domain_name  # string
        self.chat_size_max = chat_size_max  # int
        self.megagroup_size_max = megagroup_size_max  # int
        self.forwarded_count_max = forwarded_count_max  # int
        self.online_update_period_ms = online_update_period_ms  # int
        self.offline_blur_timeout_ms = offline_blur_timeout_ms  # int
        self.offline_idle_timeout_ms = offline_idle_timeout_ms  # int
        self.online_cloud_timeout_ms = online_cloud_timeout_ms  # int
        self.notify_cloud_delay_ms = notify_cloud_delay_ms  # int
        self.notify_default_delay_ms = notify_default_delay_ms  # int
        self.push_chat_period_ms = push_chat_period_ms  # int
        self.push_chat_limit = push_chat_limit  # int
        self.saved_gifs_limit = saved_gifs_limit  # int
        self.edit_time_limit = edit_time_limit  # int
        self.revoke_time_limit = revoke_time_limit  # int
        self.revoke_pm_time_limit = revoke_pm_time_limit  # int
        self.rating_e_decay = rating_e_decay  # int
        self.stickers_recent_limit = stickers_recent_limit  # int
        self.stickers_faved_limit = stickers_faved_limit  # int
        self.channels_read_media_period = channels_read_media_period  # int
        self.pinned_dialogs_count_max = pinned_dialogs_count_max  # int
        self.pinned_infolder_count_max = pinned_infolder_count_max  # int
        self.call_receive_timeout_ms = call_receive_timeout_ms  # int
        self.call_ring_timeout_ms = call_ring_timeout_ms  # int
        self.call_connect_timeout_ms = call_connect_timeout_ms  # int
        self.call_packet_timeout_ms = call_packet_timeout_ms  # int
        self.me_url_prefix = me_url_prefix  # string
        self.caption_length_max = caption_length_max  # int
        self.message_length_max = message_length_max  # int
        self.webfile_dc_id = webfile_dc_id  # int
        self.phonecalls_enabled = phonecalls_enabled  # flags.1?true
        self.default_p2p_contacts = default_p2p_contacts  # flags.3?true
        self.preload_featured_stickers = preload_featured_stickers  # flags.4?true
        self.ignore_phone_entities = ignore_phone_entities  # flags.5?true
        self.revoke_pm_inbox = revoke_pm_inbox  # flags.6?true
        self.blocked_mode = blocked_mode  # flags.8?true
        self.pfs_enabled = pfs_enabled  # flags.13?true
        self.tmp_sessions = tmp_sessions  # flags.0?int
        self.autoupdate_url_prefix = autoupdate_url_prefix  # flags.7?string
        self.gif_search_username = gif_search_username  # flags.9?string
        self.venue_search_username = venue_search_username  # flags.10?string
        self.img_search_username = img_search_username  # flags.11?string
        self.static_maps_provider = static_maps_provider  # flags.12?string
        self.suggested_lang_code = suggested_lang_code  # flags.2?string
        self.lang_pack_version = lang_pack_version  # flags.2?int
        self.base_lang_pack_version = base_lang_pack_version  # flags.2?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Config":
        
        flags = Int.read(b)
        
        phonecalls_enabled = True if flags & (1 << 1) else False
        default_p2p_contacts = True if flags & (1 << 3) else False
        preload_featured_stickers = True if flags & (1 << 4) else False
        ignore_phone_entities = True if flags & (1 << 5) else False
        revoke_pm_inbox = True if flags & (1 << 6) else False
        blocked_mode = True if flags & (1 << 8) else False
        pfs_enabled = True if flags & (1 << 13) else False
        date = Int.read(b)
        
        expires = Int.read(b)
        
        test_mode = Bool.read(b)
        
        this_dc = Int.read(b)
        
        dc_options = TLObject.read(b)
        
        dc_txt_domain_name = String.read(b)
        
        chat_size_max = Int.read(b)
        
        megagroup_size_max = Int.read(b)
        
        forwarded_count_max = Int.read(b)
        
        online_update_period_ms = Int.read(b)
        
        offline_blur_timeout_ms = Int.read(b)
        
        offline_idle_timeout_ms = Int.read(b)
        
        online_cloud_timeout_ms = Int.read(b)
        
        notify_cloud_delay_ms = Int.read(b)
        
        notify_default_delay_ms = Int.read(b)
        
        push_chat_period_ms = Int.read(b)
        
        push_chat_limit = Int.read(b)
        
        saved_gifs_limit = Int.read(b)
        
        edit_time_limit = Int.read(b)
        
        revoke_time_limit = Int.read(b)
        
        revoke_pm_time_limit = Int.read(b)
        
        rating_e_decay = Int.read(b)
        
        stickers_recent_limit = Int.read(b)
        
        stickers_faved_limit = Int.read(b)
        
        channels_read_media_period = Int.read(b)
        
        tmp_sessions = Int.read(b) if flags & (1 << 0) else None
        pinned_dialogs_count_max = Int.read(b)
        
        pinned_infolder_count_max = Int.read(b)
        
        call_receive_timeout_ms = Int.read(b)
        
        call_ring_timeout_ms = Int.read(b)
        
        call_connect_timeout_ms = Int.read(b)
        
        call_packet_timeout_ms = Int.read(b)
        
        me_url_prefix = String.read(b)
        
        autoupdate_url_prefix = String.read(b) if flags & (1 << 7) else None
        gif_search_username = String.read(b) if flags & (1 << 9) else None
        venue_search_username = String.read(b) if flags & (1 << 10) else None
        img_search_username = String.read(b) if flags & (1 << 11) else None
        static_maps_provider = String.read(b) if flags & (1 << 12) else None
        caption_length_max = Int.read(b)
        
        message_length_max = Int.read(b)
        
        webfile_dc_id = Int.read(b)
        
        suggested_lang_code = String.read(b) if flags & (1 << 2) else None
        lang_pack_version = Int.read(b) if flags & (1 << 2) else None
        base_lang_pack_version = Int.read(b) if flags & (1 << 2) else None
        return Config(date=date, expires=expires, test_mode=test_mode, this_dc=this_dc, dc_options=dc_options, dc_txt_domain_name=dc_txt_domain_name, chat_size_max=chat_size_max, megagroup_size_max=megagroup_size_max, forwarded_count_max=forwarded_count_max, online_update_period_ms=online_update_period_ms, offline_blur_timeout_ms=offline_blur_timeout_ms, offline_idle_timeout_ms=offline_idle_timeout_ms, online_cloud_timeout_ms=online_cloud_timeout_ms, notify_cloud_delay_ms=notify_cloud_delay_ms, notify_default_delay_ms=notify_default_delay_ms, push_chat_period_ms=push_chat_period_ms, push_chat_limit=push_chat_limit, saved_gifs_limit=saved_gifs_limit, edit_time_limit=edit_time_limit, revoke_time_limit=revoke_time_limit, revoke_pm_time_limit=revoke_pm_time_limit, rating_e_decay=rating_e_decay, stickers_recent_limit=stickers_recent_limit, stickers_faved_limit=stickers_faved_limit, channels_read_media_period=channels_read_media_period, pinned_dialogs_count_max=pinned_dialogs_count_max, pinned_infolder_count_max=pinned_infolder_count_max, call_receive_timeout_ms=call_receive_timeout_ms, call_ring_timeout_ms=call_ring_timeout_ms, call_connect_timeout_ms=call_connect_timeout_ms, call_packet_timeout_ms=call_packet_timeout_ms, me_url_prefix=me_url_prefix, caption_length_max=caption_length_max, message_length_max=message_length_max, webfile_dc_id=webfile_dc_id, phonecalls_enabled=phonecalls_enabled, default_p2p_contacts=default_p2p_contacts, preload_featured_stickers=preload_featured_stickers, ignore_phone_entities=ignore_phone_entities, revoke_pm_inbox=revoke_pm_inbox, blocked_mode=blocked_mode, pfs_enabled=pfs_enabled, tmp_sessions=tmp_sessions, autoupdate_url_prefix=autoupdate_url_prefix, gif_search_username=gif_search_username, venue_search_username=venue_search_username, img_search_username=img_search_username, static_maps_provider=static_maps_provider, suggested_lang_code=suggested_lang_code, lang_pack_version=lang_pack_version, base_lang_pack_version=base_lang_pack_version)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.phonecalls_enabled else 0
        flags |= (1 << 3) if self.default_p2p_contacts else 0
        flags |= (1 << 4) if self.preload_featured_stickers else 0
        flags |= (1 << 5) if self.ignore_phone_entities else 0
        flags |= (1 << 6) if self.revoke_pm_inbox else 0
        flags |= (1 << 8) if self.blocked_mode else 0
        flags |= (1 << 13) if self.pfs_enabled else 0
        flags |= (1 << 0) if self.tmp_sessions is not None else 0
        flags |= (1 << 7) if self.autoupdate_url_prefix is not None else 0
        flags |= (1 << 9) if self.gif_search_username is not None else 0
        flags |= (1 << 10) if self.venue_search_username is not None else 0
        flags |= (1 << 11) if self.img_search_username is not None else 0
        flags |= (1 << 12) if self.static_maps_provider is not None else 0
        flags |= (1 << 2) if self.suggested_lang_code is not None else 0
        flags |= (1 << 2) if self.lang_pack_version is not None else 0
        flags |= (1 << 2) if self.base_lang_pack_version is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.date))
        
        b.write(Int(self.expires))
        
        b.write(Bool(self.test_mode))
        
        b.write(Int(self.this_dc))
        
        b.write(Vector(self.dc_options))
        
        b.write(String(self.dc_txt_domain_name))
        
        b.write(Int(self.chat_size_max))
        
        b.write(Int(self.megagroup_size_max))
        
        b.write(Int(self.forwarded_count_max))
        
        b.write(Int(self.online_update_period_ms))
        
        b.write(Int(self.offline_blur_timeout_ms))
        
        b.write(Int(self.offline_idle_timeout_ms))
        
        b.write(Int(self.online_cloud_timeout_ms))
        
        b.write(Int(self.notify_cloud_delay_ms))
        
        b.write(Int(self.notify_default_delay_ms))
        
        b.write(Int(self.push_chat_period_ms))
        
        b.write(Int(self.push_chat_limit))
        
        b.write(Int(self.saved_gifs_limit))
        
        b.write(Int(self.edit_time_limit))
        
        b.write(Int(self.revoke_time_limit))
        
        b.write(Int(self.revoke_pm_time_limit))
        
        b.write(Int(self.rating_e_decay))
        
        b.write(Int(self.stickers_recent_limit))
        
        b.write(Int(self.stickers_faved_limit))
        
        b.write(Int(self.channels_read_media_period))
        
        if self.tmp_sessions is not None:
            b.write(Int(self.tmp_sessions))
        
        b.write(Int(self.pinned_dialogs_count_max))
        
        b.write(Int(self.pinned_infolder_count_max))
        
        b.write(Int(self.call_receive_timeout_ms))
        
        b.write(Int(self.call_ring_timeout_ms))
        
        b.write(Int(self.call_connect_timeout_ms))
        
        b.write(Int(self.call_packet_timeout_ms))
        
        b.write(String(self.me_url_prefix))
        
        if self.autoupdate_url_prefix is not None:
            b.write(String(self.autoupdate_url_prefix))
        
        if self.gif_search_username is not None:
            b.write(String(self.gif_search_username))
        
        if self.venue_search_username is not None:
            b.write(String(self.venue_search_username))
        
        if self.img_search_username is not None:
            b.write(String(self.img_search_username))
        
        if self.static_maps_provider is not None:
            b.write(String(self.static_maps_provider))
        
        b.write(Int(self.caption_length_max))
        
        b.write(Int(self.message_length_max))
        
        b.write(Int(self.webfile_dc_id))
        
        if self.suggested_lang_code is not None:
            b.write(String(self.suggested_lang_code))
        
        if self.lang_pack_version is not None:
            b.write(Int(self.lang_pack_version))
        
        if self.base_lang_pack_version is not None:
            b.write(Int(self.base_lang_pack_version))
        
        return b.getvalue()
