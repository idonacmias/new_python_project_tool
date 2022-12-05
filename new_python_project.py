import os
# import click
from sys import platform #to defirate between linux and windows
import fire
from json import load

# @click.command()
# @click.option('-n', '--project_name')
# @click.option('--src', default='wwwwwwww', prompt='git repository link',
# 			help="conect new git reposetory by open one in github and copy it here")

def open_project(project_name, requirements=[]):
	config = load_config()
	create_new_folder(project_name)
	os.chdir(project_name)
	create_venv()
	create_commen_files(project_name)
	git_init_to_push(project_name, config["git_user_name"]) 
	install_requirements(requirements)

def load_config():
	config_file = main_folder() + '/config.json' 
	with open(config_file, 'r') as f:
		config = load(f)

	return config

def main_folder():
	split_file = __file__.split('/')
	main_folder = '/'.join(split_file[:-1])
	return main_folder

def create_venv():
	os.system(f'python3 -m virtualenv myenv')

def create_new_folder(project_name):
	project_path = os.path.join(os.getcwd(), project_name)
	os.mkdir(project_path)

def create_commen_files(project_name):
	create_file('README.txt', project_name)
	create_file('requirements.txt')

def create_file(file_name, text=''):
	with open(file_name, 'a') as f:
		f.write(f'{text}')


def generate_src(project_name, git_user_name):
	src = f'git@github.com:{git_user_name}/{project_name}.git'
	return src

def git_init_to_push(project_name, git_user_name):
	src = generate_src(project_name, git_user_name)
	git_commends = ['git init', 
			'git add .',
			'git commit . -m "first comment"',
		   f'git remote add origin {src}',
			'git push -u origin master']
	join_comends(git_commends)

def join_comends(commends):
	new_commend = '&& '.join(commends)
	print(f'new_commend: {new_commend}')
	os.system(new_commend)


def activate_venv_commend():
	#work on linux only
	return '. myenv/bin/activate'

def install_requirements(requirements):
	requirements_commends = [activate_venv_commend()]
	pip = generate_pip()
	for requirement in requirements:
		if is_file_in(requirement):
			requirements_commends.append(f'{pip} install -r {main_folder()}/requirements/{requirement}.txt')

		else:	
			
			requirements_commends.append(f'{pip} install {requirement}')
		
	requirements_commends.extend([f'{pip} freeze > requirements.txt',
								   'git commit requirements.txt -m "install requirements"',
								   'git push -u origin'])
	join_comends(requirements_commends)

def is_file_in(requirement):
	requirement_path = f'{main_folder()}/requirements/{requirement}.txt'
	if os.path.exists(requirement_path):
		return True

def generate_pip():
	if platform == 'linux':
		return 'pip3'

	else:
		return 'pip'

if __name__ == '__main__':
	fire.Fire(open_project)
	