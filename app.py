from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

gimatriya_dict = {
    1488: 1,    # Aleph (א)
    1489: 2,    # Bet (ב)
    1490: 3,    # Gimel (ג)
    1491: 4,    # Dalet (ד)
    1492: 5,    # He (ה)
    1493: 6,    # Vav (ו)
    1494: 7,    # Zayin (ז)
    1495: 8,    # Het (ח)
    1496: 9,    # Tet (ט)
    1497: 10,   # Yod (י)
    1499: 20,   # Kaf (כ)
    1500: 30,   # Lamed (ל)
    1502: 40,   # Mem (מ)
    1504: 50,   # Nun (נ)
    1505: 60,   # Samekh (ס)
    1506: 70,   # Ayin (ע)
    1508: 80,   # Pe (פ)
    1510: 90,   # Tsadi (צ)
    1511: 100,  # Qof (ק)
    1512: 200,  # Resh (ר)
    1513: 300,  # Shin (ש)
    1514: 400,   # Tav (ת)

    1498 :20, #Kaf Sofith (ך)
    1501 :40, #Mem Sofith (ם)
    1503 :50, #Nun Sofith (ן)
    1507 :80, #Pe Sofith (ף)
    1509 :90, #Tsadi Sofith (ץ)
}

def gimatiya(the_text):
    total_value = 0
    for letter in the_text:
        letter_ASCII = ord(letter)
        if letter_ASCII in gimatriya_dict:
            letter_value = gimatriya_dict[letter_ASCII]
            total_value += letter_value
    return total_value

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    text = request.form['text']
    result = gimatiya(text)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)

