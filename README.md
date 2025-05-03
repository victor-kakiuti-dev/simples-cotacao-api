# Simples_Cotacao_API


Este projeto é uma aplicação simples para consultar a **cotação de moedas** em tempo real, utilizando dados de APIs públicas. O objetivo é fornecer as informações de conversão de moedas entre diferentes valores, permitindo ao usuário obter o valor equivalente em outra moeda.

## Funcionalidades

- **Consulta de cotações** de diversas moedas.
- **Conversão de valores** de uma moeda para outra.
- **Armazenamento em CSV**: os dados de cotação podem ser exportados para um arquivo CSV para análise posterior.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal do projeto.
- **Requests**: Para consumir a API de cotação de moedas.
- **CSV**: Para exportar os dados de cotação.
- **Git**: Para versionamento de código e controle de versão.

## Instalação

### 1. Clone o repositório

Clone o repositório para sua máquina local:
```
git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
```

### 2. Crie um ambiente virtual (opcional, mas recomendado)

Para garantir que as dependências não interfiram com outros projetos, é recomendado usar um ambiente virtual:

# No Linux/macOS
```
python3 -m venv venv
```
# No Windows
```
python -m venv venv
```


Ative o ambiente virtual:

# No Linux/macOS
```
source venv/bin/activate
```

# No Windows
```
.\venv\Scripts\activate
```


### 3. Instale as dependências

Instale as bibliotecas necessárias:
```
pip install requests pandas
```


Como Usar
Obter cotação: O script principal (main.py) permite consultar a cotação de diferentes moedas, passando os parâmetros adequados.

Exportar para CSV: Os dados de cotação podem ser exportados para um arquivo .csv usando o comando presente no código.
```
python main.py
```

Exemplos de Uso
Para consultar a cotação do dólar para o real:

Execute o script que irá buscar os valores atualizados da API de cotações.

Para exportar os dados para CSV:

O script gerará um arquivo .csv com as cotações de moedas.

```
Estrutura do Projeto
simples-cotacao-api
│
├── main.py            # Script principal para consultar cotações
├── README.md          # Documentação do projeto
├── .gitignore          # Arquivo para ignorar arquivos não versionados
|── cotações.csv    # Exemplo de arquivo CSV gerado

```
Contribuições
Se você gostaria de contribuir para este projeto, fique à vontade para abrir um pull request! Se encontrar algum bug ou quiser sugerir melhorias, crie uma issue.

Licença
Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.


Agora, esse código está completamente dentro do formato de **markdown** e pode ser copiado e colado no seu editor. Se precisar de mais alguma alteração ou se algo não ficou claro, me avise!

