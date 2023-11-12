
class Employee:

    def __init__(self, pkEmployeeId=0, firstName='', lastName='', title='', email=''):
        super()
        self._pkEmployeeId = pkEmployeeId
        self._firstName = firstName
        self._lastName = lastName
        self._title = title
        self._email = email

    @property
    def pkEmployeeId(self):
        return self._pkEmployeeId

    @property
    def firstName(self):
        return self._firstName

    @property
    def lastName(self):
        return self._lastName

    @property
    def title(self):
        return self._title

    @property
    def email(self):
        return self._email

    @pkEmployeeId.setter
    def pkEmployeeId(self, value):
        self._pkEmployeeId = value

    @firstName.setter
    def firstName(self, value):
        self._firstName = value

    @lastName.setter
    def lastName(self, value):
        self._lastName = value

    @title.setter
    def title(self, value):
        self._title = value

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def displayName(self):
        return f'{self._firstName} {self._lastName}'

    def __str__(self) -> str:
        return f'Name: {self.displayName}, Title: {self.title}, Email: {self.email}'

    def __repr__(self) -> str:
        return f'Employee(\'{self.pkEmployeeId}\', \'{self.firstName}\', \'{self.lastName}\', \'{self.title}\', ' \
               f'\'{self.email}\')'
