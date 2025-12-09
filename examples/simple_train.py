"""
Simple training example placeholder using Trackle API.
"""

import trackle


def main() -> None:
    trackle.init(run_name="simple-train", tags=["demo"])
    trackle.log_params({"epochs": 3})
    for step in range(3):
        trackle.log_metric("loss", value=1.0 / (step + 1), step=step)
    trackle.set_note("First demo run.")
    trackle.finish()


if __name__ == "__main__":
    main()

