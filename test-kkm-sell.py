import win32com.client
import csv
import os 
os.system('cls' if os.name == 'nt' else 'clear')



if __name__ == '__main__':
	frDrv = win32com.client.Dispatch('Addin.DRvFR')
	frDrv.ComNumber = 3
	frDrv.BaudRate = 6
	frDrv.Timeout = 1000
	frDrv.Password = 30
	frDrv.ProtocolType = 0
	frDrv.ConnectionType = 0

	frDrv.Connect()

	csv_users = csv.reader(open('users.csv', "r"), delimiter=";")
	seller = input("Введите карту кассира:")
	for row in csv_users:
	#if current rows 2nd value is equal to input, print that row
		if seller == row[0]:
			seller_text = row[1]
			frDrv.TableNumber = 2
			frDrv.FieldNumber = 2
			frDrv.RowNumber = 1
			frDrv.ValueOfFieldString = seller_text
			frDrv.WriteTable()
			print ("Установлен кассир: ",seller_text)

	read_goods = True
	goods_list = []
	total_price=0
	while read_goods:
		barcode = str(input("Введите штрихкод (Enter для завершения):"))
		fcsv = open('list3.csv', "r")
		csv_goods = csv.reader(fcsv, delimiter=";") 
		if len(barcode)==0:
			read_goods = False
			break
		for row in csv_goods:
			if barcode == row[0]:
				print("Изделие: ", row[3])
				print("Вес: ",row[2])
				price = int(input("Укажите стоимость изделия:"))
				total_price += price
				goods_list.append([row[3],price])
				#print (len(goods_list))
		fcsv.close()
	for i in range(len(goods_list)):
		print(i+1,". ",goods_list[i][0], "цена: ",goods_list[i][1])
	print ("Выбрано изделий: ",len(goods_list)," на сумму: ",total_price)
	print ("Выбор способов оплаты: 1, Отмена чека: 0")
	command = int(input ("Введите код:"))
	if command==1:
		frDrv.Password = 1
		total_cash = int(input("Введите сумму наличными:"))
		total_card = int(input("Введите сумму по карте:"))
		if total_card+total_cash>=total_price:
			for i in range(len(goods_list)):
				frDrv.CheckType = 1
				frDrv.Price = goods_list[i][1]
				frDrv.Quantity = 1
				frDrv.Summ1Enabled = False
				#frDrv.Summ1 =
				frDrv.TaxValueEnabled = False
				frDrv.Tax1 = 4
				frDrv.Department = 1
				frDrv.PaymentTypeSign = 4
				frDrv.PaymentItemSign = 1
				frDrv.StringForPrinting = goods_list[i][0]
				frDrv.FNOperation()
				#evice.sale( (goods_list[i][0], 1000, (goods_list[i][1])*100), tax1=4)
			frDrv.Summ1 = total_cash
			frDrv.Summ2 = total_card
			frDrv.Summ3 = 0
			frDrv.Summ4 = 0
			frDrv.Summ5 = 0
			frDrv.Summ6 = 0
			frDrv.Summ7 = 0
			frDrv.Summ8 = 0
			frDrv.Summ9 = 0
			frDrv.Summ10 = 0
			frDrv.Summ11 = 0
			frDrv.Summ12 = 0
			frDrv.Summ13 = 0
			frDrv.Summ14 = 0
			frDrv.Summ15 = 0
			frDrv.Summ16 = 0
			frDrv.RoundingSumm = 0
			frDrv.TaxValue1 = 0
			frDrv.TaxValue2 = 0
			frDrv.TaxValue3 = 0
			frDrv.TaxValue4 = 0
			frDrv.TaxValue5 = 0
			frDrv.TaxValue6 = 0
			frDrv.TaxType = 8
			frDrv.StringForPrinting = ''
			frDrv.FNCloseCheckEx()
			#device.discount(0)
			#device.close_check(total_cash*100,total_card*100,0,0,0)
			#device.disconnect()