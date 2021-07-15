number = int(input())
num_dict = {
    1000000000 : "Billion",
    1000000 : "Million",
    1000 : "Thousand",
    1 : "One"
}
digits_1s =  ["Zero", "One", "Two", "Three", "Four", "Five", "Six","Seven", "Eight", "Nine","Ten",
"Eleven", "Twelve","Thirteen", "Fourteen", "Fifteen", "Sixteen","Seventeen", "Eighteen", "Nineteen"]
digits_2 = ["Twenty", "Thirty", "Forty", "Fifty","Sixty", "Seventy", "Eighty", "Ninety","Hundred"]

if number > 0:
    result = ""
    for k,v in num_dict.items():
        num1 = number // int(k)
        res1 = number % int(k)
        if num1 >=100:
            num_1 = num1 // 100
            res_1 = num1 % 100 
            
            if res_1== 0 :
                if k > 1:
                    result += digits_1s[num_1]+" "+digits_2[-1]+" "+ num_dict[k]+ " "
                else:
                    result += digits_1s[num_1]+" "+digits_2[-1]+" "
            
            else :
                if 20 > res_1 > 10:
                    result += digits_1s[num_1]+" "+digits_2[-1]+" "+digits_1s[res_1]+" "
                else:
                    num_2 = res_1 //10 
                    res_2 = res_1 % 10 
                    if res_2 ==0:
                        if k > 1:
                            if num_2 >1:
                                result += digits_1s[num_1]+" "+digits_2[-1]+" "+digits_2[num_2-2]+" " +num_dict[k]+ " "
                            else:
                                result += digits_1s[num_1]+" "+digits_2[-1]+" "+digits_1s[num_2]+" " +num_dict[k]+ " "
                        else:
                            if num_2>1:
                                result += digits_1s[num_1]+" "+digits_2[-1]+" "+digits_2[num_2-2]+" " 
                            else:
                                result += digits_1s[num_1]+" "+digits_2[-1]+" "+digits_1s[res_1]+" "
                    else:
                        if k >1:
                            if num_2 >1:
                                result += digits_1s[num_1]+" "+digits_2[-1]+" "+digits_2[num_2-2]+"-"+digits_1s[res_2]+" "  +num_dict[k]+" "
                            else:
                                result += digits_1s[num_1]+" "+digits_2[-1]+" "+digits_1s[res_1]+" "  +num_dict[k]+" "
                        
                        else :
                            if num_2 >1:
                                result += digits_1s[num_1]+" "+digits_2[-1]+" "+digits_2[num_2-2]+"-"+digits_1s[res_2]+" "
                            else:
                            
                                result += digits_1s[num_1]+" "+digits_2[-1]+" "+digits_1s[res_2]+" "
                            #print(result)
        elif 100 > num1 >=20:
            num_1 = num1 //10 
            #print(num_1)
            res_1 = num1 % 10
            if res_1 == 0:
                if  num_1 > 1 :
                    if k >1:
                        result += digits_2[num_1-2]+" "+num_dict[k]+" "
                    else:
                        result += digits_2[num_1-2]+" "
                        
                else:
                    result += digits_1s[num1]+" "+num_dict[k]+" "
                    #print(result)
            else :
                if k >1:
                    if num_1 > 1:
                        result += digits_2[num_1-2]+" " +num_dict[k]+" "+digits_1s[res_1]+" "
                    else:
                        result += digits_2[num_1-2]+" " +num_dict[k]+" "
                else:
                    if num_1 > 1:
                        result += digits_2[num_1-2]+" "+digits_1s[res_1]+" "
                    else:
                        result += digits_1s[num1]+" "
                #print(result)
            
        elif 20 > num1 >=1 :
            if  k >1:
                result += digits_1s[num1] +" "+ num_dict[k]+" "
            else:
                result += digits_1s[num1] +" "
        number = res1    
    print(result+"dollars")
else:
    print("Zero")