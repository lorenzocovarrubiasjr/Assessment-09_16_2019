import sqlite3
import os 

DIRPATH = os.path.dirname(__file__)
DBFILENAME = "organization.db"
DBPATH = os.path.join(DIRPATH,DBFILENAME)

def seed(dbpath=DBPATH):
    branches = [("Flushing", "NY", 11368),
                ("Houston", "TX", 77002)]
    
    employees = [("Walker","Lockett","S0001",45000.00,1),
                 ("Casey","Coleman", "S0002",70000.00,1),
                 ("Franklyn","Kilome","S0003",67000.00,1),
                 ("Hecton","Santiago","S0004",100000.00,1),
                 ("Framber","Valdez","S0005",39000.00,2),
                 ("Brad", "Peacock","S0006",51000.00,2),
                 ("Reymin","Guduan","S0007", 67000.00,2),
                 ("Gerrit","Cole","S0008",55000.00,2)
                 ]
    
    with sqlite3.connect(dbpath) as conn:
        curs = conn.cursor() 
        SQL = """INSERT INTO branches (city, state, zip_code) VALUES (?,?,?);"""
        for branch in branches:
            curs.execute(SQL, branch)
            
        SQL = """INSERT INTO employees (first_name, last_name, employee_id, salary, branch_id) VALUES (?,?,?,?,?);"""
        for employee in employees:
            curs.execute(SQL, employee)
          
        ###UPDATE REYMIN GUDUAN'S SALARY 
        SQL = "UPDATE employees SET salary = 73000.00 WHERE (first_name = 'Reymin' and last_name = 'Guduan');"
        curs.execute(SQL)
        
        ###SELECT EMPLOYEES FROM NEW YORK THAT MAKE OVER $70,000 
        SQL = "SELECT * FROM employees JOIN branches ON employees.branch_id = branches.pk WHERE (branches.state = 'NY' and employees.salary > 70000)"
        curs.execute(SQL)
        
seed()