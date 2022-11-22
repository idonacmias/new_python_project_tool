import os
import sys


def create_venv():
	os.system('python3 -m virtualenv myenv')
	# os.system('source myenv/bin/activate') #cant source from python3 code?	

def create_new_folder(folder_name):
	os.mkdir(os.getcwd() + f'/{folder_name}')

def create_commen_fiels(project_name):
	with open('README.txt', 'a') as f:
		f.write(f'{project_name}')
		f.close()

	with open('requirements.txt', 'a') as f:
		f.close()



def git_init_to_push(project_name, git_rep):
	os.system('git init')	
	os.system('git add .')
	os.system('git status')
	os.system('git commit . -m "first comment"')
	os.system('git status')
	os.system('git branch -M main')
	os.system(f'git remote add origin {git_rep}')
	os.system('git push -u origin main')


if __name__ == '__main__':
	print('new_python_project')
	project_name = sys.argv[1]
	ssh = sys.argv[2]
	
	create_venv()

	create_new_folder(project_name)
	
	create_commen_fiels(project_name)
	
	git_init_to_push(project_name, ssh)	
	

"click"