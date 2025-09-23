# ให้นักศึกษาเขียนโปรแกรมภาษา Python ในการใช้ Class สำหรับ “เกมต่อคำ” โดยจะมีกติกาดังต่อไปนี้

 
# 1. คำล่าสุดจะต้องไม่ซ้ำกับคำที่เคยพูดไปแล้ว เช่นถ้าหากมีคนพูดว่า “Apple” ไปก่อนหน้านั้นแล้ว
# จะไม่สามารถพูดว่า “Apple” ได้อีก


# 2. โดยการดูว่า 2 คำนั้นจะ Match กันหรือไม่ ให้ดู 2 ตัวอักษรสุดท้ายของข้อความสุดท้ายใน List กับ 2
# ตัวอักษรแรก ของคำล่าสุด เช่น [“Apple”, “lemon”] ถ้าหากคำที่จะเข้ามาเป็น “Onion” จะถือว่า Match
# แต่ถ้าหากคำที่เข้ามาเป็น “nectarine” จะถือว่าไม่ Match และเกมจะจบลงทันที


# 3. Ignore Case Sensitive


# โดยจะมีรูปแบบคำสั่งดังต่อไปนี้
# - P < word > จะเป็นการต่อคำ
# - R จะเป็นการเริ่มคำใหม่ทั้งหมด
# - X เป็นการระบุว่าจบการทำงาน

# โดยใช้ class รูปแบบดังนี้

class TorKham:

	def __init__(self):

		self.words = []

	def restart(self):

		self.words.clear()

		return "game restarted"

	def play(self, word):
		if not self.words :
			self.words.append(word)
			return f"'{word}' -> {self.words} "
		elif self.words[-1][-2:].lower() == word[:2].lower():
			self.words.append(word)
			return f"'{word}' -> {self.words} "
            
		return f"'{word}' -> game over"
            
	



torkham = TorKham()

print("*** TorKham HanSaa ***")


S = input("Enter Input : ").split(',')

for s in S:
    if s.startswith("P"):  
        a, b = s.split()
        print(torkham.play(b))
    elif s.startswith("R"):  
        print(torkham.restart())
    elif s.startswith("X"):
        break
    else:
        print(f"'{s}' is Invalid Input !!!")
        break 


		

