
import pandas as pd

class EmployeeDatabse:
    def __init__(self):
        self.employee = {}
    
    def add_employee(self , employee_ID,name, job ,salary ):
        if employee_ID in self.employee:
            print(f"Employee with ID {employee_ID} already exists. Use a different ID .")
        else: 
            self.employee[employee_ID] = {'Name' : name ,'Job':job,'Salary':salary }
            print(f"Employee added successfully with ID {employee_ID} ")

    def print_employee_data (self , employee_ID):
        if employee_ID in self.employee:
            print(f"Employee ID: {employee_ID}")
            print(f"Name: {self.employees[employee_ID]['Name']}")
            print(f"Job: {self.employees[employee_ID]['Job']}")
            print(f"Salary: {self.employees[employee_ID]['Salary']}")
        else:
            print(f"Employee with ID {employee_ID} not found.")
    def remove_employee_data (self , employee_ID):
        if employee_ID in self.employees:
            del self.employees[employee_ID]
            print(f"Employee with ID {employee_ID} removed successfully.")
        else:
            print(f"Employee with ID {employee_ID} not found.")
    def get_employee_data (self , employee_ID):
        if employee_ID in self.employee:
            return self.employee[employee_ID]
        else: 
            return None
    def export_to_excel(self, filename):
        df = pd.DataFrame.from_dict(self.employee, orient='index')
        df.to_excel(filename, index_label='EmployeeID')
        print(f"Data exported to {filename}.")

#=========================================================================================



# Example usage:
if __name__ == "__main__":
    db = EmployeeDatabse()
    
 


    # Adding employees
    emp1_id = db.add_employee("24101","Jimin", "Engineer", 60000)
    emp2_id = db.add_employee("24102","Suga", "Devoleper", 90000)
    emp3_id = db.add_employee("24103","Jane Smith", "Manager", 80000)
    emp4_id = db.add_employee("1326820","Namjoon" ,"CEO",100000)
    emp5_id = db.add_employee("8794265","Taehyung","data analysis",75000)

    
    # Printing employee data
    db.print_employee_data(emp1_id)
    db.print_employee_data(emp2_id)
    db.print_employee_data(emp3_id)
    db.print_employee_data(emp4_id)
    db.print_employee_data(emp5_id)
    
    # Exporting to Excel
    db.export_to_excel("employees.xlsx")
    
    
 