# iPhoneInformationGatherer
## What is it
Small tool that gathers data from iphone backups.  
Currently does not analyse all file contents (photos and other documents on IPhone) but this is planned to be added in soon.

## How to
### Required programs
Python 3: https://www.python.org/downloads/

### Installation
Download the newest release from the main GitHub repository  
Via Git  
_git clone https://github.com/Jjk422/IPhoneForensicsMiner.git_  
OR  
_Download the .zip file from [GitHub repository](https://github.com/Jjk422/IPhoneForensicsMiner)_  

### Basic usage:
Basic command:  
_iminer.py backup_paths [backup_paths ...]_  

Help:  
_iminer.py -h_

### Optional arguments:  
TXT output file:
_iminer.py --txt_output_file_    
_iminer.py --txt_output_file --txt_output_path [txt_output_path]_

XML output file:  
_iminer.py --xml_output_file_  
_iminer.py --xml_output_file --xml_output_path [xml_output_path]_

Minimal stdout (Useful with output file options):  
_iminer.py --min_std_out_

### Developer documentation
The development documentation can be built via Sphinx  
[Install Sphinx via system repository or pip](http://www.sphinx-doc.org/en/stable/install.html)

Open a terminal and change directory to the docs directory
_cd {Project_location}\docs_

Generate rst source files using sphinx-apidoc  
_sphinx-apidoc -o source ../_

Generate html documentation using make  
_make html_

The built development documentation will be in the new docs/build/html directory, open the index.html file in a web browser to view the documentation.

## Future plans
Some of the plans for this project in the near future are:
- Allow for auto-backup and analysis of IPhones
- Allow for database containing all files and file metadata