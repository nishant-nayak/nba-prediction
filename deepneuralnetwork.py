import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import os
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

def fetchdata():
    df=pd.DataFrame()
    for season in os.scandir('D:\\Pranav\\Code\\IEEE\\combined'):
        if season.is_dir():
            for month in os.scandir('D:\\Pranav\\Code\\IEEE\\combined\\'+season.name):
                temp=pd.read_csv('D:\\Pranav\\Code\\IEEE\\combined\\'+season.name+'\\'+month.name)
                df=df.append(temp,ignore_index=True)
    df.drop(['Team1','Team2','Team1Score','Team2Score'],axis=1,inplace=True)
    return df  

def sigmoid(Z):
    sig=1/(1+np.exp(-Z))
    sig=np.maximum(sig,0.0001)
    sig=np.minimum(sig,0.9999)
    return sig,Z

def relu(Z):
    ans=np.maximum(0,Z)
    return ans,Z

def sigmoid_backward(dA,Z):
    temp=sigmoid(Z)[0]
    temp=temp*(1-temp)
    dZ=dA*temp
    return dZ

def relu_backward(dA,Z):
    temp=Z>0
    dZ=dA*temp
    return dZ

def setdata(data):
    X=np.asarray(data.drop(['Team1Win'],axis=1))
    Y=np.asarray(data['Team1Win'])
    X=preprocessing.scale(X)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33,random_state=42)
    X_train=X_train.T
    X_test=X_test.T
    Y_train=Y_train.reshape((1,Y_train.shape[0]))
    Y_test=Y_test.reshape((1,Y_test.shape[0]))
    return X_train,Y_train,X_test,Y_test

def sethyperparameters(X):
    learning_rate=0.05
    num_iterations=15000
    layer_dims=[X.shape[0],5,4,3,1]
    return learning_rate,num_iterations,layer_dims

def initialize(layer_dims):
    L=len(layer_dims)
    parameters={}
    for l in range(1,L):
        parameters['W'+str(l)]=np.random.randn(layer_dims[l],layer_dims[l-1])
        parameters['b'+str(l)]=np.zeros((layer_dims[l],1))
    return parameters

def forward_linear(A_prev,W,b):
    Z=np.dot(W,A_prev)+b
    cache=(A_prev,W,b)
    return Z,cache

def forward_activation(A_prev,W,b,activation):
    Z,linear_cache=forward_linear(A_prev,W,b)
    A,activation_cache=(relu(Z) if activation=='relu' else sigmoid(Z))
    cache=(linear_cache,activation_cache)
    return A,cache

def forward_prop(X,parameters):
    caches=[]
    L=len(parameters)//2
    A_prev=X
    for l in range(1,L):
        A,cache=forward_activation(A_prev,parameters['W'+str(l)],parameters['b'+str(l)],'relu')
        caches.append(cache)
        A_prev=A
    AL,cache=forward_activation(A_prev,parameters['W'+str(L)],parameters['b'+str(L)],'sigmoid')
    caches.append(cache)
    return AL,caches

def compute_cost(AL,Y):
    m=Y.shape[1]
    cost=-np.sum(Y*np.log(AL)+(1-Y)*np.log(1-AL))/m
    cost=np.squeeze(cost)
    return cost

def back_linear(dZ,cache):
    A_prev,W,b=cache
    m=A_prev.shape[1]
    dW=np.dot(dZ,A_prev.T)/m
    db=np.sum(dZ,axis=1,keepdims=True)/m
    dA_prev=np.dot(W.T,dZ)
    return dA_prev,dW,db

def back_activation(dA,cache,activation):
    linear_cache,activation_cache=cache
    dZ=(relu_backward(dA,activation_cache) if activation=='relu' else sigmoid_backward(dA,activation_cache))
    dA_prev,dW,db=back_linear(dZ,linear_cache)
    return dA_prev,dW,db

def back_prop(AL,Y,caches):
    dAL = (-Y/AL) + ((1-Y)/(1-AL)) 
    L=len(caches)
    grads={}
    current_cache=caches[L-1]
    grads['dA'+str(L-1)],grads['dW'+str(L)],grads['db'+str(L)]=back_activation(dAL,current_cache,'sigmoid')
    for l in range(L-2,-1,-1):
        current_cache=caches[l]
        dA_prev,dW,db=back_activation(grads['dA'+str(l+1)],current_cache,'relu')
        grads['dA'+str(l)]=dA_prev
        grads['dW'+str(l+1)]=dW
        grads['db'+str(l+1)]=db
    return grads

def update(parameters,grads,learning_rate):
    L=len(parameters)//2
    for l in range(L):
        parameters['W'+str(l+1)]-=learning_rate*grads['dW'+str(l+1)]
        parameters['b'+str(l+1)]-=learning_rate*grads['db'+str(l+1)]
    return parameters

def gd(X,Y,learning_rate,num_iterations,parameters):
    costs=[]
    for i in range(num_iterations):
        AL,caches=forward_prop(X,parameters)
        if i%100==0 :
            cost=compute_cost(AL,Y)
            costs.append(cost)
        grads=back_prop(AL,Y,caches)
        parameters=update(parameters,grads,learning_rate)
    return parameters,costs

def model(X,Y,layer_dims,learning_rate,num_iterations):
    parameters=initialize(layer_dims)
    parameters,costs=gd(X,Y,learning_rate,num_iterations,parameters)
    return parameters,costs

def predict(parameters,X,Y):
    AL,caches=forward_prop(X,parameters) 
    Y_predict=AL>0.5
    accuracy=100-np.mean(np.abs(Y_predict-Y))*100
    return accuracy

def main():
    data=fetchdata()
    print("got data")
    X_train,Y_train,X_test,Y_test=setdata(data)
    print("split data")
    learning_rate,num_iterations,layer_dims=sethyperparameters(X_train)
    print("set hyperparameters")
    parameters,costs=model(X_train,Y_train,layer_dims,learning_rate,num_iterations)
    testaccuracy=predict(parameters,X_test,Y_test)
    print(testaccuracy)
    costs=np.squeeze(costs)
    print(costs[-1])
    plt.plot(costs)
    plt.xlabel("Number of iterations (per 100)")
    plt.ylabel("Cost")
    plt.title("Learning Rate="+str(learning_rate))
    plt.show()

main()