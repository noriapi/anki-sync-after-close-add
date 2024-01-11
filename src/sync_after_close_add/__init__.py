# SPDX-FileCopyrightText: 2024-present noriapi <70106808+noriapi@users.noreply.github.com>
#
# SPDX-License-Identifier: MIT

import aqt
import aqt.main
from aqt.addcards import AddCards


class AddCardsWithSyncHook(AddCards):
    def _close(self) -> None:
        super()._close()
        self.mw.on_sync_button_clicked()


def register():
    aqt.dialogs.register_dialog("AddCards", AddCardsWithSyncHook)


def main():
    register()


main()
