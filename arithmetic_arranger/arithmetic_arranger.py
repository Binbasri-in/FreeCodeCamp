def arithmetic_arranger(problems, answer=False):
  if len(problems) > 5:
    return "Error: Too many problems."
  first_n = []
  second_n = []
  sign = []
  answer = []

  for problem in problems:
    problem = problem.split()
    if len(problem[0]) > 4:
      return "Error: Numbers cannot be more than four digits."
    first_n.append(problem[0])
    if len(problem[2]) > 4:
      return "Error: Numbers cannot be more than four digits."
    second_n.append(problem[2])
    if not problem[1] == '+' and not problem[1] == '-':
      return 'Error: Operator must be \'+\' or \'-\'.'
    sign.append(problem[1])
    if problem[1] == '+':
      try:
        answer.append(str(int(problem[0])+int(problem[2])))
      except:
        return "Error: Numbers must only contain digits."
    else:
      try:
        answer.append(str(int(problem[0])-int(problem[2])))
      except:
        return "Error: Numbers must only contain digits."
  line1 = ""
  line2 = ""
  line3 = ""
  line4 = ""

  for i in range(len(first_n)):
    l_1 = len(first_n[i])
    l_2 = len(second_n[i])
    space = l_2 - l_1
    if space > 0:
      add_space = ' ' * space
    else:
      add_space = ""
    line1 = line1 + '  '+ add_space + first_n[i] +'    '
    
    space = l_1 - l_2
    if space > 0:
      add_space = ' ' * space
    else:
      add_space = ""
    line2 = line2 + sign[i] + ' ' + add_space + second_n[i] + '    '
    if l_1 > l_2:
      dash = l_1
    else:
      dash = l_2

    line3 = line3 + ('-' * (2+dash)) + '    '
    if answer[i][0] == '-' or (len(answer[i]) > l_1 and len(answer[i]) > l_2):
      line4 = line4 + ' ' + answer[i]+ '    '
    else:
      line4 = line4 + '  ' + answer[i]+ '    '

  if answer == True:
    return f"{line1.rstrip()}\n{line2.rstrip()}\n{line3.rstrip()}\n{line4.rstrip()}"
  else:
    return f"{line1.rstrip()}\n{line2.rstrip()}\n{line3.rstrip()}"