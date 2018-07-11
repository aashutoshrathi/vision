import tensorflow as tf


model_file = "tf_files/retrained_graph.pb"

def load_graph(pbmodelFile):
    with tf.gfile.GFile(pbmodelFile, "rb") as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())

    with tf.Graph().as_default() as graph:
        tf.import_graph_def(graph_def)

    input_name = graph.get_operations()[0].name+':0'
    output_name = graph.get_operations()[-1].name+':0'

    return graph, input_name, output_name


graph, inputName, outputName = load_graph(model_file)
input_x = graph.get_tensor_by_name(inputName)
output_y = graph.get_tensor_by_name(outputName)

print(input_x)
print(output_y)