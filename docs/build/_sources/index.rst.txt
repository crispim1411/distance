.. distance documentation master file, created by
   sphinx-quickstart on Mon Jan 13 18:31:31 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

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

   * python distance

Uso
====
* Introduzir as coordenadas x,y do ponto e a função ao fim será retornada a distância e o gráfico da função.
   * A função pode ser polinomial, exponencial, senoidal, etc
   * A descrição dos elementos das funções seguem o formato :math:`{c1*x**p1 + c2*x**p2} = c1x^{p1}+c2x^{p2}`

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

Documentação do código
=======================

.. toctree::
   :titlesonly:

.. automodule:: distance
   :members:

Índices and tabelas
====================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
