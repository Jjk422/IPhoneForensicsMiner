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


class IPhoneParser:
    # Initiation Method
    def __init__(self, parsed_info_file, parsed_manifest_file, parsed_status_file):
        self.parsed_info_file = parsed_info_file
        self.parsed_manifest_file = parsed_manifest_file
        self.parsed_status_file = parsed_status_file
        self.storage_master = {}

    # - info.plist
    def get_iphone_non_installed_applications(self):
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
        return self.parsed_info_file['Build Version']

    def get_iphone_device_name(self):
        return self.parsed_info_file['Device Name']

    def get_iphone_display_name(self):
        return self.parsed_info_file['Display Name']

    def get_iphone_GUID(self):
        return self.parsed_info_file['GUID']

    def get_iphone_ICCID(self):
        return self.parsed_info_file['ICCID']

    def get_iphone_IMEI(self):
        return self.parsed_info_file['IMEI']

    def get_iphone_last_backup_date(self):
        return self.parsed_info_file['Last Backup Date']

    def get_iphone_MEID(self):
        return self.parsed_info_file['MEID']

    def get_iphone_phone_number(self):
        return self.parsed_info_file['Phone Number']

    def get_iphone_product_name(self):
        return self.parsed_info_file['Product Name']

    def get_iphone_product_type(self):
        return self.parsed_info_file['Product Type']

    def get_iphone_product_version(self):
        return self.parsed_info_file['Product Version']

    def get_iphone_serial_number(self):
        return self.parsed_info_file['Serial Number']

    def get_iphone_target_identifier(self):
        return self.parsed_info_file['Target Identifier']

    def get_iphone_target_type(self):
        return self.parsed_info_file['Target Type']

    def get_iphone_unique_identifier(self):
        return self.parsed_info_file['Unique Identifier']

    def get_iphone_iBooks_data(self):
        if 'iBooks Data 2' in self.parsed_info_file:
            return self.parsed_info_file['iBooks Data 2']
        else:
            return ''

    def get_iphone_iTunes_files(self):
        return self.parsed_info_file['iTunes Files']

    def get_iphone_iTunes_settings(self):
        return self.parsed_info_file['iTunes Settings']

    def get_iphone_iTunes_version(self):
        return self.parsed_info_file['iTunes Version']

    # - manifest.plist
    def get_backup_key_bag(self):
        return self.parsed_manifest_file['BackupKeyBag']

    def get_backup_version(self):
        return self.parsed_manifest_file['Version']

    def get_backup_date(self):
        return self.parsed_manifest_file['Date']

    def get_backup_system_domain_version(self):
        return self.parsed_manifest_file['SystemDomainsVersion']

    def get_backup_was_passcode_set(self):
        return self.parsed_manifest_file['WasPasscodeSet']

    def get_backup_lock_down(self):
        return self.parsed_manifest_file['Lockdown']

    def get_backup_applications(self):
        return self.parsed_manifest_file['Applications']

    def get_backup_is_encrypted(self):
        return self.parsed_manifest_file['IsEncrypted']

    # - status.plist
    def get_status_is_full_backup(self):
        return self.parsed_status_file['IsFullBackup']

    def get_status_version(self):
        return self.parsed_status_file['Version']

    def get_status_UUID(self):
        return self.parsed_status_file['UUID']

    def get_status_date(self):
        return self.parsed_status_file['Date']

    def get_status_backup_state(self):
        return self.parsed_status_file['BackupState']

    def get_status_snapshot_state(self):
        return self.parsed_status_file['SnapshotState']

    # Collection output methods
    def get_iphone_applications(self):
        applications = self.get_iphone_non_installed_applications() + self.get_iphone_installed_applications()
        self.storage_master['iphone_applications'] = applications
        return applications

    def get_iphone_system_information(self):
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
        information = {
            'iBooks_data': self.get_iphone_iBooks_data()
        }

        self.storage_master['iphone_iBooks_information'] = information
        return information

    def get_iphone_iTunes_information(self):
        information = {
            'iTunes_files': self.get_iphone_iTunes_files(),
            'iTunes_settings': self.get_iphone_iTunes_settings(),
            'iTunes_version': self.get_iphone_iTunes_version()
        }

        self.storage_master['iphone_iTunes_information'] = information
        return information

    def get_backup_information(self):
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
        return self.storage_master

    # Main parse method
    def parse(self):
        self.get_iphone_system_information()
        self.get_iphone_applications()
        self.get_iphone_iTunes_information()
        self.get_iphone_iBooks_infomation()
        self.get_backup_information()
        self.get_status_information()