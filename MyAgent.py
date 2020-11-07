import gfootball.env as football_env
from keras.models import Model
from keras.layers import Input,Dense,Conv2D,Flatten,MaxPooling2D
from keras.optimizers import Adam
from keras.applications.mobilenet_v2 import MobileNetV2

env = football_env.create_environment(
                                env_name='11_vs_11_stochastic', 
                                representation='raw',
                                render=True)

def model_from_pixels():


# for episodes in range(4):
#     obs = env.reset()
#     for t in range(125):
#         env.render()
#         print(obs)
#         action = env.action_space.sample()
#         obs, reward, done, info = env.step(action)
#         if done:
#             print("Episode finished after {} timesteps".format(t+1))
#             break
env.close()



