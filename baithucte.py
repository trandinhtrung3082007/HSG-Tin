#Định mức tiền điện hàng tháng của một hộ gia đình như sau:
# + 50 kWh đầu tiên có giá là 600vnđ/1kWh.
# + 50 kWh tiếp theo có giá là 1004vnđ/1kWh.
# + 50 kWh tiếp theo nữa có giá là 1214vnđ/1kWh.
# Viết chương trình nhập chỉ số điện năng tiêu thụ cũ, chỉ số điện năng tiêu thụmới. 
# Hãy tính và in ra số điện năng tiêu thụ và tiền điện phải trả trong tháng của hộgia đình trên.
#  Mức giá này chưa bao gồm thuế giá trị gia tăng (VAT). Hãy viếtchương trình tính thuế VAT 10%.

n = int(input())
a = n -50
b = n - a 
print(b)
if n <=50:
    c = n*600
    vat = c/10
    print(vat)