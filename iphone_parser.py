# * Retrieves information from 3 files (info.plist, manifest.plist, status.plist)
# - info.plist
# Last Backup Date
# MEID
# Phone Number
# Product Name
# Product Type
# Product Version
# Serial Number
# Target Identifier
# Target Type
# Unique Identifier
# iBooks Data 2
# iTunes Files
# iTunes Settings
# iTunes Version
#
# - manifest.plist
# BackupKeyBag
# Version
# Date
# SystemDomainsVersion
# WasPasscodeSet
# Lockdown
# Applications
# IsEncrypted
#
# - status.plist
# IsFullBackup
# Version
# UUID
# Date
# BackupState
# SnapshotState

# Initiation Method
class IPhoneParser:
    """
       Parse and manage Iphone backup information.
    """
    def __init__(self, parsed_info_file, parsed_manifest_file, parsed_status_file):
        """
           Initiation method, initialised the given Iphone files and stores a dictionary in storage master
        """
        self.parsed_info_file = parsed_info_file
        self.parsed_manifest_file = parsed_manifest_file
        self.parsed_status_file = parsed_status_file
        self.storage_master = {}

    # - info.plist
    def get_iphone_non_installed_applications(self):
        """
        Return non installed applications from the IPhone
        """
        applications = []
        for application in self.parsed_info_file['Applications']:
            application_array = application.split('.')
            applications.append({
                'name': ''.join(application_array[2:]),
                'company': application_array[1],
                'domain': application_array[0]
            })
        return applications

    def get_iphone_installed_applications(self):
        """
        Return installed applications from the IPhone
        """
        applications = []
        for application in self.parsed_info_file['Installed Applications']:
            application_array = application.split('.')

            test1 = len(application_array[0]) == 2
            test2 = len(application_array[1]) == 2

            if len(application_array[0]) == 2 and len(application_array[1]) == 2:
                applications.append({
                    'name': ''.join(application_array[3:]),
                    'company': application_array[2],
                    'domain': f"{application_array[1]}.{application_array[0]}"
                })
            else:
                applications.append({
                    'name': ''.join(application_array[2:]),
                    'company': application_array[1],
                    'domain': application_array[0]
                })
        return applications

    def get_iphone_build_version(self):
        """
        Return the IPhone build version
        """
        return self.parsed_info_file['Build Version']

    def get_iphone_device_name(self):
        """
        Return the IPhone device name
        """
        return self.parsed_info_file['Device Name']

    def get_iphone_display_name(self):
        """
        Return the IPhone display name
        """
        return self.parsed_info_file['Display Name']

    def get_iphone_GUID(self):
        """
        Return the IPhone GUID
        """
        return self.parsed_info_file['GUID']

    def get_iphone_ICCID(self):
        """
        Return the IPhone ICCID
        """
        return self.parsed_info_file['ICCID']

    def get_iphone_IMEI(self):
        """
        Return the IPhone IMEI
        """
        return self.parsed_info_file['IMEI']

    def get_iphone_last_backup_date(self):
        """
        Return the IPhone last backup date
        """
        return self.parsed_info_file['Last Backup Date']

    def get_iphone_MEID(self):
        """
        Return the IPhone MEID if available
        """
        return self.parsed_info_file['MEID'] if 'MEID' in self.parsed_info_file else ''

    def get_iphone_phone_number(self):
        """
        Return the IPhone phone number
        """
        return self.parsed_info_file['Phone Number']

    def get_iphone_product_name(self):
        """
        Return the IPhone product name
        """
        return self.parsed_info_file['Product Name']

    def get_iphone_product_type(self):
        """
        Return the IPhone product type
        """
        return self.parsed_info_file['Product Type']

    def get_iphone_product_version(self):
        """
        Return the IPhone product version
        """
        return self.parsed_info_file['Product Version']

    def get_iphone_serial_number(self):
        """
        Return the IPhone serial number
        """
        return self.parsed_info_file['Serial Number']

    def get_iphone_target_identifier(self):
        """
        Return the IPhone target identifier
        """
        return self.parsed_info_file['Target Identifier']

    def get_iphone_target_type(self):
        """
        Return the IPhone target type
        """
        return self.parsed_info_file['Target Type']

    def get_iphone_unique_identifier(self):
        """
        Return the IPhone unique identifier
        """
        return self.parsed_info_file['Unique Identifier']

    def get_iphone_iBooks_data(self):
        """
        Return the IPhone iBooks data if available
        """
        if 'iBooks Data 2' in self.parsed_info_file:
            return self.parsed_info_file['iBooks Data 2']
        else:
            return ''

    def get_iphone_iTunes_files(self):
        """
        Return the IPhone iTunes files
        """
        return self.parsed_info_file['iTunes Files']

    def get_iphone_iTunes_settings(self):
        """
        Return the IPhone iTunes settings
        """
        return self.parsed_info_file['iTunes Settings']

    def get_iphone_iTunes_version(self):
        """
        Return the IPhone iTunes version
        """
        return self.parsed_info_file['iTunes Version']

    # - manifest.plist
    def get_backup_key_bag(self):
        """
        Return the IPhone backup key bag
        """
        return self.parsed_manifest_file['BackupKeyBag']

    def get_backup_version(self):
        """
        Return the IPhone backup version
        """
        return self.parsed_manifest_file['Version']

    def get_backup_date(self):
        """
        Return the IPhone backup date
        """
        return self.parsed_manifest_file['Date']

    def get_backup_system_domain_version(self):
        """
        Return the IPhone backup system domain version
        """
        return self.parsed_manifest_file['SystemDomainsVersion']

    def get_backup_was_passcode_set(self):
        """
        Return whether the IPhone password has a password set
        """
        return self.parsed_manifest_file['WasPasscodeSet']

    def get_backup_lock_down(self):
        """
        Return the IPhone backup lock down status
        """
        return self.parsed_manifest_file['Lockdown']

    def get_backup_applications(self):
        """
        Return the applications that are on the IPhone backup
        """
        return self.parsed_manifest_file['Applications']

    def get_backup_is_encrypted(self):
        """
        Return whether the IPhone backup is encrypted
        """
        return self.parsed_manifest_file['IsEncrypted']

    # - status.plist
    def get_status_is_full_backup(self):
        """
        Return whether the IPhone backup is a full backup
        """
        return self.parsed_status_file['IsFullBackup']

    def get_status_version(self):
        """
        Return the IPhone backup status version
        """
        return self.parsed_status_file['Version']

    def get_status_UUID(self):
        """
        Return the IPhone backup UUID
        """
        return self.parsed_status_file['UUID']

    def get_status_date(self):
        """
        Return the IPhone backup status date
        """
        return self.parsed_status_file['Date']

    def get_status_backup_state(self):
        """
        Return the IPhone backup state
        """
        return self.parsed_status_file['BackupState']

    def get_status_snapshot_state(self):
        """
        Return the IPhone snapshot state
        """
        return self.parsed_status_file['SnapshotState']

    # Collection output methods
    def get_iphone_applications(self):
        """
        Return all information related to the iPhone applications
        """
        applications = self.get_iphone_non_installed_applications() + self.get_iphone_installed_applications()
        self.storage_master['iphone_applications'] = applications
        return applications

    def get_iphone_system_information(self):
        """
        Return all information related to iPhone system within the backup
        """
        information = {
            'build_version': self.get_iphone_build_version(),
            'device_name': self.get_iphone_device_name(),
            'display_name': self.get_iphone_display_name(),
            'GUID': self.get_iphone_GUID(),
            'ICCID': self.get_iphone_ICCID(),
            'IMEI': self.get_iphone_IMEI(),
            'last_backup_date': self.get_iphone_last_backup_date(),
            'MEID': self.get_iphone_MEID(),
            'phone_number': self.get_iphone_phone_number(),
            'product_type': self.get_iphone_product_type(),
            'product_version': self.get_iphone_product_version(),
            'serial_number': self.get_iphone_serial_number(),
            'target_identifier': self.get_iphone_target_identifier(),
            'target_type': self.get_iphone_target_type(),
            'unique_identifier': self.get_iphone_unique_identifier()
        }

        self.storage_master['iphone_system_information'] = information
        return information

    def get_iphone_iBooks_infomation(self):
        """
        Return all information related to iBooks within the backup
        """
        information = {
            'iBooks_data': self.get_iphone_iBooks_data()
        }

        self.storage_master['iphone_iBooks_information'] = information
        return information

    def get_iphone_iTunes_information(self):
        """
        Return all information related to iTunes within the backup
        """
        information = {
            'iTunes_files': self.get_iphone_iTunes_files(),
            'iTunes_settings': self.get_iphone_iTunes_settings(),
            'iTunes_version': self.get_iphone_iTunes_version()
        }

        self.storage_master['iphone_iTunes_information'] = information
        return information

    def get_backup_information(self):
        """
        Return all information related to the backup
        """
        information = {
            'backup_key_bag': self.get_backup_key_bag(),
            'version': self.get_backup_version(),
            'date': self.get_backup_date(),
            'system_domain_version': self.get_backup_version(),
            'was_passcode_set': self.get_backup_was_passcode_set(),
            'lockdown': self.get_backup_lock_down(),
            'applications': self.get_backup_applications(),
            'is_encrypted': self.get_backup_is_encrypted()
        }

        self.storage_master['iphone_backup_information'] = information
        return information

    def get_status_information(self):
        """
        Return all information related to the backup status
        """
        information = {
            'is_full_backup': self.get_status_is_full_backup(),
            'version': self.get_status_version(),
            'UUID': self.get_status_UUID(),
            'date': self.get_status_date(),
            'backup_state': self.get_status_backup_state(),
            'snapshot_state': self.get_status_snapshot_state()
        }

        self.storage_master['iphone_status_information'] = information
        return information

    def get_storage_master(self):
        """
        Return the master storage dictionary
        """
        return self.storage_master

    # Main parse method
    def parse(self):
        """
        Parse all iphone information from the initial instance declaration.
        """
        self.get_iphone_system_information()
        self.get_iphone_applications()
        self.get_iphone_iTunes_information()
        self.get_iphone_iBooks_infomation()
        self.get_backup_information()
        self.get_status_information()