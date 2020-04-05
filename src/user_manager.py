import time
import functools
import threading
from time import sleep


class UserManager:

    def __init__(self):
        self.user_removal_time = 1800
        self.currentUsers = {}
        self.userthread = threading.Thread(target=self.__remove_old_users)
        self.userthread.start()

    def __remove_old_users(self):
        while True:
            sleep(self.user_removal_time)
            print('deleteCycle')
            print(self.currentUsers)
            users_to_delete = []
            for user in self.currentUsers.values():
                if time.time() - user.lastActivityTime > self.user_removal_time:
                    users_to_delete.append(user.chat_id)
            for id in users_to_delete:
                self.delete_user(id)
                print('deleting user')

    def delete_user(self, chat_id):
        if chat_id in self.currentUsers:
            del self.currentUsers[chat_id]
        else:
            print(f'[WARNING]DELETING UNEXISTING USER {chat_id}')

    def create_user(self, user):
        self.currentUsers[user.chat_id] = user


    # Users stored in dictionary with keys as
    # Structure {
    #   user_id: User-class object
    # }
    # chat_id


class User:
    def __init__(self, chat_id, name, specialization):
        self.chat_id = chat_id
        self.name = name
        self.email = ()
        self.specialization = specialization
        self.idea = ()
        self.prototype = ()
        self.why_we = ()
        self.expertise = ()
        self.experience = ()
        self.site = ()
        self.organization_name = ()
        self.organization_position = ()
        self.lastActivityTime = time.time()

    def __repr__(self):
        if self.specialization == 'startuper':
            return f'Startuper: Name & last name: {self.name}\nEmail: {self.email}\n' \
                   f'Idea: {self.idea}\nPrototype: {self.prototype}\n' \
                   f'Why needs an acceleration program: {self.why_we}\n'
        elif self.specialization == 'mentor':
            return f'Mentor: Name & last name: {self.name}\nEmail: {self.email}\n' \
                   f'Site: {self.site}\nExpertise: {self.expertise}\nExperience: {self.experience}\n'
        elif self.specialization == 'partner':
            return f'Partner: Name & last name: {self.name}\nEmail: {self.email}\n' \
                   f'Organization: {self.organization_name}\nPosition there: {self.organization_position}\n'

    def refresh_action(func):
        def wrapper_refresh_time(self, *args, **kwargs):
            self.update_time()
            value = func(self, *args, **kwargs)
            return value

        return wrapper_refresh_time

    def update_time(self):
        self.lastActivityTime = time.time()

    def get_name(self):
        n1, n2 = self.name.split()
        return n1

    @refresh_action
    def add_email(self, email):
        self.email = email
        return email

    @refresh_action
    def add_idea(self, idea):
        self.idea = idea
        return idea

    @refresh_action
    def add_prototype(self, prototype):
        self.prototype = prototype
        return prototype

    @refresh_action
    def add_why_we(self, why_we):
        self.why_we = why_we
        return why_we

    @refresh_action
    def add_expertise(self, expertise):
        self.expertise = expertise
        return expertise

    @refresh_action
    def add_experience(self, experience):
        self.experience = experience
        return experience

    @refresh_action
    def add_site(self, site):
        self.site = site
        return site

    @refresh_action
    def add_organization_name(self, organization_name):
        self.organization_name = organization_name
        return organization_name

    @refresh_action
    def add_organization_position(self, organization_position):
        self.organization_position = organization_position
        return organization_position


UM = UserManager()
# if __name__ == "__main__":
#     user = User(100500)
#     user.addQuestions([1,2,3,4,5])
#     user.addAnswer(1, 0)
#     print(user.answers)





