# debugging

GitHub repository: holbertonschool-chatgpt-introduction
Directory: debugging

https://onecompiler.com/html/ pour tester code html

0-
factorial.py

Test
$ ./factorial.py 2
2
$ ./factorial.py 5
120

Explanation of the Fix:
Decrement n: n -= 1 is added inside the while loop to reduce the value of n on each iteration. This allows the loop to eventually terminate when n is no longer greater than 1.

1-
print_arguments.py

Test
./print_arguments.py 1 2 3

Explanation of the Fix:
Starting the loop from 1: By starting the loop with range(1, len(sys.argv)), we skip the first element (sys.argv[0]), which is the script name, and only print the actual arguments passed to the script.

2-
change_background.html

Test

3-
mines.py

Test

4-
factorial_recursive.py

Test

5-
checkbook.py

Test

6-
tic.py

Test
