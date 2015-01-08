#coding: UTF-8

#開始宣言
def Numeron():
	hoge = u"Numer0nを開始します"
	print hoge
#入力
def Input():
	print u"数字を3桁入力してください"
	a = raw_input()
	return a

#数字が入力されたのかの確認
def Number(num):
		print u"3"
		print num.isdigit()
		return num.isdigit()

Numeron()
print u"1"
while Number(Input()) == False:
		Input()
print u"2"
