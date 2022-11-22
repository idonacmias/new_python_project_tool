import os
import sys
from pathlib import path 

def create_venv():
	os.system('python3 -m virtualenv myenv')

def create_new_folder(folder_name):
	os.mkdir(os.path.join(os.getcwd(), folder_name))

def create_commen_fiels(project_name):
	with open('README.txt', 'a') as f:
		f.write(f'{project_name}')

	with open('requirements.txt', 'a') as f:
		pass


def git_init_to_push(project_name, shh):
	cmds = ['git init',	
		   'git add .',
		   'git commit . -m "first comment"',
	       'git branch -M main',
		  f'git remote add origin {ssh}',
		   'git push -u origin main']
   	for cmd in cmds:
   		os.system(cmd) 

if __name__ == '__main__':
	print('new_python_project')
	project_name = sys.argv[1]
	ssh = sys.argv[2]
	
	create_venv()

	create_new_folder(project_name)
	
	create_commen_fiels(project_name)
	
	git_init_to_push(project_name, ssh)	
	

