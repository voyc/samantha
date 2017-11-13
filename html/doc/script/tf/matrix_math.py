# implements the examples on the Matrix Math page in the Samantha wiki
# https://github.com/voyc/samantha/wiki/Matrix-Math

import tensorflow as tf
sess = tf.Session()
init = tf.global_variables_initializer()

# data types
x = tf.constant(3, dtype=tf.float32, name='x')  # scalar
v = tf.constant([1,2,3,4], dtype=tf.float32)  # vector
A = tf.constant([[1,2],[3,4]], dtype=tf.float32)  # matrix
sess.run(init)
print(sess.run([x,v,A]))

# element-wise multiplication of two matrices
A = tf.placeholder(tf.float32)
B = tf.placeholder(tf.float32)
element_multiplier = A * B
sess.run(init)
print(sess.run(element_multiplier, {A:[[1,2],[3,4]], B:[[5,7],[6,4]]}))

# element-wise addition of vector and matrix
vector_plus_matrix = A + B
sess.run(init)
print(sess.run(vector_plus_matrix, {A:[1,2], B:[[5,7],[6,4]]}))

# element-wise multiplication of scalar and matrix
vector_times_matrix = A * B
print(sess.run(vector_times_matrix, {A:2, B:[[5,7],[6,4]]}))

# dot product multiplication of two matrices
dot_multiplier = tf.matmul(A, B)
sess.run(init)
print(sess.run(dot_multiplier, {A:[[5,7],[6,4]], B:[[2,1],[4,2]]}))

# another dot product matrix multiplication
print(sess.run(dot_multiplier, {A:[[5,7],[6,4],[3,2]], B:[[2,1,3,2],[4,2,1,5]]}))

# matrix transpose
matrix_transpose = tf.transpose(A)
print(sess.run(matrix_transpose, {A:[[5,7],[6,4],[3,2]]}))

# identity matrix
three = tf.constant(3, dtype=tf.float32)
identity_matrix = tf.eye(three)
sess.run(init)
print(sess.run(identity_matrix, {three:3}))

# matrix inversion
M = tf.constant([[3,4,8],[2,16,4],[4,2,9]], dtype=tf.float32)
invert_matrix = tf.matrix_inverse(M)
sess.run(init)
print(sess.run(invert_matrix))

# multiply M times its inverse
element_multiplier = A * B
MT = tf.matrix_inverse(M)
sess.run(init)
print(sess.run(element_multiplier, {A:M, B:pinv(M)}))

def pinv(x):
    return tf.matrix_inverse(x)

