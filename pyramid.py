
# for i in range(1,6):
#     for j in range(1,5):
#         print(1,end = "")
#     print()


# for i in range(1,6):
#     for j in range(1,5):
#         print('*',end = "")
#     print()


# for i in range(1,6):
#     for j in range(1,5):
#         print(i,end = "")
#     print()


# for i in range(1,6):
#     for j in range(1,5):
#         print(j,end = "")
#     print()


# for i in range(1,6):
#     for j in range(1,5):
#         print(j+4,end="")
#     print()
#

# for i in range(1,6):
#     for j in range(0,i):
#         print(j+1,end="")
#     print()

# for i in range(1,5):
#     for j in range(1,5-i):
#         print("*",end="")
#     print()


for i in range(1,7):
    for j in range(1,7):
        if j == 1 or i == 6 or i == 1 or j == 6 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()