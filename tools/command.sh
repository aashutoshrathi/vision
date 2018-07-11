ARCHITECTURE=mobilenet_1.0_224_quantized                                                           
DATA_DIR=~/                                                         
TRAINING_DIR=/tmp/tf_files                                                                         
                                                                                                   
python ~/example_code/retrain.py \
  --bottleneck_dir=$TRAINING_DIR/bottlenecks \
  --how_many_training_steps=500 \
  --model_dir=$TRAINING_DIR/models \
  --summaries_dir=$TRAINING_DIR/training_summaries/"${ARCHITECTURE}" \
  --output_graph=$TRAINING_DIR/retrained_graph.pb \
  --output_labels=$TRAINING_DIR/retrained_labels.txt \
  --architecture="${ARCHITECTURE}" \
  --image_dir=$DATA_DIR/flower_photos

rm -f /$TRAINING_DIR/${ARCHITECTURE}.tflite                           
                        
tensorflow/bazel-bin/tensorflow/contrib/lite/toco/toco \
  --input_file=$TRAINING_DIR/retrained_graph.pb \
  --input_format=TENSORFLOW_GRAPHDEF \
  --output_format=TFLITE \
  --output_file=/$TRAINING_DIR/${ARCHITECTURE}.tflite \
  --inference_type=QUANTIZED_UINT8 \
  --input_array=Placeholder \
  --output_array=final_result \
  --input_shape=1,224,224,3 \
  --mean_value=128 \
  --std_value=128