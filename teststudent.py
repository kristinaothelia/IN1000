from student import Student

stud1 = Student("Siri")
stud2 = Student("Geir Kjetil")
stud3 = Student("Henrik")

stud1.registrer()
stud1.registrer()
stud2.registrer()

assert(stud1.hentOppmote() == 2)
assert(stud2.hentOppmote() == 1)
assert(stud3.hentOppmote() == 0)
