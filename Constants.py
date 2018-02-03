import re

# Iphone file names
PLIST_FILE_INFO_NAME = 'Info.plist'
"""
Info.plist file name
"""
PLIST_FILE_MANIFEST_NAME = 'Manifest.plist'
"""
Manifest.plist file name
"""
PLIST_FILE_STATUS_NAME = 'Status.plist'
"""
Status.plist file name
"""

# Sqlite 3 defaults
DEFAULT_SQLITE_OUTPUT_PATH = 'iPhone_database_'
"""
Default Sqlite 3 output path template
"""
IPHONE_BACKUP_MANIFEST_DATABASE_FILE_NAME = 'Manifest.db'
"""
Iphone manifest.db file name (no need to change unless changes are made to the IOS database structure)
"""
IPHONE_BACKUP_MANIFEST_TABLE_NAME = 'Files'
"""
Iphone manifest.db table name (no need to change unless changes are made to the IOS database structure)
"""

# Ordering of Columns list is as follows: file_ID, domain, relative_Path, flags, file, file_Type, absolute_Path
# TODO: Make order of list not matter
# DEFAULT_SQL_STORAGE_COLUMNS_LIST_FORM = DEFAULT_SQL_STORAGE_COLUMNS.strip('(').strip(')').split(',')
DEFAULT_SQL_STORAGE_COLUMNS_LIST_FORM = ['file_ID', 'domain', 'relative_Path', 'flags', 'absolute_Path', 'file_Type', 'file']
"""
Default storage columns for the main storage database (in list form)
"""
# TODO: Make this string dependent on the list form version (DEFAULT_SQL_STORAGE_COLUMNS_LIST_FORM)
# DEFAULT_SQL_STORAGE_COLUMNS = f"'({','.join(DEFAULT_SQL_STORAGE_COLUMNS_LIST_FORM)})'"
DEFAULT_SQL_STORAGE_COLUMNS = '(file_ID, domain, relative_Path, flags, absolute_Path, file_Type, file)'
"""
Default storage columns for the main storage database (in string form with formatting)
"""

# Default file output paths
DEFAULT_XML_OUTPUT_PATH = 'xml_output.xml'
"""
Default filename/path for the xml output files
"""
DEFAULT_TXT_OUTPUT_PATH = 'txt_output.txt'
"""
Default filename/path for the txt output files
"""

# Formatting
# TODO: Change this variable to allow for dynamic column scaling
# COLUMN_WIDTH = 25
COLUMN_WIDTH = 75
"""
Column width of columns to be used for formatting to txt files or stdout
"""
# COLUMN_FILLER_CHARACTER = '-'
COLUMN_FILLER_CHARACTER = ' '
"""
Filler character to use for column formatting (Usually ' ' or '-')
"""
XML_IGNORE_CHARACTER_STRING = 'IMINER-TAG-IGNORE--'
"""
XML tag appending string if the tag begins with an illegal character (a number or punctuation)
"""
REGEX_CAMEL_CASE_SEARCH_EXPRESSION = re.compile("(?!^)([A-Z]+)")
"""
Regular expression to check for CamelCase characters other then first letter (used for conversion to snake_case)
"""

# IPhone backup file paths
## Paired Devices
PAIRED_BLUETOOTH_DEVICES_DB_TABLE = 'PairedDevices'
"""
Default sqlite database table name for the paired devices database
"""
PAIRED_BLUETOOTH_DEVICES_DB_PATH = 'Library/Database/com.apple.MobileBluetooth.ledevices.paired.db'
"""
Default relative path in the IOS file system of the database file
"""