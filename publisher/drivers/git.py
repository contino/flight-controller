import subprocess
from typing import Union


class Git():
    def _check_git_available(self) -> bool:
        return subprocess.run(['git', '--version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0

    def get_repo_name(self) -> Union[Exception, str]:
        if self._check_git_available() == True:
            try:
                repo_name = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], stderr=subprocess.DEVNULL).strip().decode('utf-8').split('/')[-1]
                return repo_name
            except Exception as err:
                return err
        else:
            return Exception("Git not available")
