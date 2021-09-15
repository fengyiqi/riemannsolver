import matplotlib.pyplot as plt


def plot2D(
        x,
        value,
        label,
):
    plt.figure(dpi=100)
    if isinstance(value, list) and isinstance(label, list):
        for i, prop in enumerate(value):
            plt.plot(x, prop, label=label[i])
    else:
        plt.plot(x, value, label=label)
    plt.legend()
    plt.show()
