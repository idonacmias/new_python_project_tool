import os
import sys


def create_venv(project_name):
	os.system(f'python3 -m virtualenv {os.path.join(project_name, "myenv")}')

def create_new_folder(project_name):
	project_path = os.path.join(os.getcwd(), project_name)
	os.mkdir(project_path)
	os.chdir(project_path)

def create_commen_fiels(project_name):
	file_name = 'README.txt' #os.path.join(project_name, 'README.txt')
	with open(file_name, 'a') as f:
		f.write(f'{project_name}')

	file_name = 'requirements.txt' #os.path.join(project_name, 'requirements.txt')
	with open(file_name, 'a') as f:
		f.close()


def git_init_to_push(project_name, url):
	cmds = ['git init',	
   		    'git add .',
		    'git commit . -m "first comment"',
		   f'git remote add origin {url}',
		    'git push -u origin main']
	
	for cmd in cmds:
   		os.system(cmd) 


if __name__ == '__main__':
	project_name = sys.argv[1]
	url = sys.argv[2]
	
	create_new_folder(project_name)

	create_venv(project_name)
	
	create_commen_fiels(project_name)
	
	git_init_to_push(project_name, url)	
	

