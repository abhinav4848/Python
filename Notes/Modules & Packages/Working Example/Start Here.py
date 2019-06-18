from my_module import my_func
# the current folder has a my_module.py file which has function my_func()

from mainPackage import mainscript
# mainPackage is the folder inside which mainscript.py is a file which has a function main_script()

from mainPackage.subPackage import subscript
# mainPackage has a subfolder called subPackage which has subscript.py which has function sub_script()

my_func()
# outputs "Hey, i am in my_module.py"

mainscript.main_script()
# outputs "Hey, i'm a function in mainPackage"

subscript.sub_script()
# outputs "Hey, i'm a function in subPackage"
