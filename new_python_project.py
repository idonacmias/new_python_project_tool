import os
from sys import platform 
import fire
from json import load

def open_project(project_name, requirements=[]):
	config = load_config()
	create_new_folder(project_name)
	os.chdir(project_name)
	create_venv()
	create_commen_files(project_name)
	git_init_to_push(project_name, config["git_user_name"]) 
	install_requirements(requirements)

def load_config():
	config_file_path = main_folder() + '/config.json' 
	if not os.path.isfile(config_file_path):
		create_config_file(config_file_path)

	with open(config_file_path, 'r') as f:
		config = load(f)

	return config

def main_folder():
	split_file = __file__.split('/')
	main_folder = '/'.join(split_file[:-1])
	return main_folder

def create_config_file(config_file_path):
	git_user_name = input('git user name:')
	text = f'{{"git_user_name" : "{git_user_name}"}}'
	
	print(text)
	create_file(config_file_path, text)

def create_venv():
	os.system(f'python3 -m virtualenv myenv')

def create_new_folder(project_name):
	project_path = os.path.join(os.getcwd(), project_name)
	os.mkdir(project_path)

def create_commen_files(project_name):
	create_file('README.md', project_name)
	create_file('requirements.txt')
	create_file('to_do_list.txt')

def create_file(file_name, text=''):
	with open(file_name, 'a') as f:
		f.write(f'{text}')


def generate_src(project_name, git_user_name):
	return f'git@github.com:{git_user_name}/{project_name}.git'

def git_init_to_push(project_name, git_user_name):
	src = generate_src(project_name, git_user_name)
	git_commends = ['git init', 
			'git add .',
			'git commit . -m "first comment"',
		   f'git remote add origin {src}',
			'git push -u origin master']
	join_and_execute_commend(git_commends)

def join_and_execute_commend(commends):
	new_commend = '&& '.join(commends)
	print(new_commend)
	os.system(new_commend)


def activate_venv_commend():
	if platform == 'darwin':  return '. myenv/bin/activate'
	elif platform == 'linux': return '. myenv/bin/activate'
	elif platform == 'win32': return 'myenv\scripts\activate'

def install_requirements(requirements):
	requirements_commends = [activate_venv_commend()]
	pip = generate_pip()
	for requirement in requirements:
		if is_file_in(requirement): commend = f'{pip} install -r {main_folder()}/requirements/{requirement}.txt'
		else: commend = f'{pip} install {requirement}'
		requirements_commends.append(commend)

	requirements_commends.extend([f'{pip} freeze > requirements.txt',
								   'cat requirements.txt',
								   'git commit requirements.txt -m "install requirements"',
								   'git push -u origin'])
	join_and_execute_commend(requirements_commends)

def is_file_in(requirement):
	requirement_path = f'{main_folder()}/requirements/{requirement}.txt'
	if os.path.exists(requirement_path): return True

def generate_pip():
	if platform == 'linux' or platform == 'darwin': return 'pip3'
	elif platform == 'win32': return 'pip'

if __name__ == '__main__':
	fire.Fire(open_project)
	
