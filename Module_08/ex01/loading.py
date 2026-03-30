
import sys
import importlib.metadata
try:
    import pandas
    import requests
    import numpy as np
    import matplotlib.pyplot as plt
except Exception as e:
    print(f"Please install dependencies {e}")
    sys.exit(1)


def checking_dependencies() -> None:
    matplotlib_version = importlib.metadata.version('matplotlib')
    pandas_version = importlib.metadata.version('pandas')
    requests_version = importlib.metadata.version('requests')
    print(f"[OK] pandas ({pandas_version}) - Data manipulation ready")
    print(f"[OK] requests ({requests_version}) - Network access ready")
    print(f"[OK] matplotlib ({matplotlib_version}) - Visualization ready")


def analyzing_matrix_data() -> None:
    print("\nAnalyzing Matrix data...")
    prix_btc:float = 0
    try:
        reponse = requests.get(
            "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
        prix_btc = float(reponse.json()["price"])
    except Exception as e:
        print(e)
    print("Processing 1000 data points...")
    data_pointes = np.random.randint(1000, size=(1000))
    data_pointes_2 = np.random.randint(1000, size=(1000))
    print("Generating visualization...")
    xpoints = np.array(data_pointes)
    ypoints = np.array(data_pointes_2)
    plt.text(330, -20, f'BTC PRICE {prix_btc}', fontsize=12,
             bbox=dict(facecolor='orange', alpha=0.9))
    df = pandas.DataFrame({'X': xpoints, 'Y': ypoints})
    plt.plot(df['X'], df['Y'], 'o')
    plt.savefig("matrix_analysis.png")
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    print("\nLOADING STATUS: Loading programs...\n")
    checking_dependencies()
    analyzing_matrix_data()


if __name__ == '__main__':
    main()
