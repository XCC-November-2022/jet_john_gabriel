import logging
import subprocess

logger = logging.getLogger('jet')

def Merge_Error():
    ...

class Branch:
    ...

class Git:

    def fetch(self):
        self.cmd_run(['fetch'])

    def get_current_branch(self):
        cur_branch = self.cmd_run(['branch', '--show-current'])
        return cur_branch

    def checkout(self, name: Branch, new_branch = False):
        logger.debug('checkout', branch_name = name, new_branch = new_branch)
        if new_branch:
            self.cmd_run(['checkout', '-b'] + name)
        else:
            self.cmd_run('checkout')

    def cmd_run(self, cmd):
        process = subprocess.run(
            ['git'] + cmd,
        )
        try:
            out = process.communicate(timeout=15)
        except subprocess.TimeoutExpired:
            process.kill()
            out = process.communicate()

        if (process.returncode < 0):
            raise subprocess.CalledProcessError
        
        return out

    def merge_conflict(self, branch_name: Branch):
        current_branch = self.get_current_branch()
        try:
            self.cmd_run(['merge', branch_name])
            logger.debug('Checking merge', branch = branch_name, to = current_branch)

        except subprocess.CalledProcessError as e:
            logger.debug('Merge failed', branch = branch_name, to = current_branch, error = e)
            self.cmd_run(['merge', '--abort'])
            raise Merge_Error

        except Exception as e:
            logger.debug('Nani..?', error = e)
        
        logger.debug('Merge commit', branch = branch_name, to = current_branch)
        self.cmd_run(['commit', '-m', f'Jet merged {branch_name} to {current_branch}'])