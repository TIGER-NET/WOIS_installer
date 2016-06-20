import unittest
import os
import shutil

import installer_utils


class TestInstallerUtils(unittest.TestCase):

    def test_modify_ram(self):

        datadir = os.path.join(
                os.path.dirname(__file__), 'data')

        batfile = os.path.join(datadir, 'gpt.bat')
        vmoptionsfile = os.path.join(datadir, 'gpt.vmoptions')

        all_worked = []
        for fname in [batfile, vmoptionsfile]:

            root, base = os.path.split(fname)
            tempcopy = os.path.join(root, 'copy_of_' + base)
            shutil.copyfile(fname, tempcopy)
            print(tempcopy)
            assert os.path.isfile(tempcopy)

            try:
                installer_utils.modifyRamInBatFiles(tempcopy, 0.0)

                worked = False
                with open(tempcopy, 'r') as f:
                    for line in f:
                        if '-Xmx0' in line:
                            worked = True
                all_worked.append(worked)
            finally:
                os.remove(tempcopy)
                os.remove(tempcopy + '.backup')

        self.assertTrue(all(all_worked))

