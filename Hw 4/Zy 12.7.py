#Ahmad Sliman 1898612

def get_age():
    age = int(input())
    if age < 18 or age > 75:
        print("Invalid age.")
        print("Could not calculate heart rate info.")
        print("")
        raise ValueError()
    else:
        fat_burning_heart_rate(age)
    return age


def fat_burning_heart_rate(age):
    heart_rate = (220 - age) * .7
    print(f'Fat burning heart rate for a {age} year-old: {heart_rate} bpm')
    return heart_rate

if __name__ == "__main__":

    age = get_age()