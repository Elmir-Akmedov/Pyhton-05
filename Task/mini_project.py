import time
# num1, num2 = (int(_) for _ in input("Enter the first and second number with space: ").split())
num1, num2 = map(int, input("Enter the first and second number with space: ").split())
print(num1 // num2) if num2 != 0 else print("Error: You can't divide by zero")

# nums = input("Enter the first and second number with space: ").split()
# if len(nums) != 2 or not nums[0].isdigit() or not nums[1].isdigit():
#     num1, num2 = int(nums[0]), int(nums[1])
#     if num2 == 0:
#         print("Error: You can't divide by zero")
#     else:
#         print(num1 // num2)
# else:
#     print("Error: Please enter two valid numeric values separated by space.")

# while True:
#     nums = [int(x if x.isdigit() else print("Error: Please enter valid numeric values separated by space.")) for x in input("Enter the first and second number with space: ").split()]
#     break
# start = time.time()
# # nums = input("Enter the first and second number with space: ").split()
# # print(int(nums[0]) // int(nums[1]))
# print("{} // {}".format([lambda x: int(x) in input("Enter the first and second number with space: ").split()]))
# end = time.time()
# print(end - start)
