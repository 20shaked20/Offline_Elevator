a_global_var = "hello"


class A():
    def modify_global(self):
        global a_global_var
        a_global_var += " world"


A().modify_global()

print(a_global_var)
