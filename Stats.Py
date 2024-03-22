def median(numbers):
numbers = sorted(numbers)
n = len(numbers)
m = n // 2
if n % 2 == 0:
return (numbers[m - 1] + numbers[m]) / 2.0
else:
return numbers[m]
def mode(numbers):
if len(numbers) == 0:
return 0
else:
return max(numbers, key=numbers.count)
def mean(numbers):
if len(numbers) == 0:
return 0
else:
return sum(numbers) / float(len(numbers))
We will now test these functions using the list [3, 1, 7, 1, 4, 10] defined in main using the below code:
def main():
nums = [3, 1, 7, 1, 4, 10]
print("List: ", nums)
print("Median: ", median(nums))
print("Mode: ", mode(nums))
print("Mean: ", mean(nums))
if __name__ == "__main__":
main()
Output:
List: [3, 1, 7, 1, 4, 10]