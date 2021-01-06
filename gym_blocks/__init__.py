from gym.envs.registration import register

register(
    id='blocks-v0',
    entry_point='gym_blocks.envs:BlocksEnv',
)
register(
    id='blocks-extrahard-v0',
    entry_point='gym_blocks.envs:BlocksExtraHardEnv',
)
