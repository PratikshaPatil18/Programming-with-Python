#Write a Program to accept five subject marks from user and Calculate total marks and its average.
php=int(input('enter your PHP marks :'));
pwp=int(input('enter your PWD marks :'));
mad=int(input('enter your MAD marks :'));
eti=int(input('enter your ETI marks :'));
cgr=int(input('enter your CGR marks :'));
total=php + pwd + mad + eti + cgr;
avg=total/5;
print('PHP marks :',php);
print('PWD marks :',pwd);
print('MAD marks :',mad);
print('ETI marks :',eti);
print('CGR marks :',cgr);
print("Total marks :",total);
print('Average :',avg);
