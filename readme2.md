# Estrutura de pastas em Python para testes
    📂site
      📂tests
        📝test_example.py
    📂utils
      📝operations.py
      📝variables.py

  [**Exemplo real de teste**: test_variables.py](\\site\tests\test_variables.py)      

**Em cada arquivo de teste deve conter:**

>import sys

>sys.path.append(".")

... que são necessários para "apendar" o apontamento da pasta raiz (*utils*), para
que nao ocorram erros quanto ao caminho de importação.

Dentro da pasta **utils** você deve criar um arquivo **dunder init.py** ( `__init__.py` )
> basicamente toda a pasta que contiver este arquivo ao ser chamada a pasta, tudo o que contiver no arquivo dunderInit.py será executado. [Ref. no YT (Modularização com Python)](https://youtu.be/_bZe0sh0tCs?t=650)

Dentro do arquivo `__init__.py` você pode importar funções, variáveis etc, de outros arquivos desta forma:

>from .[operations](\\utils\operations.py) import soma

>from .[variables](\\utils\variables.py) import *

Neste caso o ponto ( . ) faz referência à própria pasta utils, onde estao os arquivos operations.py e variables.py onde, do arquivo operations.py estamos importando apenas a função soma, e do arquivo variables.py todo o conteúdo, sejam funções, variáveis ou qualquer outra coisa.

Se quisesse **importar do arquivo `calcula.py` uma função chamada `divisao`** e que tudo estivesse estruturado assim:

**Estrutura:**

    📁utils
      📂funcoes
         📝calcula.py
 A importação seria escrita da seguinte forma:
>from .funcoes.calcula import divisao


 [<< Voltar para "Criando ambiente de testes em Python + Selenium WebDriver" ](readme.md)

 >Para configurar o framework padrão de testes do Python, pressione **Ctrl+Shit+P**, depois digite 'tests', selecione a opção **Python: Configure Tests** e siga as intruções sugeridas. Depois disso você poderá rodar os testes clicando no botão de testes:  
 ![ícone de testes vscode](/imgs/vscode-test50-icon.PNG) na barra lateral esquerda do vscode e em segida no botão de play
 ![ícone de testes vscode](/imgs/vscode-testplay-icon.PNG) no canto superior esquerdo.<hr>
 


