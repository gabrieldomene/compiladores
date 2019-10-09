import sys
import re

file_name = open(sys.argv[1], 'r')
reservedWords = {'write' : 0, 'while' : 1, 'until' : 2, 'to' : 3, 'then' : 4, 'string' : 5, 'repeat' : 6, 'real' : 7, 'read' : 8, 'program' : 9, 'procedure' : 10, 'or' : 11, 'of' : 12, 'literal' : 13, 'integer' : 14, 'if' : 15, 'for' : 18, 'end' : 19, 'else' : 20, 'do' : 21,'declaravariaveis': 22, 'const' : 23, 'char' : 24, 'chamaprocedure' : 25, 'begin' : 26, 'array' : 27, 'end' : 28}


dictRegex = {'reservada|identificador':'^[A-Za-z]\w+$', 'stringInicio':'^\"', 'stringFim':'.*\"$', 'stringTotal':'^\".*\"$', 'char' : '^\'.\'$', 'numReal' : '^-?\d+\.\d+$', 'numInteiro' : '^-?\d+$', '>=' : '^\>\=$', '>': '^\>$', '=' : '^\=$', '<>' : '^\<\>$', '<=' : '^\<\=$', '<' : '^\<$', '+' : '^\+$', ']' : '^\]$', '[' : '^\[$', ';' : '^;$', ':' : '^:$', '/' : '^\/$', '..' : '^\.\.$', '.' : '^\.$', ',' : '^,$', '*' : '^\*$', ')' : '^\)$', '(' : '^\($', '-' : '^-$', 'lineComment' : '^\/\/.*$', 'beginComment' : '^\/\*', 'endComment' : '\*\/$', 'blockComment' : '^\/\*.*\*\/$'}
output = ''
strFlag = 0
strFlagLine = None
commentFlag = 0
flagError = 0
for idx, line in enumerate(file_name):
    line = re.sub('\t|\n', '', line)
    line_elements = line.split(' ')
    for idLine, element in enumerate(line_elements):
        if len(element) < 1:
            break
        if commentFlag:
            if re.match(dictRegex['endComment'], element):
                commentFlag = 0
        elif strFlag:
            if re.match(dictRegex['stringFim'], element):
                print('<nomestring, 38> identificado na linha {}' .format(strFlagLine))
                strFlag = 0
                strFlagLine = None
                output += '38 '
        elif re.match(dictRegex['reservada|identificador'], element):
            if element in reserverdWords.keys():
                print('<{}, {}> identificado na linha {}' .format(element, reservedWords[element], idx+1))
                output += str(reservedWords[element]) + ' ' #Token dict palavra reservada
            else:
                print('<identificador, 16> identificado na linha {}' .format(idx+1))
                output += '16 ' #Identificador
        elif re.match(dictRegex['stringTotal'], element):
            print('<nomestring, 38> identificado na linha {}' .format(idx+1))
            output += '38 '
        elif re.match(dictRegex['stringInicio'], element):
            strFlag = 1
            strFlagLine = idx+1
        elif re.match(dictRegex['char'], element):
            print('<nomechar, 39> identificado na linha {}' .format(idx+1))
            output += '39 '
        elif re.match(dictRegex['numReal'], element):
            element = float(element)
            if element <= 3.456789e+7 and element >= -3.456789e+7:
                print('<numreal, 36> identificado na linha {}' .format(idx+1))
                output += '36 '
            else:
                print('[ERRO] <{}> limite float na linha {}' .format(element, idx+1))
        elif re.match(dictRegex['numInteiro'], element):
            element = int(element)
            if element <= 2097152 and element >= -2097152:
                print('<numinteiro, 37> identificado na linha {}' .format(idx+1))
                output += '37 '
            else:
                print('[ERRO] <{}> limite integer na linha {}' .format(element, idx+1))
        elif re.match(dictRegex['>='], element):
            print('<{}, 29> identificado na linha {}' .format(element, idx+1))
            output += '29 '
        elif re.match(dictRegex['>'], element):
            print('<{}, 30> identificado na linha {}' .format(element, idx+1))
            output += '30 '
        elif re.match(dictRegex['='], element):
            print('<{}, 31> identificado na linha {}' .format(element, idx+1))
            output += '31 '
        elif re.match(dictRegex['<>'], element):
            print('<{}, 32> identificado na linha {}' .format(element, idx+1))
            output += '32 '
        elif re.match(dictRegex['<='], element):
            print('<{}, 33> identificado na linha {}' .format(element, idx+1))
            output += '33 '
        elif re.match(dictRegex['<'], element):
            print('<{}, 34> identificado na linha {}' .format(element, idx+1))
            output += '34 '
        elif re.match(dictRegex['+'], element):
            print('<{}, 35> identificado na linha {}' .format(element, idx+1))
            output += '35 '
        elif re.match(dictRegex[']'], element):
            print('<{}, 40> identificado na linha {}' .format(element, idx+1))
            output += '40 '
        elif re.match(dictRegex['['], element):
            print('<{}, 41> identificado na linha {}' .format(element, idx+1))
            output += '41 '
        elif re.match(dictRegex[';'], element):
            print('<{}, 42> identificado na linha {}' .format(element, idx+1))
            output += '42 '
        elif re.match(dictRegex[':'], element):
            print('<{}, 43> identificado na linha {}' .format(element, idx+1))
            output += '43 '
        elif re.match(dictRegex['/'], element):
            print('<{}, 44> identificado na linha {}' .format(element, idx+1))
            output += '44 '
        elif re.match(dictRegex['..'], element):
            print('<{}, 45> identificado na linha {}' .format(element, idx+1))
            output += '45 '
        elif re.match(dictRegex['.'], element):
            print('<{}, 46> identificado na linha {}' .format(element, idx+1))
            output += '46 '
        elif re.match(dictRegex[','], element):
            print('<{}, 47> identificado na linha {}' .format(element, idx+1))
            output += '47 '
        elif re.match(dictRegex['*'], element):
            print('<{}, 48> identificado na linha {}' .format(element, idx+1))
            output += '48 '
        elif re.match(dictRegex[')'], element):
            print('<{}, 49> identificado na linha {}' .format(element, idx+1))
            output += '49 '
        elif re.match(dictRegex['('], element):
            print('<{}, 50> identificado na linha {}' .format(element, idx+1))
            output += '50 '
        elif re.match(dictRegex['-'], element):
            print('<{}, 52> identificado na linha {}' .format(element, idx+1))
            output += '52 '
        elif re.match(dictRegex['lineComment'], element):
            break
        elif re.match(dictRegex['blockComment'], element):
            pass
        elif re.match(dictRegex['beginComment'], element):
            commentFlag = 1
        else:
            print('[ERRO] <{}> desconhecido na linha {}' .format(element, idx+1))
            flagError = 1

if strFlagLine:
    print('[ERRO] string não fechada na linha {}' .format(strFlagLine))
    flagError = 1
file_name.close()

if commentFlag:
    print('[ERRO] comentário de bloco não fechado')
    flagError = 1

if not flagError:
    output_file = open('out.lex', 'w')
    output_file.write(output)
    output_file.close()
