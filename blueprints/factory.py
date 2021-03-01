#!/usr/bin/env python
## -*- coding: utf-8 -*-

import base64
import zlib

class BluePrintFactory(object):

    def decode(self, raw_str):
        blueprint_script = raw_str[1:]
        base64_decoded_str = base64.b64decode(blueprint_script)
        inflated_str = zlib.decompress(base64_decoded_str)
        return inflated_str

    def encode(self, json_str):
        deflated_str = zlib.compress(json_str)
        base64_encoded_str = base64.b64encode(deflated_str)
        result = '0' + base64_encoded_str
        return result
