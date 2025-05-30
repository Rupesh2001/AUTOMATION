from faker import Faker

fake = Faker()
name = fake.name()
address = fake.address()
Country_code = fake.country_code()
Text = fake.text()
postal_code = fake.postalcode()
print("The user name is ", name)
print("The address is ", address)
print("The country code is ",Country_code)
print("The text is generated from fake library ==>",Text)
print("The postal code is ", postal_code)
