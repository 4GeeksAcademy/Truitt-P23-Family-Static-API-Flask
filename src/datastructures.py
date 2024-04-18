
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = []
    
        # example list of members

    # read-only: Use this method to generate random members ID's when adding members into the list
    def generateId(self):
        # generated_id = self._next_id
        # self._next_id += 1
        # return generated_id
        return randint(0, 999999999)

    def add_member(self, member):
        # fill this method and update the return
        if 'id' not in member:
            member['id'] = self.generateId()
        self._members.append(member)

        return self._members

    def delete_member(self, id):
        # fill this method and update the return
        for i, member in enumerate(self._members):
            if member['id'] == id:
                self._members.pop(i)
                return True
        return False

# Alternate delete member code
    # def delete_member(self, id):
    #     # fill this method and update the return
    #     for index in range(len(self._members)):
    #         member = self._members[index]
    #         if member['id'] == id:
    #             self._members.pop(index)
    #             return True
            
    #     return False

    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member['id'] == id:
                return member
        return "member not found"

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
