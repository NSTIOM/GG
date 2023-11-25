"""
การทำงาน
คำสั่ง import socket นำเข้าโมดูล socket ที่จำเป็นสำหรับการสร้างและใช้งาน Socket สำหรับการสแกนพอร์ต.

ฟังก์ชัน main() คือฟังก์ชันหลักของโปรแกรมที่ทำหน้าที่รับค่าอินพุตจากผู้ใช้และเรียกใช้ฟังก์ชันสแกนพอร์ตตามโหมดที่ผู้ใช้เลือก.

ในส่วนนี้:

โปรแกรมแสดงเมนูตัวเลือกสำหรับผู้ใช้เลือกโหมดสแกนที่ต้องการ (1: สแกนทุกพอร์ต, 2: สแกนพอร์ตที่ระบุล่วงหน้า).
ใช้ลูป while เพื่อตรวจสอบว่าผู้ใช้ป้อนตัวเลือกที่ถูกต้องหรือไม่ ถ้าไม่ถูกต้องโปรแกรมจะแสดงข้อความ "Invalid input, please try again." และให้ผู้ใช้ป้อนใหม่.
ผู้ใช้ถูกให้ป้อนที่อยู่ IP ที่ต้องการสแกนพอร์ต.

โค้ดส่วนนี้ทำการสแกนพอร์ตตามโหมดที่ผู้ใช้เลือก:

ในโหมด 1 (สแกนทุกพอร์ต), โค้ดนี้ทำการวนลูปผ่านพอร์ตทุกหมายเลขตั้งแต่ 1 ถึง 65535 และใช้ socket ในการเชื่อมต่อไปยังที่อยู่ IP แล้วตรวจสอบว่าพอร์ตนั้นเปิดหรือไม่ ถ้าเปิดโปรแกรมจะแสดงข้อความ "IP: [IP address], port [port number] is open" และหลังจากนั้นจะปิดการเชื่อมต่อ.

ในโหมด 2 (สแกนพอร์ตที่ระบุล่วงหน้า), โค้ดนี้จะวนลูปผ่านรายการของพอร์ตที่ระบุล่วงหน้า (common ports) และทำการสแกนพอร์ตในลิสต์ดังกล่าวเช่นเดียวกัน.

โปรแกรมสิ้นสุดการทำงานเมื่อผู้ใช้เลือกโหมดและสแกนเสร็จสมบูรณ์.

ในส่วนสุดท้ายของโปรแกรม (if __name__ == "__main__":), ฟังก์ชัน main() ถูกเรียกเมื่อโปรแกรมถูกเรียกใช้.
"""
import socket

def main():
    print('Option 1: Scan ports from 1 to 65535')
    print('Option 2: Scan common ports')
    while True:
        mode = input("Please enter an option: ")
        if mode == "1" or mode == "2":
            break
        else:
            print('Invalid input, please try again.')
            continue

    ip = input('Please enter the IP address: ')

    if mode == '1':
        for port in range(1, 65536):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            if not s.connect_ex((ip, port)):
                print('IP: %s, port %s is open' % (ip, port))
            s.close()
    else:
        common_ports = [20, 21, 22, 23, 53, 80, 161, 162, 443, 1234, 3389, 8080, 8086, 8888]
        for port in common_ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            if not s.connect_ex((ip, port)):
                print('IP: %s, port %s is open' % (ip, port))
            s.close()

if __name__ == "__main__":
    main()
