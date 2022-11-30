import os
import click

@click.command()
@click.option('--project_name', prompt='project name')
@click.option('--src', prompt='git repository link',
			help="conect new git reposetory buy open one in git hub and copy it here")
def open_project(project_name, src):
	create_new_folder(project_name)
	os.chdir(project_name)
	create_venv(project_name)
	create_commen_files(project_name)
	git_init_to_push(project_name, src)	

def create_venv(project_name):
	os.system(f'python3 -m virtualenv {os.path.join("myenv")}')

def create_new_folder(project_name):
	project_path = os.path.join(os.getcwd(), project_name)
	os.mkdir(project_path)

def create_commen_files(project_name):
	create_file('README.txt', project_name)
	create_file('requirements.txt')

def create_file(file_name, text=''):
	with open(file_name, 'a') as f:
		f.write(f'{text}')

def git_init_to_push(project_name, src):
	cmds = ['git init',	
   		    'git add .',
		    'git commit . -m "first comment"',
		   f'git remote add origin {src}',
		    'git push -u origin master']
	
	for cmd in cmds:
   		os.system(cmd) 

if __name__ == '__main__':
	open_project()
	