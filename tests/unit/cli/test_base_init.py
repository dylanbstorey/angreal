import os
import shutil
import sys

from angreal.cli.base_init import base_init

import unittest

from click.testing import CliRunner


class TestBaseInit(unittest.TestCase):

    def test_base_init(self):
        """
        test base init

        """

        original_dir = os.getcwd()
        os.chdir(os.path.join(os.path.dirname(__file__), '..'))

        runner = CliRunner()
        results = runner.invoke(base_init, ['fake-repo-pre', '--foo', 'baz', '--no-input'])

        try:
            assert results.exit_code == 0
        except Exception as e:
            print(results, file=sys.stderr)
            raise(e)

        os.chdir(os.path.join(os.path.dirname(__file__), '..'))
        shutil.rmtree('fake-project')

        os.chdir(original_dir)

        pass

    def test_print_nested_help(self):
        """
        test nested help
        """
        original_dir = os.getcwd()
        os.chdir(os.path.join(os.path.dirname(__file__), '..'))
        runner = CliRunner()
        results = runner.invoke(base_init, ['fake-repo-pre', '--help'])
        assert results.exit_code == 0

        os.chdir(original_dir)
