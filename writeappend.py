#write a file
import csv 

def write_into_csv(info list):

    with open('student_into.csv','w+',newline=' ') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(info.list)
                        
condition=true
      
while(condition):
  student_info=input("Enter student information in following format (name  age  contact_number  E_mail_ID): ")
  print("Entered information" + student_info)
   
  student_info_list = student_info.split(' ')   
  print("Entered split up information is :" + str(student_info_list))
  
  write_into_csv(student_info_list)
  
  condition check = input("Enter (yes/no) if you want to enter information for another students:")
  if condition_check == "yes":
    condition=true
  if condition_check == "no":
    condition=false 
    

#appending a file



import csv 

def write_into_csv(info list):
  with open('student_into.csv','a',newline=' ') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow("Name","Age","Contact_number", "E-mail_Id")
    writer.writerow(info.list)

    
condition=true
 
while(condition):
  student_info=input("Enter student information in following format (name  age  contact_number  E_mail_ID): ")
  print("Entered information" + student_info)
  
  student_info_list = student_info.split(' ')
  print("Entered split up information is : " +str(student_info_list))
  
  write_into_csv(student_info_list)
  
  
  condition check=input("Enter (yes/no) if you want to enter information for another students: ")
  if condition_check == "yes":
    condition=true
  if condition_check == "no":
    condition=false
      
 
        

        

        



        



    

    

    

    

    
   

   

   

   
   

    

   

 



    
    

    

    

    

   

   

   

   

   





    
