import unittest

def compound_interest(P,t,r,n):
    if n!=0:
        A = P*pow(1+((r/100)/n),(n*t))
    if n==0:
        A = 0
        print("Given n value is not applicable")
    return A

def simple_interest(P,t,r):
    A = P+((P*t*r)/100)
    return A

class UnitTesting(unittest.TestCase):

    def test_si(self):
        self.assertEqual(simple_interest(10000,12,10),22000,"It should be 22000")
    def test_ci1(self):
        self.assertEqual(compound_interest(10000,2,2,1),10404,"It should be 10404")
    def test_ci2(self):
        self.assertEqual(compound_interest(10000,2,2,0),0,"It should be 10404")
    
if __name__=='__main__':
    unittest.main()
