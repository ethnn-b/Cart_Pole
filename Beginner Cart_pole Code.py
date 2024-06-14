# tested on     
# gym==0.26.2
# gym-notices==0.0.8
 
#gymnasium==0.27.0
#gymnasium-notices==0.0.1
 
# classical gym 
import gym
# instead of gym, import gymnasium 
#import gymnasium as gym
import numpy as np
import time
 
 
# create environment
env=gym.make('CartPole-v1',render_mode='human')
# reset the environment, 
# returns an initial state
(state,_)=env.reset()
# states are
# cart position, cart velocity 
# pole angle, pole angular velocity

#We create the environment by using


env=gym.make('CartPole-v1',render_mode='human')
#render_mode=’human’ means that we want to generate animation in a separate window. You can also create the environment without specifying the render_mode parameter. This will create the environment without creating the animation. This is beneficial for training a reinforcement learning algorithm since animation generation during training will slow down the training process.

#After we create the environment, we need to reset the environment in order to initialize the environment to an initial state (initial state components are selected as small random values). We do that with the following command


(state,_)=env.reset()
#the env.reset() function returns the initial state.

#The following code lines render the environment and apply an action left (corresponding to 0):


# render the environment
env.render()
# close the environment
#env.close()
 
# push cart in one direction
env.step(0)
##You can close the generated animation window by calling (env.close()). The function env.step() returns the following output tuple:
##
##
##(array([-0.02076359, -0.19763313, -0.03636114,  0.24699631], dtype=float32),
## 1.0,
## False,
## False,
## {})
##The tuple
##
##1
##(array([-0.02076359, -0.19763313, -0.03636114,  0.24699631], dtype=float32)
##is the observed state after the action is applied. Number 1 is the obtained reward. ‘False’ denotes that the returned state is NOT the terminal state. That is, the episode did not finish by applying the action. Next ‘False’ is a truncation parameter, and the last empty dictionary ‘{}’ is a dictionary that in the case of some other environments contains additional information. Here it is empty, since there is no additional information.
##
##We can obtain basic information about our environment by using these code lines


# observation space limits
env.observation_space
 
# upper limit
env.observation_space.high
 
# lower limit
env.observation_space.low
 
 
# action space
env.action_space
 
# all the specs
env.spec
 
# maximum number of steps per episode
env.spec.max_episode_steps
 
# reward threshold per episode
env.spec.reward_threshold
##These specs are already explained previously.
##
##We simulate the cart pole system by using these code lines

# simulate the environment
episodeNumber=5
timeSteps=100
 
 
for episodeIndex in range(episodeNumber):
    initial_state=env.reset()
    print(episodeIndex)
    env.render()
    appendedObservations=[]
    for timeIndex in range(timeSteps):
        print(timeIndex)
        random_action=env.action_space.sample()
        observation, reward, terminated, truncated, info =env.step(random_action)
        appendedObservations.append(observation)
        time.sleep(0.1)
        if (terminated):
            time.sleep(1)
            break
env.close()   
##First, we select the number of simulation episodes and maximal number of time steps within every episode. Then in every simulation episode, on the code line 6, we reset the environment in order to ensure that the state from the previous episode simulation is reset. Then we render the environment. The code lines 11-19 are used to simulate an episode. On the code line 13, we generate a random action. On the code line 14, we apply this random action to our cart pole environment. If the returned state is terminal state (that is, if the cart or pole position and angle reach the limits), then the flag “terminated” becomes ‘True’ and we break the current episode simulation. We introduce pause in the code by using “time.sleep()” in order to ensure that the environment is properly animated. Finally, we close the animation window with ‘env.close()’.
##
##Post navigation


























