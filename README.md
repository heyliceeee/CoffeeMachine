# ☕ Coffee Machine – Python OOP  
Simulação de uma máquina de café totalmente funcional, construída em Python, utilizando Programação Orientada a Objetos (OOP).  
O utilizador pode escolher bebidas, inserir moedas, receber troco e ver o relatório de recursos da máquina.

---

## 🚀 Funcionalidades

- Escolha entre **espresso**, **latte** e **cappuccino**  
- Sistema de moedas com cálculo automático  
- Verificação de recursos antes de preparar a bebida  
- Dedução automática dos ingredientes  
- Relatório completo da máquina com emojis  
- Troco calculado automaticamente  
- Estrutura OOP limpa e extensível  

---

## 🧩 Estrutura do Projeto

```
coffee_machine/
│
├── main.py
├── coffee_maker.py
├── menu.py
├── money_machine.py
└── README.md
```

### **main.py**
Ponto de entrada do programa.  
Coordena a interação entre Menu, CoffeeMaker e MoneyMachine.

### **menu.py**
Contém:
- Lista de bebidas disponíveis  
- Classe `MenuItem`  
- Classe `Menu` para obter itens e procurar bebidas  

### **coffee_maker.py**
Responsável por:
- Verificar recursos  
- Preparar bebidas  
- Mostrar relatório  

### **money_machine.py**
Responsável por:
- Processar moedas  
- Calcular troco  
- Gerir o dinheiro da máquina  

---

## 💰 Sistema de Moedas

A máquina aceita:

| Moeda     | Valor |
|-----------|--------|
| quarters  | $0.25 |
| dimes     | $0.10 |
| nickles   | $0.05 |
| pennies   | $0.01 |

O utilizador insere quantidades e o programa calcula automaticamente o total.

---

## 📊 Relatório da Máquina

O comando:

```
report
```

Mostra algo como:

```
📊 MACHINE REPORT:
💧 water: 300ml
🥛 milk: 200ml
☕ coffee: 100g
💵 money: $0.00
```

---

## 🧪 Exemplo de Execução

```
What would you like? (espresso/latte/cappuccino/report/off): latte
💲 The latte costs $2.50
💰 Insert coins:
How many 🪙 quarters ($0.25)? : 10
How many 🪙 dimes ($0.10)? : 0
How many 🪙 nickles ($0.05)? : 0
How many 🪙 pennies ($0.01)? : 0
💵 Here is your change: $0.00
☕ Here is your latte. Enjoy! 😄
```