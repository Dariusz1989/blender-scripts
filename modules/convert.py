import bpy
import os
import sys
import shutil
import tempfile
import subprocess


if sys.platform.startswith('linux'):
    MAGICK_BIN = 'magick'
elif sys.platform.startswith('win'):
    MAGICK_BIN = 'magick.exe'


def sequence_to_gif(inputs, output, fps=15, optimize=True, depth=8):
    ''' Convert image sequence to gif
    inputs can be folder or list of image path'''

    if isinstance(inputs, str):
        if os.path.isdir(inputs):
            inputs = [os.path.join(inputs, i) for i in os.listdir(inputs)]
            inputs.sort()

    fps = '1x{}'.format(fps)
    command = [
        MAGICK_BIN,
        '-delay', fps,
        '-loop', '0']
    command.extend(inputs)
    if optimize:
        command.extend(['-layers', 'optimize'])
    if depth:
        command.extend(['-depth', str(depth)])
    command.append(output)
    subprocess.call(command)
