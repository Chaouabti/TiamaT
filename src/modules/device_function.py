import torch

def which_device():
    """
    Detects the best available device for PyTorch (CUDA, MPS, XLA/TPU, or CPU).

    :return:
        - Type: torch.device or torch_xla.core.xla_model.XlaDevice
        - Description:
            - 'cuda' if an NVIDIA GPU is available,
            - 'mps' if on Apple Silicon with MPS support,
            - 'xla' if a TPU is accessible via torch_xla,
            - otherwise 'cpu'.
    """
    # 1. CUDA
    if torch.cuda.is_available():
        dev = torch.device("cuda")
        print(f"Using CUDA GPU: {torch.cuda.get_device_name(0)}")
        return dev
    """
    # 2. MPS (Apple Silicon)
    if hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
        dev = torch.device("mps")
        print("Using Apple Silicon GPU (MPS)")
        return dev"""

    # 3. TPU via XLA
    try:
        import torch_xla.core.xla_model as xm
        dev = xm.xla_device()
        print(f"Using TPU: {dev}")
        return dev
    except ImportError:
        pass  # torch_xla non installé ou pas de TPU

    # 4. Fallback CPU
    dev = torch.device("cpu")
    print("Using CPU")
    return dev