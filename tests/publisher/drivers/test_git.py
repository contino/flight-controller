import subprocess
from unittest.mock import patch

from publisher.drivers.git import Git

GIT = Git()


@patch("subprocess.check_output")
def test_git_repo_name_returns_correct_type(mock_check_output):
    mock_check_output.return_value = b"/this/is/a/fake/repo"
    assert isinstance(GIT.get_repo_name(), str)


@patch("subprocess.check_output")
def test_git_repo_name_returns_correct_name(mock_check_output):
    mock_check_output.return_value = b"/this/is/a/fake/repo"
    assert GIT.get_repo_name() == "repo"


@patch("subprocess.check_output")
def test_git_repo_name_returns_exception_on_failed_command(mock_check_output):
    mock_check_output.side_effect = subprocess.CalledProcessError(1, "git rev-parse --show-toplevel")
    assert isinstance(GIT.get_repo_name(), Exception)


@patch.object(GIT, "_check_git_available")
def test_git_repo_name_returns_exception_when_git_unavailable(mock_check_git_available):
    mock_check_git_available.return_value = False
    assert isinstance(GIT.get_repo_name(), Exception)


@patch("subprocess.run")
def test_check_git_available_returns_true_when_git_available(mock_run):
    mock_run.return_value.returncode = 0
    assert GIT._check_git_available() == True


@patch("subprocess.run")
def test_check_git_available_returns_false_when_git_unavailable(mock_run):
    mock_run.return_value.returncode = 1
    assert GIT._check_git_available() == False
