# blackjack

## A brief description
Creating a simplified blackjack-like game with changed rules for counting points.  
PS. I apologize in advance to all card game enthusiasts ;)

## Lessons Learned - among the others:
- Using composition, one of fundamental concept in object-oriented programming
- List comprehension
- Special methods like '\_\_str__' or '\_\_repr__'
- Handling Exceptions with custom types of exceptions
- Using unicode symbols in Python

## Run Locally

Clone the project

```bash
  git clone https://github.com/pawelbihun/blackjack.git
```

Go to the project directory

```bash
  cd blackjack
```

Create virtual environment, e.g. venv

```bash
  python3 -m venv venv
```
Activate venv

```bash
  source venv/bin/activate
```
Install dependencies

```bash
  python3 -m pip install -r requirements.txt
```
Run game
```bash
  python3 play.py
```

## How to  play
The game consists of two turns, first the cards are drawn by the player then the dealer plays. The player draws two cards and decides whether to draw another card.
If the player exceeds 21 points, he loses immediately.  
The number of a card is equivalent to its point value. 
Face cards are scored for 10 points. The exception is the ace, which has different values depending on what cards it is surrounded by. Two aces equals 21 points - an immediate win. 
An ace next to another card counts for 10 points. With three or more cards, the first ace counts for 10 another one point each.


## 🚀 About Me
I'm a software tester and Python enthusiast. More information on the [LinkedIn](https://linkedin.com/in/pawel-bihun) profile.