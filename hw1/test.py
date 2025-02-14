import gymnasium as gym
env = gym.make("Ant-v5", render_mode="human", width=1280, height=720)
env.reset()
done = False
while not done:
    env.render()
    action = env.action_space.sample()
    ob, rew, done, _, _ = env.step(action)
