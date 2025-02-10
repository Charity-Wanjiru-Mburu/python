class dad:
    def football(self):
        print("I like playing football")
class mum:
    def cooking(self):
        print("Mummy love cooking with you")

class girl(dad):
    def girlage(self):
        print("This girl is 20 years old")
my_girl=girl()
my_girl.football()
my_girl.girlage()

class boy(mum):
    def boyage(self):
        print("This boy is 2 years old")
my_boy=boy()
my_boy.cooking()
my_boy.boyage()