# kwargs basic funtionality

class Employee():
    def __init__(self):
        self.employee_db = {
            'adam_smith' : {
                'user_name': 'adam_smith',
                'age': 22,
                'email': 'adam@gmail.com',
                'token' : 'abcd'
            },
            
            'john_dae' : {
                'user_name': 'john_dae',
                'age': 25,
                'email': 'john@gmail.com',
                'token': 'xyz'
            }
        }
        
        
    def emp(self, **kwargs):
        for key, value in kwargs.items():
            try:
                print('{} details: {} \n'.format(value, self.employee_db[value]))
            except:
                print(f"{value} - Employee Not found")
    
    
    def validateEmp(self, **kwargs):
        if(self.employee_db[kwargs['user']]['user_name'] == kwargs['user'] and self.employee_db[kwargs['user']]['token']==kwargs['token'] ):
            print(f"{kwargs['user']} is your Employee ")
            return
        print(f"{kwargs['user']} is not your Employee ")
       

e = Employee()
e.emp(user='adam_smith', user1='john_dey')

e.validateEmp(user='john_dae', token='xyz')
e.validateEmp(user='adam_smith', token='acd')