print("Enter your marks for each subject")

math=int(input("Math: "))
english=int(input("English: "))
science=int(input("Science: "))
language=int(input("Language: "))

sum=math+english+science+language
print("Total marks are", sum)

p=(sum/400)*100
print("Average Percentage: ", p)