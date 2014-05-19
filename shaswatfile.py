def disp(x):
	if x<20:
		print "The number is :",x
	i=0
	items=('shaswat','sunder','nayak')
	while i<3:
		print items[i]
		i=i+1		
disp(10)


class Calculator(object):
        """simple calc
        """
        
        def samplecalc(self):
                print "press 1 for addition."
                print "press 2 for substraction."
                print "press 3 for multiplication."
                print "press 4 for division."
                choice=input("Enter your choice:")
                if choice==1:
                        a=input("Enter the 1st number:")
                        b=input("Enter the 2nd number:")
                        print "The sum is: ",a+b
                elif choice==2:
                        a=input("Enter the 1st number:")
                        b=input("Enter the 2nd number:")
                        print "The substration is: ",a-b
                elif choice==3:
                        a=input("Enter the 1st number:")
                        b=input("Enter the 2nd number:")
                        print "The product is: ",a*b
                elif choice==4:
                        a=input("Enter the 1st number:")
                        b=input("Enter the 2nd number:")
                        print "The quotient is: ",a/b
                        print "The remainder is: ",a%b
                else:
                        print "wrong choice"


                        
calc = Calculator()
calc.samplecalc()
