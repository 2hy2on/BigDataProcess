#!/usr/bin/python3
import os
import numpy as np
import operator
import sys


train_path = sys.argv[1]
test_path = sys.argv[2]

trainData = []
trainDataLabel = []
testDataLabel = []
testData =[]
testDataPredict = []


def modifyDataSet(dataX):
    newDataX = dataX.reshape(-1, 32 *32)
    return newDataX

def classify(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize,1)) -dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis= 1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = int(labels[sortedDistIndicies[i]].item())
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) +1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]



try:
    # 폴더 내 모든 파일 목록 얻기
    file_list = os.listdir(train_path)

    # 폴더 내 모든 파일에 대해 반복
    for file_name in file_list:
        if file_name.endswith('.txt'):  # txt 파일
            file_path = os.path.join(train_path, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                # 파일 내용 읽기
                content = file.read()
                
                data_lines = content.strip().split('\n')
                binary = []
                for line in data_lines:
                    for data in line:
                        binary.append(int(data))
                trainData.append(binary)

                label = int(file_name[0]) 
                trainDataLabel.append(label)
                # print('-----------------------')
    # print(trainDataLabel)
except FileNotFoundError:
    print(f'{train_path}를 찾을 수 없습니다.')
except Exception as e:
    print(f'sss파일 목록을 얻는 중 오류가 발생했습니다: {e}')


try:
    # 폴더 내 모든 파일 목록 얻기
    file_list = os.listdir(test_path)

    # 폴더 내 모든 파일에 대해 반복
    for file_name in file_list:
        if file_name.endswith('.txt'):  # txt 파일
            file_path = os.path.join(test_path, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                # 파일 내용 읽기
                content = file.read()
                
                data_lines = content.strip().split('\n')
                binary = []
                for line in data_lines:
                    for data in line:
                        binary.append(int(data))
                testData.append(binary)

                label = int(file_name[0]) 
                testDataLabel.append(label)

                
                # print('-----------------------')
except FileNotFoundError:
    print(f'{test_path}를 찾을 수 없습니다.')
except Exception as e:
    print(f'파일 목록을 얻는 중 오류가 발생했습니다: {e}')



trainData = modifyDataSet(np.array(trainData))
testData = modifyDataSet(np.array(testData))

# print(testData.shape)
# print(testData)

for k in range(1, 21):
    testDataPredict = []
    for i in range(testData.shape[0]):
        testDataPredict.append((classify(testData[i], trainData, np.array(trainDataLabel, dtype=int), k)))
    print(np.sum(np.array(testDataLabel) != np.array(testDataPredict)) )
