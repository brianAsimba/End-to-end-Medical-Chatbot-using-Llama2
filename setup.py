# Since we gave created so many files inside the folder, if we want to import something  from heloer.py

'''
if we want to import it inside app.py, we need to write from src.helper import function_name
for this kinds of operations we need to create set up the src as my local package.
The src is not in the pip list, packages fom the pypi website, to import somrhing from src we 
need to tell python that this is our local package by creating setup.py file.
'''

from setuptools import find_packages, setup     

setup(
    name="medical_chatbot",   #name of the package
    version="0.0.0",          #version of the package
    author="Brian Asimba",       #author name
    author_email="briano377@gmail.com",
    packages=find_packages(),  #find all the packages inside the src folder
    install_requires=[],    #list of dependencies
    license="MIT",            #license type
    description="An end-to-end medical chatbot using Llama2 and Langchain", #description about the package
    
)

'''
When we call the find_packages, it will look at the constructor file, __init__.py inside the src folder 
and it will treat the src as a package, as my local package
'''

