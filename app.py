#D13oug
# Importando os módulos necessários do Flask
from flask import Flask, render_template, request, redirect, url_for, flash

# Criando uma instância do aplicativo Flask
app = Flask(__name__)

#app.static_folder = 'templates'

# Configurando uma chave secreta para proteger a sessão
app.secret_key = 'bb6db5c91c90a1a1788ea1f7323fdd0154c5b0a3008e9d3fa9c723e057e25b9c'
# Lista para armazenar as tarefas pendentes
tarefas = []

# Lista para armazenar o histórico de tarefas concluídas
historico_tarefas = []

# Definindo a rota principal, que renderiza a página inicial
@app.route('/')
def index():
    return render_template('index.html', tarefas=tarefas, historico_tarefas=historico_tarefas)

# Definindo a rota para adicionar uma nova tarefa
@app.route('/adicionar_tarefa', methods=['POST'])
def adicionar_tarefa():
    # Obtendo os dados do formulário
    tarefa = request.form['tarefa']
    categoria = request.form['categoria']

    # Adicionando uma classe CSS à tarefa com base na categoria
    if categoria == 'urgente':
        tarefa = f'<span class="bolinha vermelha"></span> {tarefa}'
    elif categoria == 'sem_pressa':
        tarefa = f'<span class="bolinha verde"></span> {tarefa}'
    elif categoria == 'com_prazo':
        tarefa = f'<span class="bolinha amarela"></span> {tarefa}'

    # Adicionando a tarefa à lista de tarefas
    tarefas.append(tarefa)

    # Exibindo uma mensagem de sucesso
    flash("Tarefa adicionada com sucesso!", 'success')

    # Redirecionando de volta para a página inicial
    return redirect(url_for('index'))

# Definindo a rota para marcar uma tarefa como concluída
@app.route('/marcar_concluida/<int:index>')
def marcar_concluida(index):
    if index < len(tarefas):
        # Removendo a tarefa da lista de tarefas pendentes
        tarefa_concluida = tarefas.pop(index)
        
        # Adicionando a tarefa ao histórico de tarefas concluídas
        historico_tarefas.append(tarefa_concluida)
        
        # Exibindo uma mensagem de sucesso
        flash("Parabéns por concluir mais uma tarefa", 'success')

    # Redirecionando de volta para a página inicial
    return redirect(url_for('index'))

# Definindo a rota para exibir o histórico de tarefas concluídas
@app.route('/historico')
def historico():
    return render_template('historico.html', historico_tarefas=historico_tarefas)

# Inicializando o aplicativo Flask
if __name__ == '__main__':
    app.run(debug=True)