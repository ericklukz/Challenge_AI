from gtts import gTTS
from pygame import mixer
import pyttsx3
from bardapi import BardCookies
from flask import Flask, request

app = Flask(__name__)

query = ""

cookie_dict = {
    "__Secure-1PSID": "bwgxJWaf0xiNht761XuUAmxwCy-PA4z218JPRm5APIfm295tcmiHauBZW-iv5_FgZHgp3Q.",
    "__Secure-1PSIDTS": "sidts-CjIBNiGH7mS5Q9J-I3s-00xNPpWm2DI-MTZATEPJy5fenO6t_1NuveD59hWxrOgyH-7JUxAA",
}

bard = BardCookies(cookie_dict=cookie_dict)

@app.route('/receber-texto', methods=['POST'])
def receber_texto():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            if 'texto' in data:
                texto = data['texto']
                print(texto)
                query = texto + " Resuma em poucas palavras"
                resposta = bard.get_answer(query)['content']
                audio = gTTS(resposta, lang='pt')
                audio.save("resposta_bard.mp3")
                return resposta

            else:
                return "Chave 'texto' não encontrada nos dados JSON", 400
        else:
            return "A solicitação não contém dados JSON válidos", 400
    else:
        return "Método não suportado", 405

if __name__ == '__main__':
    app.run()
