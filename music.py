print("Please write in the following format :  letter#(if required)octave-number \n")

c1 = [".Sa", "..Ni", "..ni", "..Dh", "..dh", "..Pa",
      "..ma", "..Ma", "..Ga", "..ga", "..Re", "..Sa", "...Ni"]
ca1 = [".re", ".Sa", "..Ni", "..ni", "..Dh", "..dh",
       "..Pa", "..ma", "..Ma", "..Ga", "..ga", "..Re", "..Sa"]
d1 = [".Re", ".re", ".Sa", "..Ni", "..ni", "..Dh", "..dh",
      "..Pa", "..ma", "..Ma", "..Ga", "..ga", "..Re"]
da1 = [".ga", ".Re", ".re", ".Sa", "..Ni", "..ni", "..Dh",
       "..dh", "..Pa", "..ma", "..Ma", "..Ga", "..ga"]
e1 = [".Ga", ".ga", ".Re", ".re", ".Sa", "..Ni", "..ni",
      "..Dh", "..dh", "..Pa", "..ma", "..Ma", "..Ga"]
f1 = [".Ma", ".Ga", ".ga", ".Re", ".re", ".Sa", "..Ni",
      "..ni", "..Dh", "..dh", "..Pa", "..ma", "..Ma"]
fa1 = [".ma", ".Ma", ".Ga", ".ga", ".Re", ".re", ".Sa",
       "..Ni", "..ni", "..Dh", "..dh", "..Pa", "..ma"]
g1 = [".Pa", ".ma", ".Ma", ".Ga", ".ga", ".Re", ".re",
      ".Sa", "..Ni", "..ni", "..Dh", "..dh", "..Pa"]
ga1 = [".dh", ".Pa", ".ma", ".Ma", ".Ga", ".ga", ".Re",
       ".re", ".Sa", "..Ni", "..ni", "..Dh", "..dh"]
a1 = [".Dh", ".dh", ".Pa", ".ma", ".Ma", ".Ga", ".ga",
      ".Re", ".re", ".Sa", "..Ni", "..ni", "..Dh"]
aa1 = [".ni", ".Dh", ".dh", ".Pa", ".ma", ".Ma",
       ".Ga", ".ga", ".Re", ".re", ".Sa", "..Ni", "..ni"]
b1 = [".Ni", ".ni", ".Dh", ".dh", ".Pa", ".ma",
      ".Ma", ".Ga", ".ga", ".Re", ".re", ".Sa", "..Ni"]

c2 = ["Sa", ".Ni", ".ni", ".Dh", ".dh", ".Pa",
      ".ma", ".Ma", ".Ga", ".ga", ".Re", ".re", ".Sa"]
ca2 = ["re", "Sa", ".Ni", ".ni", ".Dh", ".dh",
       ".Pa", ".ma", ".Ma", ".Ga", ".ga", ".Re", ".re"]
d2 = ["Re", "re", "Sa", ".Ni", ".ni", ".Dh", ".dh",
      ".Pa", ".ma", ".Ma", ".Ga", ".ga", ".Re"]
da2 = ["ga", "Re", "re", "Sa", ".Ni", ".ni", ".Dh",
       ".dh", ".Pa", ".ma", ".Ma", ".Ga", ".ga"]
e2 = ["Ga", "ga", "Re", "re", "Sa", ".Ni", ".ni",
      ".Dh", ".dh", ".Pa", ".ma", ".Ma", ".Ga"]
f2 = ["Ma", "Ga", "ga", "Re", "re", "Sa", ".Ni",
      ".ni", ".Dh", ".dh", ".Pa", ".ma", ".Ma"]
fa2 = ["ma", "Ma", "Ga", "ga", "Re", "re", "Sa",
       ".Ni", ".ni", ".Dh", ".dh", ".Pa", ".ma"]
g2 = ["Pa", "ma", "Ma", "Ga", "ga", "Re", "re",
      "Sa", ".Ni", ".ni", ".Dh", ".dh", ".Pa"]
ga2 = ["dh", "Pa", "ma", "Ma", "Ga", "ga", "Re",
       "re", "Sa", ".Ni", ".ni", ".Dh", ".dh"]
a2 = ["Dh", "dh", "Pa", "ma", "Ma", "Ga", "ga",
      "Re", "re", "Sa", ".Ni", ".ni", ".Dh"]
aa2 = ["ni", "Dh", "dh", "Pa", "ma", "Ma",
       "Ga", "ga", "Re", "re", "Sa", ".Ni", ".ni"]
b2 = ["Ni", "ni", "Dh", "dh", "Pa", "ma",
      "Ma", "Ga", "ga", "Re", "re", "Sa", ".Ni"]

c3 = ["Sa.", "Ni", "ni", "Dh", "dh", "Pa",
      "ma", "Ma", "Ga", "ga", "Re", "re", "Sa"]
ca3 = ["re.", "Sa.", "Ni", "ni", "Dh", "dh",
       "Pa", "ma'", "Ma", "Ga", "ga", "Re", "re"]
d3 = ["Re.", "re.", "Sa.", "Ni", "ni", "Dh",
      "dh", "Pa", "ma'", "Ma", "Ga", "ga", "Re"]
da3 = ["ga.", "Re.", "re.", "Sa.", "Ni", "ni",
       "Dh", "dh", "Pa", "ma", "Ma", "Ga", "ga"]
e3 = ["Ga.", "ga.", "Re.", "re.", "Sa.", ".Ni",
      "ni", "Dh", "dh", "Pa", "ma", "Ma", "Ga"]
f3 = ["Ma.", "Ga.", "ga.", "Re.", "re.", "Sa.",
      "Ni", "ni", "Dh", "dh", "Pa", "ma", "Ma"]
fa3 = ["ma.", "Ma.", "Ga.", "ga.", "Re.", "re.",
       "Sa.", "Ni", "ni", "Dh", "dh", "Pa", "ma"]
g3 = ["Pa.", "ma.", "Ma.", "Ga.", "ga.", "Re.",
      "re.", "Sa.", "Ni", "ni", "Dh", "dh", "Pa"]
ga3 = ["dh.", "Pa.", "ma.", "Ma.", "Ga.", "ga.",
       "Re.", "re.", "Sa.", "Ni", "ni", "Dh", "dh"]
a3 = ["Dh.", "dh.", "Pa.", "ma.", "Ma.", "Ga.",
      "ga.", "Re.", "re.", "Sa.", "Ni", "ni", "Dh"]
aa3 = ["ni.", "Dh.", "dh.", "Pa.", "ma.", "Ma.",
       "Ga.", "ga.", "Re.", "re.", "Sa.", "Ni", "ni"]
b3 = ["Ni.", "ni.", "Dh.", "dh.", "Pa.", "ma.",
      "Ma.", "Ga.", "ga.", "Re.", "re.", "Sa.", "Ni"]

c4 = ["Sa..", "Ni.", "ni.", "Dh.", "dh.", "Pa.",
      "ma.", "Ma.", "Ga.", "ga.", "Re.", "re.", "Sa."]
ca4 = ["re..", "Sa..", "Ni.", "ni.", "Dh.", "dh.",
       "Pa.", "ma.'", "Ma.", "Ga.", "ga.", "Re.", "re."]
d4 = ["Re..", "re..", "Sa..", "Ni", "ni", "Dh.",
      "dh.", "Pa.", "ma'.", "Ma.", "Ga.", "ga.", "Re."]
da4 = ["ga..", "Re..", "re..", "Sa..", "Ni", "ni.",
       "Dh.", "dh.", "Pa.", "ma.", "Ma.", "Ga.", "ga."]
e4 = ["Ga..", "ga..", "Re..", "re..", "Sa..", "Ni.",
      "ni.", "Dh.", "dh.", "Pa.", "ma.", "Ma.", "Ga."]
f4 = ["Ma..", "Ga..", "ga..", "Re.", "re..", "Sa..",
      "Ni.", "ni.", "Dh.", "dh.", "Pa.", "ma.", "Ma."]

initialOctave = input("write the name of the octave")
print("your initiaL octave is : ", initialOctave)

changeOctave = input("write the name of the changes required octave")
print("your other octave is :", changeOctave)

if "c1" in initialOctave:
    print("\nc1 octave is : \n", c1)
elif "c#1" in initialOctave:
    print("\nc#1 octave is : \n", ca1)
elif "d1" in initialOctave:
    print("\nd1 octave is : \n", d1)
elif "d#1" in initialOctave:
    print("\nd#1 octave is : \n", da1)
elif "e1" in initialOctave:
    print("\ne1 octave is : \n", e1)
elif "f1" in initialOctave:
    print("\nf1 octave is : \n", f1)
elif "g1" in initialOctave:
    print("\ng1 octave is : \n", g1)
elif "g#1" in initialOctave:
    print("\ng#1 octave is : \n", ga1)
elif "a1" in initialOctave:
    print("\na1 octave is : \n", a1)
elif "a#1" in initialOctave:
    print("\n a#1 octave is : \n", aa1)
elif "b1" in initialOctave:
    print("\n b1 octave is : \n", b1)
elif "c2" in initialOctave:
    print("\n c2 octave is : \n", c2)
elif "c#2" in initialOctave:
    print("\n c#2 octave is : \n", ca2)
elif "d2" in initialOctave:
    print("\n d2 octave is : \n", d2)
elif "d#2" in initialOctave:
    print("\n d#2 octave is : \n", da2)
elif "e2" in initialOctave:
    print("\n e2 octave is : \n", e2)
elif "f2" in initialOctave:
    print("\n f2 octave is : \n", f2)
elif "f#2" in initialOctave:
    print("\n f#2 octave is : \n", fa2)
elif "g2" in initialOctave:
    print("\n g2 octave is : \n", g2)
elif "g#2" in initialOctave:
    print("\n g#2 octave is : \n", ga2)
elif "a2" in initialOctave:
    print("\n a2 octave is : \n", a2)
elif "a#2" in initialOctave:
    print("\n a#2 octave is : \n", aa2)
elif "b2" in initialOctave:
    print("\n b2 octave is : \n", b2)
elif "c3" in initialOctave:
    print("\n c3 octave is : \n", c3)
elif "c#3" in initialOctave:
    print("\n c#3 octave is : \n", ca3)
elif "d3" in initialOctave:
    print("\n d3 octave is : \n", d3)
elif "d#3" in initialOctave:
    print("\n d#3 octave is : \n", da3)
elif "e3" in initialOctave:
    print("\n e3 octave is : \n", e3)
elif "f3" in initialOctave:
    print("\n f3 octave is : \n", f3)
elif "f#3" in initialOctave:
    print("\n f#3 octave is : \n", fa3)
elif "g3" in initialOctave:
    print("\n g3 octave is : \n", g3)
elif "g#3" in initialOctave:
    print("\n g#3 octave is : \n", ga3)
elif "a3" in initialOctave:
    print("\n a3 octave is : \n", a3)
elif "a#3" in initialOctave:
    print("\n a#3 octave is : \n", aa3)
elif "b3" in initialOctave:
    print("\n b3 octave is : \n", b3)
elif "c4" in initialOctave:
    print("\n c4 octave is : \n", c4)
elif "c#4" in initialOctave:
    print("\n c#4 octave is : \n", ca4)
elif "d4" in initialOctave:
    print("\nd4 octave is : \n", d4)
elif "d#4" in initialOctave:
    print("\nd#4 octave is : \n", da4)
elif "e4" in initialOctave:
    print("\ne4 octave is : \n", e4)
elif "f4" in initialOctave:
    print("\nf4 octave is : \n", f4)
else:
    print("You have given wrong intial octave")


if "c1" in changeOctave:
    print("\nc1 octave is : \n", c1)
elif "c#1" in changeOctave:
    print("\nc#1 octave is : \n", ca1)
elif "d1" in changeOctave:
    print("\nd1 octave is : \n", d1)
elif "d#1" in changeOctave:
    print("\nd#1 octave is : \n", da1)
elif "e1" in changeOctave:
    print("\ne1 octave is : \n", e1)
elif "f1" in changeOctave:
    print("\nf1 octave is : \n", f1)
elif "g1" in changeOctave:
    print("\ng1 octave is : \n", g1)
elif "g#1" in changeOctave:
    print("\ng#1 octave is : \n", ga1)
elif "a1" in changeOctave:
    print("\na1 octave is : \n", a1)
elif "a#1" in changeOctave:
    print("\na#1 octave is : \n", aa1)
elif "b1" in changeOctave:
    print("\nb1 octave is : \n", b1)
elif "c2" in changeOctave:
    print("\nc2 octave is : \n", c2)
elif "c#2" in changeOctave:
    print("\nc#2 octave is : \n", ca2)
elif "d2" in changeOctave:
    print("\nd2 octave is : \n", d2)
elif "d#2" in changeOctave:
    print("\nd#2 octave is : \n", da2)
elif "e2" in changeOctave:
    print("\ne2 octave is : \n", e2)
elif "f2" in changeOctave:
    print("\nf2 octave is : \n", f2)
elif "f#2" in changeOctave:
    print("\nf#2 octave is : \n", fa2)
elif "g2" in changeOctave:
    print("\ng2 octave is : \n", g2)
elif "g#2" in changeOctave:
    print("\ng#2 octave is : \n", ga2)
elif "a2" in changeOctave:
    print("\na2 octave is : \n", a2)
elif "a#2" in changeOctave:
    print("\na#2 octave is : \n", aa2)
elif "b2" in changeOctave:
    print("\nb2 octave is : \n", b2)
elif "c3" in changeOctave:
    print("\nc3 octave is : \n", c3)
elif "c#3" in changeOctave:
    print("\nc#3 octave is : \n", ca3)
elif "d3" in changeOctave:
    print("\nd3 octave is : \n", d3)
elif "d#3" in changeOctave:
    print("\nd#3 octave is : \n", da3)
elif "e3" in changeOctave:
    print("\ne3 octave is : \n", e3)
elif "f3" in changeOctave:
    print("\nf3 octave is : \n", f3)
elif "f#3" in changeOctave:
    print("\nf#3 octave is : \n", fa3)
elif "g3" in changeOctave:
    print("\ng3 octave is : \n", g3)
elif "g#3" in changeOctave:
    print("\ng#3 octave is : \n", ga3)
elif "a3" in changeOctave:
    print("\na3 octave is : \n", a3)
elif "a#3" in changeOctave:
    print("\na#3 octave is : \n", aa3)
elif "b3" in changeOctave:
    print("\nb3 octave is : \n", b3)
elif "c4" in changeOctave:
    print("\nc4 octave is : \n", c4)
elif "c#4" in changeOctave:
    print("\nc#4 octave is : \n", ca4)
elif "d4" in changeOctave:
    print("\nd4 octave is : \n", d4)
elif "d#4" in changeOctave:
    print("\nd#4 octave is : \n", da4)
elif "e4" in changeOctave:
    print("\ne4 octave is : \n", e4)
elif "f4" in changeOctave:
    print("\nf4 octave is : \n", f4)
else:
    print("You have given wrong change octave")
