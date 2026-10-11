mport random

class Environment:
    def __init__(self):
        self.start = 0

    def reset(self):
        self.start = 0
        return self.start

    def step(self, action):
        self.state += action
        if self.state == 5:
            reward = 10
            done = True
        else:
            reward = 0
            done = False
        return self.state, reward, done


class Agent:
    def __init__(self):
        self.action = [-1, +1]

    def select_action(self):
        return random.choice(self.actions)

env = Environment()
agent = Agent()

state = env.reset()
done = False
step_count = 0

print("Starting episode...")

while not done:
    action = agent.select_action()
    next_state, reward, done = env.step(action)
    print(f"Step {step_count): State = {state), Action = {action}, Next State = {next_state}, Reward = {reward}")
    state = next_start
    step_count += 1

print("Episode finished!")    
    
