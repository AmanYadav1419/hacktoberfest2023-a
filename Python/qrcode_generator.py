import qrcode
def convert(url):
    if url.startswith('http://'):
        return 'http://' + url[len('http://www.'):]
    if url.startswith('www.'):
        return 'https://' + url[len('www.'):]
    return f'https://www.{url}.com' if not url.startswith('https://') else url 
url=input("Enter a website name/url: ")
print(convert(url))
img=qrcode.make(url)
img.save("Qrcode.png","PNG")  
print("Qrcode generated")
