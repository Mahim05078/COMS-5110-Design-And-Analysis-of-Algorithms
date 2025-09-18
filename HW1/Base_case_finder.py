import math

def lhs(n):
  return 32*math.log2(n)
def rhs(n):
  return n
def check_for_first_case(start=46, end=1000):
  """
    minimum value of n needed for the inductive step to hol was shown to be 46
    in the theoretical analysis.
    """
  for k in range(start, end):
        left = lhs(k)
        right = rhs(k)
        if(left <= right):
          print(f"First integer to satisfy the inequality: {k}")
          break

          
if __name__ == "__main__":
    check_for_first_case()
