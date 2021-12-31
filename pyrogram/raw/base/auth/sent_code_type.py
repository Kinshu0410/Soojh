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

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

SentCodeType = Union[raw.types.auth.SentCodeTypeApp, raw.types.auth.SentCodeTypeCall, raw.types.auth.SentCodeTypeFlashCall, raw.types.auth.SentCodeTypeMissedCall, raw.types.auth.SentCodeTypeSms]


# noinspection PyRedeclaration
class SentCodeType:  # type: ignore
    """This base type has 5 constructors available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`auth.SentCodeTypeApp <pyrogram.raw.types.auth.SentCodeTypeApp>`
            - :obj:`auth.SentCodeTypeCall <pyrogram.raw.types.auth.SentCodeTypeCall>`
            - :obj:`auth.SentCodeTypeFlashCall <pyrogram.raw.types.auth.SentCodeTypeFlashCall>`
            - :obj:`auth.SentCodeTypeMissedCall <pyrogram.raw.types.auth.SentCodeTypeMissedCall>`
            - :obj:`auth.SentCodeTypeSms <pyrogram.raw.types.auth.SentCodeTypeSms>`
    """

    QUALNAME = "pyrogram.raw.base.auth.SentCodeType"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/sent-code-type")
