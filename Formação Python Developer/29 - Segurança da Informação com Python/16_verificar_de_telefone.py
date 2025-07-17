import phonenumbers

from phonenumbers import geocoder

phone = input('Digite o número do telefone no formato +5511961761340: ')

phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, 'pt'))
