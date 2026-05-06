# This is the utils file for executing the EpiCastBench codes

import numpy as np
import random
import torch

def set_seed(seed=42):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


def get_horizon(frequency, horizon_type):
    horizons = {"daily": {"long": 30, "medium": 14, "short": 7},
                "weekly": {"long": 12, "medium": 8, "short": 4},
                "monthly": {"long": 24, "medium": 12, "short": 6}
    }

    # Normalize inputs
    frequency = frequency.lower()
    horizon_type = horizon_type.lower()

    if frequency not in horizons:
        raise ValueError("Invalid frequency. Choose from 'daily', 'weekly', 'monthly'.")

    if horizon_type not in horizons[frequency]:
        raise ValueError("Invalid horizon type. Choose from 'long', 'medium', 'short'.")

    horizon = horizons[frequency][horizon_type]
    return horizon
