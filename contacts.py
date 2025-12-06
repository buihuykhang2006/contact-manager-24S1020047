# Danh sách toàn cục
phonebook = []


def show_menu():
    print("==== PHONEBOOK MENU ====")
    print("1. Thêm liên hệ")
    print("2. Hiển thị danh sách")
    print("3. Tìm kiếm liên hệ")
    print("4. Thoát")
    print("========================")


def main():
    while True:
        show_menu()
        choice = input("Nhập lựa chọn: ")

        if choice == "1":
            name = input("Nhập tên: ")
            phone = input("Nhập số điện thoại: ")
            phonebook.append({"name": name, "phone": phone})
            print(">> Đã thêm liên hệ!\n")

        elif choice == "2":
            print("=== DANH SÁCH LIÊN HỆ ===")
            for p in phonebook:
                print(f"- {p['name']} : {p['phone']}")
            print()

        elif choice == "3":
            keyword = input("Nhập tên cần tìm: ")
            result = [p for p in phonebook if keyword.lower() in p["name"].lower()]
            if result:
                print(">> KẾT QUẢ TÌM KIẾM:")
                for p in result:
                    print(f"- {p['name']} : {p['phone']}")
            else:
                print(">> Không tìm thấy liên hệ nào!")
            print()

        elif choice == "4":
            print("Thoát chương trình...")
            break
        else:
            print("Lựa chọn không hợp lệ!\n")


# Chạy chương trình
if __name__ == "__main__":
    main()
phonebook = []   # danh sách toàn cục

def add_contact(name, phone):
    contact = {
        'name': name,
        'phone': phone
    }
    phonebook.append(contact)
    print(">> Đã thêm liên hệ thành công!")
    
    phonebook = []   # danh sách toàn cục

def view_contacts():
    if len(phonebook) == 0:
        print(">> Danh sách liên hệ trống!")
        return

    print("=== DANH SÁCH LIÊN HỆ ===")
    for contact in phonebook:
        print(f"- {contact['name']} : {contact['phone']}")

phonebook = []   # danh sách toàn cục

def Contacts(name):
    found = False

    for contact in phonebook:
        if contact['name'].lower() == name.lower():
            print(f"Số điện thoại của {contact['name']}: {contact['phone']}")
            found = True
            break

    if not found:
        print("Không tìm thấy")

