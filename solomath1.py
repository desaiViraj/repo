from math import *
equation = list(input())
print("f(x)=",''.join(equation),'\n')
graph = list((chr(250)*7+'^'+chr(250)*7)*7+'^'*15+7*(chr(250)*7+'^'+chr(250)*7))
y_values = []
for i in range(-7,8):
    replace = '(' + str(i) + ')'
    if 'x' in equation:
        for j in range(len(equation)):
            if equation[j] == 'x':
                equation[j] = replace
        try:
            y_values.append(eval(''.join(equation)))
        except:
            y_values.append(20)
        for j in range(len(equation)):
            if equation[j] == replace:
                equation[j] = 'x'
    else:
        try:
            y_values.append(eval(''.join(equation)))
        except:
            y_values.append(20)
        for i in range(len(y_values)):
            try:
                if 112-int(abs(y_values[i]+20)/(y_values[i]+20)*7)-round(y_values[i])*15+i>=0:
                    if y_values[i] > 0:
                        graph[112-int(abs(y_values[i]+20)/(y_values[i]+20)*7)-round(y_values[i])*15+i] = '#'
                    else:
                        graph[105-round(y_values[i])*15+i] = '#'
            except:
                pass
        for i in range(0,len(graph),15):
            print(''.join(graph[i:i+15]))

            
    
