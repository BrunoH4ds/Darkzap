# Darkzap

Este é um aplicativo de chat simples usando Flask e Socket.IO para permitir a comunicação em tempo real entre clientes conectados. Ele suporta o envio de mensagens para todos os usuários conectados ao servidor.

## Funcionalidades
Envio de mensagens em tempo real
Mensagens são transmitidas para todos os usuários conectados
Utiliza Flask para o backend e Socket.IO para comunicação
## Instalação
**Pré-requisitos**
- Python 3
- Flask
- Flask-SocketIO

Instale as dependências:

    pip install Flask Flask-SocketIO
## Uso
1. Clone este repositório:
    ```bash
    git clone https://github.com/BrunoH4ds/Darkzap.git
2. Navegue até o diretório e execute o aplicativo:
      ```bash
    cd Darkzap
    python main.py
Acesse http://(IPHospedado):5001 no seu navegador para usar o chat.

**OBS:** o IP em que a aplicacao fica hospedada e dada automaticamente com a execucao do main.py
## Estrutura
- main.py: Código principal da aplicação Flask.
- templates/index.html: Interface HTML do chat.
## Contribuições
Contribuições são bem-vindas! Para mudanças maiores, abra uma issue para discussão.

## Licença
Este projeto está licenciado sob a MIT License.
