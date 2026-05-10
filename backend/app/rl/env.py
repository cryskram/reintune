import gymnasium as gym
from gymnasium import spaces
import numpy as np
import random

NOTES = [60, 62, 64, 65, 67, 69, 71, 72]


class MusicEnv(gym.Env):

    def __init__(self):
        super(MusicEnv, self).__init__()

        self.action_space = spaces.Discrete(len(NOTES))

        self.observation_space = spaces.Box(
            low=0, high=127, shape=(8,), dtype=np.float32
        )

        self.state = np.zeros(8)

    def reset(self, seed=None, options=None):
        self.state = np.zeros(8)

        return self.state, {}

    def step(self, action):
        note = NOTES[action]

        reward = 0

        if note in [60, 64, 67]:
            reward += 1

        if abs(note - self.state[-1]) > 12:
            reward -= 1

        self.state = np.roll(self.state, -1)

        self.state[-1] = note

        done = False

        return self.state, reward, done, False, {}
