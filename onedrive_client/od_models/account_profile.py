
class AccountTypes:
    PERSONAL = 0
    BUSINESS = 1


class OneDriveAccount:

    def __init__(self, data):
        self.data = data

    @property
    def account_id(self):
        return self.data['id']

    @property
    def account_name(self):
        return self.data['name']

    @property
    def account_firstname(self):
        return self.data['first_name']

    @property
    def account_lastname(self):
        return self.data['last_name']

    @property
    def account_email(self):
        raise NotImplementedError

    def get_account(self):
        if self.data['account_type'] == AccountTypes.BUSINESS:
            return OneDriveAccountBusiness(self.data)
        else:
            return OneDriveAccountPersonal(self.data)


class OneDriveAccountPersonal(OneDriveAccount):

    def __init__(self, data):
        super().__init__(data)
        self.account_type = AccountTypes.PERSONAL

    @property
    def account_email(self):
        return self.data.account_email['account']


class OneDriveAccountBusiness(OneDriveAccount):

    def __init__(self, data):
        super().__init__(data)
        self.account_type = AccountTypes.BUSINESS

    @property
    def account_email(self):
        return self.data['emails']
