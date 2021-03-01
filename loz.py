#!/usr/bin/env python
## -*- coding: utf-8 -*-

import os
import sys

from blueprints.factory import BluePrintFactory

if __name__ == '__main__':
    factory = BluePrintFactory()
    with open('in.txt', 'r') as f:
        content = f.read()

    result = factory.decode(content)

    with open('out.json', 'w') as f:
        f.write(result)

    blueprint_encode = factory.encode(result)
    with open('rein.txt', 'w') as f:
        f.write(blueprint_encode)