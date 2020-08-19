import os
import re

file_name = input("What is the Python file's name (with extension)?  ")
#file_name = "right_triangle_trig.py"

code = os.popen("type " + file_name).read()

pattern = re.compile(r'def\s.*')

matches = pattern.findall(code)

file_name = file_name[0:-3]
new_code = f"import {file_name}\nimport unittest\n\nclass Test{file_name.capitalize()}" + "(unittest.TestCase):"

functions = []
for match in matches:
    match = re.sub("\(.*", "", match)
    functions.append(match[4:])

for function in functions:
    new_code += f"\n    \n    def test_{function}(self):\n        self.assertEqual({file_name}.{function}(,)"

new_code += "\n\n\nif __name__ == '__main__':\n    unittest.main()\n"

with open(f"test_{file_name}.py","w+") as f:
    f.write(new_code)
