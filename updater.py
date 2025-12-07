#MIT License

#Copyright (c) 2024 deleted-account

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import asyncio
import difflib
import shlex
import sys

from typing import Tuple

async def lines_differnce(file1, file2):
    with open(file1) as f1:
        lines1 = f1.readlines()
        lines1 = [line.rstrip("\n") for line in lines1]
    with open(file2) as f2:
        lines2 = f2.readlines()
        lines2 = [line.rstrip("\n") for line in lines2]
    diff = difflib.unified_diff(
        lines1, lines2, fromfile=file1, tofile=file2, lineterm="", n=0
    )
    lines = list(diff)[2:]
    added = [line[1:] for line in lines if line[0] == "+"]
    removed = [line[1:] for line in lines if line[0] == "-"]
    additions = [i for i in added if i not in removed]
    removedt = [i for i in removed if i not in added]
    return additions, removedt


async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )


async def update_requirements(main , test):
    a, r = await lines_differnce(main, test)
    try:
        for i in a:
            await runcmd(f"pip install {i}")
            print(f"Succesfully installed {i}")
    except Exception as e:
        print(f"Error installing requirments {str(e)}")


asyncio.run(update_requirements(sys.argv[1] , sys.argv[2]))
