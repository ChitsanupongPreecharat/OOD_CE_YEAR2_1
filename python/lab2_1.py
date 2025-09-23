class translator:

    def deciToRoman(self, num):
        result = ''
        dic = {1000:"M",900:"CM",500:"D",400:"CD",100:"C",90:"XC",50:"L",40:"XL",10:"X",9:"IX",5:"V",4:"IV",1:"I"}
        for value in dic:
            while num >= value:
                result += dic[value]
                num -= value
        return result        

    def romanToDeci(self, s):
        result = 0
        dic = {"M": 1000, "CM": 900, "D": 500, "CD": 400,"C": 100, "XC": 90, "L": 50, "XL": 40,"X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}
        
        i = 0
        while i < len(s):
            if i + 1 < len(s) and s[i:i+2] in dic:
                result += dic[s[i:i+2]]
                i+=2
            else:
                result += dic[s[i]]
                i +=1    
        return result
        

num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))

print(translator().romanToDeci(translator().deciToRoman(num)))