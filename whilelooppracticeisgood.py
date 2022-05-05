"""
Simple loop program with while und
"""
read_count=0
book_count = 10
print("mother said 'Read all your books until you understand'")
understood_count = 0
print(f"the book i read is {understood_count}")

while read_count < book_count * 2 :
    read_count = read_count + 1
    if understood_count == 9:
        print(f"the 10th book don't understand")
    else:
        print(f"the number of books i read and i understand {understood_count + 1} ")
        understood_count = understood_count + 1

if read_count == book_count :
    print(f"ma'am I have read and I understand all books")
else :
    print(f"the only book i understand {understood_count}")
