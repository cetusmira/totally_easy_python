#section_01.py

def isPhoneNumber(text):
    
    for i in range(0, 3):               # '010'
        if not text[i].isdecimal():
            return False
        
    if text[3] != '-':                  # '-'
        return False
    
    for i in range(4, 8):               # '1234'
        if not text[i].isdecimal():
            return False
        
    if text[8] != '-':                  # '-'
        return False
    
    for i in range(9, 13):              # '5678'
        if not text[i].isdecimal():
            return False
        
    return True
           
message = '''
그의 전화번호는 010-1234-5678이에요.
그리고 제 번호는 010-2345-6789구요.
아 참, 제 ID는 245-08이에요. 
현지 시각 13시 정각에 원하는 번호로 연락주세요.'''
print(message)
print()

for i in range(len(message)):
    chunk = message[i:i+13]
    if len(chunk) < 13:
        break
    if isPhoneNumber(chunk):
        print('발견된 전화번호: ' + chunk)

print('프로그램 종료')
