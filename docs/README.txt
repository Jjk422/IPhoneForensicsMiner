To generate documentation use the following commands
cd {Project_location}\docs
sphinx-apidoc -o source ../
make html

OR

cd {Project_location}\docs
sphinx-apidoc -o source ../ && make html