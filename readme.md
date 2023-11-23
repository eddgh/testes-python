# Instruções após clonar o projeto:

- 01 - depois de clonar, verifique se você tem o pipenv instalado:
>pipenv --version

- 02 - caso nao tenha:
>pip install pipenv

- 03 - crie o ambiente virtual na pasta do seu projeto
>python -m venv.

- 04 - ative o ambiente virtual
>source Scripts/activate

- 05 - instale as dependencias
>pipenv install

- 06 - Garanta que as principais dependências estejam instaladas:
>pipenv install selenium webdriver-manager pytest pytest-html

- 07 - Para configurar o framework padrão de testes do Python:
>Pressione Ctrl+Shit+P, depois digite 'tests', selecione a opção 'Python: Configure Tests'. Escolha a opção 'pytest framework'. Selecione o diretório que contém os testes (no caso desse projeto é a pasta 'site'). Depois disso você poderá rodar os testes clicando no botão de testes (icone do frasco Balão de laboratório https://github.com/eddgh/testes-python/blob/472c796b1bddb32a8204d59ff14dab74809e668e/imgs/vscode-test-icon.PNG ) na barra lateral esquerda do vscode e em segida no botão de play https://github.com/eddgh/testes-python/blob/472c796b1bddb32a8204d59ff14dab74809e668e/imgs/vscode-testplay-icon.PNG no canto superior esquerdo.<hr> 

# Criando ambiente de testes em Python + Selenium WebDriver

[Ref. YT para melhor entendimento - 'Utilizando o Selenium para testes de interface com Python 3 | Pytest | Pytest HTML | Front-end'](https://youtu.be/HPUrFjJJSQQ)

- 01 - crie uma pasta
- 02 - abra esta pasta no vscode
- 03 - verifique se tem você tem o pipenv instalado digitando: 
```
pipenv --version
```
 caso não tenha, para instalar digite:
```
pip install pipenv
```
- 04 - instale o ambiente virtual com pipenv
```
pipenv install
```
isto criará os arquivos Pipfile e Pipfile.lock que são como uma espécie de package.json e vão gerenciar os pacotes que voce instalar com ` pipenv install nomedopacote`
- 05 - digite: 
```
pipenv --python three
```
para que a versao 3 (three) do Python seja instalada quando quem baixar seu projeto rodar o comando ` pipenv install`
- 05 - para saber mais comandos do pipenv digite `pipenv -h`
- 06 - Instale suas dependencias com pipenv install:
```
pipenv install selenium webdriver-manager pytest pytest-html
```
### Preparando os testes
- 01 - Crie uma pasta chamada `site` na raiz do seu projeto
- 02 - Dentro da pasta `site` crie outra pasta, chamada `tests`
- 03 - Dentro da pasta de tests crie seus testes, nomeando o arquivo iniciando o nome com `test_` e finalizando o nome com `.py` , por exemplo `test_random.py`
- 04 - Dentro deste arquivo crie funções iniciando por `test_` , por exemplo: `def test_loginSuccess(self):`
- 05 - ative o seu ambiente virtual digitando:
```
pipenv shell
```
- 06 - para fazer apenas o teste digite:
```
pytest site/
```
e assimm o pytest rastreará todos os seus testes presentes nessa pasta/subpastas
- 07 - para fazer o teste e gerar um relatório do mesmo digite:
```
pytest site/ --html=report.html
```
isto criará um aqrquivo chamado `report.html` na raiz do seu projeto contendo os resultados.
- 08 - para imprimir algo no log do  `Captured stdout call` de cada teste, inclua o comando `print()` no seu código.

 [Veja mais informações importantes sobre a estruturação das pastas do projeto](readme2.md)