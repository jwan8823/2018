


NETWORK_PATH="/notebooks_for_training/model"
FROZEN_MODEL= 'resnet.pb'
dpu__dir="board/zcu111/ZCU111.json"
output_dir="coutput/zcu111"
name="resnet"
vai_c_tensorflow--${TF_NETWORK_PATH} qoutput/${FROZEN_MODEL}  \
                    --arch ${dpu__dir} \
                    --outputdir ${output_dir} \
                    --net_name ${resnet}
