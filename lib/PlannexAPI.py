#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             :
# Date created       :
# Date last modified :
# Python Version     : 3.*

import datetime
import json
import requests
import urllib

class PlannexAPI(object):
    """
    Documentation of PlannexAPI Python API
    """

    def __init__(self):
        super(PlannexAPI, self).__init__()
        raw_data = json.loads(requests.get('http://planex.insa-toulouse.fr/wsAdeGrp.php?projectId=6').content.decode('UTF-8'))
        self.entities = { raw_data[ent_id]['name'] : ent_id for ent_id in raw_data }
        self.groups = {
            raw_data[ent_id]['name'] : {
                element['name'] : element['id']
                for element in raw_data[ent_id]['content']
            }
            for ent_id in raw_data
        }

    def retreive(self, group_id:int, begin_date, end_date):
        """
        Documentation of retreive

        """
        req_timestamp = datetime.datetime.now()
        params = {
            'id'    : str(int(group_id)),
            'start' : begin_date.strftime('%Y-%m-%dT%H:%M:%S'),
            'end'   : end_date.strftime('%Y-%m-%dT%H:%M:%S'),
            '_'     : req_timestamp.strftime('%s')+req_timestamp.strftime('%f')[3:].rjust(3,'0')
        }
        link  = "http://planex.insa-toulouse.fr/wsAde.php?"
        link += '&'.join([p + '=' + urllib.parse.quote(params[p]) for p in params])
        raw_data = requests.get(link)
        results  = json.loads(raw_data.content.decode('UTF-8'))
        final    = []
        for r in results:
            r['start'] = datetime.datetime.strptime(r['start'], "%Y%m%dT%H%M%S")
            r['end']   = datetime.datetime.strptime(r['end'], "%Y%m%dT%H%M%S")
            final.append(r)
        return final

    def get_groups(self):
        """
        Documentation for get_groups
        Returns list of availble groups
        """
        return [c for c in self.groups.keys()]

    def get_groups(self, group):
        """
        Documentation for get_groups
        Returns list of availble classes of a specified group
        """
        return [c for c in self.groups[group].keys()]
