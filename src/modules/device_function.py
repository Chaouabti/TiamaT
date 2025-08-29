import torch

def which_device() -> str:
    """
    Detects the best available device for PyTorch-based inference (CUDA, MPS, XLA/TPU, or CPU).

    Returns
    -------
    str
        The best available device, one of: 'cuda', 'mps', 'xla', or 'cpu'.
    """

    # 1. CUDA (NVIDIA GPUs)
    if torch.cuda.is_available():
        print(f"✅ Using CUDA GPU: {torch.cuda.get_device_name(0)}")
        return "cuda"

    """# 2. MPS (Apple Silicon GPUs)
    if hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
        print("✅ Using Apple Silicon GPU (MPS)")
        return "mps"""

    # 3. TPU (XLA - PyTorch/XLA)
    try:
        import torch_xla.core.xla_model as xm
        dev = xm.xla_device()
        print(f"✅ Using TPU: {dev}")
        return "xla"
    except ImportError:
        pass  # torch_xla not installed or no TPU available

    # 4. CPU fallback
    print("⚠️ Using CPU")
    return "cpu"
