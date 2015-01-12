#coding: UTF-8

PlayerNumber = 56513 

#開始宣言
def Numeron():
	hoge = u"Numer0nを開始します"
	print hoge
#入力
def Input():
	print u"違う数字を3桁入力してください"
	PlayerNumber = raw_input()
	return PlayerNumber 

#数字が入力されたのかの確認
def Number(num):
		print num 
		if len(num) != 3:
				return False 
		if num[0] == num[1] or num[0] == num[2] or num[1] == num[2]:
				return False
		print num.isdigit()
		return num.isdigit()

Numeron()
print u"違う数字を3桁入力してください"
PlayerNumber = raw_input()
while Number(PlayerNumber) == False:
	print u"違う数字を3桁入力してください"
	PlayerNumber = raw_input()
print PlayerNumber 
