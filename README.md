# 🛒 Sistema de Desconto Progressivo

📚 Projeto desenvolvido para a **ETEC**, na atividade de Desenvolvimento de Sistemas I — **Agenda 06**.

Um projeto simples feito em **Python** para calcular descontos de acordo com o valor total de uma compra.

A ideia é informar o valor da compra e descobrir qual desconto será aplicado e quanto o cliente deverá pagar no final.

💰 **Como funciona?**

O programa pede:

Valor total da compra

Depois, verifica o valor informado e aplica uma das seguintes regras:

* Compras menores que R$ 200,00 → **5% de desconto**
* Compras de R$ 200,00 até R$ 299,99 → **10% de desconto**
* Compras de R$ 300,00 ou mais → **15% de desconto**

O desconto é calculado usando a fórmula:

```text
desconto = valor_compra × porcentagem
```

E o valor final é calculado por:

```text
total = valor_compra - desconto
```

💻 **Tecnologias**

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python\&logoColor=white)

![GitHub](https://img.shields.io/badge/GitHub-Projeto-black?logo=github\&logoColor=white)

📌 **Exemplo**

```text
Digite o valor da compra: R$ 300

Seu desconto é de 15%!
Valor do desconto: R$ 45.00
Valor total da compra: R$ 255.00
```

▶️ **Como executar**

É necessário ter o **Python** instalado no computador.

Abra o projeto no **VS Code**, abra o terminal e execute:

```bash
python leticiaPaulaDeOliveira_Ag6_DS_I.py
```

Depois, digite o valor da compra quando solicitado.

🎯 **Objetivo**

A atividade tem como objetivo praticar conceitos básicos de Python, como **entrada de dados, variáveis, cálculos e estruturas de decisão (`if`, `elif` e `else`)**.

👩‍💻 **Desenvolvido por Letícia Paula**
