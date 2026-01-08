from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Lógica de D&D: (Valor - 10) // 2
def calcular_modificador(valor):
    try:
        return (int(valor) - 10) // 2
    except:
        return 0

@app.route('/')
def index():
    # Dados iniciais da ficha
    personagem = {
        "nome": "Aragorn",
        "forca": 16,
        "destreza": 14,
        "constituicao": 15
    }
    
    # Calcula modificadores para enviar ao HTML
    mods = {attr: calcular_modificador(val) for attr, val in personagem.items() if attr != "nome"}
    
    return render_template('ficha.html', char=personagem, mods=mods)

if __name__ == '__main__':
    app.run(debug=True)
