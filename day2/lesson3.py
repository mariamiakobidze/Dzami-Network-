grade = input("-")

match grade:
    case 'A':
        print ('Very Good Job')
    case 'B':
        print('Good Job')
    case 'C':
        print('Decent Job')
    case 'D':
        print('So Bad')
    case default:
        print('Input Correct Grade')