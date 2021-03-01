if self.s_repo.is_in_list(s_id) == False:
    print("ID not found in the current list! ")
else: 
    self.s_repo.updateStudent(s_id)