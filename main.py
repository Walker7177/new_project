menu = int(input("Enter number(Press 1 to get information): "))

if menu == 1:
    print('2 for sending message, 3 to get information about device')
elif menu == 2:
    phone1 = input('Enter phone number you want to message: ')
    message1 = input('Enter the message you want to send: ')
    data = {
    'key': 'e621422587543386d9d3c82419bb2c27ee0a1f9f',
    'phone': phone1,
    'message': message1,
    'device': '3304',
    'sim': '1'

    }
req = requests.post('https://smstel.ru/api/send', params = data)

print(req.json())
