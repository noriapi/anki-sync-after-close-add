# SPDX-FileCopyrightText: 2024-present noriapi <70106808+noriapi@users.noreply.github.com>
#
# SPDX-License-Identifier: MIT

import aqt
import aqt.main
from aqt import addcards
from aqt.qt import qconnect


def add_cards_dialog() -> addcards.AddCards:
    [
        d,
    ] = aqt.dialogs._dialogs["AddCards"]

    if not isinstance(d, addcards.AddCards):
        raise Exception("AddCards dialog not found")

    return d


def connect_add_cards_dialog(mw: aqt.main.AnkiQt):
    d = add_cards_dialog()
    qconnect(d.closeButton.clicked, mw.on_sync_button_clicked)


def main():
    from aqt import mw

    assert mw is not None
    connect_add_cards_dialog(mw)


main()
