from codeblog import db

class EmployeeDetails(db.Model):
    employee_id                  = db.Column(db.Integer,primary_key=True)
    employee_name                = db.Column(db.String(30),nullable=False)


    def __repr__(self):
        return f"('{self.employee_id}','{self.employee_name}')"