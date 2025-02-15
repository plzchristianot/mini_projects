#This is an arithmetic formatter, please use it this way: arithmetic_arranger(["3801 - 2", "123 + 49"])

def arithmetic_arranger(problems, show_answers=False):
    
    if len(problems)>5:
        return "Error: Too many problems."
    linea1 = ""
    linea2 = ""
    dash = ""
    results = ""
    for caracter in problems:
        suma = caracter.split()
        num1_str,op_str,num2_str = suma 

        if op_str not in ("+","-"):
            return "Error: Operator must be '+' or '-'."
        if not suma[0].isdigit():
            return 'Error: Numbers must only contain digits.'
        if not suma[2].isdigit():
            return 'Error: Numbers must only contain digits.'
        #operation
        if len(num1_str) and len(num2_str) > 4 :
            return 'Error: Numbers cannot be more than four digits.'

        lenght = max(len(num1_str),len(num2_str)) + 2
        #suma0_right=num1_str.rjust(lenght)
        ##suma2_right=num2_str.rjust(lenght)
        
        linea1 += num1_str.rjust(lenght) + "    "
        linea2 += op_str + num2_str.rjust(lenght - 1) + "    "
        dash += "-" * lenght + "    "

        result = str(eval(caracter))
        results += result.rjust(lenght) + "    "

        final = linea1.rstrip() + "\n" + linea2.rstrip() + "\n" + dash.rstrip()
        final_with_result = final + "\n" + results.rstrip()
    
    if show_answers == True:
        return final_with_result
    else:
        return final