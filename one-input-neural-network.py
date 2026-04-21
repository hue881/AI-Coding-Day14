import random

w = 0.1  # weight for x
b = 0.0  # bias
lr = 0.05  # learning rate

for step in range(40):
    x = random.randint(0, 20)
    target = 1 if x >= 10 else 0

    # Forward pass
    raw = w * x + b
    pred = 1 if raw >= 0.5 else 0

    error = target - pred

    # Update
    w = w + lr * error * x
    b = b + lr * error

    print('step', step, 'x', x, 'target', target, 'pred', pred, 'w', round(w, 2), 'b', round(b, 2))

