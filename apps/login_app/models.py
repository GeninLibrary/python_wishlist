
# LOGIN APP --- MODELS

from __future__ import unicode_literals

from django.db import models

from time import gmtime,strftime

import bcrypt   # ENCODES PASSWORD


class CheckUser(models.Manager):
    
    def createUser(self, post_data):            
        encrypted_password = bcrypt.hashpw(post_data['password'].encode(), bcrypt.gensalt())
        self.create(
            name = post_data["name"],                       # CREATES NEW USER IN DATABASE
            username = post_data["username"],
            date = strftime(post_data["date"]),                         # WITH ENCRYPTED PASSWORD
            password = encrypted_password,
        )


    def registerVal(self, post_data):                                   # RECIEVES AND VALIDATES POST DATA
        results = {                                                     # APPENDS MESSAGES TO 'ERRORS'
            'errors' : [],                                              # BOOLEAN SHOWS INPUT VALIDITY
            'status' : True,                                            # TRUE --> CREATE
        }                                                               # FALSE --> DISPLAY ERRORS
        if len(post_data['name']) < 3:
            results['status'] = False
            results['errors'].append("You must enter a longer name")
        if len(post_data['username']) < 3:                                     # -----------------------
            results['status'] = False                                           # COME BACK TO MAKE A CONDITION 
            results['errors'].append("You must enter a longer username")              # THAT CHECKS FOR INVALID CHARACTERS  

        if len(post_data['password']) < 3:
            results['status'] = False
            results['errors'].append("You must enter a longer password")
        if post_data['password'] != post_data['c_password']:                # CONFIRM PASSWORD                     
            results['status'] = False                                 
            results['errors'].append('These passwords are not a match') 

        user_match = self.filter(username = post_data['username'])                # QUERIES DATABASE FOR OBJECTS WITH SAME EMAIL
        if len(user_match) != 0:                                            # IF IT FINDS ANY THAT MEANS SOMEONE HAS ALREADY CREATED THIS ACCOUNT
            results['status'] = False               
            results['errors'].append("This user is already in the database")               
                                                                            
        
        return results                                                      # RETURNS 'RESULTS' OBJECT



    def loginVal(self, post_data):
        results = {
            'errors' : [],
            'status' : True,
            'retrieved_account' : None,
        }
        user_match = self.filter(username = post_data['username'])                   # CHECKS FOR OBJECT WITH SAME EMAIL IN DATABASE
        if len(user_match) == 0:                                                # IF NONE THEN NO LOGIN
            results['status'] = False
            results['errors'].append("This username is not in our database")
        else:                                                                   # IF EXISTS THEN PULL OBJECT AND TEST PASSWORD
            results['retrieved_account'] = user_match[0] 
            if not bcrypt.checkpw(post_data['password'].encode(), results['retrieved_account'].password.encode()):                           
                results['errors'].append('Your password is whack.')                  
                results['status'] = False                                      
        
        return results
            


class User(models.Model):
    name = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100)
    date = models.CharField(max_length= 100)
    password = models.CharField(max_length = 100)
    objects = CheckUser()
    

