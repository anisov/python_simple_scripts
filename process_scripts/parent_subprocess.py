import subprocess
import sys
import os


child = os.path.join(os.path.dirname(__file__), 'child_subprocess.py')
text = 'Hello World'

pipes = []
for i in range(10):
    command = [sys.executable, child]
    pipe = subprocess.Popen(command, stdin=subprocess.PIPE)
    pipes.append(pipe)
    pipe.stdin.write(text.encode('utf-8')+b'\n')
    pipe.stdin.close()

while pipes:
    pipe = pipes.pop()
    pipe.wait()

