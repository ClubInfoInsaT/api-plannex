#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             :
# Date created       :
# Date last modified :
# Python Version     : 3.*

from lib import PlannexAPI
import datetime
import json

if __name__ == '__main__':
    p = PlannexAPI()
    liste_cours = p.retreive(
        p.groups['GEI']['4IR_I_A1'],     # Classe de cours
        datetime.datetime(2020, 11, 8), # Date de début
        datetime.datetime(2020, 11, 13)  # Date de fin
    )

    for cours in liste_cours:
        print('[>]', cours['start'].strftime('Le %d %h de %Hh%M') + cours['end'].strftime(' à %Hh%M'),' | ',cours['title'])
