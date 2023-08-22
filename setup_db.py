db.drop_all()
db.create_all()

users = [
     	{'first_name': 'Scott', 'last_name' : 'Tiger', 'username':'stiger', 'email':'stiger@gmail.com'},
	{'first_name': 'Jayashree', 'last_name' : 'Sha', 'username':'jsha', 'email':'sha.jayashree@gmail.com'},
	{'first_name': 'Tushar', 'last_name' : 'Sha', 'username':'tsha', 'email':'tusharksha@gmail.com'}
	] 

for user in users:
     user_rec = User(**user)
     db.session.add(user_rec)  


courses = [ 
	{'course_name': 'Mastering Python','course_author':'Scott Tiger' ,'course_endpoint':'mastering-python'},
	{'course_name': 'Python App Development','course_author':'Donald Duck' ,'course_endpoint':'Python_Ap_Development'},
	{'course_name': 'DEVOp BootCamp','course_author':'Mickey Mouse' ,'course_endpoint':'DEVOp_BootCamp'}
] 
for course in courses:
     course_rec = Course(**course)
     db.session.add(course_rec)  
