## 这是什么

个人摸鱼的项目，尝试在格斗游戏用RL探索下，但暂时没有大进展。

目前想法是一个Actor是最小执行单元，每个Actor配备一个合法的`actionlist`，并通过一个配套的神经网络`model`进行动作的选择。

一个角色由三个Actor进行控制，分别对应的是技能、位移以及基础行动。技能目前只完成我最爱的`Filia`的按键映射，并且预估也是先用Filia进行实验看看算法能不能成功。

## 短期TODO

- [x] `config.py`的按键设置同步到`actor.py`中，以及处理一下游戏内的画面，特征选择等。
- [x] `model.py`完成，初版网络构建完成。
- [ ] 特征提取网络的训练。