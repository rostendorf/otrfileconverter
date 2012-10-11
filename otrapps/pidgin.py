#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-

import os
import platform
import sys
import plistlib
import util

from otr_private_key import OtrPrivateKeys
from otr_fingerprints import OtrFingerprints

class PidginProperties():

    if platform.system() == 'Windows':
        path = os.path.expanduser('~/Application Data/.purple')
    else:
        path = os.path.expanduser('~/.purple')

    @staticmethod
    def parse(settingsdir=None):
        if settingsdir == None:
            settingsdir = PidginProperties.path

        kf = os.path.join(settingsdir, 'otr.private_key')
        if os.path.exists(kf):
            keydict = OtrPrivateKeys.parse(kf)
        else:
            keydict = dict()

        fpf = os.path.join(settingsdir, 'otr.fingerprints')
        if os.path.exists(fpf):
            util.merge_keydicts(keydict, OtrFingerprints.parse(fpf))

        return keydict

    @staticmethod
    def write(keys, savedir):
        pass

if __name__ == '__main__':

    import pprint

    print 'Pidgin stores its files in ' + PidginProperties.path

    if len(sys.argv) == 2:
        settingsdir = sys.argv[1]
    else:
        settingsdir = '../tests/pidgin'

    l = PidginProperties.parse(settingsdir)
    pprint.pprint(l)
