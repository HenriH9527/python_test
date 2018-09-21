#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther:Awe H

username = input('username:')
age = int(input('age:')) #integer
job = input('job:')
salary = input('salary')

info = '''
-------- info of %s--------
Name:%s
Age:%s
Job:%s
Salary:%s
''' % (username, username, age, job, salary)

info2 = '''
-------- info of {_name}--------
Name:{_name}
Age:{_age}
Job:{_job}
Salary:{_salary}
'''.format(_name=username,
            _age=age,
            _job=job,
            _salary=salary)

info3 = '''
-------- info of {0}--------
Name:{0}
Age:{1}
Job:{2}
Salary:{3}
'''.format(username, age, job, salary)

print(info3)
#print(type(age),type(str(age)))
