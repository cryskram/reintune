from stable_baselines3 import PPO
from env import MusicEnv

env = MusicEnv()

model = PPO("MlpPolicy", env, verbose=1)

model.learn(total_timesteps=10000)

model.save("music_agent")
