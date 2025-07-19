import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import numpy as np
import matplotlib.dates as mdates
import os

def plot_clusters(df, labels, plot_3d=False, save_path=None):
    n_clusters = len(set(labels))

    base_cmap = cm.get_cmap("tab10")
    colors = base_cmap(np.linspace(0, 1, n_clusters))
    cmap = mcolors.ListedColormap(colors)

    if plot_3d:
        fig = plt.figure(figsize=(12, 8))
        ax = fig.add_subplot(111, projection='3d')

        x = df["longitude"]
        y = df["latitude"]
        z = mdates.date2num(df["time"])

        scatter = ax.scatter(
            x, y, z,
            c=labels,
            cmap=cmap,
            s=10,
            depthshade=True,
            marker='o',
            edgecolors='w',
            linewidths=0.2
        )

        ax.set_xlabel("Longitude")
        ax.set_ylabel("Latitude")
        ax.set_zlabel("Time")
        ax.zaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

        cbar = fig.colorbar(scatter, ax=ax, pad=0.1)
        cbar.set_label("Cluster")

        plt.title(f"Kernel K-Means Clustering (k={n_clusters}) in 3D Space")
        plt.tight_layout()

        if save_path:
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            plt.savefig(save_path)
            print(f"3D plot saved to: {save_path}")

        plt.show()

    else:
        plt.figure(figsize=(10, 6))
        scatter = plt.scatter(
            df["longitude"], df["latitude"],
            c=labels,
            cmap=cmap,
            s=10
        )
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        plt.title(f"Kernel K-Means Clustering (k={n_clusters})")
        plt.colorbar(scatter, label="Cluster")
        plt.grid(True)
        plt.tight_layout()

        if save_path:
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            plt.savefig(save_path)
            print(f"2D plot saved to: {save_path}")

        # plt.show()
