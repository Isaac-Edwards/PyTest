def setup_module(module):
    print("Setup module!")

def teardown_module(module):
    print("Teardown Module!")

class TestClass:
    @classmethod
    def setup_class(cls):
        print("Setup TestClass!")
    
    @classmethod
    def teardown_class(cls):
        print("Teardown TestClass!")

    def setup_method(self, method):
        if method == self.test1:
            print("\nSetting up test1!")
        if method == self.test2:
            print("\nSetting up test2!")
        else:
            print("\nSetting up something else...")

    def teardown_function(self, method):
        if method == self.test1:
            print("\nTearing down test1!")
        if method == self.test2:
            print("\nTearing down test2!")
        else:
            print("\nTearing down something else...")

    def test1(self):
        print("Executing test1!")
        assert True

    def test2(self):
        print("Executing test2!")
        assert True

    def test3(self):
        print("Executing test3!")
        assert False
