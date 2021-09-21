#! /home/polymath/.pyenv/shims/python

class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = []
        li = path.split("/")
        for p in li:
            if not p or p == '.':
                continue
            elif p == '..':
                if directories:
                    directories.pop()
            else:
                directories.append(p)
        
        return "/"+"/".join(directories)