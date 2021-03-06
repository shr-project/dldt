"""
 Copyright (c) 2018-2019 Intel Corporation

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

from extensions.ops.ReduceOps import ReduceMax
from mo.front.common.partial_infer.utils import int64_array
from mo.front.extractor import FrontExtractorOp
from mo.front.mxnet.extractors.utils import get_mxnet_layer_attrs


class MaxFrontExtractor(FrontExtractorOp):
    op = 'max'
    enabled = True

    @staticmethod
    def extract(node):
        attrs = get_mxnet_layer_attrs(node.symbol_dict)
        ReduceMax.update_node_stat(node, {'axis': int64_array([attrs.int('axis', 0)]), 'keep_dims': False})
        return __class__.enabled
