# Projeto Monsten
# Sistema de Votação de Filmes e Séries

Este projeto é uma aplicação web completa que permite aos usuários votar em filmes e séries, registrando votos positivos e negativos. Também possibilita o cadastro de novos títulos, armazenamento persistente dos dados e exibição dos totais de votos por item e no geral.

---

## Funcionalidades

- Exibição inicial de filmes e séries com título, gênero, descrição e imagem.  
- Botões interativos para registrar votos de "Gostei" e "Não Gostei", atualizando os contadores instantaneamente.  
- Cadastro de novos filmes ou séries com campos obrigatórios e opcionais.  
- Persistência dos dados utilizando banco SQLite.  
- Totais gerais de votos positivos e negativos exibidos em tempo real.  
- Comunicação entre front-end e back-end via API RESTful, garantindo integração dinâmica.

---

## Tecnologias Utilizadas

- **Back-end:** Python 3, Flask, SQLite, Flask-CORS  
- **Front-end:** HTML5, CSS3, JavaScript (Fetch API)

---

## Como Executar o Projeto

1. Clone este repositório:  
   ```bash
   git clone <url-do-repositorio>  
   cd <pasta-do-projeto>  
   ```

2. Configure o ambiente virtual e instale as dependências:  
   ```bash
   python3 -m venv venv  
   source venv/bin/activate  # Linux/macOS  
   # ou no Windows:  
   venv\Scripts\activate

   pip install -r requirements.txt  
   ```

3. Execute o back-end:  
   ```bash
   python app.py  
   ```

4. Abra o arquivo `index.html` no navegador para acessar o front-end.

---

## Sobre este Projeto

Participar deste processo seletivo foi uma experiência extremamente gratificante. Ao desenvolver este sistema, não apenas apliquei conhecimentos técnicos como também aprimorei minha capacidade de criar soluções integradas e funcionais. Esse projeto representou uma oportunidade valiosa de aprendizado prático, que me motivou e me deixou muito satisfeito com o resultado final.

Agradeço a oportunidade de contribuir e demonstrar minhas habilidades por meio deste trabalho.

---

Obrigado pela atenção e pela oportunidade!
