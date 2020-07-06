Configuração do Ambiente do Projeto
************************************

Código para retornar e plotar a distância entre um ponto e uma curva.

Overview sobre como rodar
==========================
#. Crie um ambiente virtual Python utilizando Poetry
#. Instale os pacotes requeridos
#. Instale a biblioteca de Python para plot
#. Execute o código

Procedimento de setup
======================
#. Criar um ambiente com Poetry:

   * poetry init
   * poetry shell

#. Instalar os pacotes Numpy, Scipy e Matplotlib

   * poetry add numpy scipy matplotlib

#. Instalar python3-tk para plotagem

   * sudo apt install python3-tk -y

#. Executar

   * python3 distance

Uso
====
* Introduzir as coordenadas x,y do ponto e a função ao fim será retornada a distância e o gráfico da função.
   * A função pode ser polinomial, exponencial, senoidal, etc
   * A descrição dos elementos da funções seguem o formato da linguagem Python, então para representar um elemento de coeficiente 3 atrelado a um termo x de expoente 2 resultará 3*x**2

Documentar código
==================
#. Instalar Sphinx

   * sudo apt install python3-sphinx

#. Iniciar

   * sphinx-quickstart

#. Configurar estrutura de documentação

   * arquivos conf.py e index.rst na pasta source

#. Construir documentação em html

   * sphinx-build -b html source build
