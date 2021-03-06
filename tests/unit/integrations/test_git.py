import pytest
import os
import  shutil

from angreal.integrations.git import Git, GitException





def test_git_no_path():
    """
    test git object fails with no path
    """
    git = Git(git_path=None)


def test_git_bad_path():
    """
    test git object fails with bad path
    """
    with pytest.raises(OSError):
        git = Git(git_path='not git')

def test_git_bad_subcommand():
    """
    test that object fails with bad sub-command
    """

    git = Git()

    with pytest.raises(GitException):
        git.frombicate()


def test_git_initialization():
    """
    test git object initialization
    """
    os.mkdir('git_test')
    os.chdir('git_test')
    git = Git()
    git.init()
    assert os.path.isdir('.git')
    os.chdir('..')
    shutil.rmtree('git_test')


