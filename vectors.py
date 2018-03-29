height_weight_age = [70,170,40]

grades = [95,80,75,62]

#Adding two vectors
def vector_add(v,w):
    return [v_i+w_i
    for v_i,w_i in zip(v,w)]

print(vector_add(height_weight_age,grades))

#Dot product of two vectors

def dot(v,w):
    return[v_i*w_i
    for v_i,w_i in zip(v,w)]

print(dot(height_weight_age,grades))

