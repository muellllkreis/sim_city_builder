class PlayView:
    def __init__(self, left, top):
        self.top_left = (left + 10, top - 256)
        self.top_right = (left + 465, top - 256)
        self.bottom_left = (left + 10, top - 5)
        self.bottom_right = (left + 465, top - 5)
        self.center = (int((self.top_right[0] - self.top_left[0])/2), int((self.bottom_right[0] - self.top_right[1])/2))
