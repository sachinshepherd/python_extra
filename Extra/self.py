class Restaurant():
    bankrupt = False
    def open_branch(self):
        if not self.bankrupt:
            print("branch opened")

a = Restaurant()
print a.bankrupt
print a.open_branch()