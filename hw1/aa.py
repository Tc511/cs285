import gym
import mujoco_py

# 创建环境
env = gym.make('Ant-v4')

# 创建渲染窗口
env.reset()
for _ in range(1000):
    action = env.action_space.sample()  # 随机动作
    env.step(action)  # 执行动作
    env.render()  # 渲染图形
