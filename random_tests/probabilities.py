import random


def calculate_probabilities(rounds, dices):
    def compute_shots(n, shots):
        if n == 1:
            return shots

        shot = [random.randint(1, 6) for i in range(dices)]
        total = sum(shot)

        previous_shots = shots.get(str(total), [])[:]
        previous_shots.append(shot)
        shots.update({str(total): previous_shots})

        return compute_shots(n - 1, shots)

    shots = compute_shots(rounds, {})

    probabilities = {key: len(value) / rounds for key, value in shots.items()}

    return probabilities

if __name__ == '__main__':
    rounds = int(input('how many rounds: '))
    dices = int(input('how many dices: '))
    probabilities = calculate_probabilities(rounds, dices)
    print(probabilities)
