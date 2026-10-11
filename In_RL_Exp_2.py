import numpy as np
import matplotlib.pyplot as plt

n_arms = 3
true_rewards = [0.2, 0.5, 0.75]
n_steps = 100

reward_sums = np.zeros(n_arms)
counts = np.zeros(n_arms)
estimated_rewards = np.zeros(n_arms)
reward_history  = []
cumulative_reward = []

for arm in range(n_arms):
  reward = int(np.random.rand() < true_rewards[arm])
  reward_sums[arm] += reward
  counts[arm] += 1
  estimated_rewards[arm] = reward_sums[arm] / counts[arm]
  reward_history.append(reward)
  cumulative_reward.append(sum(reward_history))

for step in range(n_arms, n_steps):
  arm = np.argmax(estimated_rewards)
  reward = int(np.random.rand() < true_rewards[arm])
  reward_sums[arm] += reward
  counts[arm] += 1
  estimated_rewards[arm] = reward_sums[arm] / counts[arm]
  reward_history.append(reward)
  cumulative_reward.append(cumulative_reward[-1] + reward)

print("\n=== Final Results ===")
print("True Reward Probabilities:", true_rewards)
print("Estimated Reward Probabilities:", np.round(estimated_rewards, 2))
print("Number of Time each arm was pulled:", counts)
print("Total Rewards Earned:", int(sum(reward_history)))

plt.figure(figsize=(10, 5))
plt.plot(cumulative_reward, label="Cumulative Reward", color= 'blue')
plt.xlabel("Steps")
plt.ylabel("Total Reward")
plt.title("Greedy Agent - Reward Over Time")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
