"""Closed-form reference experiment for the one-dimensional heat equation."""

from pathlib import Path

import numpy as np
import plotly.graph_objects as go

LENGTH = 1.0
FINAL_TIME = 1.0
DIFFUSIVITY = 0.1
POSITIONS = (0.1*LENGTH, 0.25*LENGTH, 0.5*LENGTH, 0.65*LENGTH, 0.85*LENGTH)


def temperature(x, t):
    """Closed form solution for the one-dimensional heat equation."""
    return np.sin(np.pi * np.asarray(x) / LENGTH) * np.exp(
        -DIFFUSIVITY * (np.pi / LENGTH) ** 2 * np.asarray(t)
    )


def save_figures(output_dir: Path) -> None:
    """Save fixed-position temperature curves and a space-time heatmap."""
    output_dir.mkdir(parents=True, exist_ok=True)
    times = np.linspace(0.0, FINAL_TIME, 201)
    positions = np.linspace(0.0, LENGTH, 201)

    trajectories = go.Figure()
    styles = ("solid", "solid", "solid", "dash", "dash")
    for x, style in zip(POSITIONS, styles):
        trajectories.add_trace(
            go.Scatter(
                x=times,
                y=temperature(x, times),
                mode="lines",
                name=f"x = {x:g}",
                line={"dash": style},
            )
        )
    trajectories.update_layout(
        title="Temperature at five fixed positions",
        xaxis={"title": "Time t", "range": [0, FINAL_TIME]},
        yaxis={"title": "Temperature u(x, t)"},
        legend_title="Rod position",
    )
    trajectories.write_image(
        output_dir / "heat_trajectories.png",
        width=1200,
        height=800,
        scale=2,
    )

    values = temperature(positions[:, None], times[None, :])
    heatmap = go.Figure(
        data=go.Heatmap(
            x=times,
            y=positions,
            z=values,
            zmin=0,
            zmax=1,
            colorscale="Inferno",
            colorbar={"title": "Temperature u(x, t)"},
        )
    )
    heatmap.update_layout(
        title="Temperature in the rod",
        xaxis={"title": "Time t"},
        yaxis={"title": "Position x"},
    )
    heatmap.write_image(
        output_dir / "heat_heatmap.png",
        width=1200,
        height=800,
        scale=2,
    )


def main() -> None:
    output_dir = Path("outputs/figures")
    save_figures(output_dir)
    print(f"Saved heat experiment images to {output_dir}")


if __name__ == "__main__":
    main()
