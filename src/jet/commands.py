import subprocess
import os


class Commands:

    def __init__(self, test_path):
        self.git = None
        self.repo_base_path = test_path

    def commit(self):
        pass

    def commit_uncommitted(self):
        result = subprocess.call(['git', 'diff', '--check', self.repo_base_path])
        print(result)

    def resolve_conflicts(self):
        pass

    def init_repo(self):
        pass

    def get_repo_status(self):
        result = subprocess.call(['git', 'status', self.repo_base_path])
        print(result)
        if result == 0:
            return True
        else:
            return False

    def get_current_branch(self):
        result = subprocess.check_output(['git', 'branch', '--show-current'])
        s = ''.join(map(chr, result))
        return s

    def checkout_main(self):
        args = ['git', 'checkout', '-b', 'origin/main']
        try:
            result = subprocess.check_output(args)
            print(result)
        except Exception:
            print("dunno what exception")
    def checkout_jet(self):
        jet_name = "jet-" + self.get_current_branch()
        args = ['git', 'checkout', '-b', jet_name]
        result = subprocess.check_output(args)



#test = Commands(f'/home/gaburierus/a04nov/people')
#test = Commands(f'/home/gaburierus/a04nov/roman-matthijs')
test = Commands(os.getcwd())
#assert test.get_repo_status() is True
#test.commit_uncommitted()
test.checkout_main()



