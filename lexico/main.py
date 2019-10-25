import sys
import re

file_name = open(sys.argv[1], 'r')
reservedWords = {'write' : 0, 'while' : 1, 'until' : 2, 'to' : 3, 'then' : 4, 'string' : 5, 'repeat' : 6, 'real' : 7, 'read' : 8, 'program' : 9, 'procedure' : 10, 'or' : 11, 'of' : 12, 'literal' : 13, 'integer' : 14, 'if' : 15, 'for' : 18, 'end' : 19, 'else' : 20, 'do' : 21,'declaravariaveis': 22, 'const' : 23, 'char' : 24, 'chamaprocedure' : 25, 'begin' : 26, 'array' : 27, 'and' : 28}


dictRegex = {'reservada|identificador':'^[A-Za-z]\w+$', 'literalInicio':'^\`', 'literalFim':'.*\`$', 'literalTotal':'^\`.*\`$', 'stringInicio':'^\"', 'stringFim':'.*\"$', 'stringTotal':'^\".*\"$', 'char' : '^\'.\'$', 'numReal' : '^-?\d+\.\d+$', 'numInteiro' : '^-?\d+$', '>=' : '^\>\=$', '>': '^\>$', '=' : '^\=$', '<>' : '^\<\>$', '<=' : '^\<\=$', '<' : '^\<$', '+' : '^\+$', ']' : '^\]$', '[' : '^\[$', ';' : '^;$', ':' : '^:$', '/' : '^\/$', '..' : '^\.\.$', '.' : '^\.$', ',' : '^,$', '*' : '^\*$', ')' : '^\)$', '(' : '^\($', '-' : '^-$', 'lineComment' : '^\/\/.*$', 'beginComment' : '^\/\*', 'endComment' : '\*\/$', 'blockComment' : '^\/\*.*\*\/$'}
output = ''
log = ''
strFlag = 0
strFlagLine = None
litFlag = 0
litFlagLine = None
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
                log += ('<nomestring, 38> identificado na linha {}\n'.format(strFlagLine))
                strFlag = 0
                strFlagLine = None
                output += '38-{} '.format(idx)
        elif litFlag:
            if re.match(dictRegex['literalFim'], element):
                log += ('<literal, 13> identificado na linha {}\n' .format(litFlagLine))
                litFlag = 0
                litFlagLine = None
                output += '13-{} '.format(idx)
        elif re.match(dictRegex['reservada|identificador'], element):
            if element in reservedWords.keys():
                log += ('<{}, {}> identificado na linha {}\n'.format(element, reservedWords[element], idx+1))
                output += str(reservedWords[element]) + '-{} '.format(idx) #Token dict palavra reservada
            else:
                log += ('<identificador, 16> identificado na linha {}\n'.format(idx+1))
                output += '16-{} '.format(idx) #Identificador
        elif re.match(dictRegex['stringTotal'], element):
            log += ('<nomestring, 38> identificado na linha {}\n'.format(idx+1))
            output += '38-{} '.format(idx)
        elif re.match(dictRegex['stringInicio'], element):
            strFlag = 1
            strFlagLine = idx+1
        elif re.match(dictRegex['literalTotal'], element):
            log += ('<literal, 13> identificado na linha {}\n' .format(idx+1))
            output += '13-{} '.format(idx)
        elif re.match(dictRegex['literalInicio'], element):
            litFlag = 1
            litFlagLine = idx+1
        elif re.match(dictRegex['char'], element):
            log += ('<nomechar, 39> identificado na linha {}\n'.format(idx+1))
            output += '39-{} '.format(idx)
        elif re.match(dictRegex['numReal'], element):
            element = float(element)
            if element <= 3.456789e+7 and element >= -3.456789e+7:
                log += ('<numreal, 36> identificado na linha {}\n'.format(idx+1))
                output += '36-{} '.format(idx)
            else:
                log += ('[ERRO] <{}> limite float na linha {}\n'.format(element, idx+1))
        elif re.match(dictRegex['numInteiro'], element):
            element = int(element)
            if element <= 2097152 and element >= -2097152:
                log += ('<numinteiro, 37> identificado na linha {}\n'.format(idx+1))
                output += '37-{} '.format(idx)
            else:
                log += ('[ERRO] <{}> limite integer na linha {}\n'.format(element, idx+1))
        elif re.match(dictRegex['>='], element):
            log += ('<{}, 29> identificado na linha {}\n'.format(element, idx+1))
            output += '29-{} '.format(idx)
        elif re.match(dictRegex['>'], element):
            log += ('<{}, 30> identificado na linha {}\n'.format(element, idx+1))
            output += '30-{} '.format(idx)
        elif re.match(dictRegex['='], element):
            log += ('<{}, 31> identificado na linha {}\n'.format(element, idx+1))
            output += '31-{} '.format(idx)
        elif re.match(dictRegex['<>'], element):
            log += ('<{}, 32> identificado na linha {}\n'.format(element, idx+1))
            output += '32-{} '.format(idx)
        elif re.match(dictRegex['<='], element):
            log += ('<{}, 33> identificado na linha {}\n'.format(element, idx+1))
            output += '33-{} '.format(idx)
        elif re.match(dictRegex['<'], element):
            log += ('<{}, 34> identificado na linha {}\n'.format(element, idx+1))
            output += '34-{} '.format(idx)
        elif re.match(dictRegex['+'], element):
            log += ('<{}, 35> identificado na linha {}\n'.format(element, idx+1))
            output += '35-{} '.format(idx)
        elif re.match(dictRegex[']'], element):
            log += ('<{}, 40> identificado na linha {}\n'.format(element, idx+1))
            output += '40-{} '.format(idx)
        elif re.match(dictRegex['['], element):
            log += ('<{}, 41> identificado na linha {}\n'.format(element, idx+1))
            output += '41-{} '.format(idx)
        elif re.match(dictRegex[';'], element):
            log += ('<{}, 42> identificado na linha {}\n'.format(element, idx+1))
            output += '42-{} '.format(idx)
        elif re.match(dictRegex[':'], element):
            log += ('<{}, 43> identificado na linha {}\n'.format(element, idx+1))
            output += '43-{} '.format(idx)
        elif re.match(dictRegex['/'], element):
            log += ('<{}, 44> identificado na linha {}\n'.format(element, idx+1))
            output += '44-{} '.format(idx)
        elif re.match(dictRegex['..'], element):
            log += ('<{}, 45> identificado na linha {}\n'.format(element, idx+1))
            output += '45-{} '.format(idx)
        elif re.match(dictRegex['.'], element):
            log += ('<{}, 46> identificado na linha {}\n'.format(element, idx+1))
            output += '46-{} '.format(idx)
        elif re.match(dictRegex[','], element):
            log += ('<{}, 47> identificado na linha {}\n'.format(element, idx+1))
            output += '47-{} '.format(idx)
        elif re.match(dictRegex['*'], element):
            log += ('<{}, 48> identificado na linha {}\n'.format(element, idx+1))
            output += '48-{} '.format(idx)
        elif re.match(dictRegex[')'], element):
            log += ('<{}, 49> identificado na linha {}\n'.format(element, idx+1))
            output += '49-{} '.format(idx)
        elif re.match(dictRegex['('], element):
            log += ('<{}, 50> identificado na linha {}\n'.format(element, idx+1))
            output += '50-{} '.format(idx)
        elif re.match(dictRegex['-'], element):
            log += ('<{}, 52> identificado na linha {}\n'.format(element, idx+1))
            output += '52-{} '.format(idx)
        elif re.match(dictRegex['lineComment'], element):
            break
        elif re.match(dictRegex['blockComment'], element):
            pass
        elif re.match(dictRegex['beginComment'], element):
            commentFlag = 1
        else:
            print('[ERRO] <{}> desconhecido na linha {}'.format(element, idx+1))
            flagError = 1

if strFlagLine:
    print('[ERRO] string não fechada na linha {}'.format(strFlagLine))
    flagError = 1
file_name.close()

if litFlagLine:
    print('[ERRO] literal não fechado na linha {}' .format(litFlagLine))
    flagError = 1

if commentFlag:
    print('[ERRO] comentário de bloco não fechado')
    flagError = 1

if not flagError:
    output_file = open('out.lex', 'w')
    output_file.write(output)
    output_file.close()

    log_file = open('log.txt', 'w')
    log_file.write(log)
    log_file.close()