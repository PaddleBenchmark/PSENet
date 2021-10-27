import sys
import os
import subprocess

python_path = sys.executable

ori_path = os.getcwd()
os.chdir('models/post_processing/pse')
if subprocess.call(
        '{} setup.py build_ext --inplace'.format(python_path), shell=True) != 0:
    raise RuntimeError('Cannot compile pse: {}'.format(
        os.path.dirname(os.path.realpath(__file__))))
os.chdir(ori_path)

from .pse import pse