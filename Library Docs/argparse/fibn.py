import argparse
def fib(n):
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
    return a

def Main():
    parser = argparse.ArgumentParser(description='This is a fibonacci generator.')
    
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v","--verbose", action="store_true", dest="verb")
    group.add_argument("-q","--quiet", action="store_true")
    
    group2 = parser.add_argument_group('authentication')
    group2.add_argument('--user', help="Doesn't do anything")
    group2.add_argument('--password', action="store",default="meh",help="Doesn't do anything")
    
    parser.add_argument("num", help="The fibonacci number you wish to calculate.", type=int)
    # parser.add_argument("name", help="Doesn't do anything.")
    # these are positional arguments and always need to be passed.
    parser.add_argument("-o","--output",help="Output the result to a file", action="store_true")
    
    args=parser.parse_args()
    print("Args:",args)
    
    result=fib(args.num)
    
    if args.verb:
        print("The", args.num, "fib number is",result)
    elif args.quiet:
        print(result)
    else:
        print("Fib ("+ str(args.num)+ "):",result)
        
        
    if args.output:
        f=open("fibonacci.txt",'a')
        f.write(str(result)+'\n')
        f.close()
        print('Output to file "fibonacci.txt"')
            
if __name__ == '__main__':
    Main()
