class Follower:
    def __init__(self, name):
        self.follower_name = name
    def react(self):
        print(self.follower_name, 'лайкает сообщение')
    def __str__(self):
        return f'follower({self.follower_name})'
    def __repr__(self):
        return f'follower({self.follower_name})'

    
class Creator:
    def __init__(self,name):
        self.sub_list = []
        self.creator_name = name
    def follow(self, follower):
        self.sub_list.append(follower)
    def show_followers(self):
        print(self.sub_list)
    def notify_all(self):
        for follower in self.sub_list:
            follower.react()
    def create_post(self, message):
        print(self.creator_name, 'опубликовал это сообщение:')
        print(message)
        print()
        self.notify_all()

        
creator1 = Creator('MyChannel')
f1 = Follower('Petya')
f2 = Follower('Dimas')
f3 = Follower('Kolyan')

creator1.show_followers
creator1.create_post('run run run')
creator1.follow(f1)
creator1.show_followers()
creator1.create_post('run run run')
creator1.follow(f3)
creator1.create_post('run run run')
creator1.follow(f2)
creator1.create_post('run run run')
