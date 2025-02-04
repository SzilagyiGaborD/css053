import pytest
from bs4 import BeautifulSoup

def test_html_structure():
    with open("index.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
    
    assert soup.title.text == "Styled Text"
    assert soup.find("h1").text.strip() == "Lorem"
    assert len(soup.find_all("p")) == 3
    gray_box = soup.find("div", class_="gray-box")
    assert gray_box is not None
    assert gray_box.find("p") is not None
    assert "background-color: gray;" in str(soup)
