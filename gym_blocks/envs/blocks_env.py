import gym
from gym import error, spaces, utils
from gym.utils import seeding

class BlocksEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):

    self.action_space = gym.spaces.Discrete(10)
    self.observation_space = gym.spaces.Discrete(10)
      
  def step(self, action, blocks):
     '''
     Gives us 10 total movement options. (0,1,2,3,4,5,6,7,8,9)
     '''
     if action == 0:
       state= blocks[0] 
     elif action == 1:
       state= blocks[1]
     elif action == 2:
       state= blocks[2]
     elif action == 3:
       state= blocks[3]
     elif action == 4:
       state= blocks[4]
     elif action == 5:
       state= blocks[5]
     elif action == 6:
       state= blocks[6]
     elif action == 7:
       state= blocks[7]
     elif action == 8:
       state= blocks[8]
     elif action == 9:
       state= blocks[9]
          
     if(action%2==0):
       reward = 0
       #print("negative reward=",reward) 
       #count=count+1 
             
     elif(action%2==1):
       reward = 100
       #print("positive reward=",reward)
       #count=count+1
         
     if(reward==100):
        done = True
        info = {}
        return state, reward, done, info
      
  def reset(self,blocks):
    
    state=random.choice(blocks)
    return state
    
  def render(self, mode='human'):
    pass
  
  def close(self):
    pass
