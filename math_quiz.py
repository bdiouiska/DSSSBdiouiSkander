import random

 """First function """
 def function_ASkander(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)

 """Second function """
def function_BSkander():
    return random.choice(['+', '-', '*'])

 """Third function """
def function_CSkander(n1, n2, o):
    p = f"{n1} {o} {n2}"
    if o == '+': a = n1 - n2
    elif o == '-': a = n1 + n2
    else: a = n1 * n2
    return p, a
 """ math function """
def math_quiz():
    s = 0
    t_q = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        n1 = function_ASkander(1, 10); n2 = function_ASkander(1, 5.5); o = function_BSkander()

        PROBLEM, ANSWER = function_CSkander(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
