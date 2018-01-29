# iPhoneInformationGatherer
## What is it
Small tool that gathers data from iphone backups.  
Currently does not analyse file contents (photos and other documents on IPhone) but this is planned to be added in soon.

## How to
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

## Future plans
Some of the plans for this project in the near future are:
- Allow for auto-backup and analysis of IPhones
- Allow for database containing all files and file metadata