# Machine-Learning   
  
数学知识补充：
---
泊松分布  ：  [甜在心头馒头店]（https://www.zhihu.com/question/26441147）  

机器学习知识补充：
---
### 熵（Entropy）：    

[无痛的机器学习](https://zhuanlan.zhihu.com/p/30854084)  
在某一个随机事件中，某个事件的不确定度越大，熵也就越大，那我们要搞清楚的信息量就越大。  
概率越大 不确定性越小  

x,y是相互独立的，h(x) + h(y) = h(x+y)   
预期信息量： [x] = p(x)h(x) + p(y)h(y)   
在我们的生活中，信息的大小跟随机事件的概率有关，越小概率的事情产生的信息量越大。越大概率的事情产生的信息量越小。  
  
1. 当一个事件发生的概率p(x)为1并且它发生了，那我们等到的信息量是h(x) = 0。

2. 当一个事件发生的概率p(x) 为0 并且它发生了，那我们得到的信息可能是无限大。

3. H(x）随p(x)单调递增。

4. p(x,y) = p(x)p(y)。

5. h(x,y) = h(x) + h(y)。

6. 信息量h(x) 反比于p(x) 。  
7.信息量是非负的。 ## Stanford 
  
信息量 h（x）= -log(p(x))    
H[x] = - p(x)log2(p(x)) - p(y)log2(p(y))  
  
### 信息增益 （Information Gain）  
概率分布最均匀，预测的风险最小。因为这是的概率分布的信息熵最大，称为“最大熵法”  
  
信息熵增益越大，这个属性作为根结点就能使这棵树更简洁  

 
## GWU
What is machine learning  
---
Arthur Samuel(chess)  
#[checkers](https://en.wikipedia.org/wiki/Draughts): (Java)
gives computers the ability to learn without being explicitly progammed   
-Supervised learning    
"right answer" given    
regression: predict continuous valued output  
Classification : Discrete valued output
-Unsupervised learning    
clustering algorithm, many places (google news)  
cocktail party problem  (Java)
  
 Octave faster  
(reinforcement learning recommender systems )  

Model and Cost Function  
---
Training set of housing prices  
Training -- learning Algorithm -- h (hypothesis) function that maps from x's to y's    
Linear regression with one variable  -- Univariate linear regression  
  
Cost Function  
---
cost function ( Squared error function )  
  
  ![image](https://github.com/xu9449/Machine-Learning/blob/master/IMG_6488.JPG)Welcome to the Machine-Learning wiki!
   
 GWU-LESSON1    
 ---    
 Machine learning setup    
 label space C:   
 Basic variations    
 Cluster   
 fearhers never fully describe the situation  
 Lecture02  
 ---
 supervised machine learning  
 no free lunch theorem
 ### Loss Function  
 * Squared loss  
    Absolutelosee
    
      
伯努利分布  

