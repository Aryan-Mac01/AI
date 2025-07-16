#lists
Participants =  ['john', ' jane', 'doe']
print(Participants[1])#output: jane
Participants[2] = 'Maria'
del Participants[0]
print(Participants) #output: ['jane', 'Maria']

#methods
Participants.append('Alice')
print(Participants) #output: ['jane', 'Maria', 'Alice']

Participants.extend(['Bob', 'Charlie'])
print(Participants) #output: ['jane', 'Maria', 'Alice', 'Bob', 'Charlie']

print('The number of participants is:', len(Participants)) #output: The number of participants is: 5

len("Dolphin") #output: 7
len(Participants) #output: 5


#slicing
print(Participants[1:3]) #output: ['Maria', 'Alice']

Participants.sort(reverse=True)
print(Participants) #output: ['Charlie', 'Maria', 'Alice', 'jane

