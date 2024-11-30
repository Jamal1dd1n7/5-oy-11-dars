from database import db 

if __name__ == "__main__":
    while True:
        print("Buyruqlar: \n"
            "1 -> Categories jadvalini yaratish.\n"
            "2 -> News jadvalini yaratish.\n"
            "3 -> Comments jadvalini yaratish.\n"
            "4 -> Add Column Views - news jadvaliga yangi ustun qo'shish.\n"
            "5 -> Change Type comments - comments jadvalidagi author_name ustuni ma'lumot turini o'zgartirish.\n"
            "6 -> Insert Categories - categories jadvaliga ma'lumot qo'shish.\n"
            "7 -> Insert News - news jadvaliga ma'lumotlar qo'shish.\n"
            "8 -> Insert Comments - comments jadvaliga ma'lumotlar qo'shish.\n"
            "9 -> Increase Views - news jadvalidagi ko'rishlar sonini yangilash.\n"
            "10 -> Select Alias - alias ustunidan foydalanib ma'lumotlarni chiqarish.\n"
            "11 -> Select Technology - technology kategoriyasidagi yangiliklarni chiqarish.\n"
            "12 -> Update Is_Published - is_published ustunini yangilash.\n"
            "13 -> Delete Old Comments - yaratilganiga 1 yil bo'lgan izohlarni o'chirib tashlash.\n"
            "14 -> Sorted News - tartiblangan yangiliklani chiqarish.\n"
            "15 -> Select Filtered Views - 10 va 100 orasidagi ko'rishlar soniga ega xabarlarni chiqarish.\n"
            "16 -> Select A - A harfi bilan boshlangan author_name ni chiqaradi.\n"
            "17 -> Select Null - author_name null bo'lgan comment larni olib berish.\n"
            "18 -> Select Categories - categoriyalarda nechtadan yangiliklar borligini ko'rish.\n"
            "19 -> Add Constraint - news jadvalidagi title ustuniga unique cheklovini o'rnatish.")
        command = int(input("Buyruq raqamini kiriting: "))
        if command == 1:
            db.create_table_categories()
            print("Jadval yaratildi")
        elif command == 2:
            db.create_table_news()
            print("Jadval yaratildi")
        elif command == 3:
            db.create_table_comments()
            print("Jadval yaratildi")
        elif command == 4:
            try:
                db.alter_table_news()
                print("Jadvalga yangi ustun qo`shildi")
            except:
                print("Jadvalga yangi ustun qo`shilmadi")
        elif command == 5:
            try: 
                db.alter_table_comments()
                print("Coments jadvalidagi author_name ustuni type i TEXT type ga o`zgartirildi")
            except:
                print("Coments jadvalidagi author_name ustuni type i TEXT type ga o`zgartirilmadi")
        elif command == 6:
            try:
                count = int(input("Nechta categoriya kiritmoqchisiz: "))
                for i in range(count):
                    print("Categories jadvaliga ma`lumot kiritish yo`li: \n | categoriya nomi |, | categoriya haqida |")
                    category_name = input("Categoriyaga nom bering: ")
                    category_about = input("Categoriya haqida narsa yozing: ")
                    db.insert_categories(category_name, category_about)
                    print("Categories table ga ma`lumot qo`shildi")
            except Exception as e:
                print(f"Categories table ga ma`lumot qo`shilmadi \n{e}")
        elif command == 7:
            try:
                news_count = int(input("Nechta yangilik kiritmoqchisi: "))
                for i in range(news_count):
                    print("News jadvaliga ma`lumot kiritish yo`li: \n| yangilik nomi | | yangilik tavfsilotlari |")
                    news_name = input("Yangilik nomini kiriting: ")
                    news_about = input("Yangilik haqida ma`lumot kiriting: ")
                    db.insert_news(news_name, news_about)
                    print("News jadvaliga ma`lumot qo`shildi")
            except Exception as e:
                print(f"News jadvaliga ma`lumot qo`shildi \n{e}")
        elif command == 8:
            try:
                db.sorted_news()
                comment_id = int(input("Qaysi xabarga koment yozmoqchisiz(raqamini kiriting): "))
                if comment_id >= 1:
                    name = input("Ismingizni kiriting: ")
                    if name != '': 
                        comment = input("Komment yozing: ")
                        if comment != '':
                            print("Koment qo`shildi")
                    else:
                        print("Ismingizni kiriting")
                else:
                    print("Koment id kiritilmagan")
                db.insert_comments(comment_id, name, comment)
            except Exception as e:
                print(f"Koment qo`shilmadi \n{e}")
        elif command == 9:
            try:
                db.increase_news()
                print("Ko`rishlar soni yangilandi")
            except Exception as e:
                print(f"Ko`rishlar soni yangilanmadi \n{e}")
        elif command == 10:
            try:
                for i in db.select_alias():
                    print(i)
            except Exception as e:
                print(f"Jadvallar yaratilmagan!\n{e}")
        elif command == 11:
            try:
                for i in db.select_technology():
                    print(i)
            except Exception as e:
                print(f"Technolog categoriyasi yaratilmagan!\n{e}")
        elif command == 12:
            try:
                db.update_is_published()
                print("Ma'lumotlar yangilandi!")
            except Exception as e:
                print(f"Yangilash uchun ma'lumot mavjud emas!: {e}")
        elif command == 13:
            try:
                db.delete_old_comments()
                print("Izohlar o'chirildi!")
            except Exception as e:
                print(f"O'chirish uchun comments mavjud emas!\n{e}")
        elif command == 14:
            try:
                for i in db.sorted_news():
                    print(i)
            except Exception as e:
                print(f"Jadval yaratilmagan!\n{e}")
        elif command == 15:
            try:
                for i in db.select_views():
                    print(i)
            except Exception as e:
                print(f"Jadval yaratilmagan!\n{e}")
        elif command == 16:
            try:
                for i in db.select_capital_a('A%'):
                    print(i)
            except Exception as e:
                print(f"Jadval yaratilmagan!\n{e}")
        elif command == 17:
            try:
                for i in db.select_null():
                    print(i)
            except Exception as e:
                print(f"Jadval mavjud emas!\n{e}")
        elif command == 18:
            try:
                for i in db.select_categories():
                    print(i)
            except Exception as e:
                print(f"Categories jadvali mavjud emas!\n{e}")
        elif command == 19:
            try:
                db.add_constraint()
                print("Cheklov o'rnatildi!")
            except Exception as e:
                print(f"Cheklov qo'yish uchun jadval mavjud emas!\n{e}")

        else:
            print("Mavjud bo'lmagan buyruq kiritildi!")                
    


                






