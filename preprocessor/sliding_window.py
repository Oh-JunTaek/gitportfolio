def sliding_window(text, window_size, step_size):
    """슬라이딩 윈도우 방식으로 텍스트를 작은 구간으로 나누는 함수"""
    words = text.split()
    windows = []
    for i in range(0, len(words) - window_size + 1, step_size):
        window = " ".join(words[i:i + window_size])
        windows.append(window)
    return windows
