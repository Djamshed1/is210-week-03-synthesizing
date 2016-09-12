#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

FIRSTPART = 'Spanish'
SECONDPART = 'Flemish'
STRING_LENGH = len(FIRSTPART)
INDEXED = inquisition.SPANISH.index(FIRSTPART)
REMOVE = INDEXED + STRING_LENGH
BEFORE = inquisition.SPANISH[:INDEXED]
AFTER = inquisition.SPANISH[REMOVE:]

FLEMISH = BEFORE + SECONDPART + AFTER
