import google.generativeai as g

file=open("C:\\Users\\A\\Desktop\\Python Programs\\Mygpt\\result.txt","w")

g.configure(api_key='AIzaSyCrbSe3rns4bVYbURGOswtira4UJUzKtSQ')

model = g.GenerativeModel('gemini-pro')

prompt=input("Enter  a question: ")


response = model.generate_content(prompt)

try:
    file.writelines(response.text)
    print("Operation successful")
except FileNotFoundError:
    print("Operation failed")
    
file.close()    