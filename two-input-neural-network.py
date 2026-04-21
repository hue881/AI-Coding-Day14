import random

w1, w2 = 0.1, 0.1
b = 0.0
lr = 0.05

for step in range(40):
    x1 = random.randint(0, 10)  # homework
    x2 = random.randint(0, 10)  # quiz

    total = x1 + x2
    target = 1 if total >= 12 else 0

    raw = w1 * x1 + w2 * x2 + b
    pred = 1 if raw >= 0.5 else 0

    error = target - pred

    w1 = w1 + lr * error * x1
    w2 = w2 + lr * error * x2
    b = b + lr * error

    print(
        'x1', x1,
        'x2', x2,
        'target', target,
        'pred', pred,
        'w1', round(w1, 2),
        'w2', round(w2, 2),
        'b', round(b, 2)
    )
