from file_reader import Filetext
from child_class import child

# file_reader
# this is property 
name=input ("may i have your name? ")
file= Filetext(name)


# setter
name_make_sure= input("are you sure this your name? (yes/no) ")
if name_make_sure== "no":
    x= input("enter you name man/lady ")
    file.filetxt= x
    print("good boy MR/MS",file.filetxt)
else:
    print("thank u MR/MS",file.filetxt)

open_your_file= input("are you here to open your file text? yes/no ")
if open_your_file== "yes":
    zz= input("file name pls: ")
    file_text= Filetext(zz)
    for  line in file_text.text():
     print(line)
else:
    print("get out!!")
    exit()
    # @staticmethod becouse it is outsider so we add the file name
line_count= input("would you like me count your lines num? yes/no ")

if line_count== "yes":
    print(file_text.line_num(zz))
else:
    print("okay")

print("_"*8)
# text we used for it make the yeild go to the next line

# @staticmethod becouse it is outsider so we add the file name


# @ classmethod we used for in because of yield
add_new_lines= input("we add a new feature it is adding line wanna try it? yes/no ")
if add_new_lines=="yes":
    x1= input("same file? yes/no ")
    if x1=="yes":
        a_b=input(" new line(add at the start of the new line ): ")
        a_b = '\n' + a_b 
        edit_file= Filetext.adding(zz,a_b)

        for new_line in edit_file.text():
            print(new_line)
    else:
     a= input("file name: ")
     b= input(" your lines:")
     b= '\n'+b
     edit_file= Filetext.adding(a,b)
     for new_line in edit_file.text():
            print(new_line)
else:
    print("okay")
        
      



print("+"*8)
#str it tell that this file is used in Filetext

# add 

add_two= input(" wanna add 2 file toghether it is cool? yes/no  ")

if add_two== "yes":
    fst=input("first file pls:")
    snd=input("2nd file:")
    file1= Filetext(fst)
    file2= Filetext(snd)
    both_file= file1+file2
    #color
    for two in both_file.text():
        print(two)
    color= input("wann coloer the text blue ? yes/no ")
    if color== "yes":
        print(both_file.colored_text())
    else:
        print("ok")
else:
    print("okay")




# more than 2
print("="*10)
more_than_2= input("wann see something better? yes/no ")
if more_than_2== "yes":
    print("now you can join more than 2 file \n u will try it any way")
    one= input("first: ")
    two= input("2nd: ")
    three= input("3d: ")
    all= Filetext.more_than2(one,two,three)
    print("="*8)
    for l in all.text():
        print(l)
    color= input("wann coloer the text blue ? yes/no ")
    if color== "yes":
        print(all.colored_text())
    else:
        print("ok")
else:
    print("you are boring get out but i can forgive u")

child_class_use= input ("can you tell me the name of the author of the texts if you did the more the 2 ones? yes/no ")

if child_class_use == 'yes':
    o_ne= input(f"who is the author of {one}? ")
    t_wo= input(f"who is the author of {two}? ")
    three_hree= input(f"who is the author of {three}? ")
    oone= child(one,o_ne)
    ttwo= child(two,t_wo) 
    tthree= child(three,three_hree)
    print(oone)
    print(oone.word_count())
    print(ttwo)
    print(ttwo.word_count())
    print(tthree)
    print(tthree.word_count())
else:
    print("i think we are done for today")

print("thank you for your time")















