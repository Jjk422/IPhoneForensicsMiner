import sqlite3
import Constants


class IphoneFileDatabase:
    """
    IPhone File Database class.
    Manages the main storage database for file storage.
    Also parses and reads the manifest.db file in the IPhone backup to get file contents stored within the IPhone.
    """
    def __init__(self, iphone_backup_path, iPhone_backup_object_id):
        """
        Initialization method, initialize all required values and databases for the database.
        :param iphone_backup_path: Path to the iphone backup path directory.
        :param iPhone_backup_object_id: Backup id for the iphone object (used in naming the databases to ensure database collisions do not happen).
        .. warnings also:: Ensure that the iPhone_backup_object_id is always unique, this is not currently done automatically and could lead to overwriting an existing database file if multiple databases are being used..
        """
        self.iphone_backup_object_id = iPhone_backup_object_id

        self.manifest_db_database_file_path = f"{iphone_backup_path}\{Constants.IPHONE_BACKUP_MANIFEST_DATABASE_FILE_NAME}"
        self.manifest_db_database_connection = sqlite3.connect(self.manifest_db_database_file_path)
        self.manifest_db_database_cursor = self.manifest_db_database_connection.cursor()
        self.manifest_db_table_name = Constants.IPHONE_BACKUP_MANIFEST_TABLE_NAME

        self.file_database_file_path = f"{Constants.DEFAULT_SQLITE_OUTPUT_PATH}_{iPhone_backup_object_id}.db"
        self.file_database_connection = sqlite3.connect(self.file_database_file_path)
        self.file_database_cursor = self.file_database_connection.cursor()
        self.file_database_table_name = f"iPhone_database_{self.iphone_backup_object_id}"

        self.initialize_file_database()

    def initialize_file_database(self):
        """
        Initialize the file database (used for storing information about the files within the machine).
        """
        # TODO: Change the string formatting, insecure method of assignment
        sql_command = f"DROP TABLE IF EXISTS {self.file_database_table_name}"
        self.file_database_cursor.execute(sql_command)

        sql_command = f'''CREATE TABLE {self.file_database_table_name} {Constants.DEFAULT_SQL_STORAGE_COLUMNS}'''
        self.file_database_cursor.execute(sql_command)

        self.file_database_connection.commit()

    def separate_data(self, information_dictionary):
        """
        Separates the inputted dictionary into two arrays of the keys and values.
        :param information_dictionary: Information dictionary to split to key value arrays.
        :return: False, False if failed otherwise two seperate arrays of keys and values.
        """
        if isinstance(information_dictionary, dict):
            columns = []
            values = []

            for key, value in information_dictionary.items():
                columns.append(key)
                values.append(f"'{value}'")

            column_string = ", ".join(columns)
            value_string = ", ".join(values)

            return column_string, value_string
        else:
            return False, False

    def insert_table_row(self, information_dictionary_to_add):
        """
        Inserts a row into the main database for the object.
        :param information_dictionary_to_add: Information dictionary containing information on the new row to add to the main object database.
        """
        column_string, value_string = self.separate_data(information_dictionary_to_add)

        if (column_string != False) or (value_string != False):
            sql_command = f"INSERT INTO {self.file_database_table_name} ({column_string}) VALUES ({value_string});"
            self.file_database_cursor.execute(sql_command)

    def change_table_row(self, information_dictionary_to_change):
        """
        Change/update a row in the table.
        :param information_dictionary_to_change: Dictionary containing information to change within the database.
        """
        # TODO: More rigourous testing needs to be done of this method.

        update_key_value_array = []
        for update_information_key, update_information_value in information_dictionary_to_change.items():
            update_key_value_array.append(f"{update_information_key} = {update_information_value}")

        sql_command = f"UPDATE {self.file_database_table_name} SET {','.join(update_key_value_array)};"
        self.file_database_cursor.execute(sql_command)

    def get_manifest_db(self):
        """
        Get all information within the manifest.db file within the iphone backup in the form of rows.
        :return: Return the rows from the manifest.db file within the iphone backup.
        """
        try:
            database_rows = []
            sql_command = f"SELECT * FROM {self.manifest_db_table_name}"
            for row in self.manifest_db_database_cursor.execute(sql_command):
                database_rows.append(row)

            return database_rows
        except:
            print(f"Database file {self.manifest_db_database_file_path} could not be opened, check if it is encrypted.")
            return False

    def get_iminer_file_database(self):
        """
        Return all information within the main file storage database for the object in the form of rows.
        :return: Return the rows from the main storage database.
        """
        database_rows = []
        sql_command = f"SELECT * FROM {self.file_database_table_name}"
        for row in self.file_database_cursor.execute(sql_command):
            database_rows.append(row)

        return database_rows

    def commit_database_changes(self):
        """
        Commit all previous database changes to the main file storage database.
        """
        self.file_database_connection.commit()

    def close_file_database(self):
        """
        Close the file storage database.
        """
        self.file_database_connection.close()

    def close_manifest_database(self):
        """
        Close the manifest.db database.
        :rtype: Void
        """
        self.manifest_db_database_connection.close()

    def close_databases(self):
        """
        Close all databases (manifest.db and main file storage database).
        :rtype: Void
        """
        self.close_file_database()
        self.close_manifest_database()

    # TODO: Remove or use unused methods
    # def delete_database(self, table_name):
    #     sql_command = f"DROP TABLE {table_name};"
    #     self.file_database_cursor.execute(sql_command)
    #
    # def print_manifest_db(self):
    #     sql_command = f"SELECT * FROM {self.manifest_db_table_name}"
    #     for row in self.manifest_db_database_cursor.execute(sql_command):
    #         print(row)
    #
    # def print_iminer_file_database(self):
    #     sql_command = f"SELECT * FROM {self.file_database_table_name}"
    #     for row in self.file_database_cursor.execute(sql_command):
    #         print(row)
    #
    # def print_manifest_tables(self):
    #     self.manifest_db_database_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    #     tables = self.manifest_db_database_cursor.fetchall()
    #
    #     for table in tables:
    #         print(f"Table: {table}")
    #
    # def print_iminer_file_database_tables(self):
    #     self.file_database_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    #     tables = self.file_database_cursor.fetchall()
    #
    #     for table in tables:
    #         print(f"Table: {table}")