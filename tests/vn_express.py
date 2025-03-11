import requests
from bs4 import BeautifulSoup

url = "https://vnexpress.net/goc-nhin"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    paragraphs = soup.find_all(["p", "h1", "h2", "h3"])  # Lấy tiêu đề và đoạn văn
    for para in paragraphs:
        print(para.get_text(strip=True))  # Giữ nguyên cách xuống hàng
    
else:
    print("Không thể lấy dữ liệu từ trang web")
