n = int(input())
ans = 0
for _ in range(n):
    num = int(input())
    ans = ans ^ num
print(ans)

# time : O(n)
# space: O(1) since we are not consuming any extra space that depends on input size
