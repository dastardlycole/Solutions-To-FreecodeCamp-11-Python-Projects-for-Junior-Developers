bill = float(input("What is the total bill for today?\r\n"))
calc_bill = bill * 100
eighteen_tip = 0.18 *calc_bill
eighteen_tip =round(eighteen_tip / 100, 2)
eighteen_total = round(eighteen_tip + bill,2)

twenty_tip = 0.2 * calc_bill
twenty_tip =round(twenty_tip / 100, 2)
twenty_total = round(twenty_tip + bill,2)

twenty_five_tip = 0.25 * calc_bill
twenty_five_tip =round(twenty_five_tip / 100, 2)
twenty_five_total = round(twenty_five_tip + bill,2)

num_of_people = int(input("How many people received the service?"))
each18 = round(eighteen_total/4,2)
each20 = round(twenty_total/4,2)
each25 = round(twenty_five_total/4,2)

print(f"18% tip is {eighteen_tip}, which brings your total to {eighteen_total}. Each person pays {each18}")
print(f"20% tip is {twenty_tip}, which brings your total to {twenty_total}. Each person pays {each20}")
print(f"25% tip is {twenty_five_tip}, which brings your total to {twenty_five_total}. Each person pays {each25}")
