#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
"""
Programme ou module pour ...

Créé le Fri Nov 26 15:36:57 2021

@author: ejetzer
"""

import datetime

import sqlalchemy as sqla

from sqlalchemy import Column, MetaData, Table
from sqlalchemy.orm import declarative_base

from ..outils.database.dtypes import get_type, column

metadata = MetaData()

def colonnes_communes():
    return (column('index', int, primary_key=True),)

cols = colonnes_communes() + (column('Technicien', str),
                              column('Payeur', str),
                              column('Date', datetime.datetime),
                              column('Description des travaux effectués', str),
                              column('Demandeur', str),
                              column('Heures', float),
                              column('Atelier', bool),
                              column('Précision si pour département', str),
                              column('Autres', str))
cols_admin = cols + (column('Facturé', bool),)

heures = Table('heures', metadata, *cols)
#admin = Table('admin', metadata, *cols_admin)
