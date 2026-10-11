import random

class Environment:
    def __init__(self):
        self.state = 0

    def reset(self):
        self.state = 0
        return self.state

    def step(self, action):
      self.state += action
      if self.state == 10:
          reward = 20
          done = True
      elif self.state == 5:
          reward = -5
          done = False    
      else:
          reward = 0
          done = False
      return self.state, reward, done


class Agent:
    def __init__(self):
        self.action = [-1, +1]

    def select_action(self):
        return random.choice(self.action)

env = Environment()
agent = Agent()

state = env.reset()
done = False
step_count = 0

print("Starting episode...")

while not done:
    action = agent.select_action()
    next_state, reward, done = env.step(action)
    print(f"Step {step_count}: State = {state}, Action = {action}, Next State = {next_state}, Reward = {reward}")
    state = next_state
    step_count += 1

print("Episode finished!")    
    
