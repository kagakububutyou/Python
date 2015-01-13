#coding: UTF-8
import random
PlayerNumber = 56513 
EnemyNumber = 401
End = True 

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
	if len(num) != 3:
		return False 
	if num[0] == num[1] or num[0] == num[2] or num[1] == num[2]:
		return False
	return num.isdigit()
#EAT BITE 判定	
def Call(num1,num2):
	EAT = 0
	BITE = 0
	if num1[0] == num2[0]:
		EAT += 1
	if num1[1] == num2[1]:
		EAT += 1
	if num1[2] == num2[2]:
		EAT += 1
	if num1[0] == num2[1]:
		BITE += 1
	if num1[0] == num2[2]:
		BITE += 1
	if num1[1] == num2[0]:
		BITE += 1
	if num1[1] == num2[2]:
		BITE += 1
	if num1[2] == num2[0]:
		BITE += 1
	if num1[2] == num2[1]:
		BITE += 1
	print str(EAT) + "EAT " + str(BITE) + "BITE"	
	if EAT <  2:
		return True	
	if EAT >= 3:
		return False	
def EnemyNum():
	hoge = random.randint(100,999)
	while Number(str(hoge)) == False:
		hoge = random.randint(100,999)
def main():
	print u"違う数字を3桁入力してください"
	PlayerNumber = raw_input()
	while Number(PlayerNumber) == False:
		print u"違う数字を3桁入力してください"
		PlayerNumber = raw_input()
	#print hoge
	return Call(str(PlayerNumber),str(hoge))
			
#開始宣言
Numeron()
hoge = random.randint(100,999)
EnemyNum()
while main() == True:
	main()

print u"正解です"	
