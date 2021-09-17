print('Hello World')
naam = input('naam: ')
print('hallo ' + naam)
age = input('hoe oud ben je? ')
confirm = input('dus je bent ' + age + ' jaar oud? ')
if confirm == 'ja':
	print('nice')
elif confirm == 'nee':
	age2 = input('hoe oud ben je dan?: ')
	print('je bent ' + age2 + ' jaar oud')
huisdier = input('heb je huisdieren? ')
if huisdier == 'ja':
	huisdier2 = input('wat voor huisdier heb je? ')
	if huisdier2 == 'hond':
		ras = input = ('wat voor ras is je hond? ')				
		print('je naam is ' + naam + ' je bent ' + age + ' jaar oud, je heb een hond, met het ras ' + ras)
elif huisdier == 'nee':
    huisdier3 = input('wil je een huisdier? ')
    if huisdier3 == 'ja':
        huisdier4 = input('wat voor huisdier wil je? ')
        huisdier5 = input('dus je wil een ' + huisdier4)
        if huisdier5 == 'ja':
            print('je naam is ' + naam + ' je bent ' + age + ' jaar oud en je wilt een ' + huisdier4 + ' als huisdier')
    elif huisdier4 == 'nee':
        print('je naam is ' + naam + ' je bent ' + age + 'jaar oud en je wilt geen huisdieren')
