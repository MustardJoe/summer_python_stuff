def solution(a, b):
  if (len(a) <= len(b)):
    print(a+b+a)
    return a+b+a
  elif (len(b) < len(a)):
    print(b+a+b)
    return b+a+b

solution("1bosco", "22")