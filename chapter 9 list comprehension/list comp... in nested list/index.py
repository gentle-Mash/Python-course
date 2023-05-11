# we want list = [[1,2,3],[1,2,3],[1,2,3]] by list comp...

nested_comp = [[i for i in range(1,4)] for j in range(3)]
print(nested_comp)

# the later j is for looping the loop for 3 times