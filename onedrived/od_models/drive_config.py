class LocalDriveConfig:
    """Configuration for the local drive. This is saved on UserContext.DEFAULT_CONFIG_FILENAME."""

    def __init__(self, drive_id, account_id, ignorefile_path, localroot_path,
                 from_local_config='dmn', from_cloud_config='dmn'):
        self.drive_id = drive_id
        self.account_id = account_id
        self.ignorefile_path = ignorefile_path
        self.localroot_path = localroot_path
        self.from_local_config = from_local_config
        self.from_cloud_config = from_cloud_config

    def to_dict(self):
        return{
            'drive_id': self.drive_id,
            'account_id': self.account_id,
            'ignorefile_path': self.ignorefile_path,
            'localroot_path': self.localroot_path,
            'from_local_config': self.from_local_config,
            'from_cloud_config': self.from_cloud_config,
        }
