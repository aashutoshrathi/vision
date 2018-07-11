import tensorflow as tf
from tensorflow.python.framework import graph_util

saver = tf.train.import_meta_graph('./_retrain_checkpoint.meta', clear_devices=True)
graph = tf.get_default_graph()
input_graph_def = graph.as_graph_def()
sess = tf.Session()
saver.restore(sess, "./_retrain_checkpoint")


output_node_names="final_result"
output_graph_def = graph_util.convert_variables_to_constants(
    sess, # The session
    input_graph_def, # input_graph_def is useful for retrieving the nodes 
    output_node_names.split(",") 
)


output_graph="/frozen_model.pb"
with tf.gfile.GFile(output_graph, "wb") as f:
    f.write(output_graph_def.SerializeToString())

sess.close()